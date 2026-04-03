# Nocna Rutyna (Night Routine Bundle)

*Last updated: 2026-03-28*

## Basic info

| Field | Value | Status |
|-------|-------|--------|
| Title | Nocna Rutyna | Done |
| Description | (empty - PDP uses metafields) | Done |
| Category | Bundles | Done |
| Type | Zestaw | Done |
| Vendor | LUSENA | Done |
| Tags | jedwab, zestaw, nocna-rutyna, bundle, poszewka, czepek, bonnet, 22-momme | Done |
| Theme template | product.bundle | Done |
| Status | Draft | Done |

## Bundle contents

| Product | Individual price | Colors available |
|---------|-----------------|------------------|
| Poszewka jedwabna 50x60 | 269 zł | Czarny, Brudny róż, Szampan |
| Jedwabny czepek do spania (bonnet) | 239 zł | Czarny, Brudny róż |

## Pricing

| Field | Value | Status |
|-------|-------|--------|
| Price | 399 zł (VAT inclusive) | Done |
| `lusena.bundle_original_price` | 508 | Done |
| `lusena.bundle_nudge_map` | `{"poszewka-jedwabna":{"label":"czepek jedwabny","handle":"czepek-jedwabny"},"czepek-jedwabny":{"label":"poszewkę jedwabną","handle":"poszewka-jedwabna"}}` | Done |
| Savings | 109 zł (21.5%) | Done |
| Charge tax | Yes (23% VAT, tax-inclusive) | Done |
| `lusena.upsell_role` | bundle | Done |
| `lusena.upsell_message` | Kompletna ochrona na noc - twarz i włosy | Done |
| `lusena.upsell_primary` | (set manually) | Done |
| Free shipping | Yes (399 > 275 zł threshold) | Done |
| Psychological threshold | Under 400 zł | Done |

## Variants / Colors

Customer picks color independently for each product in the set:
- Poszewka: Czarny / Brudny róż / Szampan (3 options)
- Bonnet: Czarny / Brudny róż (2 options)

Colors can be matched or mixed. Bundle strategy recommends matching (A+A, B+B).

## Inventory

| Field | Value | Status |
|-------|-------|--------|
| Inventory tracked | Yes (via Simple Bundles component sync) | Done |
| Max sets before stock pressure | ~20 (draws from 120 poszewki + 60 bonnety) | Done |

## Shipping

| Field | Value | Status |
|-------|-------|--------|
| Physical product | Yes | Done |
| Free shipping | Yes (399 > 275 zł threshold) | Done |

## SEO

| Field | Value | Status |
|-------|-------|--------|
| Page title | Nocna Rutyna - jedwabna poszewka i czepek w zestawie · LUSENA | Done |
| Meta description | Jedwabna poszewka 50x60 + czepek do spania w jednym zestawie. Oszczędzasz 109 zł. Jedwab dla skóry i włosów - na całą noc. 22 momme, OEKO-TEX®. | Done |
| URL handle | nocna-rutyna | Done |

## Feature card strategy

**Approved 2026-03-21.** First bundle processed - establishes the pattern for all 3 bundles.

**UNIVERSAL bundle cards (positions 2, 4, 6 - locked, same across all bundles):**

| Pos | Icon | Title | Description |
|-----|------|-------|-------------|
| 2 | `layers` | Dlaczego 22 momme? | Momme to gęstość jedwabiu - im wyższe, tym grubszy i trwalszy materiał. Standard rynkowy to 16-19 momme. Nasze 22 momme to gęstszy splot, który lepiej trzyma kształt i dłużej służy. |
| 4 | `shield-check` | Jedwab, nie satyna z poliestru | Satyna to nazwa splotu, nie materiału - najczęściej kryje się za nią poliester. LUSENA to 100% jedwab morwowy: naturalne włókno białkowe, które oddycha i nie elektryzuje. |
| 6 | `gift` | Gotowe do wręczenia | Każdy zestaw LUSENA przychodzi w eleganckim opakowaniu prezentowym - idealny upominek, który robi wrażenie. Bez dodatkowego pakowania. |

> Card 5 was previously universal (OEKO-TEX). Now product-specific - see product-metafields-reference.md.

**PER-BUNDLE cards (positions 1, 3, 5 - unique per bundle):**

| Pos | Angle for Nocna Rutyna | Status |
|-----|----------------------|--------|
| 1 | Complementary mechanisms - how each product protects differently | Done |
| 3 | Nightly ritual - daily use positioning + cumulative benefit | Done |
| 5 | Morning result - what changes when you wake up (bundle-specific gap argument + lifestyle payoff) | Done (2026-03-28) |

## LUSENA metafields

> **UNIVERSAL FIELDS - DO NOT MODIFY.** Fields marked "Pre-filled (universal)" are shared
> across ALL LUSENA bundle products. See feature card strategy above.

### Buybox content

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_emotional_headline` | Twarz bez zagnieceń, włosy bez plątaniny. | Done |
| `lusena.pdp_tagline` | Poszewka chroni skórę, ale włosy nadal mają kontakt z poduszką przez 8 godzin. Czepek zamyka tę lukę - razem masz pełną rutynę na noc. | Done |
| `lusena.pdp_show_price_per_night` | false | Done |

> Price-per-night disabled for bundles. Savings badge and crossed-out price serve the same reframing purpose.

### Benefit bullets

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_benefit_1` | Zasypiasz w jedwabiu - twarz na gładkiej poszewce, włosy pod lekkim czepkiem | Done |
| `lusena.pdp_benefit_2` | Jedwab wchłania znacznie mniej niż bawełna - krem zostaje na skórze, olejek na włosach | Done |
| `lusena.pdp_benefit_3` | Mniej tarcia od pierwszej nocy - i na twarzy, i we włosach | Done |

### Packaging

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_packaging_items` | (N/A for bundles - no packaging accordion on bundle template. "W zestawie" section lists products, card 6 covers gift packaging, FAQ covers packaging details. Photos will handle the rest.) | N/A |

### Care & Badge

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_care_steps` | (empty - theme defaults used, FAQ handles care) | Done |
| `lusena.badge_bestseller` | true | Done |

> Nocna Rutyna is the hero bundle per bundle strategy.

### Feature highlights (6 cards)

| Metafield | Value | Status |
|-----------|-------|--------|
| `lusena.pdp_feature_1_icon` | heart | Done |
| `lusena.pdp_feature_1_title` | Inna ochrona, ten sam jedwab | Done |
| `lusena.pdp_feature_1_description` | Poszewka kładzie gładką powierzchnię pod twarz - mniej tarcia, mniej zagnieceń. Czepek otula włosy ze wszystkich stron - mniej plątania, mniej puszenia. Dwa produkty, jeden materiał, pełna rutyna. | Done |
| `lusena.pdp_feature_2_icon` | layers | Pre-filled (universal) |
| `lusena.pdp_feature_2_title` | Dlaczego 22 momme? | Pre-filled (universal) |
| `lusena.pdp_feature_2_description` | Momme to gęstość jedwabiu - im wyższe, tym grubszy i trwalszy materiał. Standard rynkowy to 16-19 momme. Nasze 22 momme to gęstszy splot, który lepiej trzyma kształt i dłużej służy. | Pre-filled (universal) |
| `lusena.pdp_feature_3_icon` | moon | **UPDATED** (icon consistency: "every night ritual" = overnight; echoes Bonnet C3) |
| `lusena.pdp_feature_3_title` | Rutyna na każdą noc | Done |
| `lusena.pdp_feature_3_description` | Zakładasz poszewkę, naciągasz czepek - gotowe. Przez 8 godzin gładki jedwab ogranicza tarcie na twarzy i we włosach jednocześnie. Im dłużej, tym lepiej widać różnicę. | Done |
| `lusena.pdp_feature_4_icon` | shield-check | Pre-filled (universal) |
| `lusena.pdp_feature_4_title` | Jedwab, nie satyna z poliestru | Pre-filled (universal) |
| `lusena.pdp_feature_4_description` | Satyna to nazwa splotu, nie materiału - najczęściej kryje się za nią poliester. LUSENA to 100% jedwab morwowy: naturalne włókno białkowe, które oddycha i nie elektryzuje. | Pre-filled (universal) |
| `lusena.pdp_feature_5_icon` | sparkles | **UPDATED** (icon consistency: "effortless morning" = radiant result; echoes Poszewka C5) |
| `lusena.pdp_feature_5_title` | Poranek bez porannej rutyny | Done (2026-03-28, 27 chars) |
| `lusena.pdp_feature_5_description` | Sama poszewka nie ochroni włosów. Sam czepek nie ochroni twarzy. Dopiero razem dają Ci poranek, który zaczyna się od kawy, nie od szczotki. | Done (2026-03-28, 142 chars) |
| `lusena.pdp_feature_6_icon` | gift | Pre-filled (universal) |
| `lusena.pdp_feature_6_title` | Gotowe do wręczenia | Pre-filled (universal) |
| `lusena.pdp_feature_6_description` | Każdy zestaw LUSENA przychodzi w eleganckim opakowaniu prezentowym - idealny upominek, który robi wrażenie. Bez dodatkowego pakowania. | Pre-filled (universal) |

### Icon animation specs (for SVG coding agent)

| Card | Icon | Animation spec |
|------|------|---------------|
| 1 | heart | Heart shape with a very slow, gentle scale pulse (1.0→1.02→1.0) over 7 seconds. The heart seems to "breathe" - calm, protective feeling toward both skin and hair. Easing: ease-in-out. Barely perceptible. |
| 2 | layers | 3 stacked horizontal layers. Bottom layer gently shifts down 1px then back, middle stays still, top shifts up 1px then back - a slow "breathing" of the stack over 8 seconds. Reinforces the feeling of density and substance. Easing: ease-in-out. |
| 3 | moon | Crescent moon with a very slow glow pulse (scale 1→1.04→1, opacity 1→0.82→1) over 8 seconds. Calm, protective nighttime feeling. Easing: ease-in-out. Reinforces the every-night ritual. |
| 4 | shield-check | Shield outline with a checkmark inside. Checkmark draws itself once via stroke-dashoffset animation over 1.5s on first viewport entry, then stays static permanently. Reinforces "verified, authentic" feeling. No looping. |
| 5 | sparkles | Three sparkle elements with sequential opacity pulse (0.4→1.0→0.4), staggered by 2.3s, over 7 seconds. Clean, radiant feeling. Easing: ease-in-out. Reinforces the radiant, effortless morning result. |
| 6 | gift | Gift box with ribbon on top. Very subtle "unwrap" motion - lid shifts up 1px then back down over 6 seconds. The ribbon bow has a tiny wiggle (rotate ±1°). Playful but restrained. Reinforces the excitement of receiving a beautifully wrapped gift. |

## Re-evaluation (2026-03-22)

Re-evaluated using orchestrator + Polish e-commerce copywriter flow (introduced during Piękny Sen session). 5 minor phrase-level fixes applied to improve Polish naturalness. No structural changes — all angles, meanings, and the overall copy direction remain identical. Original scores (Trust 8.25, Intent 7.75, Premium 7.5) protected — no customer re-validation needed for wording-only fixes. Legal re-check passed on all changed elements.

| Field | Change | Reason |
|-------|--------|--------|
| Tagline (end) | "razem tworzą kompletną ochronę od wieczora do rana" → "razem masz pełną rutynę na noc" | "Kompletna ochrona" = English calque, sounds like insurance. "Pełna rutyna" echoes bundle name, natural Polish. |
| Benefit 3 (end) | "na twarzy i we włosach jednocześnie" → "i na twarzy, i we włosach" | "Jednocześnie" = technical adverb. Doubled "i...i" is natural Polish emphasis. |
| Card 1 desc (last sentence) | "Dwie metody" → "Dwa produkty" | "Metody" = wrong register for physical products. |
| Card 3 desc (full rewrite) | Old: "Nie jest to produkt na okazje..." → New: "Zakładasz poszewkę, naciągasz czepek - gotowe..." | Old had "noc/nocy" 4x + pharmaceutical register ("użytkowanie sprzyja"). New is sensory, zero "noc" repetition. |
| SEO meta (3rd sentence) | "Kompletna ochrona na noc - twarz i włosy pod jedwabiem" → "Jedwab dla skóry i włosów - na całą noc" | Same "kompletna ochrona" fix + "pod jedwabiem" factually wrong for face (face is ON pillowcase, not under silk). |

## Validation results

### Legal check
- **Date:** 2026-03-22 (final)
- **Verdict:** PASS (0 issues, 2 advisories)
- **Checks:** Initial check (2026-03-21) on buybox copy + SEO. Rework check (2026-03-22) on revised benefits + card 3. Three fixes applied: "nie wchłania" → "wchłania znacznie mniej" (B2), "nie czekasz na rezultaty" → "bez okresu oczekiwania" (B3), "kumulują się" → "sprzyja widocznym efektom" (card 3).
- **Notes:** All claims are physical/mechanical (friction, absorption, creases) or factual (care instructions). No medical claims, no fabricated social proof. Advisory 1: OEKO-TEX® trademark symbol in SEO meta. Advisory 2: verify free shipping threshold (275 zł) configured in Shopify admin before publishing.

### Customer validation
- **Date:** 2026-03-21 to 2026-03-22
- **Runs:** 3 initial + 1 rework (after owner review identified structural issues)

**Run 1-3 summary (2026-03-21):**
Initial runs tested buybox copy with operational benefits (60-day guarantee, 109 zł savings, care/washing). Trust improved 6.0→7.75, intent 5.5→7.125, premium 6.5→7.25. However, owner review identified that benefits 2+3 repeated information already visible in buybox UI elements (guarantee box, savings badge). Card 3 (washing) was FAQ-level, not conversion-worthy.

**Rework run (2026-03-22) — after replacing operational benefits with experiential ones:**

| Criteria | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Average |
|----------|-----------|---------|-----------|---------|---------|
| Trust | 8/10 | 8.5/10 | 8/10 | 8.5/10 | 8.25/10 |
| Purchase intent | 7.5/10 | 9/10 | 7/10 | 7.5/10 | 7.75/10 |
| Premium feel | 7/10 | 7.5/10 | 7/10 | 8.5/10 | 7.5/10 |

- **Strongest elements:** Tagline (4/4 unanimously strongest across ALL runs), headline (4/4), benefit 2/product retention (4/4 in rework — "strzał w dziesiątkę" Ewa, "dosłownie mój problem" Zuzia, "fizyka materiału" Maja), benefit 1/sensory (4/4)
- **Key improvement path:** Runs 1-3 optimized wording. Rework replaced the TYPES of benefits: operational (guarantee, savings, washing) → experiential (sensory, product retention, immediate effect). This structural change produced the biggest score jump.
- **Critical learning:** All 4 personas confirmed that savings (109 zł) and guarantee (60 dni) are FINE in their dedicated buybox UI elements and should NOT be repeated in benefit bullets. Zuzia: "Korzyści powinny mówić o produkcie, nie o cenie." Maja: "Gwarancja to element zaufania przy decyzji zakupowej, nie cecha produktu."
- **One wording fix applied post-rework:** "ochrona mechaniczna" dropped from B3 (4/4 flagged as too technical/clinical). Final B3: "Jedwab ogranicza tarcie od pierwszej nocy - bez okresu oczekiwania."
- **Core tension:** Zuzia's intent (7/10) capped by price sensitivity (399 zł on student budget), not copy quality. Kasia: "trwałość dalej brakuje" (site-level, not copy).
- **Site-level improvements flagged (not copy issues):** product photos (4/4), reviews (4/4), packaging photos (Ewa), Allegro comparison (Kasia, Zuzia), curly hair/CGM info (Zuzia), durability data (Kasia, Zuzia)
- **Final decision:** Copy finalized after rework. All averages above 7.0 (Trust 8.25, Intent 7.75, Premium 7.5). Highest scores of any LUSENA product creative session.

### Card 5 creative session (2026-03-28)

**Scope:** Feature card 5 only (icon + title + description). Previously universal OEKO-TEX card, freed up for product-specific content.

**Angle:** Morning result — what changes when you wake up after both products worked overnight. Distinct from card 1 (mechanism) and card 3 (nightly process).

**Legal check:** PASS (0 issues, 0 advisories). All claims factual/experiential. No absolutes in final version.

**Customer validation (3 runs):**

| Criteria | Run 1 | Run 2 | Run 3 |
|----------|-------|-------|-------|
| Trust | 6.0 | 7.0 | **7.0** |
| Intent | 6.0 | 6.0 | **7.25** |
| Premium | 6.5 | 6.6 | **6.75** |

- **Run 1 → 2 fix:** Description restated headline (4/4 flagged). Rewrote with "Sama poszewka nie... Sam czepek nie... Dopiero razem" structure. Trust jumped +1.0.
- **Run 2 → 3 fix:** "mniejszą listą rzeczy do poprawienia" too abstract (4/4 flagged). Replaced with "bez poprawek przed lustrem - i porankiem, który zaczyna się od kawy, nie od szczotki." Intent jumped +1.25.
- **Unanimously strongest element (4/4 in Run 3):** "Od kawy, nie od szczotki." Kasia: "najlepsza fraza na całej stronie zestawu." Maja: "ekonomia słów godna japandi."
- **Premium gap (6.75 vs 7.0):** Driven by Maja (6/10) preferring higher register. Her own strongest element pick ("od kawy, nie od szczotki") contradicts the concern. No composite needed — v3 is best across all dimensions.
- **Zuzia's intent (6/10) capped by price sensitivity** (399 zł on student budget), consistent with prior sessions.
- **Post-Run-3 owner edit:** Owner flagged "bez poprawek przed lustrem" as unnatural Polish ("poprawek" sounds like document corrections, "gotowa do lustra" also rejected). Restructured to drop the "budzisz się bez X" pattern entirely: "Dopiero razem dają Ci poranek, który zaczyna się od kawy, nie od szczotki." Cleaner, punchier, preserves the unanimously praised closer.
- **Final decision:** Finalized after Run 3 + owner edit. Trust and intent above threshold (7.0, 7.25). Premium 0.25 short — acceptable given single-card scope and structural price ceiling.

## Media

| Type | Status |
|------|--------|
| Product photos | **PENDING** (no physical product yet) |
| Lifestyle photos | **PENDING** |
| Video | **PENDING** |
| Packaging/unboxing photos | **PENDING** (critical for gift buyers per Ewa) |

## Remaining action items

1. **Fill metafields in Shopify admin** - all creative fields finalized, pending owner approval
2. **Update product.bundle.json** - update template feature card blocks with new card 1+3 content, reorder to match positions 1-6
3. **Media** - upload product photos when available; include packaging/unboxing shots (Ewa critical)
4. **Homepage bundles section** - wire up in `templates/index.json`
5. **Reviews system** - enable before launch (4/4 personas flagged)
6. **Free shipping threshold** - configure 275 zł in Shopify admin before publishing (legal advisory)
