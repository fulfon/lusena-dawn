# Active Context

*Last updated: 2026-03-06*

## Current focus

**Dawn pages → LUSENA migration.** Batches 1, 2, 5, 6 COMPLETE. Next: Batch 7 (password page), then polish backlogs.

## Recent completed work (2026-03-06)

- **Content pages migration COMPLETE + polished (Batch 2)** — Created `sections/lusena-404.liquid` (centered error message + 4-product bestseller grid + viewport-fill), `sections/lusena-main-page.liquid` (breadcrumbs + title + richtext + viewport-fill), `sections/lusena-contact-form.liquid` (full `.lusena-form` system: Name/Email side-by-side, Phone, Message textarea, success/error messages, customer pre-fill). Extended `lusena-breadcrumbs.liquid` for `page` type with `breadcrumb_label` override param. Polish translations for 404 + contact in `en.default.json`. Contact page includes `lusena-newsletter` as footer section. Zero new CSS added to foundations — all reused existing components.
  - **Polish pass:** Viewport-fill on contact + generic page (page section grows, not newsletter — lesson #48). Animations: all content blocks use `scroll-trigger animate--slide-in` (not fade-in — lesson #47), form animated via class on `{% form %}` tag (not wrapper div, which breaks flex gap). Submit button full-width on mobile. Mobile top padding tightened to 16px (`--lusena-space-2`) on both contact and generic page. Breadcrumb `breadcrumb_label` param added for Polish override ("Kontakt").
- **Blog + Article page migration COMPLETE (Batch 6)** — Created `sections/lusena-blog.liquid` (2-col grid, pagination, rich empty state with viewport fill) and `sections/lusena-article.liquid` (breadcrumbs, 16:9 hero, richtext body, share button, LD+JSON structured data). New snippets: `lusena-article-card.liquid`, `lusena-share-button.liquid` (Web Share API + clipboard fallback), `lusena-date-pl.liquid` (Polish date formatting — bypasses English store locale). Extended `lusena-breadcrumbs.liquid` for `blog`/`article` page types. Added `share` icon to `lusena-icon.liquid`.

## Next steps

1. **Batch 7: Password** — `password.json` (last theme-controlled page)
2. PDP migration backlog items (see `memory-bank/doc/features/pdp-migration-backlog.md`)
3. Homepage migration backlog items (see `memory-bank/doc/features/homepage-migration-backlog.md`)

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

Shared sections (reusable across pages): `lusena-faq` (homepage, quality, returns, PDP), `lusena-trust-bar` (homepage, about, quality), `lusena-final-cta` (about, quality, returns), `lusena-newsletter` (homepage, article, contact — with optional secondary link on article).
