# Product Page (product.json)

**Status:** v2 proof blocks added, production-ready

## Section inventory

| # | Section | Spacing tier | Status |
|---|---------|-------------|--------|
| 1 | `lusena-main-product` | custom (inline overrides) | Done |
| 2 | `lusena-pdp-feature-highlights` | standard | Done |
| 3 | `lusena-pdp-quality-evidence` | standard | Done |
| 4 | `lusena-pdp-truth-table` | standard | Done |
| 5 | `lusena-faq` (shared) | standard | Done |

## PDP snippets (11)

- `lusena-pdp-media.liquid` — Gallery/media
- `lusena-pdp-summary.liquid` — Title, price, rating
- `lusena-pdp-variant-picker.liquid` — Variant selection
- `lusena-pdp-atc.liquid` — Add to cart button
- `lusena-pdp-buybox-panels.liquid` — Buybox info panels
- `lusena-pdp-proof-chips.liquid` — Evidence chips
- `lusena-pdp-guarantee.liquid` — Guarantee messaging
- `lusena-pdp-cross-sell.liquid` — Cross-sell recommendations
- `lusena-pdp-sticky-atc.liquid` — Sticky add-to-cart bar
- `lusena-pdp-scripts.liquid` — PDP JavaScript
- `lusena-pdp-styles.liquid` — Doc-only stub (CSS in `assets/lusena-pdp.css`)

## Pending work

See `memory-bank/doc/features/pdp-migration-backlog.md` for 4 deferred items:
- Checkbox upsell component
- Reviews widget integration
- Notify-me flow for out-of-stock
- Schema cleanup pass
