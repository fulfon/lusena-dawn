# Product Page (product.json)

**Status:** Full UX audit completed 2026-03-09, production-ready

## Visual rhythm (alternating backgrounds)

```
1. Main Product       → surface-1 (white)
2. Feature Highlights → surface-2 (cream)    — white icon circles
3. Quality Evidence   → brand-bg (porcelain) — white cards, cream icon circles
4. Truth Table        → surface-1 (white)    — cream mobile cards
5. FAQ                → surface-2 (cream)    — text accordions
6. Final CTA          → brand-bg (porcelain)
```

## Section inventory

| # | Section | Background | Spacing tier | Status |
|---|---------|-----------|-------------|--------|
| 1 | `lusena-main-product` | surface-1 | custom (inline overrides) | Done |
| 2 | `lusena-pdp-feature-highlights` | surface-2 | standard | Done (heading "Co zyskujesz", bg_style, white icon-wrap, border-top removed, animated icons via `lusena-icon-animated` + `lusena-icon-animations.css` 2026-03-15) |
| 3 | `lusena-pdp-quality-evidence` | brand-bg | standard | Done (white cards, cream icon circles, no hover, scrollHeight accordion, funnel CTAs removed, content rewritten "why LUSENA?" angle, certificate verification URL from metafield, panel text alignment fix 76/80px, `rotate-ccw` icon added) |
| 4 | `lusena-pdp-truth-table` | surface-1 | standard | Done (5 rows, legally safe copy, lusena-icon, cream mobile cards) |
| 5 | `lusena-faq` (shared) | surface-2 | standard | Done (6 items, anchor_id=details, is_returns_target) |
| 6 | `lusena-final-cta` (shared) | brand-bg | spacious | Done ("Sprawdź kolekcję" → /collections/all) |

## PDP snippets (11)

- `lusena-pdp-media.liquid` — Gallery/media (breakpoint aligned to 768px, OEKO-TEX tile diacritics fixed)
- `lusena-pdp-summary.liquid` — Title, price, rating (per-product metafield overrides: headline, tagline, per-night toggle)
- `lusena-pdp-variant-picker.liquid` — Variant selection
- `lusena-pdp-atc.liquid` — Add to cart button
- `lusena-pdp-buybox-panels.liquid` — Buybox info panels (social proof reordered to slot 2, spacing tightened, conditional specs rendering, last-item border removed)
- `lusena-pdp-proof-chips.liquid` — Evidence chips
- `lusena-pdp-guarantee.liquid` — Guarantee messaging (restructured: p instead of div, no nested p tags)
- `lusena-pdp-cross-sell.liquid` — Cross-sell recommendations
- `lusena-pdp-sticky-atc.liquid` — Sticky add-to-cart bar (per-night toggle via `pdp_show_price_per_night` metafield)
- `lusena-pdp-scripts.liquid` — PDP JavaScript (returns deep-link fixed: clicks summary instead of setting .open)
- `lusena-pdp-styles.liquid` — Doc-only stub (CSS in `assets/lusena-pdp.css`)

## Pending work

See `memory-bank/doc/features/pdp-migration-backlog.md` for 4 deferred items:
- Checkbox upsell component
- Reviews widget integration
- Notify-me flow for out-of-stock
- Schema cleanup pass
