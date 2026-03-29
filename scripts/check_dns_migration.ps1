[CmdletBinding()]
param(
    [string]$Domain = 'grouppolicy.biz',
    [string[]]$SourceNameServers = @('ns1.dreamhost.com', 'ns2.dreamhost.com', 'ns3.dreamhost.com'),
    [string[]]$DestinationNameServers = @('ns1.crazydomains.com', 'ns2.crazydomains.com'),
    [string]$SiteUrl = '',
    [switch]$AsJson,
    [string]$OutputJsonPath = ''
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Import-EnvSettings {
    param([string]$EnvPath = '.env')

    $settings = @{}

    if (-not (Test-Path $EnvPath)) {
        return $settings
    }

    foreach ($rawLine in Get-Content -Path $EnvPath -Encoding UTF8) {
        $line = $rawLine.Trim()
        if ([string]::IsNullOrWhiteSpace($line)) {
            continue
        }

        if ($line.StartsWith('#')) {
            continue
        }

        if ($line -notmatch '=') {
            continue
        }

        $parts = $line.Split('=', 2)
        $key = $parts[0].Trim()
        $value = $parts[1].Trim().Trim('"').Trim("'")

        if (-not [string]::IsNullOrWhiteSpace($key)) {
            $settings[$key] = $value
        }
    }

    return $settings
}

$envSettings = Import-EnvSettings
if ([string]::IsNullOrWhiteSpace($SiteUrl) -and $envSettings.ContainsKey('SITE_URL')) {
    $SiteUrl = $envSettings['SITE_URL']
}

if ([string]::IsNullOrWhiteSpace($SiteUrl)) {
    $SiteUrl = "https://$Domain"
}

$canonicalUri = [Uri]$SiteUrl
$canonicalHost = $canonicalUri.Host.ToLowerInvariant()
$wwwHost = "www.$Domain"
$canonicalIsApex = $canonicalHost -eq $Domain.ToLowerInvariant()
$canonicalIsWww = $canonicalHost -eq $wwwHost.ToLowerInvariant()

$expectedApexA = @(
    '185.199.108.153',
    '185.199.109.153',
    '185.199.110.153',
    '185.199.111.153'
)

$expectedApexAAAA = @(
    '2606:50c0:8000::153',
    '2606:50c0:8001::153',
    '2606:50c0:8002::153',
    '2606:50c0:8003::153'
)

$expectedGitHubPagesHost = 'alanburchill.github.io'

$publicResolvers = @(
    [pscustomobject]@{ Label = 'System'; Server = $null },
    [pscustomobject]@{ Label = 'Cloudflare'; Server = '1.1.1.1' },
    [pscustomobject]@{ Label = 'Google'; Server = '8.8.8.8' },
    [pscustomobject]@{ Label = 'Quad9'; Server = '9.9.9.9' }
)

$recordPlan = @()
$recordPlan += [pscustomobject]@{ Label = 'Apex A'; Name = $Domain; Type = 'A'; Expected = $expectedApexA; Required = $canonicalIsApex }
$recordPlan += [pscustomobject]@{ Label = 'Apex AAAA'; Name = $Domain; Type = 'AAAA'; Expected = $expectedApexAAAA; Required = $false }
$recordPlan += [pscustomobject]@{ Label = 'www CNAME'; Name = $wwwHost; Type = 'CNAME'; Expected = @($expectedGitHubPagesHost); Required = $true }
$recordPlan += [pscustomobject]@{ Label = 'www A'; Name = $wwwHost; Type = 'A'; Expected = @(); Required = $false }
$recordPlan += [pscustomobject]@{ Label = 'MX'; Name = $Domain; Type = 'MX'; Expected = @(); Required = $false }
$recordPlan += [pscustomobject]@{ Label = 'TXT'; Name = $Domain; Type = 'TXT'; Expected = @(); Required = $false }

function Get-ComparableDnsHost {
    param([string]$Value)

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return ''
    }

    return $Value.Trim().TrimEnd('.').ToLowerInvariant()
}

function Get-UniqueStringList {
    param([string[]]$Values)

    return @($Values | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Sort-Object -Unique)
}

function Test-RecordProperty {
    param(
        [object]$Record,
        [string]$PropertyName
    )

    return @($Record.PSObject.Properties.Name) -contains $PropertyName
}

function Test-ExactSetMatch {
    param(
        [string[]]$Actual,
        [string[]]$Expected
    )

    $normalizedActual = @(Get-UniqueStringList -Values $Actual)
    $normalizedExpected = @(Get-UniqueStringList -Values $Expected)

    if ($normalizedActual.Count -ne $normalizedExpected.Count) {
        return $false
    }

    for ($index = 0; $index -lt $normalizedActual.Count; $index += 1) {
        if ($normalizedActual[$index] -ne $normalizedExpected[$index]) {
            return $false
        }
    }

    return $true
}

function Get-RecordValues {
    param(
        [object[]]$Records,
        [string]$Type
    )

    $values = @()

    foreach ($record in @($Records)) {
        switch ($Type) {
            'A' {
                if ((Test-RecordProperty -Record $record -PropertyName 'IPAddress') -and $record.IPAddress) {
                    $values += $record.IPAddress.ToString()
                }
            }
            'AAAA' {
                if ((Test-RecordProperty -Record $record -PropertyName 'IPAddress') -and $record.IPAddress) {
                    $values += $record.IPAddress.ToString().ToLowerInvariant()
                }
            }
            'NS' {
                if ((Test-RecordProperty -Record $record -PropertyName 'NameHost') -and $record.NameHost) {
                    $values += (Get-ComparableDnsHost -Value $record.NameHost)
                }
            }
            'CNAME' {
                if ((Test-RecordProperty -Record $record -PropertyName 'NameHost') -and $record.NameHost) {
                    $values += (Get-ComparableDnsHost -Value $record.NameHost)
                }
            }
            'MX' {
                if ((Test-RecordProperty -Record $record -PropertyName 'NameExchange') -and $record.NameExchange) {
                    $exchange = Get-ComparableDnsHost -Value $record.NameExchange
                    $values += "$($record.Preference) $exchange"
                }
            }
            'TXT' {
                if ((Test-RecordProperty -Record $record -PropertyName 'Strings') -and $record.Strings) {
                    $values += (($record.Strings -join '')).Trim()
                }
            }
        }
    }

    return @(Get-UniqueStringList -Values $values)
}

function Resolve-RecordSnapshot {
    param(
        [string]$ResolverLabel,
        [string]$Name,
        [string]$Type,
        [string]$Server
    )

    $serverDisplay = if ([string]::IsNullOrWhiteSpace($Server)) { 'system' } else { $Server }

    try {
        if ([string]::IsNullOrWhiteSpace($Server)) {
            $records = Resolve-DnsName -Name $Name -Type $Type -ErrorAction Stop
        }
        else {
            $records = Resolve-DnsName -Name $Name -Type $Type -Server $Server -ErrorAction Stop
        }

        $values = @(Get-RecordValues -Records $records -Type $Type)

        return [pscustomobject]@{
            ResolverLabel = $ResolverLabel
            Name = $Name
            Type = $Type
            Server = $serverDisplay
            Values = $values
            Error = ''
        }
    }
    catch {
        return [pscustomobject]@{
            ResolverLabel = $ResolverLabel
            Name = $Name
            Type = $Type
            Server = $serverDisplay
            Values = @()
            Error = $_.Exception.Message
        }
    }
}

function Get-DelegationStatus {
    param(
        [string[]]$ActualNameServers,
        [string[]]$SourceServers,
        [string[]]$DestinationServers
    )

    $actual = @(Get-UniqueStringList -Values $ActualNameServers)
    $source = @(Get-UniqueStringList -Values $SourceServers)
    $destination = @(Get-UniqueStringList -Values $DestinationServers)

    if ($actual.Count -eq 0) {
        return 'error'
    }

    if (Test-ExactSetMatch -Actual $actual -Expected $source) {
        return 'source'
    }

    if (Test-ExactSetMatch -Actual $actual -Expected $destination) {
        return 'destination'
    }

    $sourceMatches = @($actual | Where-Object { $source -contains $_ }).Count
    $destinationMatches = @($actual | Where-Object { $destination -contains $_ }).Count

    if (($sourceMatches -gt 0) -and ($destinationMatches -gt 0)) {
        return 'mixed'
    }

    if ($sourceMatches -gt 0) {
        return 'source-partial'
    }

    if ($destinationMatches -gt 0) {
        return 'destination-partial'
    }

    return 'other'
}

function Get-ExpectationStatus {
    param(
        [string[]]$Actual,
        [string[]]$Expected
    )

    if ((@(Get-UniqueStringList -Values $Expected)).Count -eq 0) {
        return 'n/a'
    }

    if ((@(Get-UniqueStringList -Values $Actual)).Count -eq 0) {
        return 'missing'
    }

    if (Test-ExactSetMatch -Actual $Actual -Expected $Expected) {
        return 'match'
    }

    $matchedValues = @($Actual | Where-Object { $Expected -contains $_ }).Count
    if ($matchedValues -gt 0) {
        return 'partial'
    }

    return 'different'
}

function Get-AuthorityCheckSet {
    param(
        [string]$Scope,
        [string[]]$Servers
    )

    $checks = @()

    foreach ($server in $Servers) {
        foreach ($recordDefinition in $recordPlan) {
            $snapshot = Resolve-RecordSnapshot -ResolverLabel $Scope -Name $recordDefinition.Name -Type $recordDefinition.Type -Server $server
            $checks += [pscustomobject]@{
                Scope = $Scope
                NameServer = $server
                Record = $recordDefinition.Label
                Name = $recordDefinition.Name
                Type = $recordDefinition.Type
                Values = @($snapshot.Values)
                ValueText = if ((@($snapshot.Values)).Count -gt 0) { @($snapshot.Values) -join ', ' } else { '' }
                Error = $snapshot.Error
                Expected = @($recordDefinition.Expected)
                ExpectedText = if (@($recordDefinition.Expected).Count -gt 0) { @($recordDefinition.Expected) -join ', ' } else { '' }
                ExpectationStatus = Get-ExpectationStatus -Actual @($snapshot.Values) -Expected @($recordDefinition.Expected)
                Required = $recordDefinition.Required
            }
        }
    }

    return $checks
}

function Get-WebReadinessStatus {
    param([object[]]$Checks)

    $requiredChecks = @($Checks | Where-Object { $_.Required })
    if ($requiredChecks.Count -eq 0) {
        return 'unknown'
    }

    $requiredStatuses = @($requiredChecks | ForEach-Object { $_.ExpectationStatus })
    if ((@($requiredStatuses | Where-Object { $_ -eq 'match' })).Count -eq $requiredStatuses.Count) {
        return 'ready'
    }

    if ((@($requiredStatuses | Where-Object { $_ -in @('match', 'partial') })).Count -gt 0) {
        return 'partial'
    }

    if ((@($requiredStatuses | Where-Object { $_ -eq 'missing' })).Count -eq $requiredStatuses.Count) {
        return 'missing'
    }

    return 'not-ready'
}

$publicChecks = @()
foreach ($resolver in $publicResolvers) {
    $snapshot = Resolve-RecordSnapshot -ResolverLabel $resolver.Label -Name $Domain -Type 'NS' -Server $resolver.Server
    $publicChecks += [pscustomobject]@{
        Resolver = $resolver.Label
        Server = if ([string]::IsNullOrWhiteSpace($resolver.Server)) { 'system' } else { $resolver.Server }
        Nameservers = @($snapshot.Values)
        NameServerText = if ((@($snapshot.Values)).Count -gt 0) { @($snapshot.Values) -join ', ' } else { '' }
        Status = Get-DelegationStatus -ActualNameServers @($snapshot.Values) -SourceServers $SourceNameServers -DestinationServers $DestinationNameServers
        Error = $snapshot.Error
    }
}

$sourceChecks = Get-AuthorityCheckSet -Scope 'source' -Servers $SourceNameServers
$destinationChecks = Get-AuthorityCheckSet -Scope 'destination' -Servers $DestinationNameServers

$publicStatuses = @($publicChecks | ForEach-Object { $_.Status })
$publicDestinationCount = @($publicStatuses | Where-Object { $_ -eq 'destination' }).Count
$publicSourceCount = @($publicStatuses | Where-Object { $_ -eq 'source' }).Count

$delegationStatus = 'unknown'
if ($publicDestinationCount -eq $publicChecks.Count) {
    $delegationStatus = 'delegated-to-destination'
}
elseif ($publicSourceCount -eq $publicChecks.Count) {
    $delegationStatus = 'still-on-source'
}
elseif (($publicDestinationCount -gt 0) -and ($publicSourceCount -gt 0)) {
    $delegationStatus = 'mixed-public-view'
}
elseif ((@($publicStatuses | Where-Object { $_ -like 'destination*' })).Count -gt 0) {
    $delegationStatus = 'moving-to-destination'
}
elseif ((@($publicStatuses | Where-Object { $_ -like 'source*' })).Count -gt 0) {
    $delegationStatus = 'mostly-source'
}

$destinationWebReadiness = Get-WebReadinessStatus -Checks $destinationChecks
$sourceWebReadiness = Get-WebReadinessStatus -Checks $sourceChecks

$summary = [pscustomobject]@{
    Domain = $Domain
    CanonicalSiteUrl = $SiteUrl
    CanonicalHost = $canonicalHost
    CanonicalMode = if ($canonicalIsApex) { 'apex' } elseif ($canonicalIsWww) { 'www' } else { 'custom-subdomain' }
    SourceNameServers = $SourceNameServers
    DestinationNameServers = $DestinationNameServers
    ExpectedGitHubPages = [pscustomobject]@{
        ApexA = $expectedApexA
        ApexAAAA = $expectedApexAAAA
        WwwCname = $expectedGitHubPagesHost
    }
    MigrationStatus = [pscustomobject]@{
        DelegationStatus = $delegationStatus
        SourceWebReadiness = $sourceWebReadiness
        DestinationWebReadiness = $destinationWebReadiness
    }
    PublicResolvers = $publicChecks
    SourceAuthority = $sourceChecks
    DestinationAuthority = $destinationChecks
}

if (-not [string]::IsNullOrWhiteSpace($OutputJsonPath)) {
    $jsonDirectory = Split-Path -Parent $OutputJsonPath
    if ((-not [string]::IsNullOrWhiteSpace($jsonDirectory)) -and (-not (Test-Path $jsonDirectory))) {
        New-Item -Path $jsonDirectory -ItemType Directory -Force | Out-Null
    }

    $summary | ConvertTo-Json -Depth 10 | Out-File -FilePath $OutputJsonPath -Encoding UTF8
}

if ($AsJson) {
    $summary | ConvertTo-Json -Depth 10
    exit 0
}

Write-Output ''
Write-Output '=== DNS MIGRATION SUMMARY ==='
Write-Output "Domain: $Domain"
Write-Output "Canonical site URL: $SiteUrl"
Write-Output "Canonical host mode: $($summary.CanonicalMode)"
Write-Output "Delegation status: $delegationStatus"
Write-Output "Source web readiness: $sourceWebReadiness"
Write-Output "Destination web readiness: $destinationWebReadiness"
Write-Output ''
Write-Output '=== EXPECTED DESTINATION WEB RECORDS ==='
Write-Output "Apex A: $($expectedApexA -join ', ')"
Write-Output "Apex AAAA: $($expectedApexAAAA -join ', ')"
Write-Output "www CNAME: $expectedGitHubPagesHost"
if (-not $canonicalIsApex) {
    Write-Output 'Note: apex A/AAAA records are recommended for redirect/support, but not treated as required for readiness when the canonical host is not the apex.'
}
Write-Output ''
Write-Output '=== PUBLIC RESOLVER DELEGATION CHECKS ==='
$publicChecks |
    Select-Object Resolver, Server, Status, NameServerText, Error |
    Format-Table -AutoSize -Wrap

Write-Output ''
Write-Output '=== SOURCE AUTHORITATIVE RECORDS ==='
$sourceChecks |
    Select-Object Scope, NameServer, Record, Type, ExpectationStatus, ValueText, Error |
    Format-Table -AutoSize -Wrap

Write-Output ''
Write-Output '=== DESTINATION AUTHORITATIVE RECORDS ==='
$destinationChecks |
    Select-Object Scope, NameServer, Record, Type, ExpectationStatus, ValueText, Error |
    Format-Table -AutoSize -Wrap

Write-Output ''
if (-not [string]::IsNullOrWhiteSpace($OutputJsonPath)) {
    Write-Output "JSON report written to: $OutputJsonPath"
    Write-Output ''
}
