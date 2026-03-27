# {Product Name}

*Last updated: {DATE}*

## Basic info

| Field | Value | Status |
|-------|-------|--------|
| Title | {Product title in Polish} | |
| Description | (empty - PDP uses metafields) | |
| Category | {Shopify standard taxonomy category} | |
| Type | {Product type in Polish} | |
| Vendor | LUSENA | |
| Tags | {comma-separated tags} | |
| Theme template | Default product | |
| Status | Draft | |

## Pricing

| Field | Value | Status |
|-------|-------|--------|
| Price | {price} zł (VAT inclusive) | |
| Compare-at price | {price or "none"} | |
| Cost per item | {cost or "-"} | |
| Charge tax | Yes (23% VAT, tax-inclusive) | |

## Variants

| Option | Values | Status |
|--------|--------|--------|
| {Option name, e.g., Kolor} | {comma-separated values} | |

| Variant | SKU | Barcode | Status |
|---------|-----|---------|--------|
| {Variant 1} | {SKU or "-"} | - | |
| {Variant 2} | {SKU or "-"} | - | |

SKU format: `LUS-{3-letter product}-{3-letter variant}` (e.g., `LUS-PIL-GRY`)

## Inventory

| Field | Value | Status |
|-------|-------|--------|
| Inventory tracked | Yes | |
| Quantity (all locations) | 0 | |
| Continue selling when OOS | No | |

## Shipping

| Field | Value | Status |
|-------|-------|--------|
| Physical product | Yes | |
| Product weight | {weight} g | |
| Country of origin | China | |
| HS code | {code - see product-setup-checklist.md} | |
| Package | Store default | |

## SEO

| Field | Value | Status |
|-------|-------|--------|
| Page title | {max 70 chars - product name + key differentiator + LUSENA} | |
| Meta description | {max 160 chars - benefit + key specs} | |
| URL handle | {url-friendly-handle} | |

## Category metafields (Shopify standard)

| Field | Value | Status |
|-------|-------|--------|
| Color | {per variant} | |
| Closure style | {if applicable} | |
| Care instructions | {select from Shopify options} | |
| Fabric | Silk | |

## LUSENA metafields

> For what each field does and how to write great copy, see `memory-bank/doc/products/product-metafields-reference.md`

> **UNIVERSAL FIELDS - DO NOT MODIFY.** Fields marked "Pre-filled (universal)" are shared
> across ALL LUSENA silk products. They were validated once and must not be rewritten or
> "improved" during creative sessions. See the "Universal fields" section in
> `memory-bank/doc/products/product-metafields-reference.md` for the canonical list and rationale.

### Buybox content (REQUIRES CREATIVE SESSION - do not copy from other products)

> These fields are the primary conversion drivers. Each product needs original copy crafted through
> research, brandbook alignment, and legal review. See `memory-bank/doc/products/product-metafields-reference.md` for
> detailed guidance on each field's purpose, copy guidelines, and good/bad examples.

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_emotional_headline` | {craft in creative session} | |
| `lusena.pdp_tagline` | {craft in creative session} | |
| `lusena.pdp_show_price_per_night` | {true for nightly products, false for daytime} | |

### Benefit bullets (REQUIRES CREATIVE SESSION - do not copy from other products)

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_benefit_1` | {craft in creative session} | |
| `lusena.pdp_benefit_2` | {craft in creative session} | |
| `lusena.pdp_benefit_3` | {craft in creative session} | |

### Specs table

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_specs_material` | {e.g., 100% jedwab morwowy (Mulberry Silk)} | |
| `lusena.pdp_specs_weave` | {e.g., Charmeuse (splot satynowy) - or leave blank} | |
| `lusena.pdp_specs_momme` | {e.g., 22 momme - or leave blank} | |
| `lusena.pdp_specs_grade` | {e.g., 6A (najwyższa) - or leave blank} | |
| `lusena.pdp_specs_dimensions` | {e.g., 50 × 60 cm} | |
| `lusena.pdp_specs_closure` | {e.g., Koperta - or leave blank} | |
| `lusena.pdp_specs_weight` | {e.g., 85 g - or leave blank} | |
| `lusena.pdp_specs_certification` | {e.g., OEKO-TEX® Standard 100 - or leave blank} | |

### Packaging

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_packaging_items` | Item 1: {the product itself} / Item 2: {gift box} / Item 3: {care card or extras} | |

### Care & Badge

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_care_steps` | {leave empty for default silk care - only fill if different} | |
| `lusena.badge_bestseller` | {true or false} | |

### Feature highlights (6 cards) - optional

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_feature_1-6_*` | {leave empty for theme defaults - only customize if product needs different cards} | |

### Icon animation specs (for SVG coding agent)

> For each feature card, describe the icon animation for the SVG agent. See constraints in `memory-bank/doc/products/product-metafields-reference.md`.

| Card | Icon | Animation spec |
|------|------|---------------|
| 1 | {icon name} | {what it looks like + how it moves + what emotion it reinforces} |
| 2 | {icon name} | {animation spec} |
| 3 | {icon name} | {animation spec} |
| 4 | {icon name} | {animation spec} |
| 5 | {icon name} | {animation spec} |
| 6 | {icon name} | {animation spec} |

## Validation results

### Legal check
- **Date:** {date}
- **Verdict:** {PASS / FAIL}
- **Notes:** {any issues found and how they were resolved}

### Customer validation
- **Date:** {date}
- **Run:** {1 or 2}

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | /10 | /10 | /10 | /10 | /10 |
| Purchase intent | /10 | /10 | /10 | /10 | /10 |
| Premium feel | /10 | /10 | /10 | /10 | /10 |

- **Key feedback:** {main objections addressed, strongest elements identified}
- **Final decision:** {finalized / escalated to owner}

## Media

| Type | Status |
|------|--------|
| Product photos | |
| Lifestyle photos | |
| Video | |

## Collections

{List collections this product belongs to, or "Not assigned yet"}

## Remaining action items

{List anything still pending for this product}
