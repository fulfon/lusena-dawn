---
name: lusena-worktree-sync
description: MANDATORY before finishing any worktree branch. Run this when work is done, before committing final changes or squash-merging to main. Updates memory bank to reflect the branch's work so the next session has accurate context.
---

# Worktree sync (branch-level memory bank update)

## Purpose

Update the memory bank to reflect this branch's work before squash-merging to main. Ensures the next session gets accurate context about what was done, without overwriting other branches' updates.

## When to use

- You are in a worktree, the feature work is done, and you are about to squash-merge to main
- The user asks to sync documentation before merging

## Prerequisites

- You are on a feature branch (not `main`)
- All code changes are committed on the branch

## Workflow

### Phase 1 — Understand what this branch changed

1. **Confirm branch and status:**
   ```bash
   git branch --show-current
   git status
   ```
   If there are uncommitted changes, ask the user whether to commit them first.

2. **Get the branch diff (three-dot = only this branch's changes):**
   ```bash
   git diff main...HEAD --stat
   git diff main...HEAD --name-only
   ```
   For detailed content analysis, read the full diff for non-trivial files:
   ```bash
   git diff main...HEAD -- sections/ snippets/ assets/ templates/
   ```

3. **Review commit messages for context:**
   ```bash
   git log main..HEAD --oneline
   ```

4. **Categorize changes** into buckets:
   - Liquid sections/snippets (new, modified, deleted)
   - CSS/JS assets
   - Templates (JSON)
   - Skills / config
   - Documentation (if any manual memory bank edits were made during the branch)

5. **Summarize** in 2-3 sentences what the branch did. Present to user for confirmation before proceeding.

### Phase 2 — Read memory bank from current main

**Critical:** Read from current `main`, not the stale worktree copies. This prevents merge conflicts when squash-merging.

Always read these (use `git show main:<path>` for each):
```bash
git show main:memory-bank/activeContext.md
git show main:memory-bank/progress.md
```

Conditionally read (only if the branch touched relevant areas):
```bash
git show main:memory-bank/systemPatterns.md        # if patterns/architecture changed
git show main:memory-bank/techContext.md            # if files added/removed/renamed
git show main:memory-bank/productContext.md         # if pages/UX/journey changed
git show main:memory-bank/projectbrief.md           # rarely needed
```

For feature/pattern docs, read from main only the ones that are relevant to this branch's changes:
```bash
git show main:memory-bank/doc/features/<relevant>.md
git show main:memory-bank/doc/patterns/<relevant>.md
```

### Phase 3 — Determine what to update

For each file read in Phase 2, determine:
- **Stale content** — info that no longer matches after this branch's changes
- **Missing content** — new work not yet documented

Build a short checklist and present it:
```
Will update:
  - activeContext.md — add this branch's work to recent completed
  - progress.md — check off milestone X
  - doc/features/pdp.md — new section added

No changes needed:
  - systemPatterns.md — still accurate
```

### Phase 4 — Apply updates with Edit tool (NEVER Write)

**CRITICAL: Use the Edit tool for all memory bank updates, not Write.** The Write tool replaces the entire file, which causes merge conflicts during squash-merge because Git sees a full-file rewrite instead of a surgical addition. The Edit tool produces clean diffs that Git can auto-merge.

**Workflow:**
1. First, ensure the worktree copy matches main: `git checkout main -- memory-bank/<file>` for each file you need to update. This gives you the current main version to edit against.
2. Then use the Edit tool to make targeted changes (insert new sections, modify specific lines).
3. Never rewrite an entire file — only touch the lines that need changing.

#### `activeContext.md` (always update)
- Edit `*Last updated:` date to today
- Edit `## Current focus` — only if the project focus shifted
- **INSERT** this branch's entry at the top of `## Recent completed work` (before existing entries). Use format: `### Branch-name (date)` followed by bullet list
- Edit `## Next steps` — only if priorities changed
- Edit `## Known issues` — add new or remove resolved, leave others untouched

#### `progress.md` (if milestones changed)
- Edit specific checkbox lines to check/uncheck
- Insert new infrastructure items at the appropriate position

#### Other files (only if directly affected)
- `systemPatterns.md` — new patterns, CSS architecture changes
- `techContext.md` — files added/removed/renamed, new skills
- `productContext.md` — pages/UX/journey changes
- `doc/features/*.md` — section inventories, snippet lists
- `doc/patterns/*.md` — CSS architecture, spacing, tokens

### Phase 5 — Commit and confirm

1. Stage all updated memory bank files:
   ```bash
   git add memory-bank/
   ```

2. Commit on the branch:
   ```bash
   git commit -m "docs: sync memory bank for <branch-name>"
   ```

3. Confirm to the user:
   > "Memory bank synced. Updated: [list of files]. Ready to squash-merge to main."

Then proceed with the standard squash-merge workflow per CLAUDE.md.

## Rules

- NEVER fabricate or guess information — only document what was actually done
- NEVER replace "Recent completed work" entries from other branches — always additive
- Keep entries concise — memory bank is for quick orientation, not history
- Use past tense for completed work, imperative for next steps
- Document "why" for non-obvious decisions, not just "what"
- If a memory bank file on main doesn't exist yet (new file needed), flag it but do NOT create it — that's the audit skill's job
