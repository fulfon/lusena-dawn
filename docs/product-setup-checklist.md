# LUSENA Product Setup Checklist

How to add a new product to the LUSENA store and configure its PDP (Product Detail Page).

## Workflow

1. Create the product in Shopify Admin (title, images, variants, price)
2. Fill in the metafields listed below (product editor → Metafields section at bottom)
3. Preview the PDP — section settings in `product.json` serve as fallbacks for any blank metafield

## Metafield Definitions Setup (one-time)

Before adding products, create these definitions in **Settings → Custom data → Products**:

| Namespace & Key | Admin Label | Type |
|---|---|---|
| `lusena.pdp_emotional_headline` | PDP: Nagłówek emocjonalny | Single-line text |
| `lusena.pdp_tagline` | PDP: Tagline / opis krótki | Multi-line text |
| `lusena.pdp_show_price_per_night` | PDP: Pokaż cenę za noc | True or false |
| `lusena.pdp_benefit_1` | PDP: Benefit 1 | Single-line text |
| `lusena.pdp_benefit_2` | PDP: Benefit 2 | Single-line text |
| `lusena.pdp_benefit_3` | PDP: Benefit 3 | Single-line text |
| `lusena.pdp_specs_material` | Specyfikacja: Materiał | Single-line text |
| `lusena.pdp_specs_weave` | Specyfikacja: Splot | Single-line text |
| `lusena.pdp_specs_momme` | Specyfikacja: Momme | Single-line text |
| `lusena.pdp_specs_grade` | Specyfikacja: Klasa | Single-line text |
| `lusena.pdp_specs_dimensions` | Specyfikacja: Wymiary | Single-line text |
| `lusena.pdp_specs_closure` | Specyfikacja: Zamknięcie | Single-line text |
| `lusena.pdp_specs_weight` | Specyfikacja: Waga | Single-line text |
| `lusena.pdp_specs_certification` | Specyfikacja: Certyfikat | Single-line text |
| `lusena.pdp_packaging_items` | Opakowanie: Zawartość | List of single-line text |
| `lusena.pdp_care_steps` | Pielęgnacja: Kroki | List of single-line text |
| `lusena.badge_bestseller` | Badge: Bestseller | True or false |
| `lusena.pdp_feature_1_icon` | Feature 1: Ikona | Single-line text |
| `lusena.pdp_feature_1_title` | Feature 1: Tytuł | Single-line text |
| `lusena.pdp_feature_1_description` | Feature 1: Opis | Multi-line text |
| `lusena.pdp_feature_2_icon` | Feature 2: Ikona | Single-line text |
| `lusena.pdp_feature_2_title` | Feature 2: Tytuł | Single-line text |
| `lusena.pdp_feature_2_description` | Feature 2: Opis | Multi-line text |
| `lusena.pdp_feature_3_icon` | Feature 3: Ikona | Single-line text |
| `lusena.pdp_feature_3_title` | Feature 3: Tytuł | Single-line text |
| `lusena.pdp_feature_3_description` | Feature 3: Opis | Multi-line text |
| `lusena.pdp_feature_4_icon` | Feature 4: Ikona | Single-line text |
| `lusena.pdp_feature_4_title` | Feature 4: Tytuł | Single-line text |
| `lusena.pdp_feature_4_description` | Feature 4: Opis | Multi-line text |
| `lusena.pdp_feature_5_icon` | Feature 5: Ikona | Single-line text |
| `lusena.pdp_feature_5_title` | Feature 5: Tytuł | Single-line text |
| `lusena.pdp_feature_5_description` | Feature 5: Opis | Multi-line text |
| `lusena.pdp_feature_6_icon` | Feature 6: Ikona | Single-line text |
| `lusena.pdp_feature_6_title` | Feature 6: Tytuł | Single-line text |
| `lusena.pdp_feature_6_description` | Feature 6: Opis | Multi-line text |

## A. Required Metafields (fill for every product)

> **Creative copy fields** (headline, tagline, benefits) should NOT be copy-pasted from old examples.
> Each product deserves a dedicated creative session — research the product's unique benefits, align with brandbook tone, verify legal compliance.
> See `docs/product-metafields-reference.md` for detailed guidance on each field's conversion role and copy guidelines.

### Buybox content (REQUIRES CREATIVE SESSION)

| Metafield | What it does |
|---|---|
| `lusena.pdp_emotional_headline` | Eyebrow text above product title — the emotional hook |
| `lusena.pdp_tagline` | Short description below title — proof + problem/solution |
| `lusena.pdp_benefit_1` | Benefit bullet 1 — primary benefit angle |
| `lusena.pdp_benefit_2` | Benefit bullet 2 — unique differentiator angle |
| `lusena.pdp_benefit_3` | Benefit bullet 3 — secondary benefit angle |

### Specs table (rows with blank values are automatically hidden)

| Metafield | Example (pillowcase) |
|---|---|
| `lusena.pdp_specs_material` | 100% jedwab morwowy (Mulberry Silk) |
| `lusena.pdp_specs_dimensions` | 50 × 60 cm |
| `lusena.pdp_specs_weight` | 85 g |

### Packaging (what's in the box)

| Metafield | Example (pillowcase) |
|---|---|
| `lusena.pdp_packaging_items` | ["Jedwabna poszewka LUSENA", "Eleganckie pudełko prezentowe LUSENA", "Karta z instrukcją pielęgnacji"] |

## B. Recommended Metafields (fill when applicable)

| Metafield | Default if blank | When to fill |
|---|---|---|
| `lusena.pdp_specs_weave` | (row hidden) | Fabric products: "Charmeuse (splot satynowy)" |
| `lusena.pdp_specs_momme` | (row hidden) | Fabric products: "22 momme" |
| `lusena.pdp_specs_grade` | (row hidden) | Fabric products: "6A (najwyższa)" |
| `lusena.pdp_specs_closure` | (row hidden) | Pillowcase: "Koperta" / Bonnet: "Elastyczny ściągacz" |
| `lusena.pdp_specs_certification` | (row hidden) | All silk products: "OEKO-TEX® Standard 100" |
| `lusena.pdp_care_steps` | Standard silk care (5 steps) | Only if product needs different care instructions |
| `lusena.pdp_show_price_per_night` | true (shows per-night price) | Set to `false` for scrunchies, heatless curlers |
| `lusena.badge_bestseller` | false | Set to `true` for top-selling products (shows badge on gallery) |

## C. Optional: Per-Product Feature Highlights

The PDP has 6 feature cards below the buybox. Defaults are configured in the theme editor. To override for a specific product, fill these metafields:

| Metafield | Type | Example |
|---|---|---|
| `lusena.pdp_feature_N_icon` | Icon name (see list below) | `sparkles` |
| `lusena.pdp_feature_N_title` | Card heading | Mniej zmarszczek, więcej blasku |
| `lusena.pdp_feature_N_description` | Card description | Jedwab nie wchłania wilgoci — Twój krem nocny zostaje na skórze... |

Replace `N` with 1-6 for each card position.

**Available icon names:** `sparkles`, `wind`, `shield-check`, `gift`, `droplets`, `heart`, `map-pin`, `layers`, `package`, `truck`, `clock`, `file-text`

## D. Factual Specs Per Product Type

> **Creative copy** (headline, tagline, benefits) is NOT included here.
> Those fields must be crafted in a dedicated creative session for each product.
> See `docs/product-metafields-reference.md` for how to approach each creative field.
> See `memory-bank/doc/products/poszewka-jedwabna.md` for a real example of finalized creative copy.

### Poszewka jedwabna (Pillowcase) — flagship

| Field | Value |
|---|---|
| `pdp_specs_material` | 100% jedwab morwowy (Mulberry Silk) |
| `pdp_specs_weave` | Charmeuse (splot satynowy) |
| `pdp_specs_momme` | 22 momme |
| `pdp_specs_grade` | 6A (najwyższa) |
| `pdp_specs_dimensions` | 50 × 60 cm |
| `pdp_specs_closure` | Koperta |
| `pdp_specs_weight` | 85 g |
| `pdp_specs_certification` | OEKO-TEX® Standard 100 |
| `pdp_show_price_per_night` | true |
| `badge_bestseller` | true |

### Bonnet jedwabny

| Field | Value |
|---|---|
| `pdp_specs_material` | 100% jedwab morwowy (Mulberry Silk) |
| `pdp_specs_weave` | Charmeuse (splot satynowy) |
| `pdp_specs_momme` | 22 momme |
| `pdp_specs_grade` | 6A (najwyższa) |
| `pdp_specs_dimensions` | Uniwersalny (elastyczny ściągacz) |
| `pdp_specs_closure` | Elastyczny ściągacz jedwabny |
| `pdp_specs_certification` | OEKO-TEX® Standard 100 |
| `pdp_show_price_per_night` | true |

### Scrunchie jedwabny

| Field | Value |
|---|---|
| `pdp_specs_material` | 100% jedwab morwowy (Mulberry Silk) |
| `pdp_specs_weave` | Charmeuse (splot satynowy) |
| `pdp_specs_momme` | 22 momme |
| `pdp_specs_grade` | 6A (najwyższa) |
| `pdp_specs_certification` | OEKO-TEX® Standard 100 |
| `pdp_show_price_per_night` | false |

### Opaska na oczy (Eye Mask)

| Field | Value |
|---|---|
| `pdp_specs_material` | 100% jedwab morwowy (Mulberry Silk) |
| `pdp_specs_weave` | Charmeuse (splot satynowy) |
| `pdp_specs_momme` | 22 momme |
| `pdp_specs_grade` | 6A (najwyższa) |
| `pdp_specs_closure` | Regulowana gumka jedwabna |
| `pdp_specs_certification` | OEKO-TEX® Standard 100 |
| `pdp_show_price_per_night` | true |

### Lokówki jedwabne (Heatless Curlers)

| Field | Value |
|---|---|
| `pdp_specs_material` | Jedwab morwowy + wypełnienie piankowe |
| `pdp_specs_dimensions` | Długość: 90 cm |
| `pdp_show_price_per_night` | false |

Note: Heatless curlers skip weave, momme, grade, closure, certification — those rows are automatically hidden.
