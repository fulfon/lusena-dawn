# LUSENA Bundle Strategy

*Last updated: 2026-03-15*
*Status: Approved - ready for Shopify admin setup*

## Overview

This document defines the complete LUSENA bundle architecture across all business phases. Every decision is backed by academic research on bundling psychology and industry data from premium DTC e-commerce (research conducted 2026-03-15).

**Key references:**
- Individual product data: `memory-bank/doc/products/{handle}.md`
- Product metafield reference: `docs/product-metafields-reference.md`
- Brandbook bundle section (original, partially superseded): `docs/LUSENA_BrandBook_v2.md` § 5.8, 7.6
- Initial order allocation: `docs/LUSENA_BrandBook_v2.md` § 7.2

---

## Research-backed principles

These principles override the original brandbook bundle plan (§ 5.8) where they conflict. The original plan proposed Starter Kit (poszewka + scrunchie), Nocna Rutyna (poszewka + bonnet + scrunchie), and Scrunchie Trio. Research showed structural problems with two of those three.

### 1. Minimum 20% discount to activate bundle preference

**Source:** Harlam, Krishna, Lehmann & Mela (1995), *Journal of Business Research*; Pereira, Galvao de Matos & Martins (2021), *JRFM*.

At 0-15% discount, consumers still prefer individual products. The 20% threshold is where bundle preference activates. Quality perception holds steady up to ~40% discount; drops significantly only above 50-60%.

**LUSENA application:** All bundles are priced at 20-26% discount. The original brandbook proposed 10-19% - too low per the research.

### 2. The Presenter's Paradox - adding cheap items DILUTES perceived value

**Source:** Weaver, Garcia & Schwarz (2012), "The Presenter's Paradox," *Journal of Consumer Research*; Shaddy & Fishbach (2017), *JMR*.

Consumers use **weighted averaging** (not addition) when evaluating bundles. Adding a moderately attractive item to a highly attractive one **reduces** willingness to pay. In one study: luggage valued at $225 alone dropped to $165 when bundled with a cheaper item (27% decrease).

**LUSENA application:** The 59 zł scrunchie was removed from all premium bundles. In the old Nocna Rutyna (269 + 239 + 59), the scrunchie would drag down perceived value via averaging. The revised Nocna Rutyna (269 + 239) keeps both items high-value, with an average of ~200 zł/item instead of ~189 zł/item.

**Exception:** Scrunchie Trio (3× identical items) is immune - the Paradox weakens when items are identical/undifferentiated (Shaddy & Fishbach 2017, Study 4).

### 3. Never discount the flagship product

**Source:** Wei, Yu & Li (2025), *Journal of Travel Research*; Khan & Dhar (2010), *JMR*.

Consumers prefer packages where the premium component is NOT discounted. Discounts on the hedonic (pleasure) item provide "guilt justification" without eroding the flagship's perceived quality.

**LUSENA application:** In all bundle framing, savings are attributed to the secondary product, never to the poszewka. The PDP cross-sell checkbox discounts the scrunchie (59 → 39 zł), not the poszewka.

### 4. Story/routine framing, not savings framing

**Source:** Luxury brand management literature (Louis Vuitton case studies); HBR (Mohammed, 2025); industry consensus from Slip, Brooklinen, Double Stitch.

Premium brands frame bundles as curated routines or sets, never as deals. "Kompletna nocna rutyna" converts better than "Oszczędzasz 78 zł" for premium positioning.

**LUSENA application:** Bundle names and headlines lead with the narrative ("Kompletna ochrona na noc - twarz i włosy"). Savings amounts are shown but always secondary. Never show percentage discounts - use absolute złoty amounts ("Oszczędzasz 109 zł") per research showing absolute > percentage for price points above ~400 zł.

### 5. Mixed bundling mandatory - always offer individual products too

**Source:** Derdenger & Kumar (2013), *Marketing Science* (Nintendo Game Boy study); Stremersch & Tellis (2002), *Journal of Marketing*.

Pure bundling (only bundle available) reduces revenues by 20%+ compared to mixed bundling (both bundle and individual products available). Mixed bundling dominates in virtually all consumer goods contexts.

**LUSENA application:** All products remain available individually at full price alongside bundles. The standalone price serves as a price anchor that makes the bundle discount visible and meaningful.

### 6. Reference price anchoring risk for new brands

**Source:** Sheng, Parker & Nakamoto (2007), *JMTP*; Simonin & Ruth (1995); Raghubir (2004), *JCP*.

Bundle discounts can lower perceived quality and anchor the customer's internal reference price downward. This risk is amplified for new brands that haven't established reference prices yet. Products offered as "free gifts" see reduced willingness to pay in future standalone purchase.

**LUSENA application:** No product is offered as "free" in any bundle (protects reference prices). Cross-sell scrunchie is priced at 39 zł (not free), maintaining a floor. Bundles launch alongside individual products so customers see full prices first.

### 7. Three bundle options is optimal

**Source:** Iyengar & Lepper (2000, the "jam study"); Price Intelligently pricing research; HubSpot pricing tier analysis.

Consumer conversion peaks at 3-4 options. Beyond that, choice paralysis reduces conversion. Structure as Entry / Popular / Premium with the middle option carrying the highest contribution margin.

**LUSENA application:** Phase 1 offers exactly 3 options: Nocna Rutyna (hero), Piękny Sen (mid), Scrunchie Trio (entry/gift). Clear differentiation by customer need (hair person, sleep person, gift person).

---

## Product prices and costs (reference)

| Product | Price (zł) | COGS (~zł) | Gross margin | Initial stock |
|---------|-----------|-----------|-------------|---------------|
| Poszewka jedwabna 50×60 | 269 | ~70 | 74% | 120 (3 colors) |
| Bonnet (czepek jedwabny) | 239 | ~70 | 71% | 60 (2 colors) |
| Jedwabny wałek do loków | 219 | ~51 | 77% | 50 (1 color) |
| Jedwabna maska 3D | 169 | ~41 | 76% | 40 (1 color) |
| Scrunchie jedwabny | 59 | ~12 | 80% | 150 (3 colors) |

COGS estimated at ~4.05 PLN/USD based on brandbook § 7.2 unit costs.

---

## Free shipping threshold: 299 zł

| Scenario | Cart total | Qualifies? | Upsell mechanism |
|----------|-----------|------------|------------------|
| Poszewka alone | 269 zł | No (-30 zł) | "Dodaj scrunchie" → 328 zł ✓ |
| Bonnet alone | 239 zł | No (-60 zł) | "Dodaj scrunchie" → 298 zł (close) |
| Maska alone | 169 zł | No (-130 zł) | Needs second product |
| Curlers alone | 219 zł | No (-80 zł) | "Dodaj scrunchie" → 278 zł (still short) |
| Any bundle | 349-499 zł | Yes ✓ | No upsell needed |
| Poszewka + cross-sell scrunchie | 308 zł | Yes ✓ | Already cleared |

Research: 81% of shoppers increase spending to qualify for free shipping (FedEx/Morning Consult 2024). The 299 zł threshold forces poszewka buyers to add a scrunchie (most natural add-on at 59 zł), while all bundles clear automatically.

---

## Phase 1 - Launch (first 8 weeks)

### Bundle 1: "Nocna Rutyna"

> Kompletna ochrona na noc - twarz i włosy w jednym zestawie

| Field | Value |
|-------|-------|
| **Contents** | Poszewka jedwabna 50×60 + Jedwabny czepek do spania (bonnet) |
| **Separate price** | 269 + 239 = 508 zł |
| **Bundle price** | **399 zł** |
| **Discount** | 109 zł (21.5%) |
| **COGS** | ~140 zł |
| **Gross margin** | 65% (259 zł profit) |
| **vs. poszewka alone** | +60 zł more profit per order (+30%) |
| **Free shipping** | Clears 299 zł ✓ |
| **Psychological threshold** | Under 400 zł ✓ |
| **Color matching** | Same color for both items (A+A, B+B) |
| **Inventory per sale** | 1 poszewka + 1 bonnet |
| **Max before stock pressure** | ~20 sets (draws from 120 poszewki + 60 bonnety) |

**Why it works:**
- Two high-value items (269 + 239) - no Presenter's Paradox dilution (average ~200 zł/item)
- 21.5% discount - above the 20% academic activation threshold
- IS the brand story: face protection (poszewka) + hair protection (bonnet) = "nocna rutyna piękna"
- 399 zł under 400 zł psychological barrier
- Hero bundle - displayed first in bundle section, "Najpopularniejszy" badge

**Framing guidelines:**
- Headline: "Kompletna ochrona na noc - twarz i włosy"
- Sub-headline or badge: "Oszczędzasz 109 zł"
- NEVER: "21% taniej" or savings-first messaging
- NEVER: attribute the discount to the poszewka - the savings come from buying together

---

### Bundle 2: "Piękny Sen"

> Jedwabna ochrona twarzy i oczu - obudź się wypoczęta

| Field | Value |
|-------|-------|
| **Contents** | Poszewka jedwabna 50×60 + Jedwabna maska 3D do spania |
| **Separate price** | 269 + 169 = 438 zł |
| **Bundle price** | **349 zł** |
| **Discount** | 89 zł (20.3%) |
| **COGS** | ~111 zł |
| **Gross margin** | 68% (238 zł profit) |
| **vs. poszewka alone** | +39 zł more profit per order (+20%) |
| **Free shipping** | Clears 299 zł ✓ |
| **Psychological threshold** | Under 350 zł ✓ |
| **Color matching** | Poszewka in customer's chosen color; maska in color A (only 1 color available) |
| **Inventory per sale** | 1 poszewka + 1 maska |
| **Max before stock pressure** | ~20 sets (draws from 120 poszewki + 40 maski) |

**Why it works:**
- Both items substantial (269 + 169) - no dilution
- Different customer than Nocna Rutyna: skin/sleep-focused (older) vs hair-focused (younger)
- Gives the Maska 3D a sales channel (Tier 3 product, "bundle addon" per brandbook - not a standalone hero)
- 349 zł is the most approachable bundle price
- Face + eyes = complete facial protection during sleep

**Framing guidelines:**
- Headline: "Jedwabna ochrona twarzy i oczu - obudź się wypoczęta"
- Sub-headline or badge: "Oszczędzasz 89 zł"
- Position as the "sleep beauty" set - different angle from Nocna Rutyna's "hair protection" angle

---

### Multi-pack: "Scrunchie Trio"

> 3 kolory, 1 zestaw - idealny prezent

| Field | Value |
|-------|-------|
| **Contents** | 3× Scrunchie jedwabny (colors A, B, C - one of each) |
| **Separate price** | 3 × 59 = 177 zł |
| **Bundle price** | **139 zł** |
| **Discount** | 38 zł (21.5%) |
| **COGS** | ~36 zł |
| **Gross margin** | 74% (103 zł profit) |
| **Free shipping** | Does NOT clear 299 zł - may trigger "dodaj poszewkę" upsell |
| **Inventory per sale** | 3 scrunchies (1 per color) |
| **Max before stock pressure** | ~16 trios from 150 units (rest reserved for cross-sell + individual) |

**Why it works:**
- Presenter's Paradox does NOT apply to identical items (Shaddy & Fishbach 2017)
- Gifting play at an accessible price point - "3 kolory, 1 zestaw"
- Impulse/repeat purchase - lowest-commitment bundle
- 139 zł feels like a steal for 3 silk scrunchies
- Separate customer need from the other two bundles (gift buyer vs self-buyer)

**Framing guidelines:**
- Headline: "3 kolory, 1 zestaw - idealny prezent"
- Sub-headline or badge: "Oszczędzasz 38 zł"
- Emphasize the gifting angle and color variety

---

### Cross-sell mechanism (REPLACES the old "Starter Kit" bundle)

The original brandbook proposed a "Starter Kit" (Poszewka + Scrunchie = 298/269 zł). Research showed this triggers the Presenter's Paradox: the 59 zł scrunchie dilutes the 269 zł poszewka's perceived value via averaging.

**Replacement: PDP checkbox cross-sell**

> ☐ Dodaj jedwabną scrunchie - 39 zł zamiast 59 zł

| Field | Value |
|-------|-------|
| **Mechanism** | Checkbox below "Dodaj do koszyka" on poszewka and bonnet PDPs |
| **Scrunchie price in cross-sell** | 39 zł (34% off the 59 zł standalone price) |
| **Combined cart (poszewka + scrunchie)** | 269 + 39 = 308 zł |
| **Free shipping** | Clears 299 zł ✓ |
| **Why 34% discount** | Khan & Dhar (2010): discount on the hedonic (fun/fashion) item increases purchase of the utilitarian item. Scrunchie = hedonic, poszewka = utilitarian. |

**Why this is better than a formal Starter Kit bundle:**
1. Customer evaluates poszewka at full 269 zł first, then considers scrunchie - no averaging/dilution
2. Poszewka reference price stays intact at 269 zł
3. Scrunchie standalone reference price stays at 59 zł (39 zł is "with purchase" price, not the "real" price)
4. No extra SKU to manage in Shopify
5. Natural free-shipping-threshold mechanic

**Implementation:** Requires a PDP checkbox upsell feature. See `memory-bank/doc/features/pdp-migration-backlog.md` item 1 for technical scope. This replaces the full "Starter Kit" bundle concept. Can be built as a simple checkbox in `lusena-main-product.liquid` buybox or via Shopify bundle app.

---

## Phase 2 - Scale (after 8-12 weeks of data)

These bundles launch ONLY when specific metrics are met. Do not create in Shopify admin until triggers are satisfied.

### Bundle 4: "Kompletna Nocna Rutyna"

> Twarz, włosy i oczy - kompletna jedwabna ochrona na noc

| Field | Value |
|-------|-------|
| **Contents** | Poszewka + Bonnet + Maska 3D |
| **Separate price** | 269 + 239 + 169 = 677 zł |
| **Bundle price** | **499 zł** |
| **Discount** | 178 zł (26.3%) |
| **COGS** | ~181 zł |
| **Gross margin** | 64% (318 zł profit) |
| **Psychological threshold** | Under 500 zł ✓ |

**Launch triggers (ALL must be met):**
- Phase 1 Nocna Rutyna attach rate >5% of orders
- Maska 3D individual + Piękny Sen combined sales below target
- Bonnet restocked OR inventory sufficient for bundle allocation

**Why 26.3% (deeper than Phase 1's ~21%):**
- Progressive discount: bigger set = bigger savings (incentivizes upselling to larger bundle)
- All 3 items are substantial (169-269 zł) - no Presenter's Paradox. Average per item: ~166 zł
- 499 zł under 500 zł psychological barrier
- Contribution margin still at 64% - well above 40-60% DTC benchmark

---

### Bundle 5: "Duo dla Pary"

> Dwie poszewki, jedna nocna rutyna - dla par, które inwestują we wspólny sen

| Field | Value |
|-------|-------|
| **Contents** | 2× Poszewka jedwabna (different colors) |
| **Separate price** | 2 × 269 = 538 zł |
| **Bundle price** | **429 zł** |
| **Discount** | 109 zł (20.3%) |
| **COGS** | ~140 zł |
| **Gross margin** | 67% (289 zł profit) |

**Launch triggers:**
- Seasonal: before Valentine's Day, wedding season, or housewarming gift season
- OR data shows organic 2× poszewka co-purchases
- Limited-time availability (creates urgency without permanent discounting)

---

## Phase 3 - Seasonal & expansion (6+ months)

### Bundle 6: "Zestaw Prezentowy" (gift packaging variant)

NOT a new bundle - it's an existing bundle (Nocna Rutyna or Piękny Sen) with **premium gift packaging** at a slight premium.

| Field | Value |
|-------|-------|
| **Base bundle** | Nocna Rutyna (399 zł) or Piękny Sen (349 zł) |
| **Gift packaging surcharge** | +20-30 zł |
| **Gift set price** | 419-429 zł (Nocna Rutyna) or 369-379 zł (Piękny Sen) |
| **Launch triggers** | Before Christmas, Mother's Day, Valentine's Day |

The surcharge covers premium packaging cost and positions the gift version as "ready to give." No additional discount - the gift experience IS the added value.

### Bundle 7: "Limitowana Edycja" (new color launches)

| Field | Value |
|-------|-------|
| **Contents** | Limited color poszewka + matching scrunchie in the same limited color |
| **Price** | At or above standard retail (NO discount) |
| **Discount** | 0% - scarcity adds value |
| **Launch triggers** | New color launches per the brandbook's "limitka" strategy (§ 7.3) |

This is the ONLY "bundle" where discounting is explicitly wrong. The limited edition framing + color exclusivity provides value beyond price. Badge: "Edycja limitowana."

### Contingency: "Jedwabny Styling" (curlers rescue bundle)

Only created if curlers sell-through <30% in 60 days (brandbook § 7.5 trigger).

| Field | Value |
|-------|-------|
| **Contents** | Jedwabny wałek do loków + 2× Scrunchie |
| **Separate price** | 219 + 59 + 59 = 337 zł |
| **Bundle price** | **269 zł** |
| **Discount** | 68 zł (20.2%) |
| **Narrative** | "Loki bez ciepła - komplet do naturalnego stylizowania" |

Curlers are NOT proactively bundled because they serve a different customer need (daytime styling) than the nighttime protection narrative. Forced pairing weakens both products' positioning. This bundle exists only as a reactive sales mechanism.

---

## What was deliberately rejected and why

| Original brandbook bundle | Decision | Research basis |
|--------------------------|----------|---------------|
| **Starter Kit** (Poszewka + Scrunchie, 10% off) | **Replaced with PDP cross-sell checkbox** | Presenter's Paradox: 59 zł scrunchie dilutes 269 zł poszewka via averaging. Cross-sell avoids this. |
| **Scrunchie as component** of premium bundles | **Scrunchie excluded from all bundles except Trio** | Same Presenter's Paradox. Also protects scrunchie's standalone reference price per Raghubir (2004). |
| **10-19% discount range** | **Raised to 20-26%** | Harlam et al. (1995): 20% is the minimum activation threshold. Below 20%, consumers still prefer individual products. |
| **"Oszczędzasz X%" framing** | **Changed to absolute złoty + routine framing** | Luxury positioning prohibits savings-first messaging. Absolute amounts outperform percentages at 400+ zł price points. |
| **Curlers in proactive bundles** | **Standalone product, reactive bundle only** | Different customer need (daytime styling vs nighttime protection). Forced pairing dilutes the "nocna rutyna" brand narrative. |
| **3-item bundles with scrunchie** | **2-item premium bundles only (Phase 1)** | Presenter's Paradox + Soman & Gourville (2001): more items = lower consumption probability per item. Keep Phase 1 bundles tight. |

---

## Bundle economics model

### Per-order contribution analysis

Estimated CAC for Meta ads in Poland (new premium DTC brand):

| Scenario | CAC estimate |
|----------|-------------|
| Pessimistic (CPC 3 zł, CR 1.5%) | 200 zł |
| Realistic (CPC 2 zł, CR 2%) | 100 zł |
| Optimistic (CPC 1.5 zł, CR 3%) | 50 zł |

Using the realistic CAC of 100 zł:

| Scenario | Revenue | Gross profit | After CAC | vs. poszewka alone |
|----------|---------|-------------|-----------|---------------------|
| Poszewka alone | 269 zł | 199 zł | 99 zł | baseline |
| Poszewka + cross-sell scrunchie (39 zł) | 308 zł | 226 zł | 126 zł | +27% |
| **Nocna Rutyna bundle** | **399 zł** | **259 zł** | **159 zł** | **+61%** |
| **Piękny Sen bundle** | **349 zł** | **238 zł** | **138 zł** | **+39%** |
| Kompletna Nocna Rutyna (Phase 2) | 499 zł | 318 zł | 218 zł | +120% |

**Key insight:** The margin percentage drops (74% → 65%), but absolute profit per order rises 30-61%. Since CAC is fixed per customer regardless of order value, bundles extract significantly more value per acquired customer.

### Cannibalization model

The only scenario where bundles reduce total profit: a customer who would have bought both items separately at full price instead buys the bundle.

Conservative estimate: 85% of bundle buyers are incremental (would have bought only 1 item), 15% would have bought both separately.

| | Without bundles | With bundles | Difference |
|---|---|---|---|
| 85 customers × 1 item | 85 × 199 = 16,915 zł | 85 × 259 = 22,015 zł | +5,100 |
| 15 customers × 2 items | 15 × 368 = 5,520 zł | 15 × 259 = 3,885 zł | -1,635 |
| **Total per 100 customers** | **22,435 zł** | **25,900 zł** | **+3,465 zł (+15.4%)** |

Bundles generate ~15% more gross profit per 100 customers even with 15% cannibalization.

### Scrunchie standalone is unprofitable as an acquisition product

| Product | Price | Gross profit | After 100 zł CAC |
|---------|-------|-------------|-------------------|
| Scrunchie | 59 zł | 47 zł | **-53 zł (loss)** |
| Scrunchie Trio | 139 zł | 103 zł | **+3 zł (break-even)** |

Scrunchie only generates profit when:
- Cross-sold to an existing customer (zero incremental CAC)
- Sold as a trio to a gift buyer (barely profitable after CAC)
- Used as the free-shipping-threshold product ("add scrunchie to reach 299 zł")

This confirms the brandbook's positioning: scrunchie is a derivative product, not a traffic driver.

---

## Post-launch KPIs and monitoring

Review these metrics weekly (every Monday):

| KPI | Target | Warning signal | Action |
|-----|--------|---------------|--------|
| **Bundle attach rate** | 15-25% of orders | >30% → possible cannibalization | Strengthen individual PDPs (more social proof, video, comparisons) |
| **AOV lift** | +15-25% vs pre-bundle baseline | Flat → bundles not converting | Review bundle merchandising, placement, framing |
| **Contribution margin per order** | >55% average across all orders | Below 50% → discount too deep | Raise bundle prices by 10-20 zł |
| **Individual product sales** | Stable or growing | Declining while bundles rise → cannibalization | Limit bundle visibility; add "individual" emphasis |
| **Revenue per session** | Trending up | Flat → traffic issue, not bundle issue | Focus on ad targeting, not bundle pricing |
| **Bonnet stock vs velocity** | 60 units lasting 8+ weeks | Projected stockout <4 weeks → constrained | Pause Nocna Rutyna if bonnet stock <15 units |
| **Maska stock vs velocity** | 40 units lasting 8+ weeks | Projected stockout <4 weeks → constrained | Pause Piękny Sen if maska stock <10 units |

**Phase 2 decision gate:** Do NOT launch Kompletna Nocna Rutyna or Duo dla Pary until Phase 1 bundles have 8+ weeks of data AND contribution margin per order stays above 55%.

---

## Shopify implementation notes

- **Method:** Use Shopify's built-in Bundles app (free) for Phase 1. Upgrade to a third-party app (Fast Bundle, Simple Bundles) only if mix-and-match or subscription bundles are needed later.
- **Inventory sync:** Shopify Bundles automatically deducts component inventory. Critical with limited bonnet (60) and maska (40) stock.
- **Bundle products:** Each bundle is created as a separate product in Shopify admin with its own title, description, metafields, SEO, and media.
- **Theme display:** Bundles use the same PDP template (`product.json`) as individual products. Metafield copy needs creative sessions (headline, tagline, 3 benefits per bundle).
- **Homepage section:** The existing `lusena-bundles` section (card grid, `assets/lusena-bundles.css`) displays bundles. Update `templates/index.json` with bundle products when ready.
- **Cross-sell checkbox:** Requires implementation in `lusena-main-product.liquid` buybox - see PDP backlog item 1 in `memory-bank/doc/features/pdp-migration-backlog.md`.

---

## Bundle copy: creative sessions needed

Each bundle needs a creative session (lighter than individual products - primarily headline, tagline, 3 benefits):

| Bundle | Creative session status |
|--------|----------------------|
| Nocna Rutyna | **PENDING** |
| Piękny Sen | **PENDING** |
| Scrunchie Trio | **PENDING** |
| Kompletna Nocna Rutyna | Not yet (Phase 2) |
| Duo dla Pary | Not yet (Phase 2) |

The creative sessions should follow the same workflow as individual products: draft → legal check → customer validation → finalize. However, bundles share most universal metafields with component products, so the unique copy is mainly:
- `lusena.pdp_emotional_headline` - bundle-specific headline
- `lusena.pdp_tagline` - bundle-specific tagline
- `lusena.pdp_benefit_1-3` - bundle-specific benefits (why buy the SET, not the individual items)
- `lusena.pdp_packaging_items` - what's in the bundle box

Feature highlights (6 cards) can largely reuse universal cards + 1-2 bundle-specific cards.

---

## Summary: complete bundle roadmap

| Phase | Bundle | Price | Discount | Status |
|-------|--------|-------|----------|--------|
| **1 (Launch)** | Nocna Rutyna (poszewka + bonnet) | 399 zł | 21.5% | Ready for setup |
| **1 (Launch)** | Piękny Sen (poszewka + maska) | 349 zł | 20.3% | Ready for setup |
| **1 (Launch)** | Scrunchie Trio (3× scrunchie) | 139 zł | 21.5% | Ready for setup |
| **1 (Launch)** | PDP cross-sell checkbox (scrunchie 39 zł) | - | 34% on scrunchie | Needs dev work |
| **2 (8-12 wks)** | Kompletna Nocna Rutyna (poszewka + bonnet + maska) | 499 zł | 26.3% | Data-gated |
| **2 (Seasonal)** | Duo dla Pary (2× poszewka) | 429 zł | 20.3% | Seasonal |
| **3 (6+ mo)** | Zestaw Prezentowy (gift packaging variant) | +20-30 zł | - | Seasonal |
| **3 (6+ mo)** | Limitowana Edycja (limited color set) | At retail | 0% | New color launches |
| **Contingency** | Jedwabny Styling (curlers + 2× scrunchie) | 269 zł | 20.2% | Only if curlers stall |
