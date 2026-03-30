# Memory Bank Skills Rework

**Date:** 2026-03-30
**Status:** Approved (via conversation)
**Replaces:** `lusena-pre-commit-sync`, `lusena-update-memory-bank`

## Problem

The old memory bank skills were designed for a "work on main with uncommitted changes" workflow. The project has moved to a worktree-based workflow where:
- Each Claude Code instance works in an isolated git worktree on a feature branch
- Changes are committed on the branch, then squash-merged to main
- Multiple instances can run in parallel

The old `lusena-pre-commit-sync` relied on `git diff` of uncommitted changes, which sees nothing in the new workflow (everything is committed). The old `lusena-update-memory-bank` had no git awareness at all.

## Design

### Two-tier skill system

**Skill 1: `lusena-worktree-sync` (branch-level, small)**

- **When:** Run in the worktree before squash-merging to main
- **Purpose:** Update memory bank files to reflect this branch's work
- **How it knows what changed:** `git diff main...HEAD` (three-dot) - shows only this branch's changes since it forked from main, regardless of what happened on main since
- **Conflict prevention:** Reads memory bank files from current main (`git show main:<path>`) instead of the stale worktree copy. This ensures updates are based on the latest state, so the squash-merge applies cleanly.
- **Update style:** Additive - adds this branch's entry to "Recent completed work," preserves existing entries from other branches
- **Scope:** Updates only docs directly affected by the branch's changes (activeContext always, others conditionally)
- **Does NOT:** Create new docs, restructure anything, touch git tags
- **Output:** Commits memory bank updates on the branch (included in the squash-merge)

**Skill 2: `lusena-memory-bank-audit` (periodic, big)**

- **When:** Manually triggered after ~10 merges accumulate on main
- **Purpose:** Two-pass comprehensive review:
  1. **Content verification** - re-read every memory bank file against the actual codebase state. Fix stale values, wrong paths, outdated sizes, incorrect statuses that small syncs missed.
  2. **Structural review** - evaluate whether the documentation structure still fits. Do we need new docs? Should something be split or merged? Have 10 small branches collectively shifted the project in a way no single branch noticed? Are there new patterns that emerged across branches?
- **Tracking:** Uses git tags (`memory-bank-audit/YYYY-MM-DD`). Each audit diffs from the last tag to current main HEAD. On first run, falls back to the last `docs: memory bank audit` commit.
- **Scope:** Everything - all memory bank files, feature docs, pattern docs, product docs, CLAUDE.md references
- **Output:** Updates all stale docs, creates new docs if needed, restructures if needed, tags main, commits

### Key technical decisions

1. **Three-dot diff (`main...HEAD`)** for the small skill - shows only this branch's changes since the fork point, ignoring main's movement. Used for analysis only (not merging).
2. **Read from current main** before updating memory bank files - prevents merge conflicts in documentation files across parallel worktrees.
3. **Git tags for audit tracking** - clean, visible in history, no extra files to manage.
4. **Additive updates** to shared sections like "Recent completed work" - preserves other branches' entries.

### What gets deleted

- `.claude/skills/lusena-pre-commit-sync/` - replaced by `lusena-worktree-sync`
- `.claude/skills/lusena-update-memory-bank/` - replaced by `lusena-memory-bank-audit`
- CLAUDE.md references updated to point to new skills
