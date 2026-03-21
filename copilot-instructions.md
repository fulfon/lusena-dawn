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
- `memory-bank/doc/products/README.md` — product catalog index, store-wide settings (currency, tax, shipping)
- `memory-bank/doc/products/{handle}.md` — per-product Shopify admin data (metafields, pricing, variants, SEO, status)

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
- **Migration lessons (read before migrating pages):** `memory-bank/doc/patterns/migration-lessons.md`
- **Product catalog (Shopify admin data):** `memory-bank/doc/products/` — per-product metafields, pricing, variants, SEO
- **Product setup checklist:** `docs/product-setup-checklist.md` — metafield definitions, example values per product type
- **Bundle strategy (pricing, phases, research):** `memory-bank/doc/bundle-strategy.md` — complete bundle architecture, economics, and decision triggers

### CSS architecture

`assets/lusena-foundations.css` is the single source of truth for all CSS tokens, spacing, typography, components, and global body/main rules. The old Tailwind files (`lusena-shop.css`, `lusena-spacing.css`, `lusena-missing-utilities.liquid`) were deleted on 2026-03-04 after full migration.

**When editing sections:** Use `lusena-foundations.css` classes. See `memory-bank/doc/patterns/spacing-system.md` for the class API.

### compiled_assets truncation guard (MANDATORY)

Shopify compiles all `{% stylesheet %}` blocks into one `compiled_assets/styles.css` file that **silently truncates at ~73KB**. Rules after the cut-off are lost with no error.

- **≤50 lines of section-scoped CSS** → OK in `{% stylesheet %}`
- **>50 lines or shared CSS** → must go in a standalone `assets/lusena-*.css` file
- **After adding CSS to any `{% stylesheet %}` block:** check compiled_assets size in DevTools Network tab — it must stay **under 55KB**
- If over 55KB: extract the largest block into a standalone asset (see `memory-bank/doc/patterns/css-architecture.md` for the extraction steps)

### Product metafields

Before creating or modifying product metafields, read `docs/product-metafields-reference.md` — it contains **universal fields** (specs, feature cards 2/4/5/6, care) that are shared across ALL products and must NOT be modified per product. Only fields marked "REQUIRES CREATIVE SESSION" in the product file should be crafted. Never use percentage claims for momme comparisons (e.g., "30% gęstszy") — use qualitative language only.

## Key Conventions

- All customer-facing text in **Polish**; code/comments in **English**
- `assets/lusena-foundations.css` is the **single source of truth** for all CSS tokens, spacing, typography, and components — use its classes for all work
- All custom files use `lusena-*` prefix
- NEVER fabricate social proof (customer counts, ratings, reviews)
- Sentence case for all headings and button labels
- **Hyphens only, never em dashes** — all customer-facing copy uses `-` (hyphen/minus), never `—` (em dash). Em dashes look AI-generated. This applies to metafield values, section defaults, and any text visible to customers.
- **Feature card titles: max 28 characters** — guarantees single-line rendering at the tightest breakpoint (288px column at 20px font). Reference: "Jedwab, nie satyna z poliestru" (30 chars) barely fits.
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
- Use `/playwright-cli` skill for any browser interaction — visual checks, debugging, testing interactions.

## MANDATORY: Shopify Dev MCP

Call `learn_shopify_api` with `api: "liquid"` ONCE before editing any Liquid files.

## Browser Interactions (Playwright CLI)

The `/playwright-cli` skill is the **only** way to interact with the browser. Use it for ALL browser tasks — not just visual verification:
- Screenshots & visual verification (layout, spacing, colors)
- Debugging CSS issues (checking computed styles, element sizes)
- Checking network resources (compiled_assets size, asset loading)
- Testing interactions (clicking buttons, opening menus, filling forms)
- Comparing before/after states
- Any situation where you need to see or interact with the live site

**CRITICAL RULES:**
- **ALWAYS use the `/playwright-cli` skill** — NEVER use Playwright MCP browser tools directly (`browser_navigate`, `browser_snapshot`, `browser_click`, etc.). The MCP tools bypass the project workflow.
- **ALWAYS use a named session** with `-s=<unique-name>` to isolate your browser from other concurrent Claude Code instances. Multiple instances share the default browser and will navigate each other's pages, causing failures. **Each instance MUST pick a DIFFERENT name** — use the specific page or feature you're working on (e.g., `-s=pdp-fix`, `-s=homepage-check`, `-s=about-migrate`, `-s=cart-debug`). NEVER use generic names like `-s=audit` or `-s=test` — another instance will pick the same name. Example: `playwright-cli -s=quality-spacing open http://...`
- When not sure about a UI/layout issue, use `/playwright-cli` — don't guess.
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
