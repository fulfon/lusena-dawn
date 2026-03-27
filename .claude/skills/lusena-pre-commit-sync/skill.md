---
name: lusena-pre-commit-sync
description: Pre-commit documentation sync. Analyzes all uncommitted changes against the current branch, reads the entire memory bank, identifies documentation gaps, updates all affected files (activeContext, progress, features, patterns, changelog, etc.), and creates new docs when needed. Run this before committing to ensure the memory bank accurately reflects the codebase.
---

# Pre-commit documentation sync

## Purpose

Ensure the memory bank is fully in sync with all uncommitted changes before committing. This is the comprehensive "measure twice, cut once" pass — every memory bank file is checked and updated if needed, the changelog gets a new entry, and missing documentation is created.

## When to use

- You have uncommitted changes ready to commit (one or many tasks batched together)
- Before any substantial commit to ensure documentation parity
- After a work session with parallel changes across multiple areas

## Workflow

### Phase 1 — Understand what changed

1. **Determine the branch:**
   ```bash
   git branch --show-current
   ```

2. **Get full picture of uncommitted changes:**
   ```bash
   git status
   git diff --stat
   git diff --name-only
   git diff          # full diff for content analysis
   ```
   For untracked files, read them to understand their content.

3. **Categorize changes** into buckets:
   - Liquid sections/snippets (new, modified, deleted)
   - CSS/JS assets
   - Templates (JSON)
   - Documentation (docs/, memory-bank/)
   - Skills (.claude/skills/, .agent/skills/, etc.)
   - Config / other

4. **Summarize the work** in your own words — what was done, why, and what areas of the store are affected. Present this summary to the user for confirmation before proceeding.

### Phase 2 — Read the entire memory bank

Read ALL of these files (use parallel reads where possible):

**Core files (always read):**
- `memory-bank/activeContext.md`
- `memory-bank/progress.md`
- `memory-bank/systemPatterns.md`
- `memory-bank/techContext.md`
- `memory-bank/productContext.md`
- `memory-bank/projectbrief.md`

**Feature docs (read all):**
- `memory-bank/doc/features/*.md`

**Pattern docs (read all):**
- `memory-bank/doc/patterns/*.md`

**Product docs (read only if product-related changes detected):**
- `memory-bank/doc/products/*.md`

**Bundle strategy (read only if bundle-related changes detected):**
- `memory-bank/doc/bundle-strategy.md`

### Phase 3 — Gap analysis

For each memory bank file, determine:

1. **Stale content** — information that no longer matches the codebase after these changes
2. **Missing content** — new features, patterns, files, or decisions not yet documented
3. **New file needed** — a change introduces something that doesn't fit any existing doc (e.g., a new page type, a new architectural pattern, a new product)

Build a checklist of files to update/create. Present it to the user:
```
Files to update:
  - memory-bank/activeContext.md — update current focus and recent work
  - memory-bank/progress.md — check off completed milestones
  - memory-bank/doc/features/pdp.md — new section added
Files to create:
  - memory-bank/doc/features/contact-page.md — new page not yet documented

No changes needed:
  - memory-bank/systemPatterns.md — still accurate
  - memory-bank/projectbrief.md — unchanged
```

### Phase 4 — Update everything

Execute all updates. Follow these rules per file:

#### `activeContext.md` (always update)
- Set `*Last updated:` to today's date
- `## Current focus` — 1-line bold summary of where the project stands
- `## Recent completed work` — bullet list of what was just done. Keep only the latest session's work; older items move to progress.md
- `## Next steps` — numbered priority list
- `## Known issues` — active technical debt or gotchas
- `## Architecture note` — only if architecture changed

#### `progress.md` (update if milestones changed)
- Check/uncheck page status items
- Update infrastructure completed list
- Update cleanup backlog

#### `systemPatterns.md` (update if patterns changed)
- CSS architecture, naming conventions, file structure, technical patterns

#### `techContext.md` (update if files/tools changed)
- Files added/removed/renamed, dev tools, skills, known warnings

#### `productContext.md` (update if pages/UX changed)
- Pages added/removed, shared sections, customer journey, snippet inventory

#### `projectbrief.md` (rarely — only if brand/product scope shifted)

#### Feature docs `doc/features/*.md` (update if sections/pages changed)
- Section inventories, snippet lists, template structure
- Create new files for new pages or major features

#### Pattern docs `doc/patterns/*.md` (update if architecture/conventions changed)
- CSS architecture, spacing system, brand tokens, migration lessons

#### Product docs `doc/products/*.md` (update if product data changed)
- Metafields, pricing, variants, SEO

### Phase 5 — Summary

Present to the user:
1. List of all files updated/created
2. Brief description of what changed in each
3. Confirmation that memory bank is in sync

Then say: **"Memory bank is synced. Ready to commit — would you like me to create the commit?"**

If the user confirms, stage all changed files and commit with a conventional commit message. Include both code changes and documentation in one commit unless the user asks to split them.

## Rules

- NEVER fabricate or guess information — only document what was actually done
- Keep entries concise — memory bank is for quick orientation, not detailed history
- Use past tense for completed work, imperative for next steps
- Include file paths where they help navigation
- Document "why" decisions were made, not just "what"
- If unsure whether a doc needs updating, err on the side of updating it
- When creating new files, follow the structure of existing similar files
- Do NOT update `CLAUDE.md`, `AGENTS.md`, or `copilot-instructions.md` unless the user explicitly asks — those are separate concerns
