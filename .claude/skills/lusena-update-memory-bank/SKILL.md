---
name: lusena-update-memory-bank
description: Update the memory bank after completing substantial theme work. Ensures a fresh session has a complete, accurate picture of the codebase, recent changes, next steps, and known issues.
---

# Update memory bank

## When to trigger

- After completing substantial theme work (new sections, migrations, deletions, architecture changes, template rewiring)
- After discovering something worth documenting for the next session (a gotcha, a pattern, a lesson learned, a decision rationale)
- Every new session starts with zero memory — the memory bank IS your memory

## Workflow

### 1. Update `memory-bank/activeContext.md` (always)

This is the most critical file — it's the first thing read every session.

- Set `*Last updated:` to today's date
- `## Current focus` — 1-line bold summary of where the project stands
- `## Recent completed work` — bullet list of what was just done (bold label + detail). Keep only the last session's work; older items graduate to `progress.md`
- `## Next steps` — numbered priority list of what comes next
- `## Known issues` — any active technical debt or gotchas
- `## Architecture note` — only update if architecture changed

### 2. Update `memory-bank/progress.md` (if milestones changed)

- Check/uncheck page status items
- Update infrastructure completed list
- Update cleanup backlog (remove items that were cleaned up)

### 3. Check & update core memory bank files (read each, update if stale)

- `memory-bank/systemPatterns.md` — update if CSS architecture, naming conventions, file structure, or technical patterns changed (e.g., new CSS layer, new naming convention, new shared component pattern)
- `memory-bank/techContext.md` — update if files were added/removed/renamed, dev tools changed, skills changed, or known warnings changed
- `memory-bank/productContext.md` — update if pages were added/removed, shared sections changed, customer journey flow changed, or snippet inventory changed
- `memory-bank/projectbrief.md` — rarely changes; update only if brand positioning, product lineup, or business strategy shifted

### 4. Update feature & pattern docs (if sections/snippets changed or new patterns emerged)

- `memory-bank/doc/features/*.md` — update section inventories and snippet lists
- `memory-bank/doc/patterns/*.md` — update if architecture, tokens, or conventions changed
- **Create new files** when a new feature page or architectural pattern was introduced (e.g., new `features/cart-page.md` when the cart page is built, or new `patterns/animation-system.md` if a reusable animation pattern emerges)
- Document lessons learned in `patterns/migration-lessons.md` if a non-obvious gotcha or technique was discovered
- Only touch/create files that are actually affected — don't update everything

### 5. Update instruction files (if conventions or architecture changed)

- `CLAUDE.md` — the primary AI instruction file
- `AGENTS.md` and `copilot-instructions.md` — keep in sync with CLAUDE.md

## Rules

- NEVER fabricate or guess information — only document what was actually done
- Keep entries concise — memory bank is for quick orientation, not detailed history
- Use past tense for completed work, imperative for next steps
- Include file paths where they help navigation
- If unsure whether a doc needs updating, read it first and check
- When in doubt, document it — a future session with zero context will thank you
- Document "why" decisions were made, not just "what" — rationale prevents re-debating the same choices
