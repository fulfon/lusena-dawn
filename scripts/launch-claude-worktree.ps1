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
$uncommitted = git status --porcelain
$commits = git log "main..$branchName" --oneline 2>$null

if ($uncommitted) {
    # Uncommitted changes — cannot auto-merge safely
    Write-Host ""
    Write-Host "  WARNING: Worktree has uncommitted changes." -ForegroundColor Red
    Write-Host "  Claude should have committed before exiting. Manual cleanup needed:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "    cd $worktreePath"
    Write-Host "    git add -A && git commit -m `"feat(lusena): ...`""
    Write-Host "    cd $mainRepo"
    Write-Host "    git merge --squash $branchName && git commit -m `"feat(lusena): ...`""
    Write-Host "    git worktree remove $worktreePath"
    Write-Host "    git branch -d $branchName"
} elseif ($commits) {
    # Committed changes — auto-squash-merge into main
    Write-Host ""
    Write-Host "  Merging into main..." -ForegroundColor Cyan

    # Show what's being merged
    Write-Host ""
    git log "main..$branchName" --oneline | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkGray }
    Write-Host ""

    Set-Location $mainRepo
    git merge --squash $branchName 2>$null
    $mergeOk = $LASTEXITCODE -eq 0

    if ($mergeOk) {
        # Build commit message from the worktree branch commits
        $commitMsg = (git log "main..$branchName" --format="%s" 2>$null) -join "; "
        if (-not $commitMsg) { $commitMsg = "feat(lusena): worktree $num changes" }
        git commit -m $commitMsg 2>$null

        Write-Host "  Merged into main." -ForegroundColor Green

        # Clean up worktree and branch
        git worktree remove $worktreePath --force 2>$null
        git branch -D $branchName 2>$null
        Write-Host "  Worktree cleaned up. Slot $num is free." -ForegroundColor Green
    } else {
        # Merge conflict — abort and leave for manual resolution
        git merge --abort 2>$null
        Write-Host "  MERGE CONFLICT — could not auto-merge." -ForegroundColor Red
        Write-Host "  The worktree is preserved. Resolve manually:" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "    cd $mainRepo"
        Write-Host "    git merge --squash $branchName"
        Write-Host "    # resolve conflicts, then:"
        Write-Host "    git commit -m `"feat(lusena): ...`""
        Write-Host "    git worktree remove $worktreePath"
        Write-Host "    git branch -d $branchName"
    }
} else {
    # No changes at all — clean up silently
    Write-Host "  No changes detected. Cleaning up..." -ForegroundColor Green
    Set-Location $mainRepo
    git worktree remove $worktreePath 2>$null
    git branch -d $branchName 2>$null
    Write-Host "  Worktree removed." -ForegroundColor Green
}

Write-Host ""
Read-Host "  Press Enter to close"
