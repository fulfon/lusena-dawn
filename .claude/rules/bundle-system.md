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
- Scrunchie at 39 zl (not 59) on pillowcase PDP only
- Free shipping threshold: 289 zl (poszewka 269 + scrunchie 39 = 308, clears it)
- Show exactly 1 upsell product (Iyengar jam study)
- Routine framing, never savings/discount framing
