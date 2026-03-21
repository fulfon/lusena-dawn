# Bundle Implementation Tracker

*Last updated: 2026-03-19*
*Strategy: `memory-bank/doc/bundle-strategy.md`*

## Architecture decision

**App: Simple Bundles & Kits** (by Freshly Commerce) — "Built for Shopify" certified.

**Why Simple Bundles over alternatives:**
- Infinite Options bundle type = zero variant explosion (1 variant per bundle, regardless of color count)
- Documented metafield API (`simple_bundles.bundled_variants`, `simple_bundles.variant_options_v2`) enables fully custom storefront UI
- Real-time inventory sync — deducts from component product variants on purchase
- SKU-level order breakdown for fulfillment
- Free plan: 3 bundles, 50 monthly orders (perfect for Phase 1)
- Scales to 5+ colors per product and 4+ item bundles without hitting Shopify's 3-option limit

**Rejected alternatives and reasons:**
- Native Shopify Bundles (free) — 3-option hard limit blocks 4-item bundles; no swatch UI; variant matrix rebuild when adding colors
- Bundler (free, 1,990 reviews) — no documented inventory sync or SKU breakdown
- Fast Bundle ($19/mo) — revenue-capped pricing ($49/mo at ~10 bundle sales); widget-only, no custom UI path
- BOGOS, Pumper, AOV.ai — discount/upsell tools, not product composition tools (no inventory sync)
- Cart Transform / Shopify Functions — overkill for 3 bundles; requires custom app development

**UI approach: Level 3 (fully custom)**
Build our own `lusena-bundle-options.liquid` that reads Simple Bundles metafields and renders LUSENA-branded color swatches. The app handles only backend (inventory, fulfillment). This gives pixel-perfect consistency with individual product PDPs.

---

## Phase A: Shopify admin setup

### A1. Individual products in Shopify
- [x] All 5 products entered in Shopify admin (2026-03-19)
- [x] Color variants finalized (renamed 2026-03-20):
  - Poszewka: 3 colors — Czarny, Brudny róż, Szampan
  - Bonnet: 2 colors — Czarny, Brudny róż
  - Scrunchie: 3 colors — Czarny, Brudny róż, Szampan
  - Maska 3D: 1 color — Czarny
  - Wałek do loków: 1 color — Brudny róż
- [x] **Rename variants in Shopify admin** to match finalized palette (done 2026-03-20, see `memory-bank/doc/color-strategy.md`)

### A2. Simple Bundles app installed
- [x] App installed on dev store (2026-03-19)
- [x] Bundle assembly method: "Manually build by creating new product options" (Infinite Options)
- [x] Widget placement: "Add manually to product template" (app block)

### A3. Bundle products created in Shopify admin
- [x] **Nocna Rutyna** — 399 zł, compare at 508 zł, Active, "Continue selling when out of stock" enabled
- [x] **Piękny Sen** — 349 zł, compare at 438 zł, Active, "Continue selling when out of stock" enabled
- [x] **Scrunchie Trio** — 139 zł, compare at 177 zł, Active, "Continue selling when out of stock" enabled

### A4. Bundles configured in Simple Bundles (Infinite Options)
- [x] **Nocna Rutyna** — 2 option groups:
  - "Poszewka jedwabna 50×60 - Color": Czarny, Brudny róż, Szampan
  - "Jedwabny czepek do spania - Color": Czarny, Brudny róż
- [x] **Piękny Sen** — 2 option groups:
  - "Poszewka jedwabna 50×60 - Color": Czarny, Brudny róż, Szampan
  - "Jedwabna maska 3D do spania - Color": Czarny
- [x] **Scrunchie Trio** — 3 option groups:
  - "Scrunchie jedwabny - Color" (×3): Czarny, Brudny róż, Szampan

> **Variant rename completed 2026-03-20.** Polish color labels set in both Shopify admin and Simple Bundles option mappings.

### A5. Add-to-cart verified
- [x] Nocna Rutyna — ATC works, appears in cart at 399 zł ✓
- [x] Piękny Sen — ATC works, appears in cart at 349 zł ✓
- [x] Scrunchie Trio — ATC works, appears in cart at 139 zł ✓

**Note:** Default Simple Bundles widget renders plain `<select>` dropdowns with English labels ("Color (Dropdown 1)", "Please select an option"). This is expected — our custom UI (Phase B) will replace these entirely.

---

## Phase B: Custom bundle template (NEXT)

### Architecture decision (2026-03-20)

**Decision: Separate `product.bundle.json` template** instead of conditionals in the shared `product.json`.

**Why separate template (not conditionals):**
1. Bundle and individual product PDPs have different persuasion goals — individual: "is this silk product worth it?"; bundle: "should I buy these together?"
2. Section content independence — bundle FAQ ("Co zawiera zestaw?", "Czy mogę wybrać różne kolory?") vs individual FAQ ("Jak prać jedwab?", "Kiedy zauważę efekty?"). Impossible with one `product.json` without a major metafield refactor.
3. Buy box is ~50% different (5 of 10 snippets replaced), which means heavy conditional branching in every snippet — hard to debug, easy to break.
4. Independent optimization — can reorder/add/remove sections for bundles without affecting individual products.
5. Premium brands (Slip, Brooklinen, Aesop) always use dedicated bundle pages.

**Template section order:**

| # | Section | Source | Purpose |
|---|---------|--------|---------|
| 1 | `lusena-main-bundle` | **NEW section** | Buy box: media + bundle summary + "what's included" + color selectors + ATC + guarantee + payment |
| 2 | `lusena-pdp-feature-highlights` | Reused section, **bundle-specific content** | "Why buy as a set" — routine benefits, matching colors, quality |
| 3 | `lusena-pdp-quality-evidence` | Reused section, **same content** | Brand trust: OEKO-TEX, sourcing, QA, 60-day guarantee |
| 4 | `lusena-pdp-truth-table` | Reused section, **same content** (optional) | Silk vs polyester education for first-time visitors |
| 5 | `lusena-faq` | Reused section, **bundle-specific content** | Bundle objection handling |
| 6 | `lusena-final-cta` | Reused section, **bundle-appropriate copy** | Closing CTA |

**Buy box snippet architecture:**

| Snippet | Status | Notes |
|---------|--------|-------|
| `lusena-pdp-media` | Shared | Bundle products have their own Shopify images — works as-is |
| `lusena-bundle-summary` | **NEW** | Price with crossed-out sum + savings badge + narrative headline. No "price per night" (doesn't apply to bundles). |
| `lusena-pdp-proof-chips` | Shared | "Darmowa dostawa", "OEKO-TEX" — universal trust chips |
| `lusena-bundle-contents` | **NEW** | "What's included" — icon + text list of component products. Upgradeable to thumbnails when photos arrive. |
| `lusena-bundle-options` | **NEW** | Color selectors per component. Reuses same swatch CSS classes (`lusena-option__swatch`, `lusena-option__input`) as individual variant picker — change swatch styling once, both templates update. Polish labels: "Kolor poszewki", "Kolor czepka", etc. Single-option components (maska = only Czarny) show pre-selected, no interaction needed. |
| `lusena-bundle-atc` | **NEW** | Same button design as individual ATC, but form submits `properties[...]` hidden inputs for Simple Bundles backend. |
| `lusena-pdp-guarantee` | Shared | 60-day guarantee — universal |
| `lusena-pdp-payment` | Shared | Secure payment — universal |

**What's NOT in the bundle buy box (vs individual PDP):**
- No "price per night" — doesn't make sense for multi-product sets
- No cross-sell checkbox — the bundle IS the upsell
- No specs/care accordion — replaced by "What's included." Customers who want material specs can click through to individual PDPs.
- No sticky ATC initially — added in Milestone 4 after core template is validated and tested

**Savings display format (agreed 2026-03-20):**
- Crossed-out sum (reference price anchor) + bundle price + absolute savings ("Oszczędzasz 109 zł")
- Savings secondary/subtle — never the headline. Story/routine framing first per bundle strategy.
- Never percentage discounts per bundle strategy research.

**Responsive approach:**
- One architecture, one section order, one HTML structure for both mobile and desktop
- CSS handles layout differences (2-col grid → single column stack, flex-direction changes, spacing adjustments)
- No device-specific sections or section reordering

---

### Execution milestones

Build order follows the natural page development flow: understand data → build visuals → add interactivity → test. Each milestone has a validation gate — don't proceed until the gate passes.

#### Milestone 1: Research (understand the data before writing code)

- [x] Read `simple_bundles.bundled_variants` metafield — empty `[]` for Infinite Options, expected (2026-03-20)
- [x] Read `simple_bundles.variant_options_v2` metafield — null on storefront, not needed (v1 sufficient) (2026-03-20)
- [x] Read `simple_bundles.variant_options` metafield — **this is the working one**, full data for all 3 bundles (2026-03-20)
- [x] Document the JSON structure — see "M1 findings" section below (2026-03-20)
- [x] Document the `properties[...]` and `properties[_bundle_selection]` hidden input format (2026-03-20)
- [x] Backend works without widget — confirmed via docs: Cart Transform runs server-side, reads metafields not widget state (2026-03-20)
- [x] Findings documented below in "M1 findings" section (2026-03-20)

**Gate:** Data structure fully documented. Hidden input format understood. Backend confirmed to work without widget. No code written yet — just knowledge.

**Why first:** Everything in M2-M4 depends on understanding the data shape. If Simple Bundles structures metafields differently than expected, the entire snippet design changes. Research first = no backtracking.

#### M1 findings (2026-03-20)

**Working metafield: `simple_bundles.variant_options`** (owner: PRODUCTVARIANT, type: json)

This is the only metafield we need for the custom UI. It's an array of option group objects:

```json
// Nocna Rutyna (poszewka + bonnet)
[
  {
    "optionName": "Poszewka jedwabna 50×60 - Color (Dropdown 1)",
    "optionValues": "Gray, Gold, Pink",
    "defaultOptionName": "Color"
  },
  {
    "optionName": "Jedwabny czepek do spania - Color (Dropdown 1)",
    "optionValues": "Gold, Gray",
    "defaultOptionName": "Color"
  }
]

// Piękny Sen (poszewka + maska)
[
  {
    "optionName": "Poszewka jedwabna 50×60 - Color (Dropdown 1)",
    "optionValues": "Gray, Gold, Pink",
    "defaultOptionName": "Color"
  },
  {
    "optionName": "Jedwabna maska 3D do spania - Color (Dropdown 1)",
    "optionValues": "Gold",
    "defaultOptionName": "Color"
  }
]

// Scrunchie Trio (3× scrunchie)
[
  {
    "optionName": "Scrunchie jedwabny - Color (Dropdown 1)",
    "optionValues": "Gold, Gray, Clear",
    "defaultOptionName": "Color"
  },
  // same object repeated 3×
]
```

**Liquid access pattern:**
```liquid
{% assign bundle_options = current_variant.metafields.simple_bundles.variant_options.value %}
{% for option in bundle_options %}
  {{ option.optionName }} → {{ option.optionValues }}
{% endfor %}
```

**Key structure notes:**
- `optionName`: `"{Product Title} - {Option Name} (Dropdown {N})"` — parse product title by splitting on ` - Color`
- `optionValues`: comma-space-separated string — split on `", "` in Liquid
- `defaultOptionName`: always `"Color"` for our bundles
- Single-option components (maska = only "Gold"): 1 value in the string, pre-select in UI
- Scrunchie Trio: 3 entries with **identical** `optionName` strings — need index-based keys for properties (see ATC format below)

**Other metafields:**
- `simple_bundles.bundled_variants` (variant-level): empty `[]` for all Infinite Options bundles — expected. Composition is dynamic.
- `simple_bundles.variant_options_v2` (product-level): `null` on storefront — either not populated for Infinite Options or needs GraphQL storefront access mutation. **Not needed** — v1 `variant_options` has everything we need.

**ATC hidden input format** (from documentation research):
```html
<!-- Per-option properties (one per option group): -->
<input type="hidden" name="properties[Poszewka jedwabna 50×60 - Color (Dropdown 1)]" value="Gray">
<input type="hidden" name="properties[Jedwabny czepek do spania - Color (Dropdown 1)]" value="Gold">

<!-- Concatenated bundle selection string: -->
<input type="hidden" name="properties[_bundle_selection]" value="Gray <> Gold">
```

**`_bundle_selection` format:**
- `" ++ "` separates options **within** the same option group (not applicable for our bundles — each group has only 1 option: Color)
- `" <> "` separates **different** option groups
- Example Nocna Rutyna: `"Gray <> Gold"` (poszewka color <> bonnet color)
- Example Scrunchie Trio: `"Gold <> Gray <> Clear"` (scrunchie 1 <> scrunchie 2 <> scrunchie 3)

**Scrunchie Trio duplicate optionName issue:**
All 3 entries have the same `optionName`. For `properties[...]` hidden inputs, duplicate keys would overwrite. Solutions to verify in M3:
1. The app may distinguish by `_bundle_selection` string alone (individual properties are just for cart display)
2. The app may expect indexed keys: `properties[Scrunchie jedwabny - Color (Dropdown 1)]` for first, etc.
3. Need to test by submitting ATC and checking order in Simple Bundles admin

**Backend without widget: CONFIRMED WORKING.**
Simple Bundles operates entirely server-side via Cart Transform (V2) or Order Editing (V1). The widget is only for rendering the frontend UI. Our custom UI submitting the same `properties[...]` format will work identically.

**⚠ ACTION REQUIRED (before M2):**

1. **Simple Bundles option values:** Nocna Rutyna updated to Polish names (Czarny/Brudny róż/Szampan) ✓. Piękny Sen and Scrunchie Trio still have old placeholder names (Gray/Gold/Pink/Clear) — will be updated later. Template renders whatever's in the metafield, so no code dependency on specific names.

2. **`compare_at_price` cleared by Simple Bundles Price Sync** (confirmed 2026-03-20). The app's API call overwrites the variant and doesn't include `compareAtPrice`, resetting it to null. **Solution: use `lusena.bundle_original_price` metafield instead.** See `docs/product-metafields-reference.md` → "Bundle-only metafields" for setup instructions. Values: Nocna Rutyna = 508, Piękny Sen = 438, Scrunchie Trio = 177.

---

#### Milestone 2: Complete visual page (static, no interactivity)

Build the full page top-to-bottom as the customer would scroll it. Everything renders and looks premium. Nothing is clickable yet.

**Template + section shell:**
- [ ] Create `templates/product.bundle.json` — wire all 6 sections in order
- [ ] Create `sections/lusena-main-bundle.liquid` — section shell with schema, shared snippet slots, placeholder slots for new snippets
- [ ] Create section schema with bundle-specific settings (savings label, "what's included" heading, component labels)
- [ ] Assign 3 bundle products to `product.bundle` template in Shopify admin

**New snippets (visual/HTML only, no JS):**
- [ ] `snippets/lusena-bundle-summary.liquid` — headline (metafield), title, tagline (metafield), price row with crossed-out compare-at + savings badge, delivery row
- [ ] `snippets/lusena-bundle-contents.liquid` — "What's included" icon + text list of component products
- [ ] `snippets/lusena-bundle-options.liquid` — render swatch fieldsets with correct Polish labels ("Kolor poszewki", "Kolor czepka") and correct color swatches using shared `lusena-option__swatch` CSS classes. Swatches display correctly but clicking does nothing yet. Single-option components (maska) show pre-selected.
- [ ] ATC button area — render button visually (disabled placeholder). No form, no hidden inputs.
- [ ] Wire shared snippets: media, proof chips, guarantee, payment, benefits (3 metafield-driven bullets)

**Below-fold content (in `product.bundle.json`):**
- [ ] Feature highlights: 6 bundle-specific cards (why buy as set, matching colors, quality, OEKO-TEX, care, gift-ready)
- [ ] Quality evidence: same content as individual (copy section config from `product.json`)
- [ ] Truth table: same content as individual (copy section config)
- [ ] FAQ: bundle-specific questions (Co zawiera zestaw? / Różne kolory? / Zwrot jednego produktu? / Wysyłka / Gwarancja / Dlaczego zestaw?)
- [ ] Final CTA: bundle-appropriate copy

**CSS (all of it):**
- [ ] Add bundle-specific styles to `assets/lusena-pdp.css` (preferred) or create `assets/lusena-bundle.css` if size warrants
- [ ] Savings badge styling (subtle, secondary)
- [ ] "What's included" component styling
- [ ] Multi-fieldset color selector spacing and grouping
- [ ] Responsive: 2-col → 1-col grid, swatch sizing, component list layout
- [ ] Verify: no compiled_assets truncation (check size < 55KB)

**Gate:** Playwright screenshots confirm all 3 bundle URLs look complete and premium on both mobile and desktop. All 6 sections render with real content. Swatches display with correct colors. Page is visually finished — just not interactive.

**Why before interactivity:** Catch all layout/CSS issues on a stable HTML base. Debugging a broken layout is much harder when JS is also running and modifying the DOM. Get the visual right first, then add behavior.

---

#### Milestone 3: Functionality (make it work)

Everything that was static now becomes interactive. Customer can select colors and buy.

- [ ] Swatch interaction JS — clicking a swatch updates selected state, highlights active swatch, updates label text ("Kolor poszewki: Brudny róż")
- [ ] `snippets/lusena-bundle-atc.liquid` — real `<form>` with hidden `properties[...]` inputs in Simple Bundles format. Same button classes as individual ATC.
- [ ] Wire options → ATC: selected swatch values feed into hidden inputs on every change
- [ ] ATC submission works — bundle appears in cart with correct price
- [ ] Cart line items show selected colors ("Kolor poszewki: Brudny róż, Kolor czepka: Czarny")
- [ ] Cart drawer: bundle displays correctly with color selections visible
- [ ] Verify cart page and cart drawer both render correctly

**Gate:** Can select colors on all 3 bundles, add to cart, see correct selections in cart drawer and cart page. Simple Bundles backend processes the order correctly.

**Why after visual:** The visual page from M2 is stable. Now we layer JS and form logic on top of a known-good layout. If something breaks, we know it's the JS — not the HTML or CSS.

---

#### Milestone 4: Full testing + sticky ATC

Production-ready. Every edge case covered, mobile enhancement added.

**Testing:**
- [ ] Full test matrix: 3 bundles × all color combinations × mobile + desktop
- [ ] Edge case: customer tries to ATC without selecting all colors — button stays disabled or shows validation message
- [ ] Edge case: single-option components (Piękny Sen maska = only Czarny) — pre-selected, no interaction needed
- [ ] Inventory deduction: buy bundle → component variant stock decreases correctly
- [ ] Price display: bundle price + crossed-out sum + savings badge renders correctly on all 3 bundles
- [ ] Playwright end-to-end on all 3 bundle URLs: open → select colors → ATC → verify cart

**Sticky ATC (mobile):**
- [ ] Add sticky ATC bar for mobile (buy box scrolls off screen quickly on mobile)
- [ ] Sticky bar shows bundle price
- [ ] Sticky bar disabled until all color selections made
- [ ] Sticky bar ATC submits same hidden inputs as main form

**Gate:** Everything works across all bundles, all combinations, both devices. Ready for Phase C (bundle creative sessions + metafield content).

---

## Phase C: Content & polish

### C1. Bundle creative sessions
- [ ] **Nocna Rutyna** — headline, tagline, 3 benefits
- [ ] **Piękny Sen** — headline, tagline, 3 benefits
- [ ] **Scrunchie Trio** — headline, tagline, 3 benefits

### C2. Bundle metafields
- [ ] Fill LUSENA metafields on bundle products (same PDP template as individual products)
- [ ] Bundle-specific feature highlight cards (1-2 unique + reused universal cards)
- [ ] `lusena.pdp_packaging_items` — what's in the bundle box

### C3. Homepage bundles section
- [ ] Wire up real bundle products in `templates/index.json` bundles section
- [ ] Verify bundle cards display with correct pricing, savings badge, images

### C4. Media
- [ ] Bundle product images (when physical products arrive)
- [ ] Bundle lifestyle photos showing items together

---

## Phase D: Cross-sell checkbox (separate from bundles)

- [ ] Implement PDP checkbox: "Dodaj jedwabną scrunchie - 39 zł zamiast 59 zł"
- [ ] Create Shopify BXGY automatic discount (poszewka = qualifier, scrunchie = 39 zł)
- [ ] Build checkbox UI in `lusena-main-product.liquid` buybox
- [ ] Only show on poszewka PDP (not bonnet — see upsell strategy)

---

## Dev store access

- **Store URL:** https://lusena-dev.myshopify.com/
- **Store password:** paufro
- **Bundle product URLs:**
  - https://lusena-dev.myshopify.com/products/nocna-rutyna
  - https://lusena-dev.myshopify.com/products/piekny-sen
  - https://lusena-dev.myshopify.com/products/scrunchie-trio

---

## Color variant reference (finalized 2026-03-20)

| Product | Variant 1 | Variant 2 | Variant 3 |
|---------|-----------|-----------|-----------|
| Poszewka | Czarny | Brudny róż | Szampan |
| Bonnet | Czarny | Brudny róż | — |
| Scrunchie | Czarny | Brudny róż | Szampan |
| Maska 3D | Czarny | — | — |
| Wałek | Brudny róż | — | — |
