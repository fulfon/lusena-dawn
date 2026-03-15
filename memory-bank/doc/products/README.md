# LUSENA Product Catalog (Shopify Admin Data)

This folder stores the complete Shopify admin configuration for each product - metafield values, pricing, variants, SEO, shipping, and status. Each file is the single source of truth for what has been entered (or needs to be entered) in Shopify admin for that product.

## Folder structure

```
products/
├── README.md               ← this file
├── _template.md             ← blank template for new products
├── poszewka-jedwabna.md     ← product docs (one per product, named by URL handle)
├── silk-bonnet.md
├── silk-scrunchie.md
├── jedwabna-maska-3d.md
├── heatless-curlers.md
├── exports/                 ← reference CSVs exported FROM Shopify
│   ├── products_export.csv              (poszewka, 2026-03-14)
│   └── products_export_3deyemask.csv    (3D mask, 2026-03-15)
└── imports/                 ← generated CSVs to import INTO Shopify
    ├── generate_import_csv.py           (run to regenerate all import CSVs)
    ├── silk-bonnet_import.csv
    ├── silk-scrunchie_import.csv
    ├── jedwabna-maska-3d_import.csv
    └── heatless-curlers_import.csv
```

## Key references

- **Metafield reference (what each field does, where it renders, how to write great copy):** `docs/product-metafields-reference.md`
- **Product setup checklist (how to create definitions + example values per product type):** `docs/product-setup-checklist.md`
- **Bundle strategy (pricing, composition, research, phases):** `memory-bank/doc/bundle-strategy.md`
- **Brand direction (tone, voice, legal rules):** `docs/LUSENA_BrandBook_v2.md`
- **Blank template for new products:** `_template.md`
- **Flagship product (reference for real values):** `poszewka-jedwabna.md`

## File naming

`{handle}.md` - one file per product, named by URL handle.

## How to add a new product

1. Copy `_template.md` and rename to `{handle}.md`
2. Read `docs/product-metafields-reference.md` to understand each field's purpose and conversion role
3. Fill in values - refer to `poszewka-jedwabna.md` as a real-world example, and `docs/product-setup-checklist.md` section D for suggested values per product type
4. The owner reviews and adjusts the values in the MD file first, then manually copies them into Shopify admin
5. Update the "Status" column in each table as fields are entered in Shopify

## Products

| Handle | Product | Tier | Status |
|--------|---------|------|--------|
| `poszewka-jedwabna` | Poszewka jedwabna 50×60 | 1 (flagship) | Copy finalized (2026-03-14) |
| `silk-scrunchie` | Scrunchie jedwabny | 2 | Copy finalized (2026-03-14) |
| `silk-bonnet` | Jedwabny czepek do spania | 2 | Copy finalized (2026-03-14) |
| `jedwabna-maska-3d` | Jedwabna maska 3D do spania | 3 | Copy finalized (2026-03-14) |
| `heatless-curlers` | Jedwabny wałek do loków | 2 | Copy finalized (2026-03-14) |

## Shopify CSV Import/Export

### How to import a product

1. Go to **Shopify Admin > Products > Import**
2. Upload the CSV from `imports/` (one product per file)
3. Use **Preview** to check for warnings before confirming
4. After import, manually set in Shopify admin:
   - **Product Category** — pick from the dropdown (don't set in CSV, taxonomy strings break easily)
   - **Shopify standard metafields** (fabric, material, care instructions) — these are category-specific, see warning below
   - **Color variants** — add when colors are finalized
5. Open PDP in theme preview — verify all LUSENA metafields render correctly

### How to regenerate import CSVs

```bash
cd imports/
python generate_import_csv.py
```

This reads the header from `exports/products_export.csv` and generates one CSV per product with all LUSENA metafield values from the finalized MD files.

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
| List fields (packaging, care) | Newlines within quoted cell | Semicolons |

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

The heatless curler is the only product with PP cotton filling inside the silk. This causes 8 legitimate deviations from the standard template (custom care steps, custom material spec, different feature icons, "użytkowania" not "pielęgnacji" in packaging, etc.). See `heatless-curlers.md` for details. These are correct and intentional — do not "fix" them to match other products.

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
