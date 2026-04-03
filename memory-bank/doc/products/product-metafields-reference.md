# LUSENA Product Metafields Reference

How each metafield connects to the PDP (Product Detail Page), what it does, and how to write great content for it.

## Creative session process (follow for every product)

### The goal

Every metafield value must maximize the chance of the customer buying the product. The copy should create an emotional experience - the customer must FEEL the benefit of owning this product, FEAR the alternative (cotton, cheap polyester), and TRUST that LUSENA delivers real quality. The PDP is not a spec sheet - it's a conversation that transforms a browser into a buyer while maintaining LUSENA's premium, calm, expert tone. Research the best possible copy, validate it, and never settle for "good enough."

### The process

Creative copy fields (headline, tagline, benefits) must NOT be copy-pasted from other products. Each product deserves original copy crafted through this process.

**Architecture: Orchestrator + Polish Copywriter**

The orchestrator (main Claude instance) NEVER writes customer-facing Polish text directly.
All Polish copy is crafted by a dedicated **Polish e-commerce copywriter agent** — a
specialist in premium beauty/lifestyle brands who writes native-sounding, conversion-optimized
Polish. The orchestrator handles research, rules validation, and routing between specialists.

**Why:** The orchestrator juggles many concerns (exclusion lists, overlap rules, legal,
bundle-specificity) which produces "technically correct but unnatural" Polish. Separating
the text-writing from the rules-checking produces copy that sounds human AND passes all
constraints. Lesson learned during the Piekny Sen session (2026-03-22).

```
1. RESEARCH (orchestrator)
   - Read brandbook: sections 1.3 (audience), 1.7 (proof points), 2.1 (voice rules)
   - Research this product's scientifically-backed benefits (internet search)
   - Research how top competitors position this product type
   - Identify EU/Polish legal constraints for the claims you want to make
   - Read completed product files for reference (copy, scores, lessons learned)

2. BRIEF THE POLISH COPYWRITER (orchestrator → copywriter agent)
   IMPORTANT: Check the "Universal fields" section below FIRST. Cards 2, 4, 6
   and all specs/care are pre-filled and must NOT be modified. Only brief for:
   a. Buybox: emotional headline, tagline, 3 benefits (5 fields)
   b. Feature highlights: cards 1, 3, and 5 - icon + title + description (9 fields)
   c. Icon animation specs: 6 briefs for SVG agent (6 specs)
   d. SEO: page title (max 70 chars), meta description (max 160 chars) (2 fields)

   The brief to the copywriter MUST include:
   - Product info: what it is, price, contents, target customer
   - Competitor research findings (from step 1)
   - Approved copy from other completed products (for tone reference)
   - ALL constraints listed below (info architecture guard, exclusion list, etc.)
   - Character limits per field
   - For bundles: the bundle addendum rules (see below)
   - Instruction: generate 2-3 options per field, recommend the best system

   POLISH COPYWRITER AGENT SPEC:
   "You are a senior Polish e-commerce copywriter specializing in premium beauty
   and lifestyle brands. You write in Polish natively and have a perfect ear for
   natural, elegant Polish phrasing. Your goal: maximize customers' chance of
   buying while providing a premium feeling and emotions.
   Rules: hyphens only (never em dashes), no exclamation marks, sentence case,
   premium calm tone, everyday language (no technical/clinical terms).
   For each field: propose 2-3 options, explain what makes each natural or
   awkward in Polish, recommend the best combination as a system."

3. RULES CHECK (orchestrator)
   After receiving copy from the copywriter, validate against ALL constraints:

   INFORMATION ARCHITECTURE GUARD (mandatory):
   The PDP has multiple content layers. The buybox (headline, tagline, benefits)
   is the FIRST layer the customer reads. Below the fold, the customer sees:
   - 6 feature cards (cards 2/4/6 are universal - see below)
   - Specs accordion (material, 22 momme, Grade 6A, OEKO-TEX, dimensions)
   - Quality evidence section ("Dlaczego LUSENA?")
   - Truth table ("Jedwab vs satyna")
   - FAQ

   DO NOT repeat below-fold content in the buybox. The buybox must focus on
   EXPERIENTIAL benefits the customer FEELS (waking up without creases, hair
   without tangles, skin that looks different). The below-fold sections handle
   MATERIAL proof (what the silk is, why it's certified, how it compares).

   BUYBOX-LEVEL EXCLUSION (applies to ALL products, not just bundles):
   The buybox itself contains visible elements NEXT TO the benefit bullets:
   - Guarantee box ("60 dni gwarancji spokojnego snu" + "Jak to działa?")
   - Delivery row ("1-2 dni robocze" + "60 dni na zwrot")
   - Payment methods row
   - Care accordion (washing instructions)
   - For bundles: savings badge (crossed-out price + "Oszczędzasz X zł")
   Benefits must NOT repeat these — the customer already sees them.
   Use benefit slots for EXPERIENTIAL content only.

   EXCLUSION LIST - these topics MUST NOT appear in headline, tagline, or
   benefit bullets because they are already covered elsewhere on the PDP:
   x "22 momme" / momme density -> feature card 2 + specs accordion
   x "OEKO-TEX" / certification -> quality evidence section + specs accordion
   x Silk vs polyester/satin distinction -> feature card 4 + truth table
   x Gift packaging/box -> feature card 6 + packaging accordion
   x "Grade 6A" / silk grade -> specs accordion
   x "z Suzhou" / origin -> quality evidence section

   TAGLINE <-> BENEFITS - rendering context:
   The tagline renders on DESKTOP as a short product description below the title.
   The 3 benefit bullets render on MOBILE as an alternative to the tagline.
   The customer sees ONE OR THE OTHER, never both at the same time.

   Because they are alternative views for different viewports, similar or even
   identical content between tagline and benefits is EXPECTED and CORRECT.
   The tagline is essentially the benefits reformulated as flowing prose for
   desktop, while the benefits are the same angles as scannable bullet points
   for mobile.

   OVERLAP RULES (what still applies):
   - No two benefits may cover the same angle (benefits must differ from EACH OTHER)
   - Benefits must not repeat below-fold content (exclusion list above still applies)
   - Benefits must not repeat buybox UI elements (buybox-level exclusion above still applies)

   What does NOT count as overlap:
   - Tagline ≈ benefits (they are alternative views, not stacked content)

   SEO note: page title and meta description are the FIRST touchpoint (Google
   search results). Write them to maximize click-through: benefit + key
   differentiator + brand name.

   If any rule fails → send specific feedback back to the copywriter agent
   with the constraint that was violated and ask for a targeted fix.

4. LEGAL CHECK → invoke /lusena-legal-check
   - Verify all claims against approved/forbidden lists
   - Check EU Regulation 655/2013 compliance
   - Check Polish UOKiK consumer protection rules
   - If issues found → send back to copywriter with legal constraints

5. CUSTOMER VALIDATION RUN 1 → invoke /lusena-customer-validation
   - 4 persona agents evaluate the copy independently (in Polish)
   - Aggregate feedback: scores, objections, weak/strong elements
   - Per-element tracking: mark each element as LOCK (praised by 3+) or REFINE (criticized by 2+)
   - If all averages ≥ 7.0 → skip to step 9

6. REFINE (orchestrator → copywriter agent)
   - Do NOT change LOCKED elements (prevents regression)
   - Send REFINE elements back to the Polish copywriter agent with:
     * The specific persona feedback for each REFINE element
     * Which elements are LOCKED (must not change)
     * Legal boundaries from step 4
   - The COPYWRITER rewrites — the orchestrator never self-edits Polish text
   - REALITY CHECK (orchestrator): Persona suggestions optimize for tone, not truth.
     Before accepting copywriter rewrites based on persona feedback, verify they
     match how real customers actually use the product.
   - If refinement introduces NEW claims → quick legal re-check on new claims only

7. CUSTOMER VALIDATION RUN 2 → invoke /lusena-customer-validation (focused)
   - Only re-evaluate changed elements
   - Update per-element tracking (lock/refine)
   - If all averages ≥ 7.0 → skip to step 9
   - If still mixed → one more targeted refinement (step 6 again) + Run 3

7b. CUSTOMER VALIDATION RUN 3 (if needed) → final validation
   - If all averages ≥ 7.0 → finalize
   - If still mixed → composite step (see below)

8. COMPOSITE STEP (only if Run 3 is still mixed)
   - Compare all 3 versions element by element
   - Pick the best-scoring version of each element based on its primary dimension:
     headline → trust+premium, tagline → trust, benefits → intent
   - Assemble composite → send to copywriter for FINAL POLISH PASS
   - The copywriter reviews the assembled composite for natural Polish flow,
     fixes any preposition issues, unnatural collocations, or register mismatches
   - Hard cap: 3 runs + 1 composite. NEVER exceed this.

9. COMPLETE THE PRODUCT FILE
   - Fill all remaining fields: factual specs, packaging, badge, price-per-night
   - Record validation scores in the product file (see Validation section in template)
   - Present to the owner for review using this format:

   REVIEW PRESENTATION (show all of this to the owner):
   a. CREATIVE COPY — all fields produced in this session, clearly labeled
      (show FULL text for every field including card descriptions)
   b. REPETITION CHECK — show creative copy side-by-side with the universal
      cards and below-fold content it must NOT overlap:
      - List each universal card title + first sentence of description
      - Note any potential proximity (even if not a direct repeat)
   c. OVERLAP MATRIX — tagline vs benefit 1/2/3: confirm each covers a
      different angle (one-line summary per field)
   d. VALIDATION SCORES — final scores table + key persona feedback
   e. REPETITION FINDINGS — what personas flagged in question 10
      (if nothing flagged, state "No repetition detected by personas")
   f. LEGAL STATUS — pass/fail + any advisories
   g. For bundles: show which feature cards are universal (locked) vs
      per-bundle (created in this session)
   h. BENEFIT CHECKS — confirm each benefit passes: experiential +
      bundle-specific + everyday language + not repeating buybox UI
```

### Bundle addendum (additional rules for bundle products)

When running the creative session for a **bundle** product, all the rules above apply (including the exclusion list and zero-overlap rule) PLUS these additional constraints:

**Framing: routine/set story, never savings-first**
- Individual products sell "what this silk does for you"
- Bundles sell "why these items TOGETHER create something greater"
- Lead with the combined experience/routine, savings amount shown but always secondary
- NEVER show percentage discounts ("21% taniej") - use absolute zloty: "Oszczędzasz 109 zł"
- NEVER attribute the discount to the flagship (poszewka) - the savings come from buying together

**Tagline must answer "why buy the SET?"**
- NOT "why buy silk?" - that's on the individual product PDPs + universal feature cards
- Focus on: the synergy between items, the convenience of one order, the complete routine
- The component products' individual benefits are already on their own PDPs - don't restate them

**Benefits must be EXPERIENTIAL, never operational:**
- Benefits must answer: "what will my life feel like with this set?"
- Bad: "Jedwab nie gniecie skóry" (individual product benefit - belongs on its PDP)
- Bad: "60 dni na test" (already in guarantee box visible alongside benefits)
- Bad: "Oszczędzasz 109 zł" (already in savings badge visible alongside benefits)
- Bad: "Darmowa dostawa" (already in delivery row visible alongside benefits)
- Good: "Zasypiasz w jedwabiu - twarz na gładkiej poszewce, włosy pod lekkim czepkiem" (sensory, experiential)
- Good: "Jedwab wchłania znacznie mniej niż bawełna - krem zostaje na skórze, olejek na włosach" (product retention, bundle-specific)
- Each benefit should answer: "what do I gain from buying TOGETHER that I wouldn't get buying separately?"

**BUNDLE-SPECIFIC TEST (mandatory — run on each benefit before finalizing):**
For each benefit, ask: "Would this sentence work unchanged on an individual product PDP?"
If yes → it's not bundle-specific. Add the second product's dimension.
- Failed test: "Jedwab ogranicza tarcie od pierwszej nocy" (true for poszewka alone)
- Passed after fix: "Mniej tarcia od pierwszej nocy - na twarzy i we włosach jednocześnie" (requires both products)
Pattern: use the silk property as the MECHANISM, but land on a BUNDLE outcome (both items working).

**BUYBOX UI EXCLUSION (bundle-specific additions):**
The bundle buybox already displays these elements NEXT TO the benefit bullets:
- Savings badge: crossed-out original price + "Oszczędzasz X zł"
- Guarantee box: "60 dni gwarancji spokojnego snu" + "Jak to działa?"
- Delivery row: "1-2 dni robocze" + "60 dni na zwrot"
- Care accordion: washing instructions in FAQ

Benefits MUST NOT repeat any of these. They are visible in the same viewport.
The customer sees them already - repeating in benefits wastes a slot and undermines
premium tone (Nocna Rutyna session: 3/4 personas flagged savings language as
"zniżkowy, nie premium"; 4/4 confirmed guarantee/savings are fine in their UI elements).

**When providing context to validation personas:**
Include a note listing the buybox UI elements visible alongside benefits, so personas
don't over-value operational information (guarantee, savings) that's already displayed.

**Headline angle per bundle** (from `memory-bank/doc/bundle-strategy.md`):
- Nocna Rutyna (399 zł): complete night protection - face + hair in one set
- Piękny Sen (349 zł): sleep beauty - face + eyes, wake up refreshed
- Scrunchie Trio (139 zł): gifting + color variety - 3 colors, 1 set

**Feature cards for bundles:**
- Universal cards 2, 4, 6 still apply (silk quality story is shared)
- Cards 1, 3, and 5: bundle-specific angles (why together > separately, complementary mechanisms, nightly ritual)
- Do not repeat individual product-specific card content from component PDPs
- Cards must be CONVERSION-WORTHY for the price point — FAQ-level details (washing instructions, color selection) are too weak for premium bundles. Ask: "Would this card make someone spend 399 zł?" If not, find a stronger angle.

**Metafields that do NOT apply to bundles:**
- `pdp_packaging_items` — skip. Bundle has no packaging accordion. "W zestawie" lists products, card 6 covers gift packaging, FAQ covers packaging details, gallery photos will provide visual proof. Adding a packaging accordion would repeat "W zestawie" content (50% overlap).
- `pdp_specs_*` — skip. Bundle has no specs accordion. Reason: (1) shared specs (momme, grade, cert) are better covered by universal feature cards 2/4 and quality evidence section which explain WHY they matter, not just state values; (2) product-specific specs (dimensions, closure) differ per component and create a messy split table; (3) bundle buybox is already long (W zestawie + color selector + ATC + guarantee + benefits + care) — adding specs adds friction before ATC; (4) no competitor (Slip, Brooklinen, Spadiora) has spec accordions on bundle pages.
- `pdp_show_price_per_night` — set to `false`. Savings badge serves the same reframing purpose.

**Bundle buybox accordion structure:**
Individual products have 3 accordion panels: Specs → Packaging → Care.
Bundles have 1 accordion panel: Care ONLY.
- Specs: handled by universal feature cards (education > raw values for bundle context)
- Packaging: handled by "W zestawie" + card 6 + FAQ + gallery photos
- Care: KEPT — removes "is silk hard to wash?" objection, not redundant with any other buybox element

**SEO for bundles:**
- Page title: bundle name + key differentiator + LUSENA (max 70 chars)
- Meta description: what's in the set + savings amount + experiential benefit (max 160 chars)

Full bundle strategy, pricing, and economics: `memory-bank/doc/bundle-strategy.md`

## Universal fields (DO NOT MODIFY during creative sessions)

These metafields are **identical across all LUSENA silk products** (pillowcase, scrunchie, bonnet, 3D eye mask). They were validated once and must be copy-pasted as-is. **Do not rewrite, "improve", or customize them** - they are shared defaults, not creative fields.

**Exception:** Heatless curlers use the same 22 momme 6A silk but have a PP cotton filling inside. All 3 universal cards apply. Care steps need custom values due to the filling. See `memory-bank/doc/products/walek-do-lokow.md` for details.

### Universal specs (same for all standard silk products)

| Metafield | Value |
|-----------|-------|
| `lusena.pdp_specs_material` | 100% jedwab morwowy (Mulberry Silk) |
| `lusena.pdp_specs_weave` | Charmeuse (splot satynowy) |
| `lusena.pdp_specs_momme` | 22 momme |
| `lusena.pdp_specs_grade` | 6A (najwyższa) |
| `lusena.pdp_specs_certification` | OEKO-TEX® Standard 100 |
| `lusena.pdp_care_steps` | (leave empty - theme defaults apply) |

### Universal feature cards (positions 2, 4, 6)

| Position | Icon | Title | Description |
|----------|------|-------|-------------|
| **2** | `layers` | Dlaczego 22 momme? | Momme to gęstość jedwabiu - im wyższe, tym grubszy i trwalszy materiał. Standard rynkowy to 16-19 momme. Nasze 22 momme to gęstszy splot, który lepiej trzyma kształt i dłużej służy. |
| **4** | `shield-check` | Jedwab, nie satyna z poliestru | Satyna to nazwa splotu, nie materiału - najczęściej kryje się za nią poliester. LUSENA to 100% jedwab morwowy: naturalne włókno białkowe, które oddycha i nie elektryzuje. |
| **6** | `gift` | Gotowa do wręczenia | *(swap product name per product - see product file)* |

Feature card positions **1**, **3**, and **5** are product-specific and REQUIRE a creative session.

> **Card 5 history:** Was previously the universal OEKO-TEX card ("Certyfikowany OEKO-TEX® 100"). Removed from universal cards (2026-03-28) because the quality evidence section ("Dlaczego LUSENA?") already covers the certificate with a verification link to oeko-tex.com, and the specs accordion also lists the certification. The freed slot is now product-specific - each product gets an extra benefit card tailored to what makes it worth buying.

### What the creative session SHOULD craft (per product)

| Field | Why it's product-specific |
|-------|--------------------------|
| `pdp_emotional_headline` | Different benefit angle per product type |
| `pdp_tagline` | Different problem/solution per product type |
| `pdp_benefit_1-3` | Different purchase motivations per product type |
| `pdp_feature_1_*` | Product-specific primary benefit card |
| `pdp_feature_3_*` | Product-specific secondary benefit card |
| `pdp_feature_5_*` | Product-specific tertiary benefit card (was universal OEKO-TEX, now freed) |
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
| **Where it renders** | Below the product title, above the price. Paragraph text in the buybox. **Desktop only** — on mobile, this is replaced by the 3 benefit bullets. Customer sees one or the other, never both. |
| **Visual style** | Secondary body text, muted color. 2-3 sentences max. |
| **Fallback if blank** | Falls back to theme editor setting (`section.settings.tagline`). If that is also blank, nothing renders. |
| **Source file** | `snippets/lusena-pdp-summary.liquid` (line 52-56) |
| **Conversion role** | **The bridge.** After the emotional headline hooks them, the tagline bridges to WHY this product delivers that benefit. Focus on the experiential difference - what changes when you switch from cotton/polyester to silk. Material specs (22 momme, OEKO-TEX, Grade 6A) are covered by the specs accordion and feature cards below - do not repeat them here. See the exclusion list in step 2. |
| **Copy guidelines** | PAS structure works best: Problem → Agitate → Solve. Lead with the everyday problem (cotton absorbs, creases, tangles), then present the experiential solution (what the customer feels/sees after switching). Max 2-3 sentences. The tagline and benefits are **alternative views** (desktop vs mobile) — similar or identical content between them is expected and correct. The tagline reformulates the benefit angles as flowing prose for desktop. |
| **Legal notes** | All claims must be substantiable. Use approved hedging for beauty claims ("sprzyja redukcji", "pomaga zachować"). Physical/mechanical claims (friction, creases, absorption) are safe. Do not reference specs (22 momme, Grade 6A, OEKO-TEX) in the tagline - those are covered elsewhere on the page. |
| **Good example** | "Zwykła bawełna chłonie wilgoć i gniecie skórę przez 8 godzin snu. Ta poszewka z jedwabiu morwowego zmienia to od pierwszej nocy." (short, experiential, no spec dump - specs are in the accordion and feature cards below) |
| **Bad example** | "Najlepsza poszewka na rynku. Kup teraz!" (no proof, aggressive, superlative without evidence). Also bad: "Jedwab 22 momme, Grade 6A z Suzhou, certyfikat OEKO-TEX" (spec dump - these are covered by feature cards + specs accordion below, see exclusion list). |

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
| **Where it renders** | Three bullet points with dot markers, in the buybox below the payment methods row and guarantee box. **Mobile alternative to the tagline** — on desktop the tagline shows as prose; on mobile the benefits replace it as scannable bullets. Customer sees one or the other, never both. |
| **Visual style** | List items with teal dots. Short, scannable lines. |
| **Fallback if blank** | Falls back to "benefit" blocks defined in the theme editor. If those are also blank, the entire benefits section is hidden. |
| **Source file** | `sections/lusena-main-product.liquid` (lines 70-160) |
| **Conversion role** | **The final push.** These are the last content elements the customer reads before deciding to click "Add to cart." They must address the TOP 3 purchase motivations. Together they should tell a complete story. |
| **Copy guidelines** | Each bullet = one benefit angle. Use a consistent structure: "[Result] - [mechanism/contrast]" or "[You experience X] - [because Y]". The 3 bullets must cover DIFFERENT angles (no overlap with each other). The tagline and benefits are **alternative views** (desktop vs mobile) — the benefits are the tagline's angles reformulated as scannable bullet points, so similar content between them is expected. Do not reference specs on the exclusion list (22 momme, OEKO-TEX, Grade 6A, etc.) - see step 2. Example trinity for poszewka: skin + product retention + hair. For bundles: synergy + convenience + experience. **Experiential only:** benefits must describe what the customer FEELS or EXPERIENCES, never operational info (guarantee, delivery, washing, savings) that's already visible in the buybox UI — see step 2 BUYBOX-LEVEL EXCLUSION. **Tone:** use everyday language the customer uses. Avoid technical/clinical terms ("ochrona mechaniczna", "regularne użytkowanie sprzyja") — these sound like product spec sheets, not premium copy. |
| **Legal notes** | Same as headline - use "sprzyja redukcji" not "usuwa". Physical/mechanical claims (friction, creases, absorption) are safe. Specific percentages (e.g., "43% less friction") need test documentation. |
| **Good set** | 1: "Budzisz się bez odcisków poduszki - jedwab nie gniecie skóry jak bawełna" / 2: "Wchłania znacznie mniej kremów i serum - pielęgnacja zostaje na skórze, nie na poszewce" / 3: "Włosy bez plątaniny i puszenia - fryzura przetrwa noc bez wysiłku" (3 different angles: skin, product retention, hair - no overlap with each other or with the tagline) |
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
| **Bundles** | **N/A — skip for bundle products.** Bundle template (`lusena-main-bundle`) does not have a packaging accordion. "W zestawie" section lists the products, card 6 covers gift packaging, FAQ covers packaging details. Packaging photos in the gallery will handle the visual proof. |
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

### `lusena.bundle_nudge_map`

- **Type:** `json`
- **Purpose:** Maps trigger product handles to cart upsell data. When a component product is in the cart, this metafield provides the headline label (accusative case), the component product handle (for resolving real title + image via `all_products`), and an optional tile label override.
- **Structure:** Each key is a trigger product handle. Each value is an object with:
  - `label` (required) — accusative case name for the headline "Dodaj {label} i zaoszczedz..."
  - `handle` (required) — Shopify handle of the component product being added. Used to resolve `all_products[handle].title` and `.featured_image` for the upsell tile.
  - `tile_label` (optional) — overrides the tile display name. Used when the product title isn't descriptive enough (e.g., Scrunchie Trio shows "2x Scrunchie jedwabny" instead of the product title).
- **Backward compatibility:** Liquid code uses `nudge_entry.label | default: nudge_entry` — if the value is still a flat string (old format), it falls back gracefully.
- **Where it renders:** `snippets/cart-drawer.liquid` and `sections/lusena-cart-items.liquid` — bundle upsell card headline + "add" tile name + "add" tile image
- **Values:**

| Bundle | JSON value |
|--------|-----------|
| Nocna Rutyna | `{"poszewka-jedwabna":{"label":"czepek jedwabny","handle":"czepek-jedwabny"},"czepek-jedwabny":{"label":"poszewkę jedwabną","handle":"poszewka-jedwabna"}}` |
| Piekny Sen | `{"poszewka-jedwabna":{"label":"maskę 3D","handle":"jedwabna-maska-3d"},"jedwabna-maska-3d":{"label":"poszewkę jedwabną","handle":"poszewka-jedwabna"}}` |
| Scrunchie Trio | `{"scrunchie-jedwabny":{"label":"dwie kolejne jedwabne gumki","handle":"scrunchie-jedwabny","tile_label":"2x Scrunchie jedwabny"}}` |

### Setup in Shopify admin

1. Go to **Settings → Custom data → Products → Add definition**
2. Name: `Bundle nudge map`
3. Namespace and key: `lusena.bundle_nudge_map`
4. Type: **JSON**
5. Save the definition
6. Go to each bundle product → paste the JSON value from the table above (single line, no newlines)

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
