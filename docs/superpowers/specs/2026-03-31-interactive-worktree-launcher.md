# Interactive Worktree Launcher

**Date:** 2026-03-31
**Status:** Approved
**Scope:** Replace `scripts/launch-claude-worktree.ps1` with an interactive menu-based launcher

## Problem

The current launcher auto-creates a new worktree on every launch and auto-cleans empty ones on startup. This causes:

1. **Lost context** - closing a terminal window kills the Claude process; there is no way to return to that conversation
2. **No resume path** - the launcher always creates new instances, never offers to resume existing ones
3. **Aggressive cleanup** - empty worktrees (agent was thinking/reading but hadn't written files yet) are silently deleted on next launch
4. **No control surface** - no menu to inspect, clean, or merge specific worktrees

Claude Code now has native `--resume` (session persistence) and `--name` (named sessions), which solve the context loss problem if the launcher exposes them.

## Design decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| No tmux | `--resume` is sufficient | Simpler, no extra tooling on Windows |
| 4-slot hard cap | Matches Shopify theme pool | Each slot needs a preview theme for browser testing |
| All 4 occupied | Block, don't auto-clean | User controls cleanup explicitly |
| Agent merges (primary) | CLAUDE.md workflow unchanged | Agent runs `/lusena-worktree-sync` before merge |
| Menu merges (fallback) | For when agent didn't finish | Shows warning about memory bank |
| No lock files | No auto-cleanup = no race risk | Git operations are atomic; errors are graceful |
| Auto commit message | Derived from branch name | `feat/pdp-redesign` -> `feat(lusena): pdp redesign` |

## Architecture

### Files changed

| File | Change |
|------|--------|
| `scripts/launch-claude-worktree.ps1` | Full rewrite - interactive menu |
| `Desktop\Claude-LUSENA.bat` | No change (still calls the same script) |
| `config/worktree-themes.json` | No change (same slot-to-theme mapping) |
| `CLAUDE.md` | Minor updates to worktree section wording |
| `.claude/settings.json` | No change |

### Menu layout

```
  LUSENA Claude Code
  ----------------------------------------

  Worktrees:
   1  feat/pdp-redesign     3 commits
   2  fix/checkout-bug      uncommitted changes!
   3  (empty)
   4  --

  [N] New instance         [R] Resume instance
  [C] Clean instance       [M] Merge to main
  [D] Dev server status    [Q] Quit

  Choice:
```

### Slot display logic

| Condition | Display |
|-----------|---------|
| Worktree dir exists + `.git` file present + commits ahead of main | Branch name + `N commits` |
| Worktree dir exists + `.git` file present + uncommitted changes | Branch name + `uncommitted changes!` |
| Worktree dir exists + `.git` file present + no changes | `(empty)` |
| Worktree dir exists + `.git` file MISSING | `(orphaned)` |
| No worktree dir | `--` |

Orphaned slots are treatable by [C] (clean) - the cleanup just removes the directory since there's no git state to unwind.

**Parent repo hazard:** `C:\Users\Karol\Documents\BusinessIdeas\SilkStore\` is itself a git repo. The worktrees directory (`lusena-worktrees/`) sits inside its tree. When a worktree's `.git` file is missing, git commands resolve upward to this parent repo and return wrong results. **Rule: never run git commands inside a worktree directory without first confirming `<slot>/.git` exists.** For orphaned slots, skip all git inspection and only allow directory removal.

### Pre-scan housekeeping

Before building the slot table on each menu loop iteration, run silently:

1. `git -C <mainRepo> worktree prune` — cleans stale internal worktree references (e.g., directory was manually deleted but git still tracks it). Fast, no side effects.

### Script lifecycle

```
.bat launch
  -> PowerShell script starts
  -> Dev server check (same as current)
  -> while (true) loop:
      -> Scan slots 1-4, build status table
      -> Display menu
      -> Read user choice
      -> Execute action
      -> If action launched Claude: wait for exit, then loop back to menu
      -> If Q: break loop, exit script
```

The window stays open until the user explicitly quits. Closing the terminal window is safe - the worktree and any Claude sessions persist on disk.

## Action details

### [N] New instance

1. Scan slots 1-4 for first slot with no worktree directory
2. If all 4 occupied: print "All slots in use. Clean one first." -> back to menu
3. If branch `work/<N>` already exists (stale from a previous incomplete cleanup): delete it with `git branch -d work/<N>` before proceeding
4. `git worktree add <worktreeBase>/lusena-<N> -b work/<N> main`
4. `cd` into the new worktree
5. Launch `claude --name "lusena-<N>"`
6. On Claude exit -> back to menu. Worktree stays. No cleanup.

### [R] Resume instance

1. Show only occupied slots (worktree dir exists)
2. If none occupied: "No active worktrees." -> back to menu
3. User enters slot number
4. `cd` into that worktree
5. Launch `claude --resume` (opens interactive session picker scoped to that directory)
6. If no previous sessions exist, Claude starts fresh - files are still there from the previous instance
7. On Claude exit -> back to menu

### [C] Clean instance

1. Show occupied slots with status (branch, commit count, uncommitted flag)
2. User enters slot number
3. If slot has uncommitted changes or commits ahead of main:
   - Print warning: "This worktree has [uncommitted changes / N unmerged commits]. Work will be lost."
   - Prompt: "Are you sure? [Y/N]"
   - If N -> back to menu
4. Run cleanup:
   - `git worktree remove <path> --force`
   - `git branch -D <branch>` (force delete since commits may not be merged)
5. Print "Slot N cleaned." -> back to menu

### [M] Merge to main

1. Show only slots that have commits ahead of main (exclude empty, uncommitted-only, no-dir)
2. If none qualify: "No worktrees with commits to merge." -> back to menu
3. User enters slot number
4. If slot has uncommitted changes: "Cannot merge - uncommitted changes. Commit or clean first." -> back to menu
5. Show commit list for the branch
6. Check main repo working tree: `git -C <mainRepo> status --porcelain`
   - If dirty: "Main repo has uncommitted changes. Resolve before merging." -> back to menu
7. Derive commit message from branch name:
   - `feat/pdp-redesign` -> `feat(lusena): pdp redesign`
   - `fix/checkout-bug` -> `fix(lusena): checkout bug`
   - `docs/update-readme` -> `docs: update readme`
   - `chore/cleanup` -> `chore: cleanup`
   - `work/N` (unrenamed) -> `feat(lusena): worktree N changes`
   - Rule: prefix before `/` is commit type. `feat` and `fix` get `(lusena)` scope. Hyphens after `/` become spaces.
8. Print the derived commit message for visibility
9. Execute:
   - `git -C <mainRepo> merge --squash <branch>`
   - If merge conflict: `git -C <mainRepo> merge --abort`, print "Merge conflict. Resolve manually." -> back to menu
   - `git -C <mainRepo> commit -m "<derived message>"`
10. Print warning: "Note: memory bank may not reflect this work (agent didn't run /lusena-worktree-sync)."
11. Prompt: "Clean up worktree now? [Y/N]"
    - If Y: same cleanup as [C] (no confirmation needed since we just merged)
    - If N: worktree stays (user may want to resume for more work)
12. Back to menu

### [D] Dev server status

1. Check `Get-NetTCPConnection -LocalPort 9292 -State Listen`
2. If running: "Dev server running on port 9292."
3. If not running: "Dev server not running. Start it? [Y/N]"
   - If Y: launch in new window (same as current script)
4. Back to menu

## Commit message derivation

```
Input branch name        -> Output commit message
feat/pdp-redesign        -> feat(lusena): pdp redesign
fix/checkout-bug         -> fix(lusena): checkout bug
docs/update-readme       -> docs: update readme
chore/cleanup-dead-code  -> chore: cleanup dead code
work/2                   -> feat(lusena): worktree 2 changes
```

Algorithm:
1. Split branch name on first `/` -> prefix, rest
2. Replace hyphens in rest with spaces
3. If prefix is `feat` or `fix`: message = `<prefix>(lusena): <rest>`
4. If prefix is `docs` or `chore`: message = `<prefix>: <rest>`
5. If prefix is `work`: message = `feat(lusena): worktree <rest> changes`

## CLAUDE.md updates

Minor wording changes in the "Git Workflow" and "Worktree Development" sections:

- Remove: "The launcher cleanup script will remove the worktree and free the slot on next startup"
- Update: "Your branch is pre-created with a generic name like `work/1`" - stays accurate
- Update: "Rename the branch immediately" - stays accurate
- Add: "When you exit, the worktree persists. The user can resume your session later with the launcher menu."
- Keep all Shopify theme push workflow, memory bank sync, and merge instructions unchanged

## What stays the same

- `config/worktree-themes.json` - slot-to-theme mapping
- `.claude/hooks/branch-guard.sh` - blocks commits on main
- `.claude/hooks/session-context.sh` - injects active context
- All CLAUDE.md agent behavior (theme push, memory bank sync, branch naming)
- All skills (`lusena-worktree-sync`, `lusena-preview-check`, etc.)
- The `.bat` desktop shortcut (still calls the same script path)

## What goes away

- Auto-cleanup of empty worktrees on startup
- Auto-cleanup of stale branches on startup
- `.claude-lock` file mechanism
- Post-exit auto-merge flow
- Post-exit "uncommitted changes" manual instructions printout

All of these are replaced by explicit menu actions that the user controls.
