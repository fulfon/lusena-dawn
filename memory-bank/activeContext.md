# Active Context

*Last updated: 2026-03-05*

## Current focus

**Dawn pages → LUSENA migration.** Batches 1 + 5 COMPLETE. Next: Batch 2 (simple content pages: 404, generic page, contact).

## Recent completed work (2026-03-05)

- **Search page migration COMPLETE (Batch 5)** — Created `sections/lusena-search.liquid` with full LUSENA styling. Features: predictive search with Polish translations, product grid (2/3/4 cols), non-product results list, empty state with bestseller suggestions, "load more" pagination. Smart viewport management: `min-height: 100dvh` on main pushes footer below fold; initial state (no query) uses `padding-top: 18vh` for upper-third positioning; results state uses flex-grow for natural content flow. Disabled Dawn's `scrollIntoView`-on-focus to prevent jarring scroll on mobile. Rewired `templates/search.json`.
- **Search translations (Polish)** — Translated all search-related strings in `locales/en.default.json`: predictive search dropdown text, no-results message, result count labels, accessibility labels ("Szukaj", "Wyczyść wyszukiwanie"), loading text ("Ładowanie..."). Polish quotation marks „..." used in user-facing strings.
- **Cart page migration COMPLETE (Batch 1)** — Full-page cart with drawer parity. 3 new files: `lusena-cart-items.liquid`, `lusena-cart-quantity.liquid`, `lusena-cart-footer.liquid`.
- **Batches 3 & 4 N/A** — Shopify deprecated legacy customer accounts (Feb 2026). All artifacts cleaned up. Branding configured in Shopify admin for checkout, thank you, sign in, orders, order status, profile pages.

## Next steps

1. **Batch 2: Simple content pages** — 404, generic page, contact
2. **Batch 6: Blog** — `blog.json`, `article.json`
3. **Batch 7: Password** — `password.json`
4. PDP migration backlog items (see `memory-bank/doc/features/pdp-migration-backlog.md`)
5. Homepage migration backlog items (see `memory-bank/doc/features/homepage-migration-backlog.md`)

## Known issues

- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` is a doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- **DEV-ONLY in cart upsell:** Hardcoded fallback product (`all_products['the-compare-at-price-snowboard']`) in both `lusena-cart-items.liquid` and `cart-drawer.liquid`. Hardcoded color label (`'Beżowy'`) in both files. Must be replaced with real product data before production.

## Shopify-managed pages (not in theme — configured via admin)

**Shopify deprecated legacy/classic customer accounts in February 2026.** These pages are hosted by Shopify and branded via admin settings (Settings → Checkout → Customize):

| Page | Status |
|------|--------|
| Checkout | Branded (2026-03-05) |
| Thank you | Branded (2026-03-05) |
| Sign in | Branded (2026-03-05) |
| Orders | Branded (2026-03-05) |
| Order status | Branded (2026-03-05) |
| Profile | Branded (2026-03-05) |

**Branding applied:** Logo (PNG), main bg `#F7F5F2`, order summary bg `#F0EEEB`, accent/buttons `#0E5E5A`, error `#B91C1C`, white fields/cards, logo centered.

**Liquid templates for `customers/*` are dead code** — bypassed by the new system. Batches 3 & 4 permanently N/A. Further customization only via customer account UI extensions (app dev).

## Architecture note

CSS loads in this order via `layout/theme.liquid`:
1. `base.css` (Dawn foundation)
2. Cart CSS (conditional)
3. `lusena-foundations.css` — tokens, utilities, components, body/main rules (~40KB)
4. `lusena-button-system.css` — button/icon-button primitives
5. `lusena-header.css` — header section styles
6. `lusena-hero.css` — hero section styles
7. `lusena-footer.css` — footer section styles
8. `lusena-pdp.css` — PDP styles (loaded per-page in section file)
9. `compiled_assets/styles.css` — remaining small `{% stylesheet %}` blocks (~38KB, limit 73KB)

**MANDATORY:** After adding CSS to any `{% stylesheet %}` block, check compiled_assets size in DevTools — must stay under 55KB. See `memory-bank/doc/patterns/css-architecture.md` for full pattern.

Shared components in foundations: `.lusena-split`, `.lusena-accordion`, `.lusena-trust-bar`, `.lusena-testimonial`, `.lusena-content-card`, `.lusena-newsletter`, `.lusena-truth-table`.

Shared sections (reusable across pages): `lusena-faq` (homepage, quality, returns, PDP), `lusena-trust-bar` (homepage, about, quality), `lusena-final-cta` (about, quality, returns).
