# Dawn Pages → LUSENA Migration Plan

*Created: 2026-03-04*

## Goal

Migrate all remaining Dawn-default pages to LUSENA standard so every surface of the store feels like one cohesive premium brand. No page should feel "off-brand." This maximizes trust, user experience, and conversion.

## Approach: Copy → Rename → Restyle

Same workflow used for homepage, PDP, collection, quality, returns, about:

1. **Copy** Dawn section → **rename** to `lusena-*`
2. **Update** template JSON to point to new `lusena-*` section
3. **Keep all Liquid logic intact** — don't rewrite cart AJAX, form submissions, account logic
4. **Strip Dawn CSS classes** → replace with `lusena-foundations.css` utilities + BEM
5. **Add section CSS** via `{% stylesheet %}` blocks (or standalone `.css` asset if large)
6. **UX audit per page** — evaluate what trust/brand elements from our toolkit would improve the page (decide together before coding)
7. **Visual verify** via Playwright

## Pre-work: shared infrastructure

Before starting individual pages, add these shared components:

### 1. `.lusena-form` component (in `lusena-foundations.css`)
Shared form styles for: login, register, activate, reset password, contact.
Covers: input fields, labels, error states, form layout, submit buttons.

### 2. `.lusena-table` / `.lusena-line-item` component (in `lusena-foundations.css`)
Shared table/list styles for: cart, account, order, addresses.
Covers: line item rows, headings, responsive stacking.

### 3. `lusena-page-header` snippet
Shared page title treatment for all system pages.
- Consistent heading typography and spacing
- **Optional breadcrumbs** — included on pages with hierarchy (article, account subpages), omitted on standalone pages (cart, login, 404, search)

## Batch order

### Batch 0: Shared infrastructure
- [ ] Add `.lusena-form` component to `lusena-foundations.css`
- [ ] Add `.lusena-table` / `.lusena-line-item` component to `lusena-foundations.css`
- [ ] Create `snippets/lusena-page-header.liquid`

### Batch 1: Cart page (highest conversion impact)
- [ ] `cart.json` → `lusena-cart-items` + `lusena-cart-footer`
- UX opportunities: trust signals, free shipping threshold bar, consistent line-item design with cart drawer

### Batch 2: Simple content pages (quick wins)
- [ ] `404.json` → `lusena-404` — branded 404 with CTA back to shop
- [ ] `page.json` → `lusena-main-page` — generic rich text page
- [ ] `page.contact.json` → `lusena-main-page` + `lusena-contact-form` — uses shared form component

### ~~Batch 3: Customer auth pages~~ — N/A
Shopify deprecated legacy/classic customer accounts in February 2026. The store uses **new customer accounts** (hosted on `shopify.com/authentication/...`). Login, register, activate, and reset password are all handled by Shopify's hosted system. No Liquid templates are used. Customization only via Shopify admin branding settings or customer account UI extensions (app development).

### ~~Batch 4: Customer account pages~~ — N/A
Same reason as Batch 3. Account overview, order detail, and addresses are Shopify-hosted. All 3 sections were built, tested, and then cleaned up after discovering the deprecation. See `memory-bank/activeContext.md` for full details.

### Batch 5: Search ✓ (2026-03-05)
- [x] `search.json` → `lusena-search` — reuses `lusena-product-card`, predictive search, Polish translations in `en.default.json`, smart viewport management (upper-third positioning + footer-below-fold), disabled Dawn's scrollIntoView-on-focus
- ~~`list-collections.json`~~ — **Skipped** — not needed for LUSENA's small catalog; customers navigate via header

### Batch 6: Blog + Article (content pattern)
- [ ] `blog.json` → `lusena-blog`
- [ ] `article.json` → `lusena-article`
- UX opportunities: related products sidebar/CTA, newsletter signup

### Batch 7: Password page
- [ ] `password.json` → `lusena-password` (uses `layout/password.liquid`)

## Per-page migration workflow

For each page:
1. **Audit** — read Dawn section, identify what to keep/change, evaluate UX enhancements
2. **Discuss** — present proposed changes + UX additions to user for approval
3. **Build** — copy, rename, restyle, add enhancements. **Use the `/frontend-design` skill** for styling and layout decisions — ensures visual consistency and high design quality across all migrated pages.
4. **Verify** — Playwright visual check
5. **Commit** — one commit per batch

## Templates & sections summary (10 templates, ~14 new sections)

| Template | Dawn sections | New LUSENA sections |
|---|---|---|
| `cart.json` | `main-cart-items`, `main-cart-footer` | `lusena-cart-items`, `lusena-cart-footer` |
| `404.json` | `main-404` | `lusena-404` |
| `page.json` | `main-page` | `lusena-main-page` |
| `page.contact.json` | `main-page`, `contact-form` | `lusena-main-page`, `lusena-contact-form` |
| `search.json` | `main-search` | `lusena-search` |
| `list-collections.json` | `main-list-collections` | `lusena-list-collections` |
| `blog.json` | `main-blog` | `lusena-blog` |
| `article.json` | `main-article` | `lusena-article` |
| `password.json` | `email-signup-banner` | `lusena-password` |

*Note: 7 `customers/*` templates (login, register, activate, reset password, account, order, addresses) removed from scope — Shopify's new customer accounts system makes Liquid templates irrelevant for these pages.*

## Excluded

- **Gift card** (`gift_card.liquid`) — standalone layout, no header/footer, only relevant if gift cards are added to LUSENA

## Decision log

- Breadcrumbs in `lusena-page-header` are **optional** — included on hierarchy pages (article, account subpages), omitted on standalone pages (cart, login, 404, search)
- UX enhancements evaluated **per-page during migration** — not pre-planned. Keeps scope controlled.
- UX enhancement principle: **reuse existing LUSENA components first** (trust bar, FAQ, final CTA, etc.). Only propose building something new if it genuinely improves the page and is clearly worth the effort. Not every page needs extras — a clean, well-styled page is already premium. Don't add for the sake of adding.
- Blog is included in scope (will be used for content marketing)
- **Batches 3 & 4 removed (2026-03-05):** Shopify deprecated legacy customer accounts in Feb 2026. Store uses new customer accounts (Shopify-hosted). All 7 `customers/*` templates are dead code — no Liquid migration possible. Customization only via admin branding settings or UI extensions (app dev). Total scope reduced from 15 to 10 templates.
