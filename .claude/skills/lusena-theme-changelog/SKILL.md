---
name: lusena-theme-changelog
description: Workflow for maintaining the LUSENA Shopify Dawn theme. Use when making substantial theme changes (Liquid/JSON/CSS/JS, templates, theme settings, cart/PDP UX) to ensure changes are validated, committed, and documented in docs/THEME_CHANGES.md.
---

# LUSENA theme changelog workflow

## Context (this repo)

- Base theme: Shopify **Dawn** (official).
- Goal: adapt Dawn for **LUSENA** (PL-first, premium feel, proof-first messaging).
- Brand source of truth: `docs/LUSENA_BrandBook_v1.md`.
- Engineering changelog: `docs/THEME_CHANGES.md` (commit-linked, semi-detailed).

## What counts as a “bigger change”

Create a commit + changelog entry when the work is meaningfully complete and would be useful to revert or reference later. Typical “bigger changes”:

- Visible UX/behavior change (header/menu behavior, PDP UX, cart behavior, new animation).
- New/removed section/snippet/block, or significant markup restructuring.
- New theme setting or changes to schema/defaults.
- Multi-file change set, or anything touching critical flows (PDP → cart → checkout).

Avoid committing tiny iteration steps (e.g. “try 1”, “adjust 2px”, “maybe fix”). Batch those locally until the result is approved.

## Workflow (for bigger changes)

### 1) Implement the change set

- Keep copy PL-first and aligned to the brandbook.
- Avoid “fixing” known baseline `shopify theme check` warnings listed in `AGENTS.md`.

### 2) Validate

- Run `shopify theme check` and ensure only the known baseline warnings remain.
- If you changed theme settings (schema/data), ensure schema constraints are respected (ranges, steps, defaults).

### 2.5) Prevent stale `(current)` entries

Before editing `docs/THEME_CHANGES.md`, ensure the existing newest detailed entry isn’t incorrectly marked as `(current)` when it already has a real commit:

- If the top detailed entry is `### (current) — ...` but `git log -1` shows a different subject, replace that entry’s `(current)` with the actual hash from `git log --oneline` (and do the same in the **All commits** summary list).
- Then add your new newest entry as `(current)` (only when the user wants a single commit).

### 3) Confirm “definition of done” (ASK THE USER)

When you believe the task is complete, ask the user explicitly:

1) “Is this the end of this task?”  
2) “Should I commit these changes?”  
3) “Should I update a changelog entry in `docs/THEME_CHANGES.md` (or another .md you specify)?”

If the user says “not done yet”, continue iterating **without committing**.

### 4) Commit (Git) — only after user confirmation

- Stage only the files relevant to the change set.
- Use a clear commit message (recommended: Conventional Commits):
  - `feat(lusena): …` for new UX/features
  - `fix(lusena): …` for bug fixes
  - `docs: …` for documentation only
  - `chore: …` for meta/infrastructure

Default: prefer **one commit per task** that includes both code changes and the `docs/THEME_CHANGES.md` update, unless the user asks to split docs into a separate commit.

**Important (avoid “extra commits”):**
- If you notice a mistake in `docs/THEME_CHANGES.md` while the task is still in progress (paths, formatting, missing files), fix it **before** committing.
- If you already committed but haven’t pushed yet, prefer `git commit --amend` (or an interactive rebase) to keep the task as a **single commit**, instead of adding follow-up “docs fix” commits.
- Only create additional commits if the user explicitly asks for separate commits, or if history-rewriting is not acceptable (e.g., commits already pushed and you can’t/shouldn’t force-push).

### 5) Update the changelog (.md)

Only do this if the user confirms they want it updated, and which file to update:

- Default: `docs/THEME_CHANGES.md`
- If the user requests a different file, update that file instead.

- Add a new entry with:
  - commit hash + commit message
  - goal (1–2 sentences)
  - “what changed” (bullets)
  - key files touched (high-signal list)
- Keep only the **latest 8** change entries detailed in `docs/THEME_CHANGES.md`.
- Keep **ALL older commit history** as a rolling summary list so it’s always possible to see everything that happened since the initial Dawn import:
  - Format (one line per commit): `<dateTime> — <hash> — <subject>`
  - Ordering: **descending by commit date/time** (newest first)
  - Content: summary only (no extra bullets)
  - Suggested source: `git log --date=iso-strict --pretty=format:"%ad — %h — %s"`

**Note on “commit hash in the same commit”:**
- If you require the changelog entry to contain the exact hash of the commit that also contains that entry, that’s not reliably achievable.
- Preferred approach for accurate hashes is: commit the code, then add the changelog entry in a follow-up `docs:` commit.
- If the user wants a single commit, write the newest entry without a hash (use `(current)` / `HEAD`) and rely on the next changelog update to record the hash once it’s in history.

Template snippet to copy:

```md
### <hash> — <commit message>

**Goal:** …

**What changed**
- …

**Key files**
- `path/to/file`
```

### 6) Sanity check in dev

- Smoke test flows impacted by the change (PDP → add to cart, cart drawer, /cart, etc.).
