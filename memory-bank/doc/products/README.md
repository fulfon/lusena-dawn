# LUSENA Product Catalog (Shopify Admin Data)

This folder stores the complete Shopify admin configuration for each product - metafield values, pricing, variants, SEO, shipping, and status. Each file is the single source of truth for what has been entered (or needs to be entered) in Shopify admin for that product.

## Folder structure

```
products/
├── README.md               ← this file
├── _template.md             ← blank template for new products
├── poszewka-jedwabna.md     ← product docs (one per product, named by URL handle)
├── czepek-jedwabny.md
├── scrunchie-jedwabny.md
├── jedwabna-maska-3d.md
├── walek-do-lokow.md
├── exports/                 ← fresh CSV exported FROM Shopify (overwrite each time)
│   └── products_export.csv              (all products — export before every update)
└── imports/                 ← generated CSVs to import INTO Shopify
    ├── generate_import_from_export.py   (THE workflow script — reads export, patches copy, writes import)
    ├── products_import_updated.csv      (output — ready to import into Shopify)
    └── generate_import_csv.py           (legacy per-product generator, kept for reference)
```

## Key references

- **Metafield reference (what each field does, where it renders, how to write great copy):** `memory-bank/doc/products/product-metafields-reference.md`
- **Product setup checklist (how to create definitions + example values per product type):** `memory-bank/doc/products/product-setup-checklist.md`
- **Bundle strategy (pricing, composition, research, phases):** `memory-bank/doc/bundle-strategy.md`
- **Brand direction (tone, voice, legal rules):** `memory-bank/doc/brand/LUSENA_BrandBook_v2.md`
- **Blank template for new products:** `_template.md`
- **Flagship product (reference for real values):** `poszewka-jedwabna.md`

## File naming

`{handle}.md` - one file per product, named by URL handle.

## How to add a new product

1. Copy `_template.md` and rename to `{handle}.md`
2. Read `memory-bank/doc/products/product-metafields-reference.md` to understand each field's purpose and conversion role
3. Fill in values - refer to `poszewka-jedwabna.md` as a real-world example, and `memory-bank/doc/products/product-setup-checklist.md` section D for suggested values per product type
4. The owner reviews and adjusts the values in the MD file first, then manually copies them into Shopify admin
5. Update the "Status" column in each table as fields are entered in Shopify

## Products

| Handle | Product | Tier | Status |
|--------|---------|------|--------|
| `poszewka-jedwabna` | Poszewka jedwabna 50×60 | 1 (flagship) | Re-evaluated 2026-03-22 |
| `scrunchie-jedwabny` | Scrunchie jedwabny | 2 | Re-evaluated 2026-03-22 |
| `czepek-jedwabny` | Jedwabny czepek do spania | 2 | Re-evaluated 2026-03-22 |
| `jedwabna-maska-3d` | Jedwabna maska 3D do spania | 3 | Re-evaluated 2026-03-22 |
| `walek-do-lokow` | Jedwabny wałek do loków | 2 | Re-evaluated 2026-03-22 |
| `nocna-rutyna` | Nocna Rutyna (bundle) | - | Re-evaluated 2026-03-22 |
| `piekny-sen` | Piękny Sen (bundle) | - | Copywriter flow 2026-03-22 |
| `scrunchie-trio` | Scrunchie Trio (bundle) | - | Copywriter flow 2026-03-22 |

## Shopify CSV Import/Export

### Updating product copy in Shopify (standard workflow)

Use this workflow every time product copy changes (re-evaluations, new creative sessions, wording fixes). It updates ONLY the copy/metafield columns — variants, prices, inventory, images, and bundle_original_price are preserved exactly as Shopify has them.

**Step 1: Export from Shopify**
1. Go to **Shopify Admin > Products > Export**
2. Select "All products", format "CSV for Excel"
3. Save the downloaded file as `exports/products_export.csv` (overwrite the old one)

**Step 2: Generate the updated import file**
```bash
cd memory-bank/doc/products/imports/
python generate_import_from_export.py
```
This reads the fresh export, patches columns 35-73 (SEO + all `lusena.*` metafields) with current values from the MD product files, and writes `products_import_updated.csv`. Everything else is kept as-is from the export.

**Step 3: Import into Shopify**
1. Go to **Shopify Admin > Products > Import**
2. Upload `imports/products_import_updated.csv`
3. Check **"Overwrite existing products that have the same handle"**
4. Preview and confirm

**What gets updated:** SEO title, SEO description, headline, tagline, benefits, feature cards, packaging, specs, care, badges, price-per-night toggle.

**What is NOT touched:** Product title, variants/colors, prices, inventory, images, bundle_original_price, Shopify category metafields, status, vendor, tags, product category.

**Safety:** The import file is your exact Shopify export with only copy cells changed. Since every column is present with its current value, nothing gets blanked. Variant rows are passed through unchanged.

### When the script needs updating

The `generate_import_from_export.py` script has the copy values hardcoded from the MD product files. **Update the script whenever:**
- A product's copy is re-evaluated or revised
- A new product is added to the catalog
- Any metafield value changes in the MD files

The MD product files (`{handle}.md`) are always the source of truth. The script must match them.

### First-time import (new products)

For products that don't exist in Shopify yet, use the same workflow but WITHOUT the "Overwrite" checkbox. Shopify will create new products. After import, manually set Product Category and Shopify standard metafields in the admin.

### CRITICAL: Shopify category metafields (cols 72-76)

**DO NOT set these in the CSV.** They cause `"Owner subtype does not match the metafield definition's constraints"` errors.

Shopify has standard metafields (`care-instructions`, `closure-style`, `color-pattern`, `fabric`, `material`) that are **tied to specific product categories**. Different categories support different metafields:

| Category | Valid standard metafields |
|----------|-------------------------|
| Bedding (pillowcase) | `fabric`, `care-instructions`, `closure-style` |
| Eye Masks (3D mask) | `material` only |
| Hair Accessories (bonnet, scrunchie) | Check in Shopify admin |
| Hair Styling Tools (curlers) | Check in Shopify admin |

Setting a metafield that doesn't belong to the product's category causes the import to fail silently (Shopify says "success" but the product isn't created). **Always leave cols 72-76 empty in import CSVs and set them manually in Shopify admin after import.**

### CSV format rules (learned from debugging)

| Rule | Correct | Wrong |
|------|---------|-------|
| Encoding | UTF-8 with BOM | UTF-8 without BOM |
| Line endings | LF | CRLF |
| Variant Grams | `0.0` | `0` |
| Variant Weight Unit | `kg` | `g` |
| Product Category | Leave empty | Guess taxonomy strings |
| Shopify category metafields | Leave empty | Set values per category |
| LUSENA metafields (lusena.*) | Set freely | — |
| En-dash in "16–19 momme" | `–` (U+2013) | `-` (U+002D) |
| Booleans (LUSENA) | `TRUE` / `FALSE` | `true` / `false` |
| Booleans (Shopify) | `true` / `false` | `TRUE` / `FALSE` |
| List fields (packaging, care) | Semicolons (`; `) | Newlines (Shopify exports newlines but rejects them on import) |

### Export vs MD discrepancies

The export CSVs in `exports/` were exported from Shopify and may contain **older metafield values**. The MD files are always the **source of truth** for finalized copy. Known differences in poszewka export:

| Field | Export (old) | MD (correct) |
|-------|-------------|--------------|
| Benefit 2 | "Nie wchłania kremów..." | "Wchłania znacznie mniej kremów..." |
| Tagline | Old version | Finalized composite version |
| Closure spec | "Zamek błyskawiczny" | "Koperta" |
| Feature 3 | (empty) | "Chłodna strona poduszki..." (temperature card) |
| Tags | (empty) | Finalized tag set |
| Inventory policy | `continue` | `deny` |

### Heatless curlers: expected deviations

The heatless curler is the only product with PP cotton filling inside the silk. This causes 8 legitimate deviations from the standard template (custom care steps, custom material spec, different feature icons, "użytkowania" not "pielęgnacji" in packaging, etc.). See `walek-do-lokow.md` for details. These are correct and intentional — do not "fix" them to match other products.

### Post-import checklist

After importing, complete these manual steps in Shopify admin:

- [ ] Set Product Category (pick from dropdown)
- [ ] Set Shopify standard metafields (fabric/material, care instructions) — category-specific
- [ ] Add color variants (when colors are finalized)
- [ ] Upload product photos (when media is ready)
- [ ] Set inventory quantities (when stock arrives)
- [ ] Fill cost per item (when import costs are calculated)
- [ ] Open PDP in theme preview — verify all metafields render

## Store-wide settings (configured 2026-03-14)

- **Store currency:** PLN (zł)
- **Primary market:** Poland (only active market)
- **Tax:** 23% VAT, tax-inclusive pricing enabled
- **Shipping zone:** Polska (free courier rate)
- **VAT registration:** PL0000000000 (dummy - replace before going live)
- **Metafield definitions:** 35 product metafields created under `lusena.*` namespace (see reference doc for full list)
