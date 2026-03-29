---
paths:
  - "sections/*bundle*"
  - "snippets/*bundle*"
  - "assets/*bundle*"
  - "memory-bank/doc/bundle*"
  - "templates/product.bundle*"
---
# Bundle System

## Pricing (all 20%+ discount, absolute zl savings only)
| Bundle | Price | Saves | Components |
|--------|-------|-------|------------|
| Nocna Rutyna | 399 zl | 109 zl | Poszewka + Bonnet |
| Piekny Sen | 349 zl | 89 zl | Poszewka + Maska 3D |
| Scrunchie Trio | 139 zl | 38 zl | 3x Scrunchie |

Never show percentage discounts. Only absolute savings ("Oszczedzasz 109 zl"). Under 400 zl psychological barrier for Nocna Rutyna.

## Critical metafield differences
- **`lusena.bundle_original_price`** (integer, e.g., 508) — NOT `compare_at_price`. Simple Bundles app overwrites `compare_at_price`, so bundles use a LUSENA metafield for the crossed-out price.
- **`lusena.bundle_nudge_map`** — JSON mapping trigger product handles to cart upsell data (label, savings, handle).

## Template differences
Bundles use `product.bundle` template. Key differences from standard PDP:
- No specs accordion (bundles don't have material specs)
- No packaging accordion (only Care accordion)
- Progressive disclosure steps instead of variant picker
- Color matching constraint: Nocna Rutyna = A+A or B+B only. Piekny Sen = any poszewka + Black mask.

## Cross-sell rules
- Scrunchie at 39 zl (not 59) via BXGY automatic discount on all individual PDPs + bundle PDPs
- **Single PDPs:** checkbox always visible between variant picker and ATC (inline `<script>` in snippet)
- **Bundle PDPs:** checkbox hidden until all colors picked, then revealed with animation (`lusena-bundle-scripts.liquid` handles JS)
- **Excluded:** scrunchie PDP (`product.handle != cs_handle`), scrunchie-containing bundles (`product.handle contains 'scrunchie'`)
- Shared snippet: `lusena-pdp-cross-sell-checkbox.liquid` with `skip_js: true` for bundles
- Free shipping threshold: 275 zl (bonnet 239 + scrunchie 39 = 278, clears it)
- Show exactly 1 upsell product (Iyengar jam study)
- Routine framing, never savings/discount framing
- Color matching: single PDP matches main variant color; bundle matches last-picked step color
