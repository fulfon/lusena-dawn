# Scrunchie Trio (Silk Scrunchie Trio)

*Last updated: 2026-03-28*

## Basic info

| Field | Value | Status |
|-------|-------|--------|
| Title | Scrunchie Trio | Done |
| Description | (empty - PDP uses metafields) | Done |
| Category | Bundles | Done |
| Type | Zestaw | Done |
| Vendor | LUSENA | Done |
| Tags | jedwab, zestaw, scrunchie-trio, bundle, scrunchie, gumka, włosy, 22-momme | Done |
| Theme template | product.bundle | Done |
| Status | Draft | Done |

## Bundle contents

| Product | Individual price | Color in set |
|---------|-----------------|--------------|
| Scrunchie jedwabny (Czarny) | 59 zł | Czarny |
| Scrunchie jedwabny (Brudny róż) | 59 zł | Brudny róż |
| Scrunchie jedwabny (Szampan) | 59 zł | Szampan |

## Pricing

| Field | Value | Status |
|-------|-------|--------|
| Price | 139 zł (VAT inclusive) | Done |
| `lusena.bundle_original_price` | 177 | Done |
| `lusena.bundle_nudge_map` | `{"silk-scrunchie":{"label":"dwie kolejne jedwabne gumki","handle":"silk-scrunchie","tile_label":"2x Scrunchie jedwabny"}}` | Done |
| Savings | 38 zł (21.5%) | Done |
| Charge tax | Yes (23% VAT, tax-inclusive) | Done |
| `lusena.upsell_role` | (none) | Done |
| Free shipping | No (139 < 275 zł threshold) | Done |
| Psychological threshold | Under 140 zł | Done |

## Variants / Colors

**No color choice.** Customer gets one of each color (Czarny + Brudny róż + Szampan). The progressive disclosure selector has no steps - ATC is immediately available.

Unlike Nocna Rutyna and Piękny Sen, there is no color selection UI. The bundle is fixed: one scrunchie per color.

## Inventory

| Field | Value | Status |
|-------|-------|--------|
| Inventory tracked | Yes (via Simple Bundles component sync) | Done |
| Max sets before stock pressure | ~16 trios from 150 units (rest for cross-sell + individual) | Done |

## Shipping

| Field | Value | Status |
|-------|-------|--------|
| Physical product | Yes | Done |
| Free shipping | No (139 < 275 zł threshold - may trigger "dodaj poszewkę" upsell) | Done |

## SEO

| Field | Value | Status |
|-------|-------|--------|
| Page title | Scrunchie Trio - 3 jedwabne gumki w zestawie · LUSENA | Done |
| Meta description | Trzy jedwabne scrunchie w zestawie za 139 zł (zamiast 177 zł). Czarny, Brudny róż, Szampan - 22 momme, OEKO-TEX®. Idealny prezent. | Done |
| URL handle | scrunchie-trio | Done |

## Feature card strategy

**Approved 2026-03-22.** Follows universal pattern (positions 2/4/6 locked).

**UNIVERSAL bundle cards (positions 2, 4, 6 - locked, same across all bundles):**

| Pos | Icon | Title | Description |
|-----|------|-------|-------------|
| 2 | `layers` | Dlaczego 22 momme? | Momme to gęstość jedwabiu - im wyższe, tym grubszy i trwalszy materiał. Standard rynkowy to 16-19 momme. Nasze 22 momme to gęstszy splot, który lepiej trzyma kształt i dłużej służy. |
| 4 | `shield-check` | Jedwab, nie satyna z poliestru | Satyna to nazwa splotu, nie materiału - najczęściej kryje się za nią poliester. LUSENA to 100% jedwab morwowy: naturalne włókno białkowe, które oddycha i nie elektryzuje. |
| 6 | `gift` | Gotowe do wręczenia | Każdy zestaw LUSENA przychodzi w eleganckim opakowaniu prezentowym - idealny upominek, który robi wrażenie. Bez dodatkowego pakowania. |

> Card 5 was previously universal (OEKO-TEX). Now product-specific (2026-03-28): "Po prostu jedwab" — silk as new normal, positive framing of the 1→3 habit shift.

**PER-BUNDLE cards (positions 1, 3, 5 - unique per bundle):**

| Pos | Angle for Scrunchie Trio | Status |
|-----|------------------------|--------|
| 1 | Color variety - capsule palette that works with everything | Done |
| 3 | Always silk at hand - micro-moments where silk is your default | Done |
| 5 | Silk as your new normal - the 1→3 shift from exception to default | Done (2026-03-28) |

**All per-bundle cards across bundles (for reference - must not repeat):**

| Bundle | Card 1 | Card 3 | Card 5 |
|--------|--------|--------|--------|
| Nocna Rutyna | "Inna ochrona, ten sam jedwab" (complementary mechanisms) | "Rutyna na każdą noc" (nightly ritual) | "Poranek bez porannej rutyny" (morning payoff of both items) |
| Piękny Sen | "Od policzka po powieki" (complete facial coverage) | "Ranek po pięknym śnie" (morning payoff) | {pending creative session} |
| Scrunchie Trio | "Kolor pod nastrój" (capsule palette variety) | "Jedwab zawsze pod ręką" (always-available silk) | "Po prostu jedwab" (silk as new normal) |

## LUSENA metafields

> **UNIVERSAL FIELDS - DO NOT MODIFY.** Fields marked "Pre-filled (universal)" are shared
> across ALL LUSENA bundle products. See feature card strategy above.

### Buybox content

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_emotional_headline` | Trzy kolory jedwabiu - jeden na każdy moment. | Done |
| `lusena.pdp_tagline` | Jedna jedwabna gumka to miły akcent. Trzy - i syntetyczna gumka po prostu przestaje mieć sens. | Done |
| `lusena.pdp_show_price_per_night` | false | Done |

> Price-per-night disabled for bundles. Savings badge and crossed-out price serve the same reframing purpose.

### Benefit bullets

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_benefit_1` | Czarna do pracy, różowa na weekend, szampanowa na wyjście - dobierasz do nastroju, nie do tego, co zostało w szufladzie | Done |
| `lusena.pdp_benefit_2` | Jedna w torebce, jedna w łazience, jedna na nadgarstku - nie szukasz, nie pożyczasz, nie sięgasz po syntetyczną | Done |
| `lusena.pdp_benefit_3` | Trzy w rotacji - każda odpoczywa między użyciami, więc jedwab dłużej zachowuje sprężystość i kształt | Done |

### Packaging

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_packaging_items` | (N/A for bundles - no packaging accordion on bundle template. "W zestawie" section lists products, card 6 covers gift packaging, FAQ covers packaging details. Photos will handle the rest.) | N/A |

### Specs

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_specs_*` | (N/A for bundles - no specs accordion on bundle template. Universal feature cards 2/4 and quality evidence section cover material education.) | N/A |

### Care & Badge

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_care_steps` | (empty - theme defaults used, FAQ handles care) | Done |
| `lusena.badge_bestseller` | false | Done |

> Scrunchie Trio is the entry/gift bundle, not the hero (Nocna Rutyna gets bestseller badge).

### Feature highlights (6 cards)

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_feature_1_icon` | palette | **UPDATED** (icon consistency: "color variety" requires dedicated icon, not moisture-retention droplets) |
| `lusena.pdp_feature_1_title` | Kolor pod nastrój | Done |
| `lusena.pdp_feature_1_description` | Czarny, brudny róż i szampan - trzy klasyki, które pasują do siebie i do wszystkiego w szafie. Dobierasz do stroju, do nastroju albo po prostu sięgasz po najbliższą. Każda opcja jest dobra. | Done |
| `lusena.pdp_feature_2_icon` | layers | Pre-filled (universal) |
| `lusena.pdp_feature_2_title` | Dlaczego 22 momme? | Pre-filled (universal) |
| `lusena.pdp_feature_2_description` | Momme to gęstość jedwabiu - im wyższe, tym grubszy i trwalszy materiał. Standard rynkowy to 16-19 momme. Nasze 22 momme to gęstszy splot, który lepiej trzyma kształt i dłużej służy. | Pre-filled (universal) |
| `lusena.pdp_feature_3_icon` | clock | **UPDATED** (icon consistency: "always at hand" = everyday routine, not breathability) |
| `lusena.pdp_feature_3_title` | Jedwab zawsze pod ręką | Done |
| `lusena.pdp_feature_3_description` | Rano w pośpiechu, w trakcie treningu, wieczorem przed snem - moment, w którym sięgasz po gumkę, jest przypadkowy. Kiedy każda pod ręką jest jedwabna, nie musisz o tym myśleć. | Done |
| `lusena.pdp_feature_4_icon` | shield-check | Pre-filled (universal) |
| `lusena.pdp_feature_4_title` | Jedwab, nie satyna z poliestru | Pre-filled (universal) |
| `lusena.pdp_feature_4_description` | Satyna to nazwa splotu, nie materiału - najczęściej kryje się za nią poliester. LUSENA to 100% jedwab morwowy: naturalne włókno białkowe, które oddycha i nie elektryzuje. | Pre-filled (universal) |
| `lusena.pdp_feature_5_icon` | sparkles | Done (2026-03-28) |
| `lusena.pdp_feature_5_title` | Po prostu jedwab | Done (2026-03-28, 16 chars) |
| `lusena.pdp_feature_5_description` | Jedna jedwabna gumka to przyjemny wyjątek. Kiedy masz trzy, nie zastanawiasz się, po którą sięgnąć - każda jest jedwabna. I właśnie tak wyjątek staje się oczywistością. | Done (2026-03-28, 168 chars) |
| `lusena.pdp_feature_6_icon` | gift | Pre-filled (universal) |
| `lusena.pdp_feature_6_title` | Gotowe do wręczenia | Pre-filled (universal) |
| `lusena.pdp_feature_6_description` | Każdy zestaw LUSENA przychodzi w eleganckim opakowaniu prezentowym - idealny upominek, który robi wrażenie. Bez dodatkowego pakowania. | Pre-filled (universal) |

### Icon animation specs (for SVG coding agent)

| Card | Icon | Animation spec |
|------|------|---------------|
| 1 | palette | Three circles (color swatches) in a gentle arc. Each circle pulses opacity in sequence (0.5→1.0→0.5), staggered by 2.3s, over 7 seconds. Three swatches echo three scrunchies. Calm, playful variety. Easing: ease-in-out. |
| 2 | layers | 3 stacked horizontal layers. Bottom layer gently shifts down 1px then back, middle stays still, top shifts up 1px then back - a slow "breathing" of the stack over 8 seconds. Reinforces the feeling of density and substance. Easing: ease-in-out. |
| 3 | clock | Clock face with hour and minute hands. Minute hand performs a gentle tick-tock motion (rotate 60→65deg), hour hand static at 300deg. 7-second cycle. Easing: ease-in-out. Reinforces silk being part of every moment of your day. |
| 4 | shield-check | Shield outline with a checkmark inside. Checkmark draws itself once via stroke-dashoffset animation over 1.5s on first viewport entry, then stays static permanently. Reinforces "verified, authentic" feeling. No looping. |
| 5 | sparkles | Three sparkle elements (main star, small cross, small circle). Each gently pulses opacity in sequence (0.5->1.0->0.5), staggered by 2s, over 8-second cycle. Represents the quiet, gradual transformation from exception to default - not a sudden flash, but a gentle brightening. Three sparkles echo three scrunchies. Easing: ease-in-out. |
| 6 | gift | Gift box with ribbon on top. Very subtle "unwrap" motion - lid shifts up 1px then back down over 6 seconds. The ribbon bow has a tiny wiggle (rotate +/-1 deg). Playful but restrained. Reinforces the excitement of receiving a beautifully wrapped gift. |

## Validation results

### Legal check
- **Date:** 2026-03-22
- **Verdict:** PASS (0 issues, 2 advisories)
- **Notes:** All claims are lifestyle/fashion statements - zero legal exposure. No beauty/skincare claims requiring hedging. No medical claims, no fabricated social proof. Advisory 1: OEKO-TEX® trademark symbol in SEO meta (ensure certificate remains valid). Advisory 2: "zamiast 177 zł" in SEO meta is factual (3x59=177) but must be updated if individual pricing changes. Cleanest legal check of any LUSENA product session.

### Customer validation
- **Date:** 2026-03-22
- **Runs:** 2 (Run 1 full + Run 2 focused on revised tagline S2, B3, Card 1 desc, Card 3 desc)

**Run 1 scores:**

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | 6/10 | 6/10 | 5/10 | 7/10 | 6.0/10 |
| Purchase intent | 5/10 | 5/10 | 4/10 | 6/10 | 5.0/10 |
| Premium feel | 7/10 | 5/10 | 5/10 | 6/10 | 5.75/10 |

**Run 1 findings:** Headline unanimously strong (3/4 praised, Maja: "perfekcyjny"). Tagline S1 strong (Kasia: strongest element). B3 unanimously weakest (4/4: "puste hasło reklamowe"). Critical structural issue: B1 repeated Card 1, B2 repeated Card 3 (4/4 flagged overlap). Missing practical info (durability, sizing) near ATC button.

**Run 2 scores (after replacing tagline S2 + B3 + Card 1/3 descriptions):**

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | 7/10 | 6/10 | 6/10 | 7.5/10 | 6.6/10 |
| Purchase intent | 7/10 | 7/10 | 5.5/10 | 7/10 | 6.6/10 |
| Premium feel | 7/10 | 7/10 | 7/10 | 7.5/10 | 7.1/10 |

- **Strongest elements:** B3/rotation (4/4 unanimously strongest new element - "jedyny moment, gdzie strona mówi coś, czego nie wiedziałam" Maja; "dokladnie ten argument, ktorego szukalam" Kasia), headline (4/4 consistent), tagline S1 (4/4), B2/locations (maintained from Run 1)
- **Key improvement:** Run 1 → Run 2 replaced B3 from empty filler to rotation/durability + differentiated cards from benefits. Intent +1.6, Premium +1.35, Trust +0.6. Structural overlap issue resolved.
- **Remaining blockers (site-level, not copy):** Product photos (4/4), reviews (4/4), packaging visuals for gift buyers (Ewa), durability specifics (Kasia: "ile prań?"), Allegro comparison (Zuzia), product sizing info (Kasia, Maja)
- **Zuzia's intent (5.5):** Capped by price sensitivity (139 zł on student budget, prefers "kup jedną za 59 zł na próbę"). Product-market fit issue, not copy quality. Same pattern as individual scrunchie (intent 6.25) and Piękny Sen (Zuzia intent 6.0).
- **Ewa's trust (6):** Capped by missing social proof and packaging visuals: "strona mówi 'uwierz nam', a nie 'sprawdź sama'." Copy quality is not the blocker.
- **Minor repetition noted (4/4):** "syntetyczna" appears in tagline + B2 + Card 3. All personas noted but none called it critical — different contexts (declaration / logistics / micro-moments). Acceptable thematic thread for the anti-synthetic value proposition.
- **Final decision:** Copy finalized after Run 2. Premium crosses 7.0. Trust and Intent moderated by site-level factors (no photos, no reviews, budget segment) — same pattern as individual scrunchie session. Copy optimized to the limit of what text alone can achieve for this product category and price point.

### Card 5 creative session
- **Date:** 2026-03-28
- **Scope:** Card 5 only (icon, title, description) — freed from universal OEKO-TEX slot
- **Angle:** "Silk as your new normal" — positive framing of the 1→3 habit shift, no anti-synthetic language
- **Legal check:** PASS (0 issues, 0 advisories). Zero product efficacy claims — purely lifestyle/habit observation.

**Card 5 validation — Run 1 (v1: "Koniec z syntetycznymi"):**

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | 5/10 | 5/10 | 4/10 | 4/10 | 4.5/10 |
| Purchase intent | 3/10 | 3/10 | 2/10 | 3/10 | 2.75/10 |
| Premium feel | 4/10 | 3/10 | 5/10 | 4/10 | 4.0/10 |

Run 1 failed: 4/4 flagged anti-synthetic repetition (4th instance on page), aggressive title tone, no new value. "Zwykłe gumki wciąż wygrywają" flagged as manipulative (3/4). Only "staje się oczywistością" praised unanimously.

**Card 5 validation — Run 2 (v2: "Po prostu jedwab"):**

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | 7/10 | 8/10 | 6/10 | 7/10 | 7.0/10 |
| Purchase intent | 5/10 | 7/10 | 3/10 | 7/10 | 5.5/10 |
| Premium feel | 8/10 | 9/10 | 7/10 | 8/10 | 8.0/10 |

- **Key improvements:** Trust +2.5, Intent +2.75, Premium +4.0. Complete rewrite to positive framing resolved all Run 1 issues.
- **Title "Po prostu jedwab":** Unanimously praised (4/4). Ewa: "ma tę nonszalancję, którą mają drogie rzeczy." Maja: "tytuł, który w końcu oddycha."
- **"Wyjątek → oczywistość" arc:** Unanimously strongest (4/4). Maja: "podstępnie skuteczna karta."
- **Intent 5.5:** Structurally capped by Zuzia's price sensitivity (3/10, same pattern as full product intent 5.5) and Kasia wanting sensory hair details (5/10, but adding them would overlap individual scrunchie cards 1/3/5). Ewa + Maja both at 7/10.
- **Post-validation polish:** "Po cichu, bez wysiłku" cut (Kasia: try-hard double closing). "Każda jest jedwabna" kept — only 1/4 personas flagged it (below REFINE threshold of 2+), and owner confirmed it sounds natural.
- **Final decision:** Card 5 finalized. Premium 8.0 exceeds threshold. Trust 7.0 meets threshold. Intent moderated by same structural factors as full product session (no photos, no reviews, price sensitivity). Copy optimized to the limit of what a single reinforcing card can achieve.

## Media

| Type | Status |
|------|--------|
| Product photos | **PENDING** (no physical product yet) |
| Lifestyle photos | **PENDING** |
| Video | **PENDING** |
| Packaging/unboxing photos | **PENDING** |

## Remaining action items

1. **Fill metafields in Shopify admin** - all creative fields finalized, pending owner approval
2. **Media** - upload product photos when available; include packaging/unboxing shots (Ewa critical)
3. **Homepage bundles section** - wire up in `templates/index.json`
4. **Update Simple Bundles option names** - rename to Polish color names
5. **Reviews system** - enable before launch (4/4 personas flagged)
6. **Add `droplets` icon to animated icon system** - new icon needed for Card 1 (not currently in `lusena-icon-animated.liquid`)
