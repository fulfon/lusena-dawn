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
- **Product page:** `sections/lusena-main-product.liquid` + `snippets/lusena-pdp-*.liquid` (13 PDP snippets)
- **Collection:** `sections/lusena-main-collection.liquid` + `snippets/lusena-product-card.liquid`
- **Homepage:** `sections/lusena-hero.liquid`, `lusena-bestsellers.liquid`, `lusena-trust-bar.liquid`, etc. (9 sections)

### Global components
- `snippets/lusena-button-system.liquid` — Button primitives
- `snippets/lusena-icon.liquid` — SVG icon system
- `snippets/lusena-missing-utilities.liquid` — Tailwind utility patches (tech debt)
- `snippets/lusena-section-gap-detector.liquid` — Same-bg section gap detection (JS)
- `snippets/lusena-spacing-system.liquid` — Doc-only stub (CSS in asset file)

### Styles
- `assets/lusena-shop.css` — Tailwind-compiled brand utilities (26KB)
- `assets/lusena-spacing.css` — Spacing token system (source of truth, 266 lines)
- `assets/base.css` — Dawn foundation (3,641 lines)

## Development tools

- **Shopify CLI:** `shopify theme dev` → `http://127.0.0.1:9292/`
- **Theme check:** `shopify theme check` (only known baseline warnings should remain)
- **Playwright MCP:** Visual verification when uncertain about layout
- **Shopify Dev MCP:** MUST call `learn_shopify_api` with `api: "liquid"` before editing Liquid

## Skills inventory

10 skills mirrored in `.claude/`, `.agent/`, `.codex/`:

| Skill | Purpose |
|-------|---------|
| `lusena-theme-changelog` | Commit + changelog workflow |
| `lusena-v2-page-migration` | Page migration to brandbook v2 |
| `lusena-draftshop-fragment-parity` | Copy UI from React prototype to theme |
| `lusena-spacing` | Spacing review and adjustment |
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
