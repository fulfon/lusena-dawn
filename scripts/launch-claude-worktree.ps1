# LUSENA - Launch Claude Code in an isolated git worktree
# Double-click the .bat wrapper on your Desktop to use this.

try {

$mainRepo = "C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-dawn"
$worktreeBase = "C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-worktrees"

# Ensure worktree parent directory exists
New-Item -ItemType Directory -Force -Path $worktreeBase | Out-Null

# --- Ensure Shopify dev server is running (syncs main repo to dev theme) ---
$devServerRunning = $false
try {
    $conn = Get-NetTCPConnection -LocalPort 9292 -State Listen -ErrorAction SilentlyContinue
    if ($conn) { $devServerRunning = $true }
} catch {}

if (-not $devServerRunning) {
    Write-Host ""
    Write-Host "  Starting Shopify dev server..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$Host.UI.RawUI.WindowTitle = 'LUSENA Dev Server'; cd '$mainRepo'; shopify theme dev -e dev"
    Write-Host "  Dev server launching in new window." -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "  Dev server already running (port 9292)." -ForegroundColor DarkGray
}

# --- Startup cleanup: prune stale worktrees and orphaned work branches ---
Push-Location $mainRepo
git worktree prune 2>$null

# Delete work/* and feat/* branches whose worktree directories no longer exist
foreach ($prefix in @('work/', 'feat/', 'fix/', 'docs/', 'chore/')) {
    $branches = git branch --list "$prefix*" 2>$null | ForEach-Object { $_.Trim().TrimStart('* ') }
    foreach ($br in $branches) {
        # Check if any active worktree uses this branch
        $inUse = git worktree list --porcelain 2>$null | Select-String -Pattern "branch refs/heads/$br$"
        if (-not $inUse) {
            git branch -d $br 2>$null
            if ($LASTEXITCODE -eq 0) {
                Write-Host "  Cleaned up stale branch: $br" -ForegroundColor DarkGray
            }
        }
    }
}
Pop-Location

# --- Clean up empty worktrees (no commits, no uncommitted changes) ---
$existingWorktrees = Get-ChildItem -Path $worktreeBase -Directory -Filter "lusena-*" -ErrorAction SilentlyContinue
foreach ($wt in $existingWorktrees) {
    $wtPath = $wt.FullName

    # Guard: if .git file is missing, this is an orphaned directory, not a valid worktree.
    # Without .git, git commands resolve to a parent repo and report false uncommitted changes.
    if (-not (Test-Path "$wtPath\.git")) {
        Remove-Item -Recurse -Force $wtPath -ErrorAction SilentlyContinue
        Write-Host "  Removed orphaned directory: $($wt.Name)" -ForegroundColor DarkGray
        continue
    }

    # Guard: skip worktrees actively used by another launcher instance.
    # The lock file is held open with an exclusive handle by the owning launcher.
    # If we can't open it exclusively, the worktree is in use. If we can, it's stale.
    $lockFile = "$wtPath\.claude-lock"
    if (Test-Path $lockFile) {
        try {
            $testStream = [System.IO.File]::Open($lockFile, [System.IO.FileMode]::Open, [System.IO.FileAccess]::ReadWrite, [System.IO.FileShare]::None)
            # Got exclusive access - lock is stale (owning process died), clean it up
            $testStream.Close()
            Remove-Item $lockFile -ErrorAction SilentlyContinue
        } catch {
            # Can't open - another launcher holds the lock, worktree is in use
            Write-Host "  Skipping $($wt.Name) - in use" -ForegroundColor DarkGray
            continue
        }
    }

    Push-Location $wtPath

    $wtBranch = git rev-parse --abbrev-ref HEAD 2>$null
    if (-not $wtBranch) { Pop-Location; continue }

    $wtUncommitted = git status --porcelain 2>$null
    $wtCommits = git log "main..$wtBranch" --oneline 2>$null

    if (-not $wtUncommitted -and -not $wtCommits) {
        Pop-Location
        Push-Location $mainRepo
        git worktree remove $wtPath --force 2>$null
        git branch -d $wtBranch 2>$null
        Write-Host "  Cleaned up empty worktree: $($wt.Name)" -ForegroundColor DarkGray
        Pop-Location
    } else {
        Pop-Location
    }
}

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

# Lock the worktree so other launcher instances don't clean it up.
# Hold the file open with an exclusive handle - Windows auto-releases on crash/kill.
$lockStream = [System.IO.File]::Open("$worktreePath\.claude-lock", [System.IO.FileMode]::Create, [System.IO.FileAccess]::Write, [System.IO.FileShare]::None)

# Launch Claude Code in the worktree
Set-Location $worktreePath
claude --effort max

# Release the lock now that Claude has exited
$lockStream.Close()
Remove-Item "$worktreePath\.claude-lock" -ErrorAction SilentlyContinue

# --- Claude Code exited ---
Write-Host ""
Write-Host "  Claude Code exited." -ForegroundColor Yellow

# Check if the worktree still exists - Claude may have already cleaned it up
if (-not (Test-Path $worktreePath)) {
    Write-Host "  Worktree already cleaned up by Claude. Nothing to do." -ForegroundColor Green
} elseif (-not (Test-Path "$worktreePath\.git")) {
    # Orphaned directory - .git file missing, so git commands would resolve to a parent repo
    Write-Host "  Worktree .git file missing (orphaned directory). Removing..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force $worktreePath -ErrorAction SilentlyContinue
    Write-Host "  Cleaned up." -ForegroundColor Green
} else {
    Set-Location $worktreePath

    # Detect the current branch (Claude may have renamed work/N to feat/...)
    $currentBranch = git rev-parse --abbrev-ref HEAD 2>$null
    if (-not $currentBranch) { $currentBranch = $branchName }

    $uncommitted = git status --porcelain
    $commits = git log "main..$currentBranch" --oneline 2>$null

    if ($uncommitted) {
        # Uncommitted changes - cannot auto-merge safely
        Write-Host ""
        Write-Host "  WARNING: Worktree has uncommitted changes." -ForegroundColor Red
        Write-Host "  Claude should have committed before exiting. Manual cleanup needed:" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "    cd $worktreePath"
        Write-Host "    git add -A && git commit -m `"feat(lusena): ...`""
        Write-Host "    cd $mainRepo"
        Write-Host "    git merge --squash $currentBranch && git commit -m `"feat(lusena): ...`""
        Write-Host "    git worktree remove $worktreePath"
        Write-Host "    git branch -d $currentBranch"
    } elseif ($commits) {
        # Committed but not merged - Claude exited before merging
        Write-Host ""
        Write-Host "  Unmerged commits found. Merging into main..." -ForegroundColor Cyan

        Write-Host ""
        git log "main..$currentBranch" --oneline | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkGray }
        Write-Host ""

        Set-Location $mainRepo
        git merge --squash $currentBranch 2>$null
        $mergeOk = $LASTEXITCODE -eq 0

        if ($mergeOk) {
            $commitMsg = (git log "main..$currentBranch" --format="%s" 2>$null) -join "; "
            if (-not $commitMsg) { $commitMsg = "feat(lusena): worktree $num changes" }
            git commit -m $commitMsg 2>$null

            Write-Host "  Merged into main." -ForegroundColor Green

            git worktree remove $worktreePath --force 2>$null
            git branch -D $currentBranch 2>$null
            Write-Host "  Worktree cleaned up. Slot $num is free." -ForegroundColor Green
        } else {
            git merge --abort 2>$null
            Write-Host "  MERGE CONFLICT - could not auto-merge." -ForegroundColor Red
            Write-Host "  The worktree is preserved. Resolve manually:" -ForegroundColor Yellow
            Write-Host ""
            Write-Host "    cd $mainRepo"
            Write-Host "    git merge --squash $currentBranch"
            Write-Host "    # resolve conflicts, then:"
            Write-Host "    git commit -m `"feat(lusena): ...`""
            Write-Host "    git worktree remove $worktreePath"
            Write-Host "    git branch -d $currentBranch"
        }
    } else {
        # No changes - clean up silently
        Write-Host "  No changes detected. Cleaning up..." -ForegroundColor Green
        Set-Location $mainRepo
        git worktree remove $worktreePath 2>$null
        git branch -d $currentBranch 2>$null
        Write-Host "  Worktree removed." -ForegroundColor Green
    }
}

} catch {
    Write-Host ""
    Write-Host "  ===== SCRIPT ERROR =====" -ForegroundColor Red
    Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "  Location: $($_.InvocationInfo.ScriptName):$($_.InvocationInfo.ScriptLineNumber)" -ForegroundColor Yellow
    Write-Host "  Line:     $($_.InvocationInfo.Line.Trim())" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  Full error:" -ForegroundColor DarkGray
    Write-Host "  $($_.Exception.ToString())" -ForegroundColor DarkGray
}

Write-Host ""
Read-Host "  Press Enter to close"

