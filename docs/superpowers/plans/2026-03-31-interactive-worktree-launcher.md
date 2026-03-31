# Interactive Worktree Launcher - Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the auto-create/auto-clean worktree launcher with an interactive menu that supports resume, manual cleanup, and merge.

**Architecture:** Single PowerShell script rewrite (`scripts/launch-claude-worktree.ps1`). The script runs a `while ($true)` loop showing a slot status table and action menu. Each action is a self-contained function. No external dependencies beyond git and the `claude` CLI.

**Tech Stack:** PowerShell 5.1+ (ships with Windows), Git, Claude Code CLI

**Spec:** `docs/superpowers/specs/2026-03-31-interactive-worktree-launcher.md`

---

### Task 1: Script skeleton with constants and main loop

**Files:**
- Rewrite: `scripts/launch-claude-worktree.ps1`

- [ ] **Step 1: Write the script skeleton**

Replace the entire contents of `scripts/launch-claude-worktree.ps1` with:

```powershell
# LUSENA - Interactive Claude Code Worktree Launcher
# Double-click the .bat wrapper on your Desktop to use this.

try {

$mainRepo = "C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-dawn"
$worktreeBase = "C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-worktrees"
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
                    if ($commitLog) { $slot.Commits = ($commitLog | Measure-Object).Count }
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

# --- Main loop placeholder (actions added in subsequent tasks) ---
while ($true) {
    $slots = Get-SlotStatus
    Show-Menu $slots

    $choice = Read-Host "  Choice"
    $choice = $choice.Trim().ToUpper()

    switch ($choice) {
        'N' { Write-Host "  [N] Not implemented yet" -ForegroundColor Yellow }
        'R' { Write-Host "  [R] Not implemented yet" -ForegroundColor Yellow }
        'C' { Write-Host "  [C] Not implemented yet" -ForegroundColor Yellow }
        'M' { Write-Host "  [M] Not implemented yet" -ForegroundColor Yellow }
        'D' { Write-Host "  [D] Not implemented yet" -ForegroundColor Yellow }
        'Q' { break }
        default { Write-Host "  Invalid choice." -ForegroundColor Red }
    }

    if ($choice -eq 'Q') { break }

    Write-Host ""
    Read-Host "  Press Enter to continue"
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
```

- [ ] **Step 2: Verify the script runs and shows the menu**

Run from the main repo directory:
```bash
powershell -ExecutionPolicy Bypass -File scripts/launch-claude-worktree.ps1
```
Expected: Menu shows with all 4 slots as `--` (or showing any existing worktrees). Press Q to exit cleanly.

- [ ] **Step 3: Commit**

```bash
git add scripts/launch-claude-worktree.ps1
git commit -m "feat(lusena): script skeleton with slot scanner and menu display"
```

---

### Task 2: [N] New instance action

**Files:**
- Modify: `scripts/launch-claude-worktree.ps1` (replace the `'N'` placeholder in the switch)

- [ ] **Step 1: Add the New Instance function**

Add this function after the `Show-Menu` function, before the main loop:

```powershell
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
}
```

- [ ] **Step 2: Wire it into the switch**

Replace:
```powershell
        'N' { Write-Host "  [N] Not implemented yet" -ForegroundColor Yellow }
```
With:
```powershell
        'N' { Invoke-NewInstance $slots }
```

- [ ] **Step 3: Verify by running the script**

Run the script. Press N. Expected: worktree created, Claude Code launches. Type `/exit` in Claude. Expected: returns to menu. Slot now shows `(empty)` with branch `work/N`.

- [ ] **Step 4: Commit**

```bash
git add scripts/launch-claude-worktree.ps1
git commit -m "feat(lusena): [N] new instance action"
```

---

### Task 3: [R] Resume instance action

**Files:**
- Modify: `scripts/launch-claude-worktree.ps1` (replace the `'R'` placeholder in the switch)

- [ ] **Step 1: Add the Resume Instance function**

Add after the `Invoke-NewInstance` function:

```powershell
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
    claude --resume
    Set-Location $mainRepo
}
```

- [ ] **Step 2: Wire it into the switch**

Replace:
```powershell
        'R' { Write-Host "  [R] Not implemented yet" -ForegroundColor Yellow }
```
With:
```powershell
        'R' { Invoke-ResumeInstance $slots }
```

- [ ] **Step 3: Verify**

Run the script. First use [N] to create a worktree and have a brief Claude session (type `/exit`). Then press [R], pick that slot. Expected: `claude --resume` opens session picker showing the previous session for that directory.

- [ ] **Step 4: Commit**

```bash
git add scripts/launch-claude-worktree.ps1
git commit -m "feat(lusena): [R] resume instance action"
```

---

### Task 4: [C] Clean instance action

**Files:**
- Modify: `scripts/launch-claude-worktree.ps1` (replace the `'C'` placeholder in the switch)

- [ ] **Step 1: Add the Clean Instance function**

Add after the `Invoke-ResumeInstance` function:

```powershell
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
        Remove-Item -Recurse -Force $target.Path -ErrorAction SilentlyContinue
        Write-Host "  Slot $($target.Num) cleaned (orphaned directory removed)." -ForegroundColor Green
        return
    }

    # Warn if there's work
    if ($target.Uncommitted -or $target.Commits -gt 0) {
        Write-Host ""
        if ($target.Uncommitted -and $target.Commits -gt 0) {
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

    Write-Host "  Slot $($target.Num) cleaned." -ForegroundColor Green
}
```

- [ ] **Step 2: Wire it into the switch**

Replace:
```powershell
        'C' { Write-Host "  [C] Not implemented yet" -ForegroundColor Yellow }
```
With:
```powershell
        'C' { Invoke-CleanInstance $slots }
```

- [ ] **Step 3: Verify**

Create a worktree with [N], exit Claude, then [C] that slot. Expected: asks for slot, shows "(empty)" status, cleans without warning. Slot shows `--` on next menu refresh.

Test with a slot that has commits: create worktree, make a commit in it, then [C]. Expected: warning about unmerged commits, Y/N prompt.

- [ ] **Step 4: Commit**

```bash
git add scripts/launch-claude-worktree.ps1
git commit -m "feat(lusena): [C] clean instance action"
```

---

### Task 5: [M] Merge to main action

**Files:**
- Modify: `scripts/launch-claude-worktree.ps1` (replace the `'M'` placeholder in the switch)

- [ ] **Step 1: Add the Merge to Main function**

Add after the `Invoke-CleanInstance` function:

```powershell
# --- Action: [M] Merge to main ---
function Invoke-MergeToMain {
    param($slots)

    $mergeable = $slots | Where-Object { $_.Exists -and -not $_.Orphaned -and $_.Commits -gt 0 }

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
```

- [ ] **Step 2: Wire it into the switch**

Replace:
```powershell
        'M' { Write-Host "  [M] Not implemented yet" -ForegroundColor Yellow }
```
With:
```powershell
        'M' { Invoke-MergeToMain $slots }
```

- [ ] **Step 3: Verify**

Create a worktree with [N], make a test commit inside it (e.g., add a temp file), exit Claude, then [M] that slot. Expected: shows commit list, derives commit message from branch name, merges, offers cleanup.

- [ ] **Step 4: Commit**

```bash
git add scripts/launch-claude-worktree.ps1
git commit -m "feat(lusena): [M] merge to main action"
```

---

### Task 6: [D] Dev server status action

**Files:**
- Modify: `scripts/launch-claude-worktree.ps1` (replace the `'D'` placeholder in the switch)

- [ ] **Step 1: Add the Dev Server Status function**

Add after the `Invoke-MergeToMain` function:

```powershell
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
```

- [ ] **Step 2: Wire it into the switch**

Replace:
```powershell
        'D' { Write-Host "  [D] Not implemented yet" -ForegroundColor Yellow }
```
With:
```powershell
        'D' { Invoke-DevServerStatus }
```

- [ ] **Step 3: Verify**

Run the script. Press D. Expected: shows whether dev server is running. If not running, offers to start it.

- [ ] **Step 4: Commit**

```bash
git add scripts/launch-claude-worktree.ps1
git commit -m "feat(lusena): [D] dev server status action"
```

---

### Task 7: Remove "Press Enter to continue" for actions that launch Claude

**Files:**
- Modify: `scripts/launch-claude-worktree.ps1` (main loop)

- [ ] **Step 1: Skip the "Press Enter" prompt after Claude exits**

The main loop currently has a `Read-Host "Press Enter to continue"` after every action. This is useful for short actions (C, D, M) so you can read the output, but annoying after [N] and [R] because Claude already occupied the screen — you want to go straight back to the menu.

Replace the main loop (everything from `while ($true)` to the closing `}` before the `catch` block) with:

```powershell
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
```

- [ ] **Step 2: Verify**

Run the script. Use [D] — should show "Press Enter to continue" after. Use [N] then /exit from Claude — should go straight back to menu without the prompt.

- [ ] **Step 3: Commit**

```bash
git add scripts/launch-claude-worktree.ps1
git commit -m "feat(lusena): skip enter prompt after Claude exits"
```

---

### Task 8: Update CLAUDE.md worktree sections

**Files:**
- Modify: `CLAUDE.md:82-101` (Worktree-based parallel instances + Branch rules)
- Modify: `CLAUDE.md:142-167` (Finishing work in a worktree)

- [ ] **Step 1: Update "Worktree-based parallel instances" section**

In `CLAUDE.md`, replace line 82-91:

```markdown
### Worktree-based parallel instances

The owner runs multiple Claude Code instances in parallel. Each instance is launched via `Desktop\Claude-LUSENA.bat`, which creates an **isolated git worktree** (script: `scripts/launch-claude-worktree.ps1`). This means:

- **You are NOT in the main repo.** Your working directory is something like `..\lusena-worktrees\lusena-2`, not `lusena-dawn`. This is intentional — it gives you an isolated copy so you don't interfere with other running instances.
- **Your branch is pre-created** with a generic name like `work/1`, `work/2`, etc. The launcher script did this for you.
- **Rename the branch immediately** once you understand the task. Use `git branch -m <new-name>` with the standard prefixes: `feat/`, `fix/`, `docs/`, `chore/`. Example: `git branch -m feat/remove-legacy-upsell`.
- **Do NOT run `git checkout -b`** — you're already on your own branch. Just rename it.
- **The main repo lives at:** `C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-dawn`. **NEVER read, edit, or write files using the main repo path.** A PreToolUse hook blocks Edit/Write to `lusena-dawn/` from worktrees. Every file you need exists in your worktree copy — always use relative paths (e.g., `scripts/launch-claude-worktree.ps1`) or your worktree absolute path (e.g., `C:\...\lusena-worktrees\lusena-1\scripts\...`). If you Glob/Grep and find a file at both paths, pick the worktree path.
- If your current branch is literally `main`, you were launched directly in the main repo (not via the worktree launcher). In that case, create a branch before any changes: `git checkout -b feat/<short-description>`.
```

With:

```markdown
### Worktree-based parallel instances

The owner runs multiple Claude Code instances in parallel via `Desktop\Claude-LUSENA.bat`, which opens an **interactive menu** (script: `scripts/launch-claude-worktree.ps1`). The menu manages up to 4 worktree slots — creating, resuming, cleaning, and merging instances. This means:

- **You are NOT in the main repo.** Your working directory is something like `..\lusena-worktrees\lusena-2`, not `lusena-dawn`. This is intentional — it gives you an isolated copy so you don't interfere with other running instances.
- **Your branch is pre-created** with a generic name like `work/1`, `work/2`, etc. The launcher did this for you.
- **Rename the branch immediately** once you understand the task. Use `git branch -m <new-name>` with the standard prefixes: `feat/`, `fix/`, `docs/`, `chore/`. Example: `git branch -m feat/remove-legacy-upsell`.
- **Do NOT run `git checkout -b`** — you're already on your own branch. Just rename it.
- **The main repo lives at:** `C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-dawn`. **NEVER read, edit, or write files using the main repo path.** A PreToolUse hook blocks Edit/Write to `lusena-dawn/` from worktrees. Every file you need exists in your worktree copy — always use relative paths (e.g., `scripts/launch-claude-worktree.ps1`) or your worktree absolute path (e.g., `C:\...\lusena-worktrees\lusena-1\scripts\...`). If you Glob/Grep and find a file at both paths, pick the worktree path.
- **When you exit, the worktree persists.** The user can resume your session later via the launcher menu's [R] option, which uses `claude --resume` to restore your full conversation history.
- If your current branch is literally `main`, you were launched directly in the main repo (not via the worktree launcher). In that case, create a branch before any changes: `git checkout -b feat/<short-description>`.
```

- [ ] **Step 2: Update "Finishing work in a worktree" section**

In `CLAUDE.md`, replace line 165:

```markdown
7. The launcher cleanup script will remove the worktree and free the slot on next startup
```

With:

```markdown
7. The worktree persists after you exit. The user can resume, clean, or merge it via the launcher menu.
```

- [ ] **Step 3: Verify CLAUDE.md reads correctly**

Read through the updated sections to confirm they are coherent and consistent with the new launcher behavior.

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: update worktree sections for interactive launcher"
```

---

### Task 9: End-to-end manual verification

No files changed — this is a verification task.

- [ ] **Step 1: Clean slate**

Remove any test worktrees created during development. Verify all 4 slots show `--`.

- [ ] **Step 2: Test [N] New instance**

Press N. Verify: worktree created, Claude launches with `--name lusena-N`, `/exit` returns to menu, slot shows `(empty)`.

- [ ] **Step 3: Test [R] Resume instance**

Press R, pick the slot from step 2. Verify: `claude --resume` opens session picker, previous session visible, selecting it restores context.

- [ ] **Step 4: Test [C] Clean instance (empty slot)**

Press C, pick the empty slot. Verify: no warning, slot cleaned, shows `--`.

- [ ] **Step 5: Test [N] + commit + [M] Merge**

Press N to create a new worktree. Inside Claude, make a test file and commit. Exit Claude. Press M, pick the slot. Verify: commit list shown, commit message derived from branch, merged to main, cleanup offered.

- [ ] **Step 6: Test [D] Dev server status**

Press D. Verify: shows running/not running correctly. If not running, start offer works.

- [ ] **Step 7: Test orphaned slot handling**

Manually delete a worktree's `.git` file (simulate corruption). Re-enter menu. Verify: slot shows `(orphaned)`. Use [C] to clean it.

- [ ] **Step 8: Test all-slots-full block**

Create worktrees in all 4 slots. Press N. Verify: "All 4 slots in use. Clean one first."

- [ ] **Step 9: Clean up and final commit**

Clean all test worktrees. Verify clean state.

```bash
git add -A
git commit -m "feat(lusena): interactive worktree launcher complete"
```
