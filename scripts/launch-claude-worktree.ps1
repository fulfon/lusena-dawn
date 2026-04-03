# LUSENA - Interactive Claude Code Worktree Launcher
# Double-click the .bat wrapper on your Desktop to use this.

try {

$mainRepo = "C:\Users\Karol\Documents\projekty_VSCode\shopify-lusena-dev\lusena-dawn"
$worktreeBase = "C:\Users\Karol\Documents\projekty_VSCode\shopify-lusena-dev\lusena-worktrees"
$maxSlots = 4

# Ensure worktree parent directory exists
New-Item -ItemType Directory -Force -Path $worktreeBase | Out-Null

# --- Helper: Derive commit message from branch name ---
function Get-CommitMessage {
    param([string]$branch)
    if ($branch -match '^(feat|fix|docs|chore|work)/(.+)$') {
        $prefix = $Matches[1]
        $rest = $Matches[2] -replace '-', ' '
        switch ($prefix) {
            'feat'  { return "feat(lusena): $rest" }
            'fix'   { return "fix(lusena): $rest" }
            'docs'  { return "docs: $rest" }
            'chore' { return "chore: $rest" }
            'work'  { return "feat(lusena): worktree $rest changes" }
        }
    }
    return "feat(lusena): $branch"
}

# --- Helper: Scan all slots and return status array ---
function Get-SlotStatus {
    # Prune stale worktree references
    git -C $mainRepo worktree prune 2>$null

    $slots = @()
    for ($i = 1; $i -le $maxSlots; $i++) {
        $path = "$worktreeBase\lusena-$i"
        $slot = [PSCustomObject]@{
            Num         = $i
            Path        = $path
            Exists      = $false
            Orphaned    = $false
            Branch      = ""
            Commits     = 0
            Uncommitted = $false
            Merged      = $false
        }

        if (Test-Path $path) {
            $slot.Exists = $true

            # Parent repo hazard: only run git commands if .git file exists
            if (-not (Test-Path "$path\.git")) {
                $slot.Orphaned = $true
            } else {
                Push-Location $path
                $slot.Branch = git rev-parse --abbrev-ref HEAD 2>$null
                if ($slot.Branch) {
                    $uncommitted = git status --porcelain 2>$null
                    if ($uncommitted) { $slot.Uncommitted = $true }
                    $commitLog = git log "main..$($slot.Branch)" --oneline 2>$null
                    if ($commitLog) {
                        $slot.Commits = ($commitLog | Measure-Object).Count
                    }
                    # Detect merged: renamed branch, at main, nothing uncommitted
                    if ($slot.Branch -notmatch '^work/\d+$' -and $slot.Commits -eq 0 -and -not $slot.Uncommitted) {
                        $slot.Merged = $true
                    }
                }
                Pop-Location
            }
        }

        $slots += $slot
    }
    return $slots
}

# --- Helper: Display the menu ---
function Show-Menu {
    param($slots)
    Clear-Host
    Write-Host ""
    Write-Host "  LUSENA Claude Code" -ForegroundColor Cyan
    Write-Host "  ----------------------------------------"
    Write-Host ""
    Write-Host "  Worktrees:"

    foreach ($s in $slots) {
        $label = "  "
        if (-not $s.Exists) {
            $label += " $($s.Num)  --"
            Write-Host $label -ForegroundColor DarkGray
        } elseif ($s.Orphaned) {
            $label += " $($s.Num)  (orphaned)"
            Write-Host $label -ForegroundColor Red
        } elseif (-not $s.Branch) {
            $label += " $($s.Num)  (unknown state)"
            Write-Host $label -ForegroundColor Yellow
        } elseif ($s.Uncommitted) {
            $label += " $($s.Num)  $($s.Branch)"
            Write-Host $label -ForegroundColor White -NoNewline
            Write-Host "  uncommitted changes!" -ForegroundColor Red
        } elseif ($s.Merged) {
            $label += " $($s.Num)  $($s.Branch)"
            Write-Host $label -ForegroundColor White -NoNewline
            Write-Host "  merged" -ForegroundColor DarkCyan
        } elseif ($s.Commits -gt 0) {
            $label += " $($s.Num)  $($s.Branch)"
            Write-Host $label -ForegroundColor White -NoNewline
            Write-Host "  $($s.Commits) commits" -ForegroundColor Green
        } else {
            $label += " $($s.Num)  (empty)"
            Write-Host $label -ForegroundColor DarkGray
        }
    }

    Write-Host ""
    Write-Host "  [N] New instance         [R] Resume instance" -ForegroundColor White
    Write-Host "  [C] Clean instance       [M] Merge to main" -ForegroundColor White
    Write-Host "  [D] Dev server status    [Q] Quit" -ForegroundColor White
    Write-Host ""
}

# --- Helper: Auto-cleanup merged worktree after Claude exits ---
function Invoke-AutoCleanup {
    param([int]$slotNum, [string]$slotPath)

    # Guard: worktree must exist and be valid
    if (-not (Test-Path $slotPath)) { return }
    if (-not (Test-Path "$slotPath\.git")) { return }

    $branch = git -C $slotPath rev-parse --abbrev-ref HEAD 2>$null
    if (-not $branch) { return }

    # Guard: branch must have been renamed (work was started)
    if ($branch -match '^work/\d+$') { return }

    # Guard: no uncommitted changes
    $uncommitted = git -C $slotPath status --porcelain 2>$null
    if ($uncommitted) { return }

    # Guard: branch must be at main (merged + reset)
    $commitLog = git -C $slotPath log "main..$branch" --oneline 2>$null
    $commitsAhead = if ($commitLog) { ($commitLog | Measure-Object).Count } else { 0 }
    if ($commitsAhead -gt 0) { return }

    # All conditions met - safe to clean
    Write-Host ""
    Write-Host "  Branch '$branch' is fully merged to main." -ForegroundColor DarkCyan
    Write-Host "  Auto-cleaning slot $slotNum ..." -ForegroundColor DarkCyan

    git -C $mainRepo worktree remove $slotPath --force 2>$null
    git -C $mainRepo branch -D $branch 2>$null

    if (Test-Path $slotPath) {
        try {
            Remove-Item -Recurse -Force $slotPath -ErrorAction Stop
        } catch {
            Write-Host "  Worktree unregistered but directory locked. Clean via [C] next time." -ForegroundColor Yellow
            return
        }
    }

    Write-Host "  Slot $slotNum cleaned." -ForegroundColor Green
}

# --- Action: [N] New instance ---
function Invoke-NewInstance {
    param($slots)

    # Find first free slot
    $freeSlot = $null
    foreach ($s in $slots) {
        if (-not $s.Exists) { $freeSlot = $s; break }
    }

    if (-not $freeSlot) {
        Write-Host ""
        Write-Host "  All $maxSlots slots in use. Clean one first." -ForegroundColor Red
        return
    }

    $num = $freeSlot.Num
    $path = $freeSlot.Path
    $branchName = "work/$num"

    # Clean up stale branch if it exists without a worktree
    Push-Location $mainRepo
    $existingBranch = git branch --list $branchName 2>$null
    if ($existingBranch) {
        git branch -d $branchName 2>$null
        if ($LASTEXITCODE -ne 0) {
            git branch -D $branchName 2>$null
        }
    }

    # Create worktree
    Write-Host ""
    Write-Host "  Creating worktree #$num ..." -ForegroundColor Cyan
    git worktree add $path -b $branchName main 2>&1 | Out-Null
    $created = $LASTEXITCODE -eq 0
    Pop-Location

    if (-not $created) {
        Write-Host "  Failed to create worktree." -ForegroundColor Red
        return
    }

    Write-Host "  Slot:   $num" -ForegroundColor Green
    Write-Host "  Path:   $path" -ForegroundColor Green
    Write-Host "  Branch: $branchName" -ForegroundColor Green
    Write-Host ""

    # Launch Claude Code
    Set-Location $path
    claude --name "lusena-$num"
    Set-Location $mainRepo
    Invoke-AutoCleanup -slotNum $num -slotPath $path
}

# --- Action: [R] Resume instance ---
function Invoke-ResumeInstance {
    param($slots)

    $occupied = $slots | Where-Object { $_.Exists -and -not $_.Orphaned }

    if (-not $occupied -or ($occupied | Measure-Object).Count -eq 0) {
        Write-Host ""
        Write-Host "  No active worktrees." -ForegroundColor Yellow
        return
    }

    Write-Host ""
    Write-Host "  Resume which slot? " -ForegroundColor Cyan -NoNewline
    $pick = Read-Host
    $pick = $pick.Trim()

    $target = $occupied | Where-Object { $_.Num -eq $pick }
    if (-not $target) {
        Write-Host "  Invalid slot." -ForegroundColor Red
        return
    }

    Write-Host ""
    Write-Host "  Resuming in slot $($target.Num) ($($target.Branch)) ..." -ForegroundColor Cyan
    Write-Host ""

    Set-Location $target.Path
    if ($target.Commits -eq 0 -and -not $target.Uncommitted) {
        claude --name "lusena-$($target.Num)"
    } else {
        claude --resume
    }
    Set-Location $mainRepo
    Invoke-AutoCleanup -slotNum $target.Num -slotPath $target.Path
}

# --- Action: [C] Clean instance ---
function Invoke-CleanInstance {
    param($slots)

    $occupied = $slots | Where-Object { $_.Exists }

    if (-not $occupied -or ($occupied | Measure-Object).Count -eq 0) {
        Write-Host ""
        Write-Host "  No worktrees to clean." -ForegroundColor Yellow
        return
    }

    Write-Host ""
    Write-Host "  Clean which slot? " -ForegroundColor Cyan -NoNewline
    $pick = Read-Host
    $pick = $pick.Trim()

    $target = $occupied | Where-Object { $_.Num -eq $pick }
    if (-not $target) {
        Write-Host "  Invalid slot." -ForegroundColor Red
        return
    }

    # Orphaned: just remove the directory
    if ($target.Orphaned) {
        git -C $mainRepo worktree prune 2>$null
        try {
            Remove-Item -Recurse -Force $target.Path -ErrorAction Stop
            Write-Host "  Slot $($target.Num) cleaned (orphaned directory removed)." -ForegroundColor Green
        } catch {
            Write-Host ""
            Write-Host "  Cannot delete directory - files are locked." -ForegroundColor Red
            Write-Host "  Close any Claude Code / editor windows using slot $($target.Num)," -ForegroundColor Yellow
            Write-Host "  then try again." -ForegroundColor Yellow
        }
        return
    }

    # Warn if there's unmerged work
    $hasUnmergedCommits = $target.Commits -gt 0 -and -not $target.Merged
    if ($target.Uncommitted -or $hasUnmergedCommits) {
        Write-Host ""
        if ($target.Uncommitted -and $hasUnmergedCommits) {
            Write-Host "  WARNING: This worktree has uncommitted changes AND $($target.Commits) unmerged commits." -ForegroundColor Red
        } elseif ($target.Uncommitted) {
            Write-Host "  WARNING: This worktree has uncommitted changes." -ForegroundColor Red
        } else {
            Write-Host "  WARNING: This worktree has $($target.Commits) unmerged commits." -ForegroundColor Red
        }
        Write-Host "  Work will be lost." -ForegroundColor Red
        Write-Host ""
        Write-Host "  Are you sure? [Y/N] " -ForegroundColor Yellow -NoNewline
        $confirm = Read-Host
        if ($confirm.Trim().ToUpper() -ne 'Y') {
            Write-Host "  Cancelled." -ForegroundColor DarkGray
            return
        }
    }

    # Cleanup
    $branch = $target.Branch
    Push-Location $mainRepo
    git worktree remove $target.Path --force 2>$null
    if ($branch) {
        git branch -D $branch 2>$null
    }
    Pop-Location

    # git worktree remove may unregister but fail to delete the directory (file locks)
    if (Test-Path $target.Path) {
        try {
            Remove-Item -Recurse -Force $target.Path -ErrorAction Stop
        } catch {
            Write-Host ""
            Write-Host "  Worktree unregistered but directory could not be deleted (files locked)." -ForegroundColor Yellow
            Write-Host "  Close any processes using slot $($target.Num), then clean again." -ForegroundColor Yellow
            return
        }
    }

    Write-Host "  Slot $($target.Num) cleaned." -ForegroundColor Green
}

# --- Action: [M] Merge to main ---
function Invoke-MergeToMain {
    param($slots)

    $mergeable = $slots | Where-Object { $_.Exists -and -not $_.Orphaned -and $_.Commits -gt 0 -and -not $_.Merged }

    if (-not $mergeable -or ($mergeable | Measure-Object).Count -eq 0) {
        Write-Host ""
        Write-Host "  No worktrees with commits to merge." -ForegroundColor Yellow
        return
    }

    Write-Host ""
    Write-Host "  Merge which slot? " -ForegroundColor Cyan -NoNewline
    $pick = Read-Host
    $pick = $pick.Trim()

    $target = $mergeable | Where-Object { $_.Num -eq $pick }
    if (-not $target) {
        Write-Host "  Invalid slot (must have commits ahead of main)." -ForegroundColor Red
        return
    }

    # Block if uncommitted changes
    if ($target.Uncommitted) {
        Write-Host ""
        Write-Host "  Cannot merge - uncommitted changes in slot $($target.Num)." -ForegroundColor Red
        Write-Host "  Commit or clean first." -ForegroundColor Yellow
        return
    }

    # Show commits
    Write-Host ""
    Write-Host "  Commits to merge ($($target.Branch)):" -ForegroundColor Cyan
    Push-Location $target.Path
    git log "main..$($target.Branch)" --oneline | ForEach-Object { Write-Host "    $_" -ForegroundColor DarkGray }
    Pop-Location
    Write-Host ""

    # Check main repo is clean
    $mainDirty = git -C $mainRepo status --porcelain 2>$null
    if ($mainDirty) {
        Write-Host "  Main repo has uncommitted changes. Resolve before merging." -ForegroundColor Red
        return
    }

    # Derive commit message
    $commitMsg = Get-CommitMessage $target.Branch
    Write-Host "  Commit message: $commitMsg" -ForegroundColor White
    Write-Host ""

    # Execute merge
    git -C $mainRepo merge --squash $target.Branch 2>$null
    if ($LASTEXITCODE -ne 0) {
        git -C $mainRepo merge --abort 2>$null
        Write-Host "  MERGE CONFLICT - could not auto-merge." -ForegroundColor Red
        Write-Host "  Resolve manually." -ForegroundColor Yellow
        return
    }

    git -C $mainRepo commit -m $commitMsg 2>$null
    Write-Host "  Merged into main." -ForegroundColor Green

    # Reset worktree branch to main so auto-cleanup detects the merge
    git -C $target.Path reset --hard main 2>$null

    Write-Host ""
    Write-Host "  Note: memory bank may not reflect this work" -ForegroundColor Yellow
    Write-Host "  (agent didn't run /lusena-worktree-sync)." -ForegroundColor Yellow
    Write-Host ""

    # Offer cleanup
    Write-Host "  Clean up worktree now? [Y/N] " -ForegroundColor Cyan -NoNewline
    $cleanup = Read-Host
    if ($cleanup.Trim().ToUpper() -eq 'Y') {
        Push-Location $mainRepo
        git worktree remove $target.Path --force 2>$null
        git branch -D $target.Branch 2>$null
        Pop-Location
        Write-Host "  Slot $($target.Num) cleaned." -ForegroundColor Green
    }
}

# --- Action: [D] Dev server status ---
function Invoke-DevServerStatus {
    $running = $false
    try {
        $conn = Get-NetTCPConnection -LocalPort 9292 -State Listen -ErrorAction SilentlyContinue
        if ($conn) { $running = $true }
    } catch {}

    Write-Host ""
    if ($running) {
        Write-Host "  Dev server running on port 9292." -ForegroundColor Green
    } else {
        Write-Host "  Dev server not running." -ForegroundColor Yellow
        Write-Host "  Start it? [Y/N] " -ForegroundColor Cyan -NoNewline
        $start = Read-Host
        if ($start.Trim().ToUpper() -eq 'Y') {
            Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$Host.UI.RawUI.WindowTitle = 'LUSENA Dev Server'; cd '$mainRepo'; shopify theme dev -e dev"
            Write-Host "  Dev server launching in new window." -ForegroundColor Green
        }
    }
}

# --- Main loop ---
while ($true) {
    $slots = Get-SlotStatus
    Show-Menu $slots

    $choice = Read-Host "  Choice"
    $choice = $choice.Trim().ToUpper()

    # Track whether Claude was launched (skip "Press Enter" after)
    $launchedClaude = $false

    switch ($choice) {
        'N' { Invoke-NewInstance $slots; $launchedClaude = $true }
        'R' { Invoke-ResumeInstance $slots; $launchedClaude = $true }
        'C' { Invoke-CleanInstance $slots }
        'M' { Invoke-MergeToMain $slots }
        'D' { Invoke-DevServerStatus }
        'Q' { break }
        default { Write-Host "  Invalid choice." -ForegroundColor Red }
    }

    if ($choice -eq 'Q') { break }

    if (-not $launchedClaude) {
        Write-Host ""
        Read-Host "  Press Enter to continue"
    }
}

} catch {
    Write-Host ""
    Write-Host "  ===== SCRIPT ERROR =====" -ForegroundColor Red
    Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "  Location: $($_.InvocationInfo.ScriptName):$($_.InvocationInfo.ScriptLineNumber)" -ForegroundColor Yellow
    Write-Host "  Line:     $($_.InvocationInfo.Line.Trim())" -ForegroundColor Yellow
}

Write-Host ""
Read-Host "  Press Enter to close"
