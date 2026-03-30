# LUSENA - Launch Claude Code in an isolated git worktree
# Double-click the .bat wrapper on your Desktop to use this.

$mainRepo = "C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-dawn"
$worktreeBase = "C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-worktrees"

# Ensure worktree parent directory exists
New-Item -ItemType Directory -Force -Path $worktreeBase | Out-Null

# Find next available slot (1, 2, 3, ...)
$num = 1
while (Test-Path "$worktreeBase\lusena-$num") { $num++ }

$worktreePath = "$worktreeBase\lusena-$num"
$branchName = "work/$num"

# Create worktree from current main
Write-Host ""
Write-Host "  Creating worktree #$num ..." -ForegroundColor Cyan
Push-Location $mainRepo
git worktree add $worktreePath -b $branchName main 2>&1 | Out-Null
$created = $LASTEXITCODE -eq 0
Pop-Location

if (-not $created) {
    Write-Host "  Failed to create worktree. Is branch '$branchName' already in use?" -ForegroundColor Red
    Write-Host "  Try: git branch -d $branchName" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "  Press Enter to close"
    exit 1
}

Write-Host "  Path:   $worktreePath" -ForegroundColor Green
Write-Host "  Branch: $branchName" -ForegroundColor Green
Write-Host ""

# Launch Claude Code in the worktree
Set-Location $worktreePath
claude

# --- Claude Code exited ---
Write-Host ""
Write-Host "  Claude Code exited." -ForegroundColor Yellow

Set-Location $worktreePath
$hasChanges = (git status --porcelain) -or (git log "main..$branchName" --oneline 2>$null)

if ($hasChanges) {
    Write-Host ""
    Write-Host "  Worktree has changes - keeping it for you to merge." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  To merge into main:" -ForegroundColor Cyan
    Write-Host "    cd $mainRepo"
    Write-Host "    git merge --squash $branchName"
    Write-Host "    git commit -m `"feat(lusena): ...`""
    Write-Host "    git worktree remove $worktreePath"
    Write-Host "    git branch -d $branchName"
} else {
    Write-Host "  No changes detected. Cleaning up..." -ForegroundColor Green
    Set-Location $mainRepo
    git worktree remove $worktreePath 2>$null
    git branch -d $branchName 2>$null
    Write-Host "  Worktree removed." -ForegroundColor Green
}

Write-Host ""
Read-Host "  Press Enter to close"
