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
- If there are more than 8 entries, compress anything older than the newest 8 into an **Older commits (summary only)** list (hash + subject only, no details).

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
