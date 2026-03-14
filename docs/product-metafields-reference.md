# LUSENA Product Metafields Reference

How each metafield connects to the PDP (Product Detail Page), what it does, and how to write great content for it.

## Creative session process (follow for every product)

Creative copy fields (headline, tagline, benefits) must NOT be copy-pasted from other products. Each product deserves original copy crafted through this process:

```
1. RESEARCH
   - Read brandbook: sections 1.3 (audience), 1.7 (proof points), 2.1 (voice rules)
   - Research this product's scientifically-backed benefits (internet search)
   - Research how top competitors position this product type
   - Identify EU/Polish legal constraints for the claims you want to make

2. CRAFT COPY
   - For each creative field: generate 2-3 options
   - Compare pros/cons of each option
   - Pick the best combination (headline + tagline + benefits must work as a SYSTEM)
   - Present options to the owner — let them pick or adjust

3. LEGAL CHECK → invoke /lusena-legal-check
   - Verify all claims against approved/forbidden lists
   - Check EU Regulation 655/2013 compliance
   - Check Polish UOKiK consumer protection rules
   - If issues found → adjust copy, preserving conversion intent

4. CUSTOMER VALIDATION RUN 1 → invoke /lusena-customer-validation
   - 4 persona agents evaluate the copy independently (in Polish)
   - Aggregate feedback: scores, objections, weak/strong elements
   - Identify what needs fixing

5. REFINE
   - Address flagged objections and weak elements
   - Stay within legal boundaries established in step 3
   - If refinement introduces NEW claims → quick legal re-check on new claims only

6. CUSTOMER VALIDATION RUN 2 → invoke /lusena-customer-validation (focused)
   - Only re-evaluate changed elements
   - Confirm fixes worked, no regressions

7. FINALIZE OR ESCALATE
   - If Run 2 is clean → done, enter values into product file
   - If still issues → present to owner for human decision
   - NEVER offer Run 3 — real validation happens with actual customers

8. COMPLETE THE PRODUCT FILE
   - Fill all remaining fields: SEO (page title, meta description), factual specs, packaging, badge, price-per-night
   - For SEO: apply the same benefit-driven approach (page title = product + key differentiator + brand, meta description = benefit + specs in 160 chars)
   - For feature highlights: check if theme defaults are appropriate for this product type. If the product is significantly different from the pillowcase (e.g., heatless curlers), customize the 6 cards.
   - Record validation scores in the product file (see Validation section in template)
   - Present the complete product file to the owner for final review
```

## PDP Visual Layout (top to bottom)

```
┌─────────────────────────────────────────────────────────┐
│  HEADER + BREADCRUMBS                                   │
├─────────────┬───────────────────────────────────────────┤
│             │  [EYEBROW]  ← pdp_emotional_headline      │
│   PRODUCT   │  PRODUCT TITLE  (from Shopify title)      │
│   GALLERY   │  [TAGLINE]  ← pdp_tagline                │
│             │  PRICE  269 zł                            │
│  [BESTSELLER│  [PER-NIGHT]  0,74 zł/noc ← show_price   │
│   BADGE]    │  DELIVERY ROW  (theme settings)           │
│             │  VARIANT PICKER  (color swatches)          │
│  ← badge_   │  ADD TO CART BUTTON                       │
│  bestseller │  PAYMENT METHODS ROW                      │
│             │  GUARANTEE BOX  (theme settings)           │
│             │  ┌─ BENEFIT 1 ← pdp_benefit_1 ──────┐    │
│             │  │  BENEFIT 2 ← pdp_benefit_2        │    │
│             │  │  BENEFIT 3 ← pdp_benefit_3        │    │
│             │  └───────────────────────────────────┘    │
│             │  [ACCORDION: Specs]  ← pdp_specs_*        │
│             │  [ACCORDION: Packaging] ← pdp_packaging   │
│             │  [ACCORDION: Care]  ← pdp_care_steps      │
├─────────────┴───────────────────────────────────────────┤
│  STICKY ADD-TO-CART BAR  (appears on scroll)            │
├─────────────────────────────────────────────────────────┤
│  FEATURE HIGHLIGHTS  "Co zyskujesz"                     │
│  6 cards  ← pdp_feature_N_icon/title/description        │
├─────────────────────────────────────────────────────────┤
│  QUALITY EVIDENCE  "Dlaczego LUSENA?"  (theme settings) │
├─────────────────────────────────────────────────────────┤
│  TRUTH TABLE  "Jedwab vs satyna"  (theme settings)      │
├─────────────────────────────────────────────────────────┤
│  FAQ  (shared section, theme settings)                  │
├─────────────────────────────────────────────────────────┤
│  FINAL CTA  (shared section, theme settings)            │
└─────────────────────────────────────────────────────────┘
```

## Metafield Details

### 1. `lusena.pdp_emotional_headline`

| Property | Value |
|----------|-------|
| **Type** | Single-line text |
| **Where it renders** | Eyebrow text ABOVE the product title, in the buybox (right column) |
| **Visual style** | Small, uppercase-ish caption text. First thing the customer reads after seeing the gallery image. |
| **Fallback if blank** | Falls back to theme editor setting (`section.settings.emotional_headline`). If that is also blank, nothing renders. |
| **Source file** | `snippets/lusena-pdp-summary.liquid` (line 42-46) |
| **Conversion role** | **The hook.** This is the #1 emotional trigger. It must make the customer feel the BENEFIT of owning this product — not describe it. It should hit vanity, aspiration, or fear of the alternative. |
| **Copy guidelines** | One short sentence. Sentence case, no exclamation marks. Benefit-driven, not feature-driven. Must create a vivid mental image (e.g., waking up, looking in the mirror). |
| **Legal notes** | Use approved hedging language for beauty claims: "sprzyja redukcji", "pomaga zachować". Never claim medical effects ("leczy", "usuwa zmarszczki"). Mechanical/physical claims (creases, friction) are safe. |
| **Good example** | "Obudź się bez zagnieceń — od pierwszej nocy." |
| **Bad example** | "Poszewka z jedwabiu 22 momme" (feature, not benefit — boring) |

---

### 2. `lusena.pdp_tagline`

| Property | Value |
|----------|-------|
| **Type** | Multi-line text |
| **Where it renders** | Below the product title, above the price. Paragraph text in the buybox. |
| **Visual style** | Secondary body text, muted color. 2-3 sentences max. |
| **Fallback if blank** | Falls back to theme editor setting (`section.settings.tagline`). If that is also blank, nothing renders. |
| **Source file** | `snippets/lusena-pdp-summary.liquid` (line 52-56) |
| **Conversion role** | **The proof.** After the emotional headline hooks them, the tagline delivers the WHY — key specs, origin, certification. It should combine problem awareness (cotton = bad) with proof (22 momme, Grade 6A, OEKO-TEX). |
| **Copy guidelines** | PAS structure works best: Problem → Agitate → Solve. Lead with the cotton problem, then present your product as the solution with proof points. Keep it scannable — max 2-3 sentences. |
| **Legal notes** | All claims must be substantiable. "22 momme" and "Grade 6A" need supplier documentation. "OEKO-TEX Standard 100" needs the actual certificate. Origin claims ("z Suzhou") need supplier records. |
| **Good example** | "Bawełna chłonie wilgoć i gniecie skórę przez 8 godzin snu. Ta poszewka z jedwabiu morwowego 22 momme, Grade 6A z Suzhou, z certyfikatem OEKO-TEX® Standard 100 — zmienia to od pierwszej nocy." |
| **Bad example** | "Najlepsza poszewka na rynku. Kup teraz!" (no proof, aggressive, superlative without evidence) |

---

### 3. `lusena.pdp_show_price_per_night`

| Property | Value |
|----------|-------|
| **Type** | True or false |
| **Where it renders** | Below the main price, as a small "0,74 zł/noc" value anchor |
| **Visual style** | Caption-size text, muted. Reframes a premium price as a daily micro-investment. |
| **Fallback if blank** | Defaults to `true` (shows per-night price). Only set to `false` for products where per-night doesn't make sense (scrunchies, heatless curlers). |
| **Source file** | `snippets/lusena-pdp-summary.liquid` (line 32-38) |
| **Conversion role** | **Price objection killer.** "269 zł" feels expensive. "0,74 zł/noc" feels like nothing. This reframing is one of the most powerful conversion tools in the buybox. |
| **When to use** | `true` for products used nightly (pillowcase, bonnet, eye mask). `false` for daytime/occasional products (scrunchie, heatless curlers). |

---

### 4-6. `lusena.pdp_benefit_1`, `lusena.pdp_benefit_2`, `lusena.pdp_benefit_3`

| Property | Value |
|----------|-------|
| **Type** | Single-line text (each) |
| **Where it renders** | Three bullet points with dot markers, in the buybox below the payment methods row and guarantee box. Visible on both mobile and desktop. |
| **Visual style** | List items with teal dots. Short, scannable lines. |
| **Fallback if blank** | Falls back to "benefit" blocks defined in the theme editor. If those are also blank, the entire benefits section is hidden. |
| **Source file** | `sections/lusena-main-product.liquid` (lines 70-160) |
| **Conversion role** | **The final push.** These are the last content elements the customer reads before deciding to click "Add to cart." They must address the TOP 3 purchase motivations. Together they should tell a complete story. |
| **Copy guidelines** | Each bullet = one benefit angle. Use a consistent structure: "[Result] — [mechanism/contrast]" or "[You experience X] — [because Y]". The 3 bullets should cover different angles (don't repeat the same point). Recommended trinity: skin + product retention + hair. |
| **Legal notes** | Same as headline — use "sprzyja redukcji" not "usuwa". Physical/mechanical claims (friction, creases, absorption) are safe. Specific percentages (e.g., "43% less friction") need test documentation. |
| **Good set** | 1: "Budzisz się bez odcisków poduszki — jedwab nie gniecie skóry jak bawełna" / 2: "Nie wchłania kremów i serum — pielęgnacja zostaje na skórze, nie na poszewce" / 3: "Budzisz się bez plątaniny i puszenia — fryzura przetrwa noc bez wysiłku" |
| **Bad set** | 1: "Wysokiej jakości jedwab" / 2: "Premium materiał" / 3: "Luksusowy produkt" (all say the same thing — features, no benefits) |

---

### 7-14. Specs table: `lusena.pdp_specs_*`

| Metafield | Renders as | Notes |
|-----------|-----------|-------|
| `lusena.pdp_specs_material` | Row: "Materiał" → value | Always fill for all products |
| `lusena.pdp_specs_weave` | Row: "Splot" → value + expandable "?" definition | Fill for fabric products. Has built-in tooltip explaining charmeuse. |
| `lusena.pdp_specs_momme` | Row: "Gęstość" → value + expandable "?" definition | Fill for fabric products. Has built-in tooltip explaining momme. |
| `lusena.pdp_specs_grade` | Row: "Klasa" → value + expandable "?" definition | Fill for fabric products. Has built-in tooltip explaining Grade 6A. |
| `lusena.pdp_specs_dimensions` | Row: "Wymiary" → value | Always fill |
| `lusena.pdp_specs_closure` | Row: "Zamknięcie" → value | Fill when product has a closure (pillowcase, bonnet) |
| `lusena.pdp_specs_weight` | Row: "Waga" → value | Fill when known |
| `lusena.pdp_specs_certification` | Row: "Certyfikat" → value | Fill for all silk products |

| Property | Value |
|----------|-------|
| **Type** | Single-line text (each) |
| **Where it renders** | Inside the first accordion panel ("Materiały i specyfikacja") in the buybox, below the benefits. Customer clicks to expand. |
| **Visual style** | Two-column table with alternating row backgrounds. Weave, momme, and grade rows have a "?" button that expands an inline definition tooltip. |
| **Fallback if blank** | Each row with a blank value is automatically hidden. No empty rows are ever shown. |
| **Source file** | `snippets/lusena-pdp-buybox-panels.liquid` (lines 62-269) |
| **Conversion role** | **The evidence.** For the detail-oriented buyer ("Seeks quality for years" segment), this is where they verify the product is real, premium, and worth the price. The expandable tooltips educate without overwhelming. |
| **Copy guidelines** | Factual, precise values. No marketing language — this is the spec sheet. Use the international term in parentheses where helpful: "100% jedwab morwowy (Mulberry Silk)". |
| **Legal notes** | All values must match supplier documentation exactly. "22 momme" must be verified by COA. "6A (najwyższa)" must be confirmed per batch. "OEKO-TEX® Standard 100" requires the actual certificate number on file. |

---

### 15. `lusena.pdp_packaging_items`

| Property | Value |
|----------|-------|
| **Type** | List of single-line text |
| **Where it renders** | Inside the second accordion panel ("Co zawiera opakowanie") in the buybox. |
| **Visual style** | Bulleted list with automatic icons: item 1 gets `sparkles`, item 2 gets `gift`, item 3+ gets `file-text`. |
| **Fallback if blank** | Shows default: "Jedwabny produkt LUSENA", "Eleganckie pudełko prezentowe LUSENA", "Karta z instrukcją pielęgnacji". |
| **Source file** | `snippets/lusena-pdp-buybox-panels.liquid` (lines 71-72, 118-121, 303-319) |
| **Conversion role** | **Gift appeal.** For the "Perfect gift" segment, this confirms the product comes beautifully packaged. Seeing "elegant gift box" removes the need to buy separate wrapping. Also signals premium positioning — cheap products don't come in presentation boxes. |
| **Copy guidelines** | Keep the order consistent: product first, box second, extras after. The icon assignment depends on item position. Short, noun-phrase items — no full sentences. |
| **Important:** | Icons are assigned by **position**, not by content. Item 1 always gets `sparkles`, item 2 always gets `gift`, item 3+ always gets `file-text`. Keep the product item first and the box item second. |

---

### 16. `lusena.pdp_care_steps`

| Property | Value |
|----------|-------|
| **Type** | List of single-line text |
| **Where it renders** | Inside the third accordion panel ("Pielęgnacja") in the buybox. |
| **Visual style** | Simple bulleted list (no icons). |
| **Fallback if blank** | Shows 5 default silk care steps: gentle machine wash 30°C, silk detergent, flat dry (no tumble dryer), no bleach, low-temp iron on reverse side. |
| **Source file** | `snippets/lusena-pdp-buybox-panels.liquid` (lines 74-75, 123-126, 352-359) |
| **Conversion role** | **Objection removal.** Many customers worry silk is hard to care for. Seeing "machine washable, gentle cycle" removes that barrier. The defaults work for all silk products — only override if a product has genuinely different care needs. |
| **Copy guidelines** | Short imperative sentences. Start each with a verb. Practical, not promotional. |
| **Recommendation** | Leave blank for all standard silk products — the defaults are well-crafted and consistent. Only fill for non-standard products (e.g., heatless curlers with foam filling might need different care). |

---

### 17. `lusena.badge_bestseller`

| Property | Value |
|----------|-------|
| **Type** | True or false |
| **Where it renders** | Gold badge overlay on the product gallery (top-left corner of the main image). Also checked via product tags (`lusena:bestseller` or `bestseller`). |
| **Visual style** | Small gold/accent badge. Premium feel, not shouty. |
| **Fallback if blank** | No badge shown. Same as `false`. |
| **Source file** | `snippets/lusena-pdp-media.liquid` (lines 19-27) |
| **Conversion role** | **Social proof signal.** "Bestseller" implies other people have bought and validated this product. Powerful for the hesitant buyer. |
| **When to use** | Only for genuinely top-selling products. The brandbook strictly forbids fabricating social proof — don't mark everything as bestseller. For launch, mark the pillowcase as bestseller (flagship product). |

---

### 18-35. Feature highlights: `lusena.pdp_feature_N_icon`, `lusena.pdp_feature_N_title`, `lusena.pdp_feature_N_description` (N=1-6)

| Property | Value |
|----------|-------|
| **Type** | Icon: single-line text. Title: single-line text. Description: multi-line text. |
| **Where it renders** | Full-width section below the buybox, titled "Co zyskujesz". 6 cards in a responsive grid: 1-column mobile (icon-left rows), 2-column tablet, 3-column desktop. |
| **Visual style** | Each card has: teal icon in a white circle → bold title → muted description paragraph. Clean, editorial feel. |
| **Fallback if blank** | Falls back to the block settings configured in the theme editor. The current defaults cover: skin/cream retention, 22 momme density, OEKO-TEX certification, gift packaging, machine washing, hair protection. |
| **Source file** | `sections/lusena-pdp-feature-highlights.liquid` (lines 47-78) |
| **Conversion role** | **Secondary benefits.** The buybox covers the top 3 reasons to buy (benefit bullets). The feature cards expand to 6 deeper angles: temperature regulation, hypoallergenic properties, origin story, durability, care ease, gift readiness. These catch buyers who scroll past the buybox wanting more detail. |
| **Copy guidelines** | Title: short benefit statement (sentence case, no exclamation marks). Description: 1-2 sentences expanding on the title with proof or vivid detail. Each card should cover a DIFFERENT angle — no overlap with each other or with the 3 benefit bullets. |
| **Available icons** | `sparkles`, `wind`, `shield-check`, `gift`, `droplets`, `heart`, `map-pin`, `layers`, `package`, `truck`, `clock`, `file-text` |
| **When to customize** | Leave blank to use theme defaults (good enough for all standard silk products). Fill only when a product has unique features that differ significantly from the pillowcase defaults (e.g., heatless curlers don't need "machine washable silk" card). |

## Metafield priority (what to fill first)

When adding a new product, fill metafields in this order of impact:

| Priority | Metafields | Why |
|----------|-----------|-----|
| **1 (Critical)** | `pdp_emotional_headline`, `pdp_tagline`, `pdp_benefit_1-3` | These are the primary conversion drivers. Every customer sees them. |
| **2 (Important)** | `pdp_specs_material`, `pdp_specs_momme`, `pdp_specs_grade`, `pdp_specs_certification`, `pdp_specs_dimensions` | Builds trust for detail-oriented buyers. Key proof points. |
| **3 (Recommended)** | `pdp_packaging_items`, `badge_bestseller`, `pdp_show_price_per_night` | Gift appeal, social proof, price reframing. |
| **4 (Nice to have)** | `pdp_specs_weave`, `pdp_specs_closure`, `pdp_specs_weight` | Completeness. Blank rows auto-hide, so no harm in skipping. |
| **5 (Optional)** | `pdp_care_steps`, `pdp_feature_N_*` | Theme defaults work well. Only customize for non-standard products. |

## Legal compliance checklist (verify for every product)

- [ ] No medical claims ("leczy", "usuwa zmarszczki", "regeneruje skórę")
- [ ] Beauty claims use hedging language ("sprzyja redukcji", "pomaga zachować", "może ograniczać")
- [ ] Physical/mechanical claims are specific and defensible ("friction", "creases", "absorption")
- [ ] Any percentage claims (e.g., "43% less friction") have test documentation
- [ ] Spec values match supplier COA/documentation
- [ ] OEKO-TEX certificate number is on file
- [ ] Origin claims reference Suzhou/Shengze (never "Made in China")
- [ ] No fabricated social proof (reviews, ratings, customer counts)
- [ ] Sentence case for all headings (no ALL CAPS, no Title Case)
- [ ] No exclamation marks in headings or benefit bullets
