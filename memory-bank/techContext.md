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
- **Collection:** `sections/lusena-main-collection.liquid` + `snippets/lusena-product-card.liquid`
- **Search:** `sections/lusena-search.liquid` — predictive search, product grid, empty state with bestsellers
- **Blog listing:** `sections/lusena-blog.liquid` — 2-col grid, pagination, rich empty state
- **Article page:** `sections/lusena-article.liquid` — hero image, richtext body, share button, LD+JSON
- **404 page:** `sections/lusena-404.liquid` — centered error message, bestseller grid, viewport-fill
- **Generic page:** `sections/lusena-main-page.liquid` — breadcrumbs, title, richtext, viewport-fill, compact spacing
- **Contact page:** `sections/lusena-contact-form.liquid` — breadcrumbs, heading, LUSENA form system, viewport-fill, full-width mobile button
- **Homepage:** `sections/lusena-hero.liquid`, `lusena-bestsellers.liquid`, `lusena-trust-bar.liquid`, etc. (9 sections)

### Translations
- `locales/en.default.json` — **Polish strings override English defaults** (store is PL-first). Search-related keys (`templates.search.*`, `accessibility.search.*`, `accessibility.loading`) translated to Polish. Polish quotation marks „..." use Unicode `\u201E` + `\u201D` (not ASCII `"`) to avoid breaking JSON.

### Global components
- `snippets/lusena-button-system.liquid` — Button primitives
- `snippets/lusena-icon.liquid` — SVG icon system (includes `share` icon)
- `snippets/lusena-section-gap-detector.liquid` — Same-bg section gap detection (JS)
- `snippets/lusena-breadcrumbs.liquid` — Breadcrumbs (supports: product, collection, blog, article, page). Has `breadcrumb_label` param to override `page.title` (e.g., "Kontakt" instead of English "Contact")
- `snippets/lusena-article-card.liquid` — Blog listing card (16:9 image, hover zoom, date, excerpt)
- `snippets/lusena-share-button.liquid` — Web Share API (mobile) + clipboard copy (desktop)
- `snippets/lusena-date-pl.liquid` — Polish date formatting (bypasses English store locale)

### Styles
- `assets/lusena-foundations.css` — Single source of truth for design tokens, utilities, containers, components, body/main global rules, preflight resets (~40KB)
- `assets/lusena-button-system.css` — Button/icon-button primitives (extracted from snippet {% stylesheet %})
- `assets/lusena-header.css` — Header section styles (extracted from section {% stylesheet %})
- `assets/lusena-hero.css` — Hero section styles (extracted from section {% stylesheet %})
- `assets/lusena-footer.css` — Footer section styles (extracted from section {% stylesheet %})
- `assets/lusena-pdp.css` — All PDP-specific CSS (~34KB), loaded per-page
- `assets/base.css` — Dawn foundation (3,641 lines)

### CSS loading architecture
- **Global assets in `theme.liquid`:** `lusena-foundations.css` → `lusena-button-system.css` → `lusena-header.css` → `lusena-hero.css` → `lusena-footer.css`
- **Page-specific assets:** `lusena-pdp.css` loaded via `{{ 'lusena-pdp.css' | asset_url | stylesheet_tag }}` in `lusena-main-product.liquid`
- **`{% stylesheet %}` compiled_assets truncation:** All `{% stylesheet %}` blocks compile into `compiled_assets/styles.css` (~38KB after extraction, 73KB hard limit). Rules after limit silently dropped. **MANDATORY:** check size stays under 55KB after adding section CSS. See `memory-bank/doc/patterns/css-architecture.md`.
- **Preflight resets in foundations:** `button`, `a`, `img`, `video` resets (replacing old Tailwind preflight). SVG intentionally excluded — SVGs expand without explicit dimensions.

## Development tools

- **Shopify CLI:** `shopify theme dev` → `http://127.0.0.1:9292/`
- **Theme check:** `shopify theme check` (only known baseline warnings should remain)
- **Playwright CLI (`/playwright-cli` skill):** The **only** way to interact with the browser. Use for ALL browser tasks: screenshots, debugging CSS, checking network resources, testing interactions, comparing before/after, anything that needs a live page. **CRITICAL: NEVER use Playwright MCP browser tools directly** (`browser_navigate`, `browser_snapshot`, `browser_click`, etc.) — they bypass the project workflow. The `/playwright-cli` skill handles correct dev server URL, viewport sizes, and screenshot naming.
- **Shopify Dev MCP:** MUST call `learn_shopify_api` with `api: "liquid"` before editing Liquid

## Skills inventory

9 skills mirrored in `.claude/`, `.agent/`, `.codex/`:

| Skill | Purpose |
|-------|---------|
| `lusena-update-memory-bank` | Post-work memory bank update |
| `lusena-v2-page-migration` | Page migration to brandbook v2 |
| `lusena-draftshop-fragment-parity` | Copy UI from React prototype to theme |
| `shopify-dev-mcp` | Shopify Dev MCP tool usage |
| `shopify-expert` | Shopify theme development |
| `frontend-design` | Production-grade frontend UI |
| `react-expert` | React 19+ patterns |
| `graphql-architect` | GraphQL schema design |
| `api-designer` | REST/GraphQL API design |

## Known theme check warnings (baseline — do not fix)

- `layout/password.liquid`: UndefinedObject `scheme_classes`
- `layout/theme.liquid`: UndefinedObject `scheme_classes`
- `sections/featured-product.liquid`: UnusedAssign `seo_media`
- `sections/main-article.liquid`: VariableName `anchorId`
- `sections/main-list-collections.liquid`: VariableName `moduloResult`
- `sections/main-product.liquid`: UnusedAssign `seo_media`
- `sections/main-product.liquid`: UndefinedObject `continue`
- `sections/main-search.liquid`: UnusedAssign `product_settings`

## React prototype status

The `lusena-shop/` directory contains a React + TypeScript prototype that was used as design reference during initial development. It is **no longer actively used** — all new design work happens directly in the Shopify theme. The prototype remains as historical reference only.
