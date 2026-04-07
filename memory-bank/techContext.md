# Tech Context

## Base theme

- **Shopify Dawn v15.4.1** — official Shopify starter theme
- **Dual-layer architecture:** LUSENA sections (`lusena-*` prefix) override Dawn defaults
- Dawn originals remain in repo but are NOT used on the live storefront
- **Rule of thumb:** If a `lusena-*` file exists for a component, edit that file

## Key file paths

### Layout
- `layout/theme.liquid` — Main layout, loads all global CSS/JS

### LUSENA sections (customer-facing)
- **Header:** `sections/lusena-header.liquid`
- **Footer:** `sections/lusena-footer.liquid`
- **Cart page:** `sections/lusena-cart-items.liquid` + `snippets/lusena-cart-quantity.liquid` + `sections/lusena-cart-footer.liquid`
- **Product page:** `sections/lusena-main-product.liquid` + `snippets/lusena-pdp-*.liquid` (13 PDP snippets)
- **Bundle product page:** `sections/lusena-main-bundle.liquid` + `snippets/lusena-bundle-*.liquid` (7 bundle snippets: summary, contents, options, atc, care, scripts, sticky-atc) — shares 4 PDP snippets (media, proof-chips, guarantee, payment). Progressive disclosure color selector, sticky ATC (mobile+desktop), `assets/lusena-bundle-pdp.css`
- **Scrunchie education:** `snippets/lusena-scrunchie-education.liquid` — server-side price swap + live JS cart sync (PubSub + MutationObserver)
- **Collection:** `sections/lusena-main-collection.liquid` + `snippets/lusena-product-card.liquid`
- **Search:** `sections/lusena-search.liquid` — predictive search, product grid, empty state with bestsellers
- **Blog listing:** `sections/lusena-blog.liquid` — 2-col grid, pagination, rich empty state
- **Article page:** `sections/lusena-article.liquid` — hero image, richtext body, share button, LD+JSON
- **404 page:** `sections/lusena-404.liquid` — centered error message, bestseller grid, viewport-fill
- **Generic page:** `sections/lusena-main-page.liquid` — breadcrumbs, title, richtext, viewport-fill, compact spacing
- **Contact page:** `sections/lusena-contact-form.liquid` — breadcrumbs, heading, LUSENA form system, viewport-fill, full-width mobile button
- **Homepage:** `sections/lusena-hero.liquid`, `lusena-trust-bar.liquid`, `lusena-benefit-bridge.liquid`, `lusena-bestsellers.liquid`, `lusena-visual-proof.liquid`, `lusena-bundles.liquid`, `lusena-testimonials.liquid`, `lusena-heritage.liquid`, `lusena-faq.liquid`, `lusena-final-cta.liquid` (10 sections)

### Translations
- `locales/en.default.json` — **Polish strings override English defaults** (store is PL-first). Search-related keys (`templates.search.*`, `accessibility.search.*`, `accessibility.loading`) translated to Polish. Polish quotation marks „..." use Unicode `\u201E` + `\u201D` (not ASCII `"`) to avoid breaking JSON.
- `locales/pl.json` — Polish locale override file. Currently minimal (mostly mirrors en.default). Prefer editing `en.default.json` for translations (see lesson #43 in migration-lessons.md).

### Global components
- `snippets/lusena-button-system.liquid` — Button primitives
- `snippets/lusena-icon.liquid` — SVG icon system (includes `share` icon)
- `snippets/lusena-icon-animated.liquid` — Animated SVG icon system (heart, layers, droplets, wind, shield-check, sparkles, gift, clock, moon, feather, palette) with CSS class hooks and stagger delay support. Falls back to static `lusena-icon` for unknown icon names.
- `snippets/lusena-section-gap-detector.liquid` — Same-bg section gap detection (JS)
- `snippets/lusena-breadcrumbs.liquid` — Breadcrumbs (supports: product, collection, blog, article, page). Has `breadcrumb_label` param to override `page.title` (e.g., "Kontakt" instead of English "Contact")
- `snippets/lusena-article-card.liquid` — Blog listing card (16:9 image, hover zoom, date, excerpt)
- `snippets/lusena-share-button.liquid` — Web Share API (mobile) + clipboard copy (desktop)
- `snippets/lusena-date-pl.liquid` — Polish date formatting (bypasses English store locale)

### Styles
- `assets/lusena-foundations.css` — Single source of truth for design tokens, utilities, containers, components, body/main global rules, preflight resets (~50KB)
- `assets/lusena-button-system.css` — Button/icon-button primitives (extracted from snippet {% stylesheet %})
- `assets/lusena-header.css` — Header section styles (extracted from section {% stylesheet %})
- `assets/lusena-hero.css` — Hero section styles (extracted from section {% stylesheet %})
- `assets/lusena-footer.css` — Footer section styles (extracted from section {% stylesheet %})
- `assets/lusena-pdp.css` — All PDP-specific CSS (~42KB), loaded per-page
- `assets/lusena-cart-page.css` — Cart page styles: items, footer, quantity stepper, upsell (625 lines, extracted from `{% stylesheet %}` blocks 2026-03-26)
- `assets/lusena-search.css` — Search page styles: layout, grid, empty state (156 lines, extracted from `{% stylesheet %}` block 2026-03-26)
- `assets/lusena-bundles.css` — Homepage bundles section: desktop 3-col card grid + mobile compact rows with SVG thumbnails, savings badge overlay, OOS states, hover underlines (loaded in lusena-bundles.liquid)
- `assets/lusena-bundle-pdp.css` — Bundle PDP buy box styles (loaded in lusena-main-bundle.liquid)
- `assets/lusena-benefit-bridge.css` — Benefit bridge section styles (loaded in lusena-benefit-bridge.liquid)
- `assets/lusena-visual-proof.css` — Visual proof block section styles (loaded in lusena-visual-proof.liquid)
- `assets/lusena-icon-animations.css` — Animated icon CSS keyframes + prefers-reduced-motion (loaded per-section in lusena-pdp-feature-highlights.liquid)
- `assets/base.css` — Dawn foundation (3,641 lines)

### CSS loading architecture
- **Global assets in `theme.liquid`:** `lusena-foundations.css` → `lusena-button-system.css` → `lusena-header.css` → `lusena-hero.css` → `lusena-footer.css`
- **Page-specific assets:** `lusena-pdp.css` loaded in `lusena-main-product.liquid` and `lusena-main-bundle.liquid`, `lusena-cart-page.css` loaded in `lusena-cart-items.liquid`, `lusena-search.css` loaded in `lusena-search.liquid`, `lusena-bundle-pdp.css` loaded in `lusena-main-bundle.liquid`, `lusena-bundles.css` loaded in `lusena-bundles.liquid`, `lusena-benefit-bridge.css` loaded in `lusena-benefit-bridge.liquid`, `lusena-visual-proof.css` loaded in `lusena-visual-proof.liquid`, `lusena-icon-animations.css` loaded in `lusena-pdp-feature-highlights.liquid`
- **`{% stylesheet %}` compiled_assets:** All `{% stylesheet %}` blocks compile into `compiled_assets/styles.css` (73KB hard limit). Currently ~59KB after 2026-03-26 extraction (cart page + search CSS moved to standalone files). Safe margin maintained.
- **Cart drawer:** Promoted from snippet render to section (`{%- section 'cart-drawer' -%}` in theme.liquid). CSS lives in `<style>` tag inside `snippets/cart-drawer.liquid` (~150 lines, not in compiled_assets). Upsell CSS selectors scoped under `.lusena-cart-drawer__upsell`.
- **Bundle swap JS:** `assets/lusena-bundle-swap.js` — shared `LusenaBundle.swap()` for bundle add + individual remove.
- **Preflight resets in foundations:** `button`, `a`, `img`, `video` resets (replacing old Tailwind preflight). SVG intentionally excluded — SVGs expand without explicit dimensions.

## Development tools

- **Shopify CLI:** Owner runs `shopify theme dev -e dev` (config in `shopify.theme.toml`). Syncs files to dev theme. Localhost (`127.0.0.1:9292`) is for the owner's manual browser use only.
- **Preview URL (for ALL Playwright testing):** NEVER use localhost with Playwright — it blocks cart AJAX. Main repo: `https://lusena-dev.myshopify.com/?preview_theme_id=144618684603`. Worktrees: use theme ID from `config/worktree-themes.json`. Store password: `paufro`.
- **Theme check:** `shopify theme check` (only known baseline warnings should remain)
- **Playwright CLI (`/playwright-cli` skill):** The **only** way to interact with the browser. Use for ALL browser tasks: screenshots, debugging CSS, checking network resources, testing interactions, comparing before/after, anything that needs a live page. **CRITICAL: NEVER use Playwright MCP browser tools directly** (`browser_navigate`, `browser_snapshot`, `browser_click`, etc.) — they bypass the project workflow. **ALWAYS use `-s=<unique-name>`** to isolate your browser session from other concurrent Claude Code instances (e.g., `playwright-cli -s=pdp-fix open http://...`). Each instance MUST pick a DIFFERENT name — never use generic names like `-s=audit` or `-s=test`. Without a named session, all instances share the default browser and will navigate each other's pages.
- **Shopify Dev MCP:** MUST call `learn_shopify_api` with `api: "liquid"` before editing Liquid

## Hooks, rules, and settings

**Hooks** (`.claude/hooks/`, 6 scripts — configured in `.claude/settings.json`):
| Hook | Event | Purpose |
|------|-------|---------|
| `branch-guard.sh` | PreToolUse (Bash) | Blocks `git commit` on main/master branches |
| `guard-dawn-edit.sh` | PreToolUse (Edit\|Write) | Blocks editing Dawn originals when lusena-* counterpart exists |
| `session-context.sh` | SessionStart | Injects activeContext.md focus/next/issues |
| `post-compact-rules.sh` | PostCompact | Re-injects critical LUSENA rules after context compaction |
| `theme-check-on-edit.sh` | PostToolUse (Edit\|Write) | Runs `shopify theme check` on edited .liquid files |
| `task-quality-gate.sh` | TaskCompleted | Runs theme check on recently modified lusena-* files |

**Rules** (`.claude/rules/`, 8 files — auto-load by path pattern):
| Rule | Triggers on |
|------|-------------|
| `animations.md` | `sections/*.liquid`, `snippets/*.liquid` |
| `bundle-system.md` | `sections/*bundle*`, `snippets/*bundle*`, `assets/*bundle*`, `memory-bank/doc/bundle*`, `templates/product.bundle*` |
| `cart-system.md` | `sections/*cart*`, `snippets/*cart*`, `assets/*cart*`, `assets/*bundle*`, `assets/lusena-bundle*` |
| `css-and-assets.md` | `assets/*.css`, `sections/*.liquid`, `snippets/*.liquid` |
| `css-cascade.md` | `assets/*.css`, `sections/*.liquid`, `snippets/*.liquid` |
| `no-inline-scripts.md` | `**/*.liquid`, `**/*.css`, `**/*.js`, `assets/**`, `sections/**`, `snippets/**`, `templates/**`, `layout/**` |
| `product-metafields.md` | `memory-bank/doc/products/**`, `sections/lusena-main-product*`, `snippets/lusena-pdp*` |
| `section-catalog.md` | (always loaded — no path filter) |

**Settings:** `.claude/settings.json` (shared, checked in) + `.claude/settings.local.json` (local permissions).

## Skills inventory

16 skills in `.claude/skills/` (mirrored in `.codex/skills/`):

| Skill | Purpose |
|-------|---------|
| `lusena-worktree-sync` | Branch-level memory bank update before squash-merge to main |
| `lusena-memory-bank-audit` | Periodic deep audit of entire memory bank (~every 10 merges) |
| `lusena-new-section` | Scaffolds new LUSENA section with correct boilerplate, spacing, CSS decision, schema |
| `lusena-product-copy-session` | Orchestrates full creative copy workflow (research → legal → validation → finalization) |
| `lusena-section-design-loop` | Autonomous design iteration: edit in worktree, push, Playwright capture, 5-agent review panel, up to 5 rounds |
| `lusena-page-audit` | Full page UX audit from customer perspective |
| `lusena-customer-validation` | 4-persona copy evaluation (Polish) |
| `lusena-legal-check` | EU/UOKiK compliance check for marketing claims |
| `lusena-spacing-audit` | Automated spacing measurement + validation via Playwright |
| `lusena-preview-check` | Delegates browser testing to a Sonnet subagent (measure, verify, screenshot, debug) |
| `shopify-dev-mcp` | Shopify Dev MCP tool usage |
| `shopify-expert` | Shopify theme development |
| `frontend-design` | Production-grade frontend UI |
| `react-expert` | React 19+ patterns |
| `graphql-architect` | GraphQL schema design |
| `api-designer` | REST/GraphQL API design |

## Worktree theme mapping

Each git worktree has a dedicated unpublished Shopify theme for browser testing via `shopify theme push`. The main repo uses `shopify theme dev` on port 9292 (pinned in `shopify.theme.toml`).

**Pool config:** `config/worktree-themes.json` maps slot numbers to theme IDs:
```json
{
  "store": "lusena-dev.myshopify.com",
  "themes": {
    "1": { "id": "146574082235", "name": "lusena-worktree-1" },
    "2": { "id": "146574115003", "name": "lusena-worktree-2" },
    "3": { "id": "146574147771", "name": "lusena-worktree-3" },
    "4": { "id": "146574180539", "name": "lusena-worktree-4" }
  }
}
```

| Context | Theme ID | URL |
|---------|----------|-----|
| Main repo (`lusena-dawn/`) | `144618684603` | `http://127.0.0.1:9292/` (live dev server) |
| Worktree slot N | from `config/worktree-themes.json` | `https://lusena-dev.myshopify.com/?preview_theme_id=<ID>` |

**How Claude Code uses this:** The instance detects its slot number from the cwd path (`lusena-worktrees/lusena-N` → slot N), reads the theme ID from `config/worktree-themes.json`, and runs:
```bash
shopify theme push --theme <THEME_ID> --store lusena-dev.myshopify.com --nodelete
```
Then uses `https://lusena-dev.myshopify.com/?preview_theme_id=<THEME_ID>` for Playwright.

**One-time setup (owner must do):** Create 4 unpublished themes and record their IDs in the JSON file. From the main repo, run 4 times:
```bash
shopify theme push --unpublished --json --store lusena-dev.myshopify.com
```
Rename each theme in Shopify admin to `lusena-worktree-1` through `lusena-worktree-4` and note the IDs.

**Why push instead of dev?** Shopify CLI shares auth state machine-globally (OAuth port 3456 hardcoded). Multiple `shopify theme dev` instances steal each other's tokens. Cart API also rate-limits aggressively on localhost — preview URLs on the real domain avoid this.

## Store URL reference (for Playwright testing)

**Store password:** `paufro` (enter on password page before testing).

Base URL for worktrees: `https://lusena-dev.myshopify.com{path}?preview_theme_id=<THEME_ID>`
Base URL for main repo: `http://127.0.0.1:9292{path}`

### Products

| Handle | Name | Type | Path |
|--------|------|------|------|
| `poszewka-jedwabna` | Poszewka jedwabna 50x60 | Standard PDP | `/products/poszewka-jedwabna` |
| `czepek-jedwabny` | Jedwabny czepek do spania | Standard PDP | `/products/czepek-jedwabny` |
| `scrunchie-jedwabny` | Scrunchie jedwabny | Standard PDP | `/products/scrunchie-jedwabny` |
| `jedwabna-maska-3d` | Jedwabna maska 3D do spania | Standard PDP | `/products/jedwabna-maska-3d` |
| `walek-do-lokow` | Jedwabny walek do lokow | Standard PDP | `/products/walek-do-lokow` |
| `nocna-rutyna` | Nocna Rutyna | Bundle PDP | `/products/nocna-rutyna` |
| `piekny-sen` | Piekny Sen | Bundle PDP | `/products/piekny-sen` |
| `scrunchie-trio` | Scrunchie Trio | Bundle PDP | `/products/scrunchie-trio` |

### Pages

| Page | Path |
|------|------|
| Homepage | `/` |
| Collection (all) | `/collections/all` |
| Cart | `/cart` |
| Quality | `/pages/nasza-jakosc` |
| About | `/pages/o-nas` |
| Returns | `/pages/zwroty` |
| Contact | `/pages/kontakt` |
| Search | `/search` |
| Blog | `/blogs/blog` |

## Known theme check warnings (baseline — do not fix)

- `layout/password.liquid`: UndefinedObject `scheme_classes`
- `layout/theme.liquid`: UndefinedObject `scheme_classes`
- `sections/featured-product.liquid`: UnusedAssign `seo_media`
- `sections/main-article.liquid`: VariableName `anchorId`
- `sections/main-list-collections.liquid`: VariableName `moduloResult`
- `sections/main-product.liquid`: UnusedAssign `seo_media`
- `sections/main-product.liquid`: UndefinedObject `continue`
- `sections/main-search.liquid`: UnusedAssign `product_settings`

## Product catalog documentation

- **Product catalog index:** `memory-bank/doc/products/README.md` — store-wide settings, product status table
- **Per-product data:** `memory-bank/doc/products/{handle}.md` — metafields, pricing, variants, SEO, status
- **Metafields reference:** `memory-bank/doc/products/product-metafields-reference.md` — what each field does, where it renders, creative process
- **Setup checklist:** `memory-bank/doc/products/product-setup-checklist.md` — metafield definitions, example values per product type

## React prototype status

The `lusena-shop/` React prototype was used during initial development but has been **removed from the repo**. All design iteration now happens directly in the Shopify theme via the `lusena-section-design-loop` skill (worktree push + Playwright capture + 5-agent review panel).
