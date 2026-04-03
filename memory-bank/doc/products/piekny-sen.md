# Piękny Sen (Beauty Sleep Bundle)

*Last updated: 2026-03-22*

## Basic info

| Field | Value | Status |
|-------|-------|--------|
| Title | Piękny Sen | Done |
| Description | (empty - PDP uses metafields) | Done |
| Category | Bundles | Done |
| Type | Zestaw | Done |
| Vendor | LUSENA | Done |
| Tags | jedwab, zestaw, piekny-sen, bundle, poszewka, maska-3d, sen, 22-momme | Done |
| Theme template | product.bundle | Done |
| Status | Draft | Done |

## Bundle contents

| Product | Individual price | Colors available |
|---------|-----------------|------------------|
| Poszewka jedwabna 50x60 | 269 zł | Czarny, Brudny róż, Szampan |
| Jedwabna maska 3D do spania | 169 zł | Czarny |

## Pricing

| Field | Value | Status |
|-------|-------|--------|
| Price | 349 zł (VAT inclusive) | Done |
| `lusena.bundle_original_price` | 438 | Done |
| `lusena.bundle_nudge_map` | `{"poszewka-jedwabna":{"label":"maskę 3D","handle":"jedwabna-maska-3d"},"jedwabna-maska-3d":{"label":"poszewkę jedwabną","handle":"poszewka-jedwabna"}}` | Done |
| Savings | 89 zł (20.3%) | Done |
| Charge tax | Yes (23% VAT, tax-inclusive) | Done |
| `lusena.upsell_role` | bundle | Done |
| `lusena.upsell_message` | Jedwabna ochrona twarzy i oczu | Done |
| `lusena.upsell_primary` | (set manually) | Done |
| Free shipping | Yes (349 > 275 zł threshold) | Done |
| Psychological threshold | Under 350 zł | Done |

## Variants / Colors

Customer picks color for the poszewka. Maska 3D is Czarny only (single color available):
- Poszewka: Czarny / Brudny róż / Szampan (3 options)
- Maska 3D: Czarny (1 option - no choice needed)

Progressive disclosure: Step 1 = poszewka color, Step 2 = maska auto-selected (Czarny only, still requires customer click to confirm).

## Inventory

| Field | Value | Status |
|-------|-------|--------|
| Inventory tracked | Yes (via Simple Bundles component sync) | Done |
| Max sets before stock pressure | ~20 (draws from 120 poszewki + 40 maski) | Done |

## Shipping

| Field | Value | Status |
|-------|-------|--------|
| Physical product | Yes | Done |
| Free shipping | Yes (349 > 275 zł threshold) | Done |

## SEO

| Field | Value | Status |
|-------|-------|--------|
| Page title | Piękny Sen - jedwabna poszewka i maska 3D w zestawie · LUSENA | Done |
| Meta description | Jedwabna poszewka 50x60 + maska 3D do spania w jednym zestawie. Oszczędzasz 89 zł. Mniej tarcia na twarzy, ciemność i spokój dla oczu. OEKO-TEX®. | Done |
| URL handle | piekny-sen | Done |

## Feature card strategy

**Approved 2026-03-22.** Follows pattern established by Nocna Rutyna session.

**UNIVERSAL bundle cards (positions 2, 4, 6 - locked, same across all bundles):**

| Pos | Icon | Title | Description |
|-----|------|-------|-------------|
| 2 | `layers` | Dlaczego 22 momme? | Momme to gęstość jedwabiu - im wyższe, tym grubszy i trwalszy materiał. Standard rynkowy to 16-19 momme. Nasze 22 momme to gęstszy splot, który lepiej trzyma kształt i dłużej służy. |
| 4 | `shield-check` | Jedwab, nie satyna z poliestru | Satyna to nazwa splotu, nie materiału - najczęściej kryje się za nią poliester. LUSENA to 100% jedwab morwowy: naturalne włókno białkowe, które oddycha i nie elektryzuje. |
| 6 | `gift` | Gotowe do wręczenia | Każdy zestaw LUSENA przychodzi w eleganckim opakowaniu prezentowym - idealny upominek, który robi wrażenie. Bez dodatkowego pakowania. |

> Card 5 was previously universal (OEKO-TEX). Now product-specific (2026-03-28): "Nic nowego w Twojej rutynie" - zero-effort material swap angle.

**PER-BUNDLE cards (positions 1, 3, 5 - unique per bundle):**

| Pos | Angle for Piękny Sen | Status |
|-----|---------------------|--------|
| 1 | Complete facial coverage - poszewka covers face skin, mask covers eye area | Done |
| 3 | Morning payoff - the combined result you see in the mirror | Done |
| 5 | Zero-effort material swap - nothing changes in your routine except the material | Done (2026-03-28) |

## LUSENA metafields

> **UNIVERSAL FIELDS - DO NOT MODIFY.** Fields marked "Pre-filled (universal)" are shared
> across ALL LUSENA bundle products. See feature card strategy above.

### Buybox content

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_emotional_headline` | Piękniejszy poranek zaczyna się wieczorem. | Done |
| `lusena.pdp_tagline` | Jedwabna poszewka chroni twarz przed tarciem przez całą noc. Ale okolice oczu potrzebują czegoś innego - ciemności i braku nacisku na powieki. Maska 3D zamyka tę lukę - cała twarz w jedwabiu. | Done |
| `lusena.pdp_show_price_per_night` | false | Done |

> Price-per-night disabled for bundles. Savings badge and crossed-out price serve the same reframing purpose.

### Benefit bullets

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_benefit_1` | Ciemność pod maską i gładkość poszewki - warunki, w których łatwiej odpocząć | Done |
| `lusena.pdp_benefit_2` | Krem i serum pod oczy pracują do rana - jedwab wchłania znacznie mniej niż bawełna | Done |
| `lusena.pdp_benefit_3` | Policzek na gładkim jedwabiu, oczy w pełnym mroku - czujesz różnicę od pierwszej nocy | Done |

### Packaging

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_packaging_items` | (N/A for bundles - no packaging accordion on bundle template. "W zestawie" section lists products, card 6 covers gift packaging, FAQ covers packaging details. Photos will handle the rest.) | N/A |

### Care & Badge

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_care_steps` | (empty - theme defaults used, FAQ handles care) | Done |
| `lusena.badge_bestseller` | false | Done |

> Piękny Sen is not the hero bundle (Nocna Rutyna gets the bestseller badge).

### Feature highlights (6 cards)

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_feature_1_icon` | heart | **UPDATED** (icon consistency: "full face protection" = gentle on body; echoes both component C1s) |
| `lusena.pdp_feature_1_title` | Od policzka po powieki | Done |
| `lusena.pdp_feature_1_description` | Poszewka chroni skórę twarzy przed tarciem - policzki, czoło, brodę. Maska 3D otula okolice oczu bez nacisku na powieki. Razem pokrywają całą twarz - żadna skóra nie zostaje bez ochrony. | Done |
| `lusena.pdp_feature_2_icon` | layers | Pre-filled (universal) |
| `lusena.pdp_feature_2_title` | Dlaczego 22 momme? | Pre-filled (universal) |
| `lusena.pdp_feature_2_description` | Momme to gęstość jedwabiu - im wyższe, tym grubszy i trwalszy materiał. Standard rynkowy to 16-19 momme. Nasze 22 momme to gęstszy splot, który lepiej trzyma kształt i dłużej służy. | Pre-filled (universal) |
| `lusena.pdp_feature_3_icon` | sparkles | **UPDATED** (icon consistency: "beautiful morning" = radiant result; echoes Poszewka C5) |
| `lusena.pdp_feature_3_title` | Ranek po pięknym śnie | Done |
| `lusena.pdp_feature_3_description` | Mniej zagnieceń na policzku, okolice oczu odciążone, twarz otulona jedwabiem przez osiem godzin. Poszewka ogranicza tarcie na skórze, maska daje oczom ciemność i spokój - efekt widać rano w lustrze. | Done |
| `lusena.pdp_feature_4_icon` | shield-check | Pre-filled (universal) |
| `lusena.pdp_feature_4_title` | Jedwab, nie satyna z poliestru | Pre-filled (universal) |
| `lusena.pdp_feature_4_description` | Satyna to nazwa splotu, nie materiału - najczęściej kryje się za nią poliester. LUSENA to 100% jedwab morwowy: naturalne włókno białkowe, które oddycha i nie elektryzuje. | Pre-filled (universal) |
| `lusena.pdp_feature_5_icon` | clock | Done (2026-03-28) |
| `lusena.pdp_feature_5_title` | Nic nowego w Twojej rutynie | Done (2026-03-28, 27 chars) |
| `lusena.pdp_feature_5_description` | Twój wieczór się nie zmienia. Poszewka trafia na tę samą poduszkę. Maskę zakładasz w pięć sekund. Zmienia się jedno - materiał, który dotyka Twojej twarzy przez całą noc. | Done (2026-03-28, 170 chars) |
| `lusena.pdp_feature_6_icon` | gift | Pre-filled (universal) |
| `lusena.pdp_feature_6_title` | Gotowe do wręczenia | Pre-filled (universal) |
| `lusena.pdp_feature_6_description` | Każdy zestaw LUSENA przychodzi w eleganckim opakowaniu prezentowym - idealny upominek, który robi wrażenie. Bez dodatkowego pakowania. | Pre-filled (universal) |

### Icon animation specs (for SVG coding agent)

| Card | Icon | Animation spec |
|------|------|---------------|
| 1 | heart | Heart shape with a very slow, gentle scale pulse (1.0→1.02→1.0) over 7 seconds. The heart seems to "breathe" - calm, protective feeling toward the entire face. Easing: ease-in-out. Barely perceptible. |
| 2 | layers | 3 stacked horizontal layers. Bottom layer gently shifts down 1px then back, middle stays still, top shifts up 1px then back - a slow "breathing" of the stack over 8 seconds. Reinforces the feeling of density and substance. Easing: ease-in-out. |
| 3 | sparkles | Three sparkle elements with sequential opacity pulse (0.4→1.0→0.4), staggered by 2.3s, over 7 seconds. Clean, radiant feeling. Easing: ease-in-out. Reinforces the beautiful, radiant morning result. |
| 4 | shield-check | Shield outline with a checkmark inside. Checkmark draws itself once via stroke-dashoffset animation over 1.5s on first viewport entry, then stays static permanently. Reinforces "verified, authentic" feeling. No looping. |
| 5 | clock | Clock face with two hands. Minute hand makes a slow, smooth 30-degree sweep over 10 seconds, then pauses 6 seconds before repeating. Hour hand barely shifts (1-2 degrees per cycle). Calm, steady passage of time - nothing rushed, nothing disrupted. Easing: linear for the sweep (steady time flow), smooth ease-in-out for start/stop. Reinforces "your routine stays the same, only the material changes." |
| 6 | gift | Gift box with ribbon on top. Very subtle "unwrap" motion - lid shifts up 1px then back down over 6 seconds. The ribbon bow has a tiny wiggle (rotate +/-1 deg). Playful but restrained. Reinforces the excitement of receiving a beautifully wrapped gift. |

## Validation results

### Legal check
- **Date:** 2026-03-22
- **Verdict:** PASS (0 issues, 3 advisories)
- **Notes:** All claims are physical/mechanical (friction, absorption, light blocking, pressure) or subjective experience. No medical claims, no fabricated social proof. Advisory 1: B2 "pracują do rana" implies skincare efficacy retention (low risk, standard inference from silk absorption). Advisory 2: B3 "czujesz różnicę" + Card 3 "efekt widać rano w lustrze" are subjective perception claims (pre-approved by brandbook §2.1 rule 2 for poszewka category). Advisory 3: Card 1 "żadna skóra nie zostaje bez ochrony" is mild marketing hyperbole (understood in context). OEKO-TEX® trademark symbol in SEO meta. Verify free shipping threshold (275 zł) configured in Shopify admin before publishing.

### Customer validation
- **Date:** 2026-03-22
- **Runs:** 2 (Run 1 full + Run 2 focused on revised B1/B3)

**Run 1 scores:**

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | 7/10 | 7/10 | 7/10 | 7/10 | 7.0/10 |
| Purchase intent | 6/10 | 7/10 | 5.5/10 | 7/10 | 6.4/10 |
| Premium feel | 7/10 | 6/10 | 7/10 | 7.5/10 | 6.9/10 |

**Run 1 findings:** Tagline unanimously strongest element (4/4). B1 and B3 flagged as redundant with tagline and cards (4/4). B3 "lustro pokaże różnicę" criticized as generic/marketing (4/4). B2 (cream/serum retention) praised as only unique benefit (3/4). Structural issue: "cała twarz pod jedwabiem" concept repeated 3-4 times.

**Run 2 scores (after replacing B1 + B3):**

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | 8/10 | 7.5/10 | 7.5/10 | 7.5/10 | 7.6/10 |
| Purchase intent | 7/10 | 7.5/10 | 6/10 | 7.5/10 | 7.0/10 |
| Premium feel | 7/10 | 6.5/10 | 7.5/10 | 8/10 | 7.25/10 |

- **Strongest elements:** Tagline (4/4 unanimously strongest across BOTH runs), B2/product retention (3/4), new B1/"warunki do odpoczynku" (3/4 praised, Maja: "mój ulubiony fragment - brzmi jak Aesop lub Muji"), headline (3/4)
- **Key improvement:** Run 1 → Run 2 replaced B1/B3 from coverage-restating to new angles (sleep conditions + immediate sensory experience). Trust +0.6, Intent +0.6, Premium +0.35. Redundancy issue resolved — all 4 personas confirmed benefits now each add unique value.
- **Remaining blockers (site-level, not copy):** Product photos (4/4), reviews (4/4), packaging visuals for gift buyers (Ewa), durability info (Kasia, Zuzia), Allegro comparison (Zuzia)
- **Zuzia's intent (6/10):** Capped by product-market fit — she's a CGM/hair customer, Piękny Sen targets skin/sleep customers. "Żaden copywriting nie sprawi, że maska 3D stanie się czepkiem na włosy." Would prefer Nocna Rutyna (poszewka + bonnet). This is expected — different customer segment per bundle strategy.
- **Ewa's premium (6.5/10):** Capped by missing packaging visuals: "wrażenie premium przy prezentach buduje się głównie WIZUALNIE." Copy quality is not the blocker.
- **Final decision:** Copy finalized after Run 2. All averages above 7.0 (Trust 7.6, Intent 7.0, Premium 7.25).

### Card 5 creative session (2026-03-28)

**Scope:** Feature card 5 only (icon + title + description). Previously universal OEKO-TEX card, freed up for product-specific content.

**Angle:** Zero-effort material swap - the set doesn't add new habits, it replaces what's already there (cotton with silk, light with darkness). Distinct from card 1 (zone coverage) and card 3 (morning result).

**Legal check:** PASS (0 issues, 0 advisories). All statements factual/verifiable. No efficacy or beauty claims.

**Customer validation (3 runs + composite):**

| Criteria | Run 1 (ritual) | Run 2 (zero-effort) | Run 3 (polished) | Composite |
|----------|---------------|--------------------|--------------------|-----------|
| Trust | 3.75 | **7.75** | 6.75 | 7.75 (v2) |
| Intent | 2.5 | **6.5** | 5.5 | 6.5 (v2) |
| Premium | 5.5 | **6.0** | 5.75 | 6.0 (v2) |

- **Run 1 (ritual angle) FAILED:** "Wieczorny rytuał dla siebie" rejected 4/4 - "rytuał" is a dead word in beauty marketing, poetic tone broke the page's factual trust pattern. All scores below 4.
- **Run 2 (zero-effort angle) BEST:** "Nic nowego w Twojej rutynie" passed trust threshold (7.75). 4/4 confirmed the angle adds genuine value. "Zmienia się jedno - materiał..." praised by 3/4 as strongest element. "Maska zakłada się w pięć sekund" criticized 4/4 as "instruction manual language."
- **Run 3 (polished) REGRESSED:** Replacing "pięć sekund" with "ostatni gest" and title with "Ten sam wieczór, lepszy sen" hurt all scores. The concrete "pięć sekund" grounded the card better than the poetic replacement, despite vocal criticism.
- **Composite decision:** v2 copy verbatim (highest scoring) + clock icon from v3 (Maja's icon/text alignment observation was valid - sparkles contradicted "nothing changes" message, clock matches "same routine").
- **Premium feel ceiling (6.0):** Structural with this angle - "nothing changes" is inherently anti-aspirational. Cards 1 and 3 handle aspiration; card 5's role is barrier removal. 6.0 is acceptable for that role.
- **Kasia's intent (5/10):** Her purchase barrier is "is this real silk?" not "is this complicated?" - card 4 addresses her actual objection. Card 5 targets different personas.
- **Zuzia's intent (7/10 in Run 2):** The zero-effort message resonated - "changes my question from 'can I afford a new habit' to 'can I afford better material'."

## Media

| Type | Status |
|------|--------|
| Product photos | **PENDING** (no physical product yet) |
| Lifestyle photos | **PENDING** |
| Video | **PENDING** |
| Packaging/unboxing photos | **PENDING** (critical for gift buyers per Ewa) |

## Remaining action items

1. **Fill metafields in Shopify admin** - all creative fields finalized, pending owner approval
2. **Media** - upload product photos when available; include packaging/unboxing shots (Ewa critical)
3. **Homepage bundles section** - wire up in `templates/index.json`
4. **Update Simple Bundles option names** - rename to Polish color names
5. **Reviews system** - enable before launch (4/4 personas flagged)
6. **Free shipping threshold** - configure 275 zł in Shopify admin before publishing (legal advisory)
