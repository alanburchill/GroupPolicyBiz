---
title: "Updated: Group Policy Hotfix&rsquo;s in Windows 7 and Windows Server 2008 Service Pack 1"
date: 2011-02-18 00:02:00
author: admin
categories: ["hotfix"]
tags: ["GPMC", "GPO", "Group Policy", "hotfix", "Service Pack 1", "Windows 7", "Windows Server 2008 R2"]
featured_image: "https://www.grouppolicy.biz/wp-content/uploads/2011/02/image_thumb1.png"
---

Microsoft today [announced](<http://blogs.technet.com/b/windowsserver/archive/2011/02/09/windows-server-2008-r2-and-windows-7-sp1-releases-to-manufacturing-today.aspx>) (after what seems to be a very long time) they have RTM'd Windows 7 / Windows Server 2008 R2 Service Pack 1 and it will be released to the public on February 22nd.

**Update:** Service Pack 1 is now available for download for TechNet and MSDN subscribers.

[![image](https://www.grouppolicy.biz/wp-content/uploads/2011/02/image_thumb1.png)](<https://www.grouppolicy.biz/wp-content/uploads/2011/02/image1.png>)

[Previously](<https://www.grouppolicy.biz/2010/07/the-complete-list-of-group-policy-hotfixs-in-windows-72008-r2-service-pack-1/>) I had listed the hotfixes in the beta version of the service pack, so I have again combed through the [hotfix list](<http://www.microsoft.com/downloads/en/details.aspx?familyId=61924cea-83fe-46e9-96d8-027ae59ddc11&hash=Ap0HO8PCDwjDmNi410aetVRg0uZOoqju7atOh4uDI7YYFOHyggYqd%2fw5zwISxq4Rr0W0DgXpW4RejmuDpTCZvw%3d%3d>) for you convenience and I have updated the list to include the release candidate hotfixes. ~~While this is not the final list of hotfixes~~[~~Ned Pyle [MSFT]~~](<http://blogs.technet.com/NedPyle/ProfileUrlRedirect.ashx>)~~says "~~[~~it's very doubtful that the lists below will be altered much~~](<http://blogs.technet.com/b/askds/archive/2011/01/14/sp1-and-directory-services-what-s-new.aspx>)~~" so you can pretty much take the following list as final. In any case I will review the list when the final list of fixes is out but for now here is the list of issues.~~

**Updated:** The final list of hotfixes is now out ( [Here](<http://www.microsoft.com/downloads/info.aspx?na=46&SrcFamilyId=61924CEA-83FE-46E9-96D8-027AE59DDC11&SrcDisplayLang=en&u=http%3a%2f%2fdownload.microsoft.com%2fdownload%2fE%2fB%2fA%2fEBA55FE2-373A-4351-9346-6D762B79AA69%2fHotfixes+and+Security+Updates+included+in+Windows+7+and+Windows+Server+2008+R2+Service+Pack+1.xls> "Download") ) and after a quick look they appear to be the same as expected.

If you have anything to do with supporting group policy in your organisation then I recommend that you at least take a look at the articles to see if you have encountered any of the problem described.

**KB Article / Link** | **KB Description**
---|---
<http://support.microsoft.com/kb/969867> |  FIX: You cannot import or paste some group policies across domains by using the "Group Policy Management" MMC snap-in
<http://support.microsoft.com/kb/970840> |  Some settings in Group Policy Preferences for Internet Explorer 7 do not deploy correctly to computers that are running Windows Server 2008 or Windows Vista
<http://support.microsoft.com/kb/972069> |  A terminal server that is running Windows Server 2008 cannot obtain terminal licenses from a Terminal Server license server that is running Windows Server 2008 after you enable the "License Server Security Group" Group Policy setting
<http://support.microsoft.com/kb/976398> |  LDAP filters in the Group Policy preference settings do not take effect on a computer that is running Windows Server 2008 R2 or Windows 7
<http://support.microsoft.com/kb/976399> |  FIX: You cannot apply Group Policy settings on a computer that is running Windows 7 or Windows Server 2008 R2 when security group filters are used in Group Policy preference settings
<http://support.microsoft.com/kb/977353> |  A Group Policy Immediate Task preference item does not run on a client computer that is running Windows 7 or Windows Server 2008 R2
<http://support.microsoft.com/kb/977695> |  The SceCli 1202 events are logged when some Group Policy settings are refreshed in Windows Server 2008 R2 and in Windows 7
<http://support.microsoft.com/kb/977944> |  The "Desktop Wallpaper" Group Policy setting is not applied in Windows 7 or in Windows Server 2008 R2
<http://support.microsoft.com/kb/978489> |  Logoff process stops responding after you create a logoff Group Policy script on a client computer that is running Windows Vista or Windows Server 2008
<http://support.microsoft.com/kb/978837> |  The Group Policy Management Editor window crashes when you apply some changes for NRPT policy settings
<http://support.microsoft.com/kb/979039> |  Error message when you view or modify the migrated Group Policy objects in Windows Server 2008 R2: "Attribute cannot be empty"
<http://support.microsoft.com/kb/979731> |  Some Group Policy preferences are not applied successfully on computers that are running Windows Vista, Windows Server 2008, Windows 7 or Windows Server 2008 R2
<http://support.microsoft.com/kb/980259> |  The SNMP service does not respond to any SNMP requests after a Group Policy refresh in Windows Vista or in Windows Server 2008
<http://support.microsoft.com/kb/980628> |  The "Load a specific theme" Group Policy setting is not applied correctly on a computer that is running Windows 7 or Windows Server 2008 R2
<http://support.microsoft.com/kb/981054> |  The Group Policy preference settings for the "Terminal Session" item-level targeting item are not applied in Windows 7 or in Windows Server 2008 R2
<http://support.microsoft.com/kb/981177> |  You can still unpin a program from the taskbar unexpectedly when you enable the "Do not allow pinning programs to the Taskbar" Group Policy on a computer that is running Windows 7 or Windows Server 2008 R2
<http://support.microsoft.com/kb/981265> |  You cannot create a software installation Group Policy setting on a read-only domain controller in Windows Server 2008 R2
<http://support.microsoft.com/kb/981750> |  Error message occurs when you use GPMC to view a software restriction Group Policy setting in Windows 7 and in Windows Server 2008 R2: "An error has occurred while collecting data for Software Restriction Policies"
<http://support.microsoft.com/kb/982606> |  The value of the "State" registry item is changed after a Group Policy preferences setting is applied in Windows Server 2008, in Windows Vista or in Windows Server 2008 R2
<http://support.microsoft.com/kb/982709> |  Only the first search term is searched for when you configure the "Pin Internet search sites to the 'Search again' links and the Start menu" Group Policy setting in Windows 7 or Windows Server 2008 R2
<http://support.microsoft.com/kb/983618> |  Some Group Policy settings are not displayed in the Group Policy Results report in Windows Server 2008, in Windows Vista, in Windows Server 2008 R2, or in Windows 7
<http://support.microsoft.com/kb/2096902> |  Virtual machines in a VDI environment are not rolled back as expected if the disconnected Remote Desktop connections on the virtual machines are stopped by Group Policy
<http://support.microsoft.com/kb/2284538> |  "Apply once and do not reapply" Group Policy setting is never applied after the first GPO deployment fails on a client computer that is running Windows 7 or Windows Server 2008 R2
<http://support.microsoft.com/kb/2254754> |  You experience a GPO report-generation issue in the GPMC window when you try to generate the report in a localized version of Windows 7 or of Windows Server 2008 R2
<http://support.microsoft.com/kb/2258620> |  You cannot find the "Find Now," "Stop," and "Clear All" buttons in the GPMC snap-in on a computer that is running Windows 7 or Windows Server 2008 R2
<http://support.microsoft.com/kb/979383> |  After you apply a WMI filter, the GPO does not take effect on a client computer that is running Windows 7 or Windows Server 2008 R2
<http://support.microsoft.com/kb/2028960> |  The Offline Files Disk Usage Limits settings do not reflect the settings that are defined in the GPO in Windows 7

You can also see the complete list of Active Directory Hotfix's at Ask the Directory Services Team blog posting [SP1 and Directory Services: What's New](<http://blogs.technet.com/b/askds/archive/2011/01/14/sp1-and-directory-services-what-s-new.aspx>) .