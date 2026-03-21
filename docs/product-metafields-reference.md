# LUSENA Product Metafields Reference

How each metafield connects to the PDP (Product Detail Page), what it does, and how to write great content for it.

## Creative session process (follow for every product)

### The goal

Every metafield value must maximize the chance of the customer buying the product. The copy should create an emotional experience - the customer must FEEL the benefit of owning this product, FEAR the alternative (cotton, cheap polyester), and TRUST that LUSENA delivers real quality. The PDP is not a spec sheet - it's a conversation that transforms a browser into a buyer while maintaining LUSENA's premium, calm, expert tone. Research the best possible copy, validate it, and never settle for "good enough."

### The process

Creative copy fields (headline, tagline, benefits) must NOT be copy-pasted from other products. Each product deserves original copy crafted through this process:

```
1. RESEARCH
   - Read brandbook: sections 1.3 (audience), 1.7 (proof points), 2.1 (voice rules)
   - Research this product's scientifically-backed benefits (internet search)
   - Research how top competitors position this product type
   - Identify EU/Polish legal constraints for the claims you want to make

2. CRAFT COPY (product-specific fields ONLY)
   IMPORTANT: Check the "Universal fields" section below FIRST. Cards 2, 4, 5, 6
   and all specs/care are pre-filled and must NOT be modified. Only craft:
   a. Buybox: emotional headline, tagline, 3 benefits (5 fields)
   b. Feature highlights: cards 1 and 3 ONLY - icon + title + description (6 fields)
   c. Icon animation specs: 6 briefs for SVG agent (6 specs)
   d. SEO: page title (max 70 chars), meta description (max 160 chars) (2 fields)

   For each creative field: generate 2-3 options
   Compare pros/cons of each option
   Pick the best combination - all fields must work as a SYSTEM
   SEO note: page title and meta description are the FIRST touchpoint (Google search results).
   Write them to maximize click-through: benefit + key differentiator + brand name.

3. LEGAL CHECK → invoke /lusena-legal-check
   - Verify all claims against approved/forbidden lists
   - Check EU Regulation 655/2013 compliance
   - Check Polish UOKiK consumer protection rules
   - If issues found → adjust copy, preserving conversion intent

4. CUSTOMER VALIDATION RUN 1 → invoke /lusena-customer-validation
   - 4 persona agents evaluate the copy independently (in Polish)
   - Aggregate feedback: scores, objections, weak/strong elements
   - Per-element tracking: mark each element as LOCK (praised by 3+) or REFINE (criticized by 2+)
   - If all averages ≥ 7.0 → skip to step 8

5. REFINE (lock + refine pattern)
   - Do NOT change LOCKED elements (prevents regression)
   - Only refine elements marked REFINE
   - Stay within legal boundaries established in step 3
   - If refinement introduces NEW claims → quick legal re-check on new claims only
   - REALITY CHECK: Persona suggestions optimize for tone, not truth.
     Before adopting any persona-suggested wording, verify it matches how
     real customers actually use the product (e.g., "pranie po praniu" for
     a scrunchie sounds elegant but women don't wash scrunchies regularly —
     "dzień po dniu" matches the real daily-stretching wear pattern).

6. CUSTOMER VALIDATION RUN 2 → invoke /lusena-customer-validation (focused)
   - Only re-evaluate changed elements
   - Update per-element tracking (lock/refine)
   - If all averages ≥ 7.0 → skip to step 8
   - If still mixed → one more targeted refinement + Run 3

6b. CUSTOMER VALIDATION RUN 3 (if needed) → final validation
   - If all averages ≥ 7.0 → finalize
   - If still mixed → composite step (see below)

7. COMPOSITE STEP (only if Run 3 is still mixed)
   - Compare all 3 versions element by element
   - Pick the best-scoring version of each element based on its primary dimension:
     headline → trust+premium, tagline → trust, benefits → intent
   - Assemble composite, save to product file as the expert recommendation
   - Hard cap: 3 runs + 1 composite. NEVER exceed this.

8. COMPLETE THE PRODUCT FILE
   - Fill all remaining fields: factual specs, packaging, badge, price-per-night
   - Record validation scores in the product file (see Validation section in template)
   - Present the complete product file to the owner for confirmation
```

## Universal fields (DO NOT MODIFY during creative sessions)

These metafields are **identical across all LUSENA silk products** (pillowcase, scrunchie, bonnet, 3D eye mask). They were validated once and must be copy-pasted as-is. **Do not rewrite, "improve", or customize them** - they are shared defaults, not creative fields.

**Exception:** Heatless curlers use the same 22 momme 6A silk but have a PP cotton filling inside. All 4 universal cards apply. Care steps need custom values due to the filling. See `memory-bank/doc/products/heatless-curlers.md` for details.

### Universal specs (same for all standard silk products)

| Metafield | Value |
|-----------|-------|
| `lusena.pdp_specs_material` | 100% jedwab morwowy (Mulberry Silk) |
| `lusena.pdp_specs_weave` | Charmeuse (splot satynowy) |
| `lusena.pdp_specs_momme` | 22 momme |
| `lusena.pdp_specs_grade` | 6A (najwyższa) |
| `lusena.pdp_specs_certification` | OEKO-TEX® Standard 100 |
| `lusena.pdp_care_steps` | (leave empty - theme defaults apply) |

### Universal feature cards (positions 2, 4, 5, 6)

| Position | Icon | Title | Description |
|----------|------|-------|-------------|
| **2** | `layers` | Dlaczego 22 momme? | Momme to gęstość jedwabiu - im wyższe, tym grubszy i trwalszy materiał. Standard rynkowy to 16-19 momme. Nasze 22 momme to gęstszy splot, który lepiej trzyma kształt i dłużej służy. |
| **4** | `shield-check` | Jedwab, nie satyna z poliestru | Satyna to nazwa splotu, nie materiału - najczęściej kryje się za nią poliester. LUSENA to 100% jedwab morwowy: naturalne włókno białkowe, które oddycha i nie elektryzuje. |
| **5** | `sparkles` | Certyfikowany OEKO-TEX® 100 | Niezależny certyfikat potwierdza, że nasz jedwab jest bezpieczny dla skóry i wolny od szkodliwych substancji. Pewność, którą możesz zweryfikować. |
| **6** | `gift` | Gotowa do wręczenia | *(swap product name per product - see product file)* |

Feature card positions **1** and **3** are product-specific and REQUIRE a creative session.

### What the creative session SHOULD craft (per product)

| Field | Why it's product-specific |
|-------|--------------------------|
| `pdp_emotional_headline` | Different benefit angle per product type |
| `pdp_tagline` | Different problem/solution per product type |
| `pdp_benefit_1-3` | Different purchase motivations per product type |
| `pdp_feature_1_*` | Product-specific primary benefit card |
| `pdp_feature_3_*` | Product-specific secondary benefit card |
| SEO (page title, meta description) | Different keywords and benefit hooks per product |

### Punctuation rule: hyphens only, never em dashes

All customer-facing copy uses `-` (hyphen/minus), never `—` (em dash). Em dashes look AI-generated. This applies to all metafield values: titles, descriptions, benefits, taglines.

### Feature card description length rule: 150-210 characters

Feature card descriptions should render to ~4 lines on desktop (target 170-185 chars). Tolerance ±1 line (130-220 chars). Hard cap 220 chars. Within each row of 3 cards, descriptions should differ by at most 1 rendered line for visual consistency.

### Feature card title length rule: max 28 characters

Feature card titles must fit in 1 line at the tightest breakpoint (1024px / 640px viewport = 288px column, 20px font). Max ~28 characters. Reference: "Jedwab, nie satyna z poliestru" (30 chars, 283px rendered) is the absolute maximum — aim for ≤28 to leave room for wide characters (m, w, uppercase).

### Legal rule: no percentage claims for momme

Never use percentage comparisons for momme (e.g., "30% gęstszy", "15% więcej"). These require dedicated test documentation we don't own. Use qualitative language instead: "gęstszy i trwalszy niż typowe 16-19 momme na rynku". The raw numbers (22 vs 16-19) speak for themselves.

---

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
| **Conversion role** | **The hook.** This is the #1 emotional trigger. It must make the customer feel the BENEFIT of owning this product - not describe it. It should hit vanity, aspiration, or fear of the alternative. |
| **Copy guidelines** | One short sentence. Sentence case, no exclamation marks. Benefit-driven, not feature-driven. Must create a vivid mental image (e.g., waking up, looking in the mirror). |
| **Legal notes** | Use approved hedging language for beauty claims: "sprzyja redukcji", "pomaga zachować". Never claim medical effects ("leczy", "usuwa zmarszczki"). Mechanical/physical claims (creases, friction) are safe. |
| **Good example** | "Obudź się bez zagnieceń - od pierwszej nocy." |
| **Bad example** | "Poszewka z jedwabiu 22 momme" (feature, not benefit - boring) |

---

### 2. `lusena.pdp_tagline`

| Property | Value |
|----------|-------|
| **Type** | Multi-line text |
| **Where it renders** | Below the product title, above the price. Paragraph text in the buybox. |
| **Visual style** | Secondary body text, muted color. 2-3 sentences max. |
| **Fallback if blank** | Falls back to theme editor setting (`section.settings.tagline`). If that is also blank, nothing renders. |
| **Source file** | `snippets/lusena-pdp-summary.liquid` (line 52-56) |
| **Conversion role** | **The proof.** After the emotional headline hooks them, the tagline delivers the WHY - key specs, origin, certification. It should combine problem awareness (cotton = bad) with proof (22 momme, Grade 6A, OEKO-TEX). |
| **Copy guidelines** | PAS structure works best: Problem → Agitate → Solve. Lead with the cotton problem, then present your product as the solution with proof points. Keep it scannable - max 2-3 sentences. |
| **Legal notes** | All claims must be substantiable. "22 momme" and "Grade 6A" need supplier documentation. "OEKO-TEX Standard 100" needs the actual certificate. Origin claims ("z Suzhou") need supplier records. |
| **Good example** | "Bawełna chłonie wilgoć i gniecie skórę przez 8 godzin snu. Ta poszewka z jedwabiu morwowego 22 momme, Grade 6A z Suzhou, z certyfikatem OEKO-TEX® Standard 100 - zmienia to od pierwszej nocy." |
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
| **When to use** | `true` for products used nightly (pillowcase, bonnet, 3D mask). `false` for daytime/occasional products (scrunchie, heatless curlers). |

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
| **Copy guidelines** | Each bullet = one benefit angle. Use a consistent structure: "[Result] - [mechanism/contrast]" or "[You experience X] - [because Y]". The 3 bullets should cover different angles (don't repeat the same point). Recommended trinity: skin + product retention + hair. |
| **Legal notes** | Same as headline - use "sprzyja redukcji" not "usuwa". Physical/mechanical claims (friction, creases, absorption) are safe. Specific percentages (e.g., "43% less friction") need test documentation. |
| **Good set** | 1: "Budzisz się bez odcisków poduszki - jedwab nie gniecie skóry jak bawełna" / 2: "Nie wchłania kremów i serum - pielęgnacja zostaje na skórze, nie na poszewce" / 3: "Budzisz się bez plątaniny i puszenia - fryzura przetrwa noc bez wysiłku" |
| **Bad set** | 1: "Wysokiej jakości jedwab" / 2: "Premium materiał" / 3: "Luksusowy produkt" (all say the same thing - features, no benefits) |

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
| **Copy guidelines** | Factual, precise values. No marketing language - this is the spec sheet. Use the international term in parentheses where helpful: "100% jedwab morwowy (Mulberry Silk)". |
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
| **Conversion role** | **Gift appeal.** For the "Perfect gift" segment, this confirms the product comes beautifully packaged. Seeing "elegant gift box" removes the need to buy separate wrapping. Also signals premium positioning - cheap products don't come in presentation boxes. |
| **Copy guidelines** | Keep the order consistent: product first, box second, extras after. The icon assignment depends on item position. Short, noun-phrase items - no full sentences. |
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
| **Conversion role** | **Objection removal.** Many customers worry silk is hard to care for. Seeing "machine washable, gentle cycle" removes that barrier. The defaults work for all silk products - only override if a product has genuinely different care needs. |
| **Copy guidelines** | Short imperative sentences. Start each with a verb. Practical, not promotional. |
| **Recommendation** | Leave blank for all standard silk products - the defaults are well-crafted and consistent. Only fill for non-standard products (e.g., heatless curlers with foam filling might need different care). |

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
| **When to use** | Only for genuinely top-selling products. The brandbook strictly forbids fabricating social proof - don't mark everything as bestseller. For launch, mark the pillowcase as bestseller (flagship product). |

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
| **Copy guidelines** | Title: short benefit statement (sentence case, no exclamation marks). Description: 1-2 sentences expanding on the title with proof or vivid detail. Each card should cover a DIFFERENT angle - no overlap with each other or with the 3 benefit bullets. |
| **Available icons** | `sparkles`, `wind`, `shield-check`, `gift`, `droplets`, `heart`, `map-pin`, `layers`, `package`, `truck`, `clock`, `file-text` |
| **When to customize** | Leave blank to use theme defaults (good enough for all standard silk products). Fill only when a product has unique features that differ significantly from the pillowcase defaults (e.g., heatless curlers don't need "machine washable silk" card). |
| **Icon animation spec** | For each feature card, write an animation brief describing how the icon should subtly animate. This spec is provided to the SVG coding agent who creates the animated icon. Include: what the icon visually represents, what motion it should have, and what emotion it should reinforce. |

**Icon animation constraints (for SVG agent briefs):**
- Each icon has a **unique** animation matching its meaning (never generic pulse/rotate)
- **5-8 second** loop cycle minimum - anything faster feels anxious
- **Barely perceptible** movement - the customer should feel "this is polished" without consciously noticing the animation
- **Stagger start times** across the 6 icons to prevent synchronized blinking
- Must include `prefers-reduced-motion` fallback (static)
- Animation only active inside the feature highlights section - icons elsewhere on the page stay static

**Example animation spec (for SVG agent):**
> Icon: `sparkles` - Feature: "Mniej zmarszczek, więcej blasku"
> Visual: 3 small diamond-shaped stars arranged in a cluster.
> Animation: Stars gently twinkle in sequence (opacity 0.4→1→0.4), one at a time, left to right. 6-second full cycle. Easing: ease-in-out. The effect should feel like a gentle shimmer, not a disco light.

## Bundle-only metafields

These metafields are only used on bundle products (assigned to `product.bundle` template). They are NOT used on individual products.

### `lusena.bundle_original_price`

- **Type:** `number_integer` (price in base currency units, e.g., 508 for 508 zł)
- **Purpose:** The sum of individual product prices before bundle discount. Renders as the crossed-out reference price in the bundle summary. Also used to calculate the "Oszczędzasz X zł" savings badge.
- **Why not `compare_at_price`:** Simple Bundles' Price Sync feature overwrites the variant's `compare_at_price` via API, clearing any value you set. Using a LUSENA metafield puts this data under our control.
- **Where it renders:** `lusena-bundle-summary` snippet — crossed-out price + savings badge
- **Values:**

| Bundle | Value | Calculation |
|--------|-------|-------------|
| Nocna Rutyna | 508 | Poszewka (269) + Bonnet (239) |
| Piękny Sen | 438 | Poszewka (269) + Maska (169) |
| Scrunchie Trio | 177 | 3 × Scrunchie (59) |

### Setup in Shopify admin

1. Go to **Settings → Custom data → Products → Add definition**
2. Name: `Bundle original price`
3. Namespace and key: `lusena.bundle_original_price`
4. Type: **Integer**
5. Save the definition
6. Go to each bundle product → set the value per the table above

---

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
