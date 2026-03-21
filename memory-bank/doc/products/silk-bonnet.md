# Jedwabny czepek do spania

*Last updated: 2026-03-16*

## Basic info

| Field | Value | Status |
|-------|-------|--------|
| Title | Jedwabny czepek do spania | Done |
| Description | (empty - PDP uses metafields) | Done |
| Category | Hair Accessories | Done |
| Type | Czepek jedwabny | Done |
| Vendor | LUSENA | Done |
| Tags | jedwab, czepek, czepek-jedwabny, czepek-do-spania, bonnet, 22-momme, nocna-rutyna, hair-care, ochrona-wlosow | Done |
| Theme template | Default product | Done |
| Status | Draft | Done |

> **Title research (2026-03-14):** "Jedwabny czepek do spania" is the dominant search term in Polish e-commerce. All major competitors (ALMANIA, SENSILK, Spadiora, BOMOYE, So Fluffy) use "czepek." "Bonnet" has near-zero Polish search volume - even Loczek.pl (the only brand using it) adds "(czepek)" for clarity. "Turban" refers to a different wrap-style product. The word "czepek" is fully reclaimed by the silk/hair care industry - adding "jedwabny" elevates it. Tag includes "bonnet" for cross-language discoverability.

## Pricing

| Field | Value | Status |
|-------|-------|--------|
| Price | 239 zł (VAT inclusive) | Done |
| Compare-at price | (none) | Done |
| Cost per item | - | **PENDING** (fill when import cost is known) |
| Charge tax | Yes (23% VAT, tax-inclusive) | Done |

> **Pricing research (2026-03-14):** 239 zł positions LUSENA in the upper-premium Polish tier - between ALMANIA (230 zł) and Spadiora (279 zł), far below Slip (355+ zł). No compare-at price - strikethrough pricing undermines premium positioning (LoveSilk's constant -50% promos are a cautionary example). Price-per-night (0,65 zł/noc) enabled for value reframing.

## Variants

> **Color strategy:** `memory-bank/doc/color-strategy.md` — research-backed unified capsule palette (2026-03-20)

| Option | Values | Status |
|--------|--------|--------|
| Kolor | Czarny, Brudny róż | **FINALIZED** (2026-03-20) |

| Variant | Role | SKU | Units (initial order) | Barcode | Status |
|---------|------|-----|-----------------------|---------|--------|
| Czarny (Black) | A — dark base | LUS-BON-BLK | 30 | - | **PENDING** (rename in Shopify from "Gold") |
| Brudny róż (Dusty Rose) | B — hero | LUS-BON-RSE | 30 | - | **PENDING** (rename in Shopify from "Gray") |

Equal split per §7.2 MOQ (60 / 2 = 30 each). Bonnet gets A+B only (§7.3) — enables matching Nocna Rutyna bundle.

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
| Product weight | - | **PENDING** (verify with actual product) |
| Country of origin | China | |
| HS code | 6505 00 90 | Done |
| Package | Store default | |

> **HS code research (2026-03-14):** Chapter 65 (Headgear), heading 6505 (hats/headgear made up from textile fabric), subheading 6505 00 90 (other). EU customs duty ~6.3-8% for MFN origins. Verify on TARIC before first import.

## SEO

| Field | Value | Status |
|-------|-------|--------|
| Page title | Jedwabny czepek do spania 22 momme - ochrona włosów · LUSENA | Done |
| Meta description | Jedwabny czepek z regulacją obwodu - 22 momme, Grade 6A z Suzhou. Ściągacz pokryty jedwabiem chroni linię włosów. Mniej tarcia, mniej plątania. OEKO-TEX® Standard 100. | Done |
| URL handle | silk-bonnet | Done |

## Category metafields (Shopify standard)

| Field | Value | Status |
|-------|-------|--------|
| Color | (per variant, after colors finalized) | **PENDING** |
| Care instructions | Machine washable, Hand wash | Done |
| Fabric | Silk | Done |

## LUSENA metafields

> For what each field does and how to write great copy, see `docs/product-metafields-reference.md`
>
> **UNIVERSAL FIELDS - DO NOT MODIFY.** Fields marked "Pre-filled (universal)" are shared
> across ALL LUSENA silk products. They were validated once and must not be rewritten or
> "improved" during creative sessions. See `docs/product-metafields-reference.md` → "Universal fields".

### Buybox content

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_emotional_headline` | Budzisz się z fryzurą - nie z plątaniną. | Done |
| `lusena.pdp_tagline` | Otula włosy gładkim jedwabiem ze wszystkich stron - mniej tarcia, plątania i puszenia niż na bawełnie. Regulowany ściągacz pokryty jedwabiem dopasowuje się do obwodu głowy. Chroni fryzurę od wieczora do rana - loki, fale czy prostowanie przetrwają noc. | **UPDATED** (2026-03-17: benefit-oriented, removed redundant specs) |
| `lusena.pdp_show_price_per_night` | true | Done |

### Benefit bullets

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_benefit_1` | Otula włosy gładkim jedwabiem ze wszystkich stron - mniej tarcia, plątania i puszenia niż na bawełnie | Done |
| `lusena.pdp_benefit_2` | Regulowany ściągacz pokryty jedwabiem - dopasujesz obwód do swojej głowy, żadne gumowe włókno nie dotyka włosów | Done |
| `lusena.pdp_benefit_3` | Chroni fryzurę od wieczora do rana - loki, fale czy prostowanie przetrwają noc | Done |

### Specs table

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_specs_material` | 100% jedwab morwowy (Mulberry Silk) | Pre-filled (universal) |
| `lusena.pdp_specs_weave` | Charmeuse (splot satynowy) | Pre-filled (universal) |
| `lusena.pdp_specs_momme` | 22 momme | Pre-filled (universal) |
| `lusena.pdp_specs_grade` | 6A (najwyższa) | Pre-filled (universal) |
| `lusena.pdp_specs_dimensions` | Regulowany (ściągacz z regulacją obwodu) | Done |
| `lusena.pdp_specs_label_closure` | Dopasowanie | Done |
| `lusena.pdp_specs_closure` | Regulowany ściągacz pokryty jedwabiem | Done |
| `lusena.pdp_specs_weight` | - | **PENDING** (verify with actual product) |
| `lusena.pdp_specs_certification` | OEKO-TEX® Standard 100 | Pre-filled (universal) |

### Packaging

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_packaging_items` | ["Jedwabny czepek LUSENA", "Eleganckie pudełko prezentowe LUSENA", "Karta z instrukcją pielęgnacji"] | Done |

### Care & Badge

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_care_steps` | (empty - theme defaults used) | Pre-filled (universal) |
| `lusena.badge_bestseller` | false | Done |

### Feature highlights (6 cards)

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_feature_1_icon` | heart | Done |
| `lusena.pdp_feature_1_title` | Chroni linię włosów | Done |
| `lusena.pdp_feature_1_description` | Zwykłe czepki mają odsłoniętą gumkę, która ściska i ociera najdelikatniejsze pasma. W czepku LUSENA ściągacz jest pokryty jedwabiem od wewnątrz - gładkie włókno zamiast twardej gumy. | Done |
| `lusena.pdp_feature_2_icon` | layers | Pre-filled (universal) |
| `lusena.pdp_feature_2_title` | Dlaczego 22 momme? | Pre-filled (universal) |
| `lusena.pdp_feature_2_description` | Momme to gęstość jedwabiu - im wyższe, tym grubszy i trwalszy materiał. Standard rynkowy to 16-19 momme. Nasze 22 momme to gęstszy splot, który lepiej trzyma kształt i dłużej służy. | Pre-filled (universal) |
| `lusena.pdp_feature_3_icon` | wind | Done |
| `lusena.pdp_feature_3_title` | Trzyma pewnie całą noc | Done |
| `lusena.pdp_feature_3_description` | Regulowany ściągacz dopasujesz dokładnie do obwodu głowy - ani za luźno, ani za ciasno. Jedwab morwowy oddycha i pomaga regulować temperaturę. Budzisz się w czepku, nie obok niego. | Done |
| `lusena.pdp_feature_4_icon` | shield-check | Pre-filled (universal) |
| `lusena.pdp_feature_4_title` | Jedwab, nie satyna z poliestru | Pre-filled (universal) |
| `lusena.pdp_feature_4_description` | Satyna to nazwa splotu, nie materiału - najczęściej kryje się za nią poliester. LUSENA to 100% jedwab morwowy: naturalne włókno białkowe, które oddycha i nie elektryzuje. | Pre-filled (universal) |
| `lusena.pdp_feature_5_icon` | sparkles | Pre-filled (universal) |
| `lusena.pdp_feature_5_title` | Certyfikowany OEKO-TEX® 100 | Pre-filled (universal) |
| `lusena.pdp_feature_5_description` | Niezależny certyfikat potwierdza, że nasz jedwab jest bezpieczny dla skóry i wolny od szkodliwych substancji. Pewność, którą możesz zweryfikować. | Pre-filled (universal) |
| `lusena.pdp_feature_6_icon` | gift | Pre-filled (universal) |
| `lusena.pdp_feature_6_title` | Gotowa do wręczenia | Pre-filled (universal) |
| `lusena.pdp_feature_6_description` | Każdy czepek LUSENA przychodzi w eleganckim pudełku prezentowym - idealny upominek, który robi wrażenie. Bez dodatkowego pakowania. | Done |

### Icon animation specs (for SVG coding agent)

> For each feature card, describe the icon animation for the SVG agent. See constraints in `docs/product-metafields-reference.md`.

| Card | Icon | Animation spec |
|------|------|---------------|
| 1 | heart | Heart shape with a very slow, gentle scale pulse (1.0→1.03→1.0) over 7 seconds. The heart seems to "breathe" - calm, protective feeling toward hair. Easing: ease-in-out. Reinforces the idea of gentle, all-around protection from the silk-covered elastic. |
| 2 | layers | 3 stacked horizontal layers. Bottom layer gently shifts down 1px then back, middle stays still, top shifts up 1px then back - a slow "breathing" of the stack over 8 seconds. Reinforces the feeling of density and substance. Easing: ease-in-out. |
| 3 | wind | Three curved wind lines. Lines gently wave from left to right in sequence (translateX 0→2px→0), staggered start times, over 7 seconds total. Feels like a soft, barely-there breeze - comforting, not chaotic. Easing: ease-in-out. Reinforces breathability and lightness of the bonnet. |
| 4 | shield-check | Shield outline with a checkmark inside. Checkmark draws itself once via stroke-dashoffset animation over 1.5s on first viewport entry, then stays static permanently. Reinforces "verified, authentic" feeling. No looping. |
| 5 | sparkles | 3 small diamond-shaped stars in a cluster. Stars gently twinkle in sequence (opacity 0.4→1→0.4), one star at a time, left to right. 7-second full cycle. Easing: ease-in-out. Subtle shimmer of quality and certification. |
| 6 | gift | Gift box with ribbon on top. Very subtle "unwrap" motion - lid shifts up 1px then back down over 6 seconds. The ribbon bow has a tiny wiggle (rotate ±1°). Playful but restrained. Reinforces the excitement of receiving a beautifully wrapped gift. |

## Validation results

### Legal checks
- **Date:** 2026-03-14 — PASS (1 fix applied). "nie osłabia" (absolute) in benefit 2 → fixed to "delikatniejszy dla linii włosów". All claims use approved hedging or physical/mechanical framing. Advisory: card 3 "reguluje temperaturę" softened to "pomaga regulować" in Run 3.
- **Date:** 2026-03-16 — PASS (0 issues, 1 warning). Adjustability claims ("regulowany ściągacz", "dopasujesz obwód") are physical/mechanical — safe. Warning: "pasuje na każdą głowę" (universality) softened to "dopasowuje się do obwodu głowy" per Option B.

### Customer validation
- **Date:** 2026-03-14 to 2026-03-16
- **Runs:** 3 (final)

**Run 1 scores (full evaluation):**

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | 7/10 | 7/10 | 6/10 | 8/10 | 7.0/10 |
| Purchase intent | 6/10 | 5/10 | 4/10 | 7/10 | 5.5/10 |
| Premium feel | 8/10 | 4/10 | 7/10 | 7.5/10 | 6.6/10 |

**Run 2 scores (after benefit 3 replacement: generic absorption → style preservation):**

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | 7/10 | 7/10 | 6/10 | 8.5/10 | 7.1/10 |
| Purchase intent | 6.5/10 | 6/10 | 5/10 | 7.5/10 | 6.25/10 |
| Premium feel | 8/10 | 5/10 | 7/10 | 8/10 | 7.0/10 |

**Run 3 scores (after adjustability correction: fixed elastic → adjustable):**

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | 7/10 | 7/10 | 5.5/10 | 8/10 | 6.9/10 |
| Purchase intent | 6/10 | 5/10 | 4/10 | 7/10 | 5.5/10 |
| Premium feel | 8/10 | 5/10 | 6/10 | 8/10 | 6.75/10 |

- **Run 3 analysis:** Scores essentially flat vs Run 2. Adjustability info was factually necessary (correcting an error about the product) but didn't move scores because all limiting factors are site-level. Zuzia noticed adjustability but wanted specific circumference range. Maja flagged elastic info repetition across 5 locations.
- **Strongest elements across all 3 runs (LOCKED):** Headline (4/4 all runs), benefit 2/silk-covered elastic (4/4 → now with adjustability), card 1/elastic explanation, SEO title
- **Core tension (consistent):** Ewa (gift buyer) finds copy too technical; Kasia/Zuzia/Maja value concrete specs. Gift positioning is a site-level issue (needs packaging photos, bundle suggestions), not a copy issue.
- **Site-level improvements flagged by personas (4/4 consensus across all runs):** reviews/social proof (4/4 critical), product photos incl. lifestyle + packaging shots (4/4 critical), return policy / 60-day guarantee visibility (3/4), comparison table vs cheaper alternatives (2/4), elastic circumference range for size/fit (Zuzia), care/durability info ("ile prań wytrzyma?" — Kasia, Maja)
- **Final decision:** Copy finalized with adjustability correction (Run 3). The adjustability update was a factual fix, not a creative optimization — the product genuinely has adjustable sizing. Scores remain capped by site-level factors. Further copy refinement cannot improve scores; only reviews, photos, return policy, and comparison content will move the needle.

## Media

| Type | Status |
|------|--------|
| Product photos | **PENDING** (critical - 4/4 personas flagged) |
| Lifestyle photos | **PENDING** |
| Packaging/unboxing photos | **PENDING** (critical for gift buyers per Ewa) |
| Detail photo: silk-covered elastic | **PENDING** (critical - Kasia: "jedno zdjęcie makro jest warte więcej niż trzy akapity") |
| Video | **PENDING** |

## Collections

Not assigned yet - to set up when collections are created.

## Remaining action items

1. **Variant colors** - finalize colors, add SKUs and Color category metafield
2. **Cost per item** - fill when import cost is calculated
3. **Product weight** - measure when physical sample arrives
4. **HS code verification** - verify 6505 00 90 on TARIC before first import
5. **Media** - upload product photos when available; include:
   - Packaging/unboxing shots (critical per Ewa's feedback)
   - Detail photo of silk-covered elastic (critical per Kasia's feedback - "pokaż mi to, o czym piszesz")
   - Product on model/hair context (Kasia: "chcę widzieć, czy nie wyglądam jak babcia w czepku")
   - Close-up texture shots
6. **Reviews system** - enable product reviews before launch (critical - 3/4 personas flagged this)
7. **Return policy** - ensure 60-day guarantee is visible on PDP (Kasia, Zuzia flagged absence)
8. **Comparison section** - add comparison table vs cheaper alternatives (Kasia, Zuzia requested)
9. **Bundle suggestion** - set up bonnet + pillowcase bundle (Ewa: "sam czepek to trochę mało na prezent")
10. **Size/fit info** - add elastic adjustment range in cm to specs (Zuzia Run 3: "'regulowany' to za mało — jakie dokładne wymiary? Jaki zakres regulacji?"). Measure when physical product arrives.
11. **OEKO-TEX certificate number** - add to specs when documentation is ready
12. **Collections** - assign when collections are created
