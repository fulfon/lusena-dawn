# LUSENA Shopify Theme

## Memory Bank

Your memory resets every session. This project uses a persistent memory bank for context continuity.

**At the start of every substantial task, read:**
1. `memory-bank/activeContext.md` — current focus, pending decisions, next steps
2. `memory-bank/progress.md` — what is done, what is pending

**For deeper context (read on demand when relevant to your task):**
- `memory-bank/projectbrief.md` — brand identity, positioning, products
- `memory-bank/productContext.md` — store pages, customer journey, UX goals
- `memory-bank/systemPatterns.md` — CSS architecture, spacing, naming conventions
- `memory-bank/techContext.md` — file paths, dev tools, skills, known warnings

**After completing substantial work, update:**
- `memory-bank/activeContext.md` — what changed, new decisions, shifted next steps
- `memory-bank/progress.md` — if milestones or page status changed

## Project Identity

This repository is the **LUSENA** Shopify theme — a premium Polish silk e-commerce store built on top of Dawn (v15.4.1). LUSENA is PL-first with premium feel and proof-first messaging. Products: silk pillowcases, bonnets, scrunchies, eye masks, heatless curlers, and bundles.

### LUSENA vs Dawn: dual-layer architecture

Custom LUSENA sections/snippets (`lusena-*` prefix) are layered on top of Dawn's base. Always check `lusena-*` files first — they override Dawn's defaults for all customer-facing surfaces.

Dawn's original sections remain in the repo but are NOT used on the live storefront. They may still be referenced by inactive templates or the theme editor.

**Rule of thumb:** If a `lusena-*` file exists for a component, edit that file. Only touch Dawn files when the feature genuinely relies on Dawn's implementation (e.g., cart drawer, base CSS variables, layout files).

### Key references

- **UI/UX brandbook (source of truth):** `docs/theme-brandbook-uiux.md`
- **Brand direction:** `docs/LUSENA_BrandBook_v2.md`
- **CSS foundations (new single CSS file):** `assets/lusena-foundations.css`
- **CSS foundations brief (design spec):** `docs/css-foundations-brief.md`
- **Design tokens (compact):** `memory-bank/doc/patterns/brand-tokens.md`
- **Spacing system:** `memory-bank/doc/patterns/spacing-system.md`
- **CSS architecture:** `memory-bank/doc/patterns/css-architecture.md`
- **Engineering changelog:** `memory-bank/doc/changelog/theme-changes.md`

### CSS migration in progress

We are migrating from a fragmented CSS setup to a single `lusena-foundations.css` file:

| Old (still loaded, being phased out) | New (target) |
|--------------------------------------|--------------|
| `assets/lusena-shop.css` (Tailwind build) | `assets/lusena-foundations.css` |
| `assets/lusena-spacing.css` (spacing tokens) | *(absorbed into foundations)* |
| `snippets/lusena-missing-utilities.liquid` (patches) | *(absorbed into foundations)* |

**Migration phases:** See `memory-bank/progress.md` → "CSS foundations migration" section.

**When editing sections:** Use `lusena-foundations.css` classes for new/migrated work. See `memory-bank/doc/patterns/spacing-system.md` for the class API.

## Key Conventions

- All customer-facing text in **Polish**; code/comments in **English**
- `assets/lusena-foundations.css` is the **target single source of truth** for all CSS tokens, spacing, typography, and components — use its classes for new work
- All custom files use `lusena-*` prefix
- NEVER fabricate social proof (customer counts, ratings, reviews)
- Sentence case for all headings and button labels
- Conventional Commits: `feat(lusena):`, `fix(lusena):`, `docs:`, `chore:`

## Implementation Principles

### Progressive development
- Implement one section/change at a time. Confirm before moving on.
- Batch small iterations locally; commit when meaningfully complete.

### Scope management
- Implement only what is explicitly requested.
- When ambiguous, choose the minimal viable interpretation.
- If a task grows beyond original scope, pause and discuss.

### Communication protocol
- Before starting: confirm understanding of the task.
- After completing: summarize what changed and what needs verification.
- For bigger changes, ask "Is this done?" before committing.

### Quality assurance
- Run `shopify theme check` — only known baseline warnings should remain.
- Visual verification via Playwright MCP when uncertain about layout.

## MANDATORY: Shopify Dev MCP

Call `learn_shopify_api` with `api: "liquid"` ONCE before editing any Liquid files.

## Visual Verification (Playwright)

- When not sure about a UI/layout issue, verify using Playwright MCP (don't guess).
- Dev server: `http://127.0.0.1:9292/` (start with `shopify theme dev` if not running).

## Animations (consistency)

Dawn's `scroll-trigger` classes gated by `settings.animations_reveal_on_scroll`:
- New section/block: add `scroll-trigger animate--slide-in` conditionally:
  `{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}`
- Repeated items: `data-cascade` on container for stagger effect.
- If element needs `transform` for layout, put scroll-trigger on a wrapper.

## Theme Check Warnings (known baseline)

These warnings have been present since the beginning and should not be treated as issues:
- `layout/password.liquid`: UndefinedObject `scheme_classes`
- `layout/theme.liquid`: UndefinedObject `scheme_classes`
- `sections/featured-product.liquid`: UnusedAssign `seo_media`
- `sections/main-article.liquid`: VariableName `anchorId`
- `sections/main-list-collections.liquid`: VariableName `moduloResult`
- `sections/main-product.liquid`: UnusedAssign `seo_media`
- `sections/main-product.liquid`: UndefinedObject `continue`
- `sections/main-search.liquid`: UnusedAssign `product_settings`

## Reference Docs (read on demand, NOT every session)

- `docs/reference/liquid-syntax.md` — Liquid filters, operators, tags, objects
- `docs/reference/theme-architecture.md` — Dawn directory structure, CSS/JS patterns, schema practices
- `docs/reference/translation-standards.md` — i18n guidelines, locale file structure
- `docs/reference/code-examples.md` — Section/block/snippet templates with full examples
