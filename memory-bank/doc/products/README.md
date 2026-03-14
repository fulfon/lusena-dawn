# LUSENA Product Catalog (Shopify Admin Data)

This folder stores the complete Shopify admin configuration for each product — metafield values, pricing, variants, SEO, shipping, and status. Each file is the single source of truth for what has been entered (or needs to be entered) in Shopify admin for that product.

## Key references

- **Metafield reference (what each field does, where it renders, how to write great copy):** `docs/product-metafields-reference.md`
- **Product setup checklist (how to create definitions + example values per product type):** `docs/product-setup-checklist.md`
- **Brand direction (tone, voice, legal rules):** `docs/LUSENA_BrandBook_v2.md`
- **Blank template for new products:** `memory-bank/doc/products/_template.md`
- **Flagship product (reference for real values):** `memory-bank/doc/products/poszewka-jedwabna.md`

## File naming

`{handle}.md` — one file per product, named by URL handle.

## How to add a new product

1. Copy `_template.md` and rename to `{handle}.md`
2. Read `docs/product-metafields-reference.md` to understand each field's purpose and conversion role
3. Fill in values — refer to `poszewka-jedwabna.md` as a real-world example, and `docs/product-setup-checklist.md` section D for suggested values per product type
4. The owner reviews and adjusts the values in the MD file first, then manually copies them into Shopify admin
5. Update the "Status" column in each table as fields are entered in Shopify

## Products

| Handle | Product | Tier | Status |
|--------|---------|------|--------|
| `poszewka-jedwabna` | Poszewka jedwabna 50×60 | 1 (flagship) | In progress |
| `silk-scrunchie` | Scrunchie jedwabny | 2 | Not started |
| `silk-bonnet` | Bonnet jedwabny | 2 | Not started |
| `silk-eye-mask` | Opaska na oczy | 2 | Not started |
| `heatless-curlers` | Lokówki jedwabne | 3 | Not started |

## Store-wide settings (configured 2026-03-14)

- **Store currency:** PLN (zł)
- **Primary market:** Poland (only active market)
- **Tax:** 23% VAT, tax-inclusive pricing enabled
- **Shipping zone:** Polska (free courier rate)
- **VAT registration:** PL0000000000 (dummy — replace before going live)
- **Metafield definitions:** 35 product metafields created under `lusena.*` namespace (see reference doc for full list)
