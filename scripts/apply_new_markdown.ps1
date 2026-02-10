# Apply Improved Markdown Conversion
# This script replaces old markdown files with new ones that have better formatting

Write-Host "`n======================================" -ForegroundColor Cyan
Write-Host "  APPLY IMPROVED MARKDOWN CONVERSION" -ForegroundColor Cyan  
Write-Host "======================================`n" -ForegroundColor Cyan

# Check if new files exist
if (-not (Test-Path "content\posts_new")) {
    Write-Host "[ERROR] content\posts_new directory not found!" -ForegroundColor Red
    Write-Host "Run: python tools\reconvert_xml_to_markdown.py first" -ForegroundColor Yellow
    exit 1
}

$newCount = (Get-ChildItem "content\posts_new\*.md").Count
$oldCount = (Get-ChildItem "content\posts\*.md").Count

Write-Host "Current posts: $oldCount files" -ForegroundColor Yellow
Write-Host "New posts: $newCount files" -ForegroundColor Green

if ($newCount -ne $oldCount) {
    Write-Host "`n[WARNING] File counts don't match!" -ForegroundColor Yellow
    Write-Host "This is expected due to improved slug generation." -ForegroundColor Gray
}

Write-Host "`nThis will:" -ForegroundColor White
Write-Host "  1. Backup content\posts to content\posts_backup"
Write-Host "  2. Replace with new formatted markdown"
Write-Host "  3. Fix UTF-8 encoding issues"
Write-Host "  4. Regenerate entire website"

$confirm = Read-Host "`nContinue? (yes/no)"
if ($confirm -ne "yes") {
    Write-Host "`nCancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host "`n[1/4] Backing up current posts..." -ForegroundColor Cyan
if (Test-Path "content\posts_backup") {
    Remove-Item "content\posts_backup" -Recurse -Force
}
Rename-Item "content\posts" "content\posts_backup"
Write-Host "  OK - Backed up to content\posts_backup" -ForegroundColor Green

Write-Host "`n[2/4] Applying new markdown files..." -ForegroundColor Cyan
Rename-Item "content\posts_new" "content\posts"
Write-Host "  OK - New files now in content\posts" -ForegroundColor Green

Write-Host "`n[3/4] Fixing UTF-8 encoding..." -ForegroundColor Cyan
python scripts\fix_encoding.py
Write-Host "  OK - Encoding fixed" -ForegroundColor Green

Write-Host "`n[4/4] Regenerating website..." -ForegroundColor Cyan
python scripts\generate_from_markdown.py
Write-Host "  OK - Site regenerated" -ForegroundColor Green

Write-Host "`n======================================" -ForegroundColor Cyan
Write-Host "  COMPLETE!" -ForegroundColor Green
Write-Host "======================================`n" -ForegroundColor Cyan

Write-Host "Next steps:" -ForegroundColor White
Write-Host "  1. Open http://127.0.0.1:5500 in browser"
Write-Host "  2. Hard refresh with Ctrl+Shift+R"
Write-Host "  3. Check several posts for proper paragraph spacing`n"

Write-Host "To revert if needed:" -ForegroundColor Yellow
Write-Host "  Remove-Item content\posts -Recurse -Force"
Write-Host "  Rename-Item content\posts_backup content\posts"
Write-Host "  python scripts\generate_from_markdown.py`n"
