# LUSENA Upsell & Free Shipping Strategy

*Last updated: 2026-03-18*
*Status: Strategy validated and finalized - ready for implementation*
*Validation: Final audit 2026-03-18 - pricing validated against Polish market (SLAAP, ALMANIA, Spadiora), research citations verified (Harlam 1995, Martins 2021, Weaver 2012, Speero 2023), brand alignment confirmed*

## Overview

This document defines the complete LUSENA cart upsell, PDP cross-sell, and free shipping architecture. Every decision is backed by academic research, competitor analysis (Slip, Blissy, Brooklinen, Mayfairsilk, Lilysilk, Ettitude), and Shopify implementation patterns (research conducted 2026-03-16).

**Key references:**
- Bundle strategy (complementary, not overlapping): `memory-bank/doc/bundle-strategy.md`
- Individual product data: `memory-bank/doc/products/{handle}.md`
- Existing cart upsell code: `snippets/cart-drawer.liquid`, `sections/lusena-cart-items.liquid`
- Existing PDP cross-sell: `snippets/lusena-pdp-cross-sell.liquid`

---

## Research-backed principles

### 1. Upselling outperforms cross-selling 20:1

**Source:** Predictive Intent via Drip; Opensend/HubSpot benchmarks.

Upselling drives >4% of e-commerce sales; cross-selling drives ~0.2% on product pages (rising to 3% at checkout). Upsell conversion rates average ~20%; cross-sell averages ~4.3%.

**LUSENA application:** The primary cart upsell should be a bundle upgrade (true upsell - "upgrade your purchase") rather than a simple add-on (cross-sell). The scrunchie cross-sell serves as a fallback and free-shipping bridging mechanism.

### 2. Premium brands must NOT use discount framing

**Source:** Small Business Institute Journal (brand personality research); ResearchGate (value-increasing promotions); Bain & Company (price perception).

Consumers use price as a mental shortcut for quality. Frequent discounting trains customers to wait for sales. Premium promotions (gifts, bundles, exclusivity) do NOT negatively impact quality perception, unlike discount promotions.

**LUSENA application:** All upsell copy uses routine/benefit framing ("Kompletna ochrona na noc"), never savings framing ("Oszczedz 109 zl"). The savings amount may appear as a secondary detail (small text, not the headline), consistent with the bundle strategy's existing framing guidelines.

### 3. Show exactly 1 upsell product in the cart

**Source:** Iyengar & Lepper (2000, "jam study"); Bain & Company (choice reduction); Baymard Institute (cart abandonment).

Consumer conversion peaks at 1-3 options. 66% of users who encountered forced cross-sells at Amazon exhibited extreme frustration. Even one irrelevant recommendation destroys trust in all recommendations.

**LUSENA application:** Cart drawer and cart page show exactly 1 upsell product (already built). The product must have an obvious, logical relationship to the cart contents.

### 4. Post-purchase upsell converts 2-3x better than in-cart

**Source:** Growth Suite 2026 benchmarks; ReConvert 2024; CartHook; Yotpo.

Post-purchase one-click upsell: 3-8% acceptance (beauty: up to 15%). Cart upsell: 2-5%. Post-purchase carries zero cart abandonment risk because the sale is already complete.

**LUSENA application:** Post-purchase upsell is a Phase 2 priority. Phase 1 focuses on cart drawer/page (already built) and PDP cross-sell checkbox (backlog).

### 5. Cross-sell item must be <50% of primary item price

**Source:** Elastic Path; GoInflow; BigCommerce.

Cross-sell items priced below 50% of the primary item feel like impulse add-ons. Above 50%, they trigger a second purchase decision that slows conversion.

**LUSENA application:** The scrunchie (59 zl) is 22% of the poszewka (269 zl) - deep in the impulse zone. It is the ideal universal cross-sell product. The PDP cross-sell at 39 zl is 14% - even better.

### 6. Free shipping is the #1 AOV lever

**Source:** FedEx/Morning Consult (2024); Baymard Institute; MIT behavioral research.

81% of shoppers increase spending to qualify for free shipping. 48% of all cart abandonments are caused by unexpected shipping costs. The "magnet effect" (motivation to close the gap) is strongest when the gap is 20-100 zl (5-25 USD equivalent).

**LUSENA application:** The free shipping threshold is calibrated so the gap from the most popular products is bridgeable with a single scrunchie (see Section 2 below).

### 7. Slip is the right competitive model for LUSENA

**Source:** Competitor analysis of 7 premium silk/bedding brands.

Slip uses premium restraint: single curated recommendation in cart ("You'll also love"), two-tier free shipping progress bar, no discounts ever. Blissy's 8-step gamification is too aggressive. Brooklinen's tiered progress bar (shipping + gifts) is a Phase 2 consideration.

**LUSENA application:** One curated upsell in cart with "Pasuje do" label. Free shipping progress bar (already built). No BOGO, no gamification, no percentage discounts.

---

## Free shipping threshold: 275 zl (was 289, was 299)

### Why 299 zl is wrong

The current plan of 299 zl has a structural defect:

**Bonnet (239 zl) + scrunchie (59 zl) = 298 zl = 1 zl SHORT.**

This is the worst possible customer experience. The shopper adds a bonnet, sees they need 60 zl more, adds a scrunchie, and is still 1 zl short. There is no product in the catalog priced at 1 zl. The customer either abandons, pays for shipping despite being 1 zl away, or feels frustrated.

### Why 289 zl is optimal

| Cart combination | Total | Clears 289? | Upsell behavior |
|-----------------|-------|-------------|-----------------|
| Poszewka (269) | 269 | NO (-20) | Cross-sell scrunchie (39 zl) -> 308 YES. Gap of 20 zl is in the MIT "magnet" sweet spot. |
| Poszewka + full-price scrunchie (59) | 328 | YES (+39) | Comfortable buffer. |
| Bonnet (239) | 239 | NO (-50) | Scrunchie (59) -> 298 YES (+9). Natural add-on works. |
| **Bonnet + scrunchie (59)** | **298** | **YES (+9)** | **1-zl-short problem FIXED.** |
| Curlers (219) | 219 | NO (-70) | Scrunchie (59) -> 278 NO (-11). Problematic - see below. |
| Maska (169) | 169 | NO (-120) | Needs second product. Scrunchie gets to 228 - still short. |
| Scrunchie Trio (139) | 139 | NO (-150) | "Add poszewka" -> 408 YES. |
| Nocna Rutyna (399) | 399 | YES (+110) | Clears easily. |
| Piekny Sen (349) | 349 | YES (+60) | Clears easily. |
| Scrunchie Trio + any product | 198+ | Varies | Most combos clear. |

### Curlers: no longer a limitation

> **Updated 2026-03-29:** With the threshold at 275, curlers (219) + scrunchie (59) = 278, which now CLEARS the threshold. This was the "accepted limitation" at 289 — resolved by the threshold reduction.

### Historical analysis (289 threshold era)

> The sections below document reasoning from the 289 zl threshold decision. Kept for reference. The threshold was lowered to 275 on 2026-03-29 after cross-sell BXGY pricing finalization.

**Psychological advantage (at 289):** "Darmowa dostawa od 289 zl" reads as "under 300". At 275: even lower psychological barrier.

**Economics (289 vs 299):** At 289, additional orders qualified (bonnet + scrunchie = 298 zl). At 275, even more combos qualify (curlers + scrunchie = 278). Absorbing ~18 zl shipping on these orders is far cheaper than:
- Losing the entire 298 zl order to abandonment (loss: ~216 zl profit)
- Customer paying shipping and rating the experience poorly (retention risk)

### Research basis

- 81% of shoppers increase spending for free shipping threshold (FedEx/Morning Consult 2024)
- Threshold should be 15-30% above AOV; at least 65% of orders should qualify (Intelligems)
- "Magnet effect" strongest at 5-25 USD gap (~20-100 zl) (MIT behavioral research)
- Allegro Smart! has conditioned Polish consumers to expect free/cheap shipping (80%+ of Polish online shoppers use Allegro)
- Comparable Polish premium stores: ASK Beauty 300 zl, Nyks 250 zl (LUSENA's 289 zl fits this range)

### Implementation

Theme setting `lusena_free_shipping_threshold` is set to `275` (updated 2026-03-29, was 289 before cross-sell pricing finalization, originally 269 default).

---

## Cart upsell matrix

### Phase 1: Simple cross-sell (no code changes needed)

Phase 1 uses the existing cart upsell infrastructure (metafield waterfall) with the scrunchie as the primary cross-sell and higher-value products as secondaries.

**Why not bundles in Phase 1:** Showing a bundle in the cart upsell risks the customer adding the bundle alongside the individual product already in cart (double-buying). The "swap" logic (remove individual, add bundle) requires JS code changes. Phase 1 avoids this complexity.

| Trigger product (in cart) | upsell_role | upsell_primary | upsell_secondary | upsell_message (on the UPSELL product) |
|---|---|---|---|---|
| **Poszewka jedwabna** | `hero` | Scrunchie jedwabny | Jedwabny czepek do spania | *(per product below)* |
| **Jedwabny czepek (bonnet)** | `hero` | Scrunchie jedwabny | Poszewka jedwabna | *(per product below)* |
| **Jedwabna maska 3D** | *(empty)* | Scrunchie jedwabny | Poszewka jedwabna | *(per product below)* |
| **Jedwabny walek do lokow** | *(empty)* | Scrunchie jedwabny | Poszewka jedwabna | *(per product below)* |
| **Scrunchie jedwabny** | *(empty)* | Poszewka jedwabna | Jedwabny czepek do spania | *(per product below)* |

### Upsell messages (stored on the UPSELL product)

The `lusena.upsell_message` metafield is stored on the product being RECOMMENDED, not the trigger. This means each product has one message shown whenever it appears as an upsell.

| Product (as upsell) | `lusena.upsell_message` |
|---|---|
| **Scrunchie jedwabny** | Jedwab na dzien - mniej tarcia, mniej lamania |
| **Poszewka jedwabna** | Jedwab na noc - obudz sie bez zagniecen |
| **Jedwabny czepek do spania** | Kompletna ochrona wlosow na noc |
| **Jedwabna maska 3D** | Ciemnosc bez nacisku na powieki |
| **Jedwabny walek do lokow** | Loki bez ciepla - jedwab formuje fale w nocy |

### Global fallback

| Setting | Value |
|---|---|
| `lusena_cart_upsell_global_fallback` | Scrunchie jedwabny |
| `lusena_cart_upsell_message_fallback` | Idealne uzupelnienie z jedwabiu |
| `lusena_cart_upsell_suppress_distinct_count` | 2 |

### Suppression rules (already built in code)

| Rule | Behavior |
|---|---|
| 2+ distinct products in cart | Suppress upsell |
| Any product with `upsell_suppress = true` | Suppress upsell |
| Any product with `upsell_role = 'bundle'` | Suppress upsell (Nocna Rutyna and Piekny Sen only - NOT Scrunchie Trio, see below) |
| Upsell product already in cart | Skip to next candidate |
| Upsell product out of stock | Skip to next candidate |

### Phase 1 upsell flow examples

**Example 1: Poszewka buyer (most common)**
1. Customer adds poszewka (269 zl) to cart
2. Cart drawer opens, shows upsell: scrunchie (59 zl) / "Jedwab na dzien - mniej tarcia, mniej lamania"
3. Free shipping bar: "Brakuje Ci 20 zl do darmowej dostawy" (289 - 269 = 20)
4. Customer adds scrunchie -> cart total 328 zl, free shipping qualified
5. Upsell success animation shows, upsell zone suppressed (2 distinct products)

**Example 2: Bonnet buyer**
1. Customer adds bonnet (239 zl) to cart
2. Cart drawer shows: scrunchie (59 zl) / "Jedwab na dzien - mniej tarcia, mniej lamania"
3. Free shipping bar: "Brakuje Ci 50 zl do darmowej dostawy"
4. Customer adds scrunchie -> 298 zl, free shipping qualified (289 threshold)
5. Upsell suppressed

**Example 3: Scrunchie buyer**
1. Customer adds scrunchie (59 zl) to cart
2. Cart drawer shows: poszewka (269 zl) / "Jedwab na noc - obudz sie bez zagniecen"
3. Free shipping bar: "Brakuje Ci 230 zl do darmowej dostawy"
4. If customer adds poszewka -> 328 zl, free shipping qualified
5. Upsell suppressed

**Example 4: Two items already in cart**
1. Customer adds poszewka + bonnet (508 zl)
2. Cart drawer: upsell suppressed (2 distinct products)
3. Free shipping already qualified

---

### Phase 2: Bundle upgrade upsell (requires JS code changes)

After Phase 1 bundles are created in Shopify admin, the cart upsell should support "upgrade to bundle" - replacing the individual product with the bundle.

| Trigger product | upsell_primary (Phase 2) | upsell_secondary (Phase 2) |
|---|---|---|
| Poszewka jedwabna | **Nocna Rutyna bundle (399 zl)** | Scrunchie jedwabny |
| Jedwabny czepek (bonnet) | **Nocna Rutyna bundle (399 zl)** | Scrunchie jedwabny |
| Jedwabna maska 3D | **Piekny Sen bundle (349 zl)** | Scrunchie jedwabny |
| Jedwabny walek do lokow | Scrunchie jedwabny | Poszewka jedwabna |
| Scrunchie jedwabny | **Scrunchie Trio (139 zl)** | Poszewka jedwabna |

**Bundle upsell messages:**

| Bundle (as upsell) | `lusena.upsell_message` |
|---|---|
| Nocna Rutyna | Kompletna ochrona na noc - twarz i wlosy |
| Piekny Sen | Jedwabna ochrona twarzy i oczu |
| Scrunchie Trio | 3 kolory, 1 zestaw - idealny prezent |

**Phase 2 "swap" behavior:**
When the upsell product has `upsell_role = 'bundle'`, clicking "Dodaj" should:
1. Add the bundle product to cart via `/cart/add.js`
2. Remove the individual product from cart via `/cart/change.js` (quantity = 0)
3. Refresh the cart drawer

This requires modifying the cart drawer JS to detect bundle upsells (via a `data-upsell-replaces` attribute on the form) and chain the two API calls.

**Phase 2 label change:**
When showing a bundle upgrade, the label changes from "Pasuje do" to "Uzupelnij do zestawu".

**Phase 2 economics:**

| Scenario | Revenue | Profit | vs baseline |
|---|---|---|---|
| Poszewka alone | 269 zl | 199 zl | baseline |
| Poszewka + scrunchie cross-sell (59) | 328 zl | 246 zl | +24% profit |
| Poszewka -> Nocna Rutyna upgrade | 399 zl | 259 zl | +30% profit |
| Bonnet alone | 239 zl | 169 zl | baseline |
| Bonnet + scrunchie (59) | 298 zl | 216 zl | +28% profit |
| Bonnet -> Nocna Rutyna upgrade | 399 zl | 259 zl | +53% profit |
| Maska alone | 169 zl | 128 zl | baseline |
| Maska + scrunchie (59) | 228 zl | 175 zl | +37% profit |
| Maska -> Piekny Sen upgrade | 349 zl | 238 zl | +86% profit |

Bundle upgrades consistently deliver the highest absolute profit. The scrunchie cross-sell is the safe fallback.

---

## PDP cross-sell strategy

### Checkbox cross-sell (from bundle strategy, unchanged)

> Dodaj jedwabna scrunchie - 39 zl zamiast 59 zl

| Field | Value |
|---|---|
| Mechanism | Checkbox on ALL individual PDPs + bundle PDPs (updated 2026-03-29, was poszewka-only) |
| Scrunchie price | 39 zl (34% off 59 zl) — via Shopify BXGY automatic discount |
| Implementation | PDP checkbox adds via Cart API + Shopify BXGY automatic discount |
| Combined (poszewka + scrunchie) | 269 + 39 = 308 zl (clears 275 free shipping) |

The checkbox uses a Shopify BXGY automatic discount: buying a poszewka triggers 34% off one scrunchie. The checkbox provides the UX (auto-add); the discount provides the price reduction at checkout.

### Consistent "with purchase" pricing: 39 zl everywhere

The scrunchie is 39 zl whenever it appears as a cross-sell alongside a qualifying product (poszewka or bonnet) - whether on the PDP checkbox OR in the cart upsell. Showing different prices for the same product across touchpoints erodes trust ("you just offered me 39 zl and now it's 59 zl?").

- **PDP checkbox**: 39 zl - "Dodaj scrunchie - 39 zl zamiast 59 zl"
- **Cart upsell**: 39 zl - shown as ~~59 zl~~ **39 zl z twoim zamowieniem**
- **Standalone scrunchie PDP**: 59 zl - full retail price (no qualifying product in the transaction)

The Shopify BXGY automatic discount handles this: "buy poszewka -> 34% off 1 scrunchie." This triggers regardless of how the scrunchie was added to cart (PDP checkbox or cart upsell button), ensuring consistent pricing within the poszewka buyer's journey.

> **SUPERSEDED 2026-03-29:** The analysis below was for the original poszewka-only scope. Cross-sell checkbox is now on ALL individual PDPs + bundle PDPs. Free shipping threshold lowered from 289 to 275. At 275: bonnet (239) + scrunchie at 39 = 278, which clears the threshold. The BXGY discount scope in Shopify admin should be verified/expanded to match.

**Cross-sell checkbox: all PDPs.** Every individual product PDP and bundle PDP shows the scrunchie cross-sell checkbox (except scrunchie's own PDP and scrunchie-containing bundles). All buyers see 39 zl scrunchie offer.

**Reference price protection:** The standalone 59 zl price anchors the scrunchie's value. The 39 zl "with purchase" price is framed as a poszewka-exclusive benefit, not as the "real" price. This follows the bundle strategy principle: "Scrunchie standalone reference price stays at 59 zl (39 zl is 'with purchase' price, not the 'real' price)."

### PDP cross-sell grid (existing)

The existing `lusena-pdp-cross-sell.liquid` renders a product grid from section blocks on the PDP. This is separate from the buybox checkbox and shows full product cards below the fold. Use this for displaying 2-3 complementary products.

**Recommended PDP cross-sell grid products:**

| PDP | Cross-sell products (in grid) |
|---|---|
| Poszewka | Bonnet, Maska 3D |
| Bonnet | Poszewka, Scrunchie |
| Maska 3D | Poszewka, Bonnet |
| Curlers | Scrunchie, Poszewka |
| Scrunchie | Poszewka, Bonnet |

These are configured via section blocks in `product.json`, not metafields.

---

## Post-purchase upsell (Phase 2)

### Rationale

Post-purchase one-click upsells convert 3-8% (beauty: up to 15%) with zero cart abandonment risk. The payment method is already on file; the customer can accept with one click.

### Recommended timing

Launch after Phase 1 cart upsell has 8+ weeks of data. The pre-purchase system must be optimized first - adding post-purchase too early fragments attention and data collection.

### Recommended app

AfterSell or ReConvert (both have free plans, native Checkout Extensibility integration).

### Post-purchase offer matrix

| Original purchase | Post-purchase offer | Price |
|---|---|---|
| Poszewka | Scrunchie | 39 zl (with-purchase price) |
| Bonnet | Scrunchie | 39 zl |
| Maska 3D | Scrunchie | 39 zl |
| Curlers | Scrunchie | 39 zl |
| Scrunchie | Poszewka (mini teaser - "Jedwab tez na noc") | Full price (269 zl) |
| Nocna Rutyna | Maska 3D | 139 zl (special "complete the trio" price) |
| Piekny Sen | Bonnet | 199 zl (special "complete the trio" price) |
| Scrunchie Trio | Poszewka | Full price (269 zl) |

### Post-purchase framing

"Inne klientki pokochaly ten produkt" (Mayfairsilk model) or "Uzupelnij swoja rutyne" (routine framing). Never savings-first.

---

## Copy and framing guidelines

### Cart upsell label

| Context | Label |
|---|---|
| Cross-sell (individual product) | **Pasuje do** |
| Bundle upgrade (Phase 2) | **Uzupelnij do zestawu** |

### Cart upsell message tone

- One line, benefit-first
- No exclamation marks
- No percentage discounts
- No "Oszczedzasz X zl" as the primary message
- The message explains WHY this product complements what's in the cart

### Free shipping bar copy

| State | Copy |
|---|---|
| Below threshold | Brakuje Ci **{amount}** do darmowej dostawy |
| Qualified | **Masz darmowa dostawe!** |

### PDP checkbox copy

> Dodaj jedwabna scrunchie - **39 zl** ~~59 zl~~

### What to NEVER do

| Don't | Why |
|---|---|
| "Oszczedzasz 21%!" as headline | Percentage discounts cheapen premium brands |
| Show 3+ upsell products | Decision paralysis (Iyengar & Lepper jam study) |
| BOGO/gamification ("Buy 3 get 1 free") | Blissy model - wrong for premium (commoditizes silk) |
| Upsell on bundles | Bundles are already the upsell - adding more feels pushy |
| Generic "You might also like" | Must be contextually relevant - one irrelevant rec destroys trust (Baymard) |

---

## Economics model

### Per-order contribution (realistic CAC = 100 zl)

| Scenario | Revenue | Gross profit | After CAC | vs poszewka alone | Free ship (275)? |
|---|---|---|---|---|---|
| Poszewka alone | 269 zl | 199 zl | 99 zl | baseline | NO (-6 zl) |
| Poszewka + scrunchie (39 "with purchase") | 308 zl | 226 zl | 126 zl | +27% | YES |
| **Poszewka -> Nocna Rutyna** | **399 zl** | **259 zl** | **159 zl** | **+61%** | **YES** |
| Bonnet alone | 239 zl | 169 zl | 69 zl | -30% | NO |
| Bonnet + scrunchie (59 full price) | 298 zl | 216 zl | 116 zl | +68% vs bonnet alone | YES |
| **Bonnet -> Nocna Rutyna** | **399 zl** | **259 zl** | **159 zl** | **+61%** | **YES** |
| Maska alone | 169 zl | 128 zl | 28 zl | -72% | NO |
| Maska + scrunchie (59) | 228 zl | 175 zl | 75 zl | -24% | NO |
| **Maska -> Piekny Sen** | **349 zl** | **238 zl** | **138 zl** | **+39%** | **YES** |
| Curlers alone | 219 zl | 168 zl | 68 zl | -31% | NO |
| Curlers + scrunchie (59) | 278 zl | 215 zl | 115 zl | +16% | **YES** (was NO at 289) |
| Scrunchie alone | 59 zl | 47 zl | **-53 zl** | loss | NO |
| Scrunchie + poszewka | 328 zl | 246 zl | 146 zl | +47% | YES |

### Shipping cost impact

Estimated shipping cost to LUSENA: ~18 zl per order.

| Scenario | Profit before shipping | Free ship? | Profit after shipping |
|---|---|---|---|
| Poszewka alone (no upsell) | 199 zl | NO (+18 shipping revenue) | 199 + 18 = 217 zl |
| Poszewka + scrunchie (59) | 246 zl | YES (-18 shipping cost) | 246 - 18 = 228 zl |
| Poszewka -> Nocna Rutyna | 259 zl | YES (-18 shipping cost) | 259 - 18 = 241 zl |

**Key insight:** Even after absorbing shipping, the upsell scenarios generate more profit than the non-upsell scenario where the customer pays for shipping. The scrunchie upsell adds 11 zl net profit (+5%) and the bundle upgrade adds 24 zl net profit (+11%) - all while giving the customer a better experience (free shipping).

### Scrunchie as free-shipping bridge: unit economics

| Metric | Value |
|---|---|
| Scrunchie COGS | ~12 zl |
| Scrunchie at 59 zl: gross profit | 47 zl |
| Scrunchie at 39 zl (PDP cross-sell): gross profit | 27 zl |
| Shipping cost absorbed | ~18 zl |
| **Net contribution of scrunchie at 59 zl (standalone or non-qualifying trigger)** | **47 - 18 = 29 zl** |
| **Net contribution of scrunchie at 39 zl (with poszewka/bonnet)** | **27 - 18 = 9 zl** |

Both are profitable. The 39 zl "with purchase" price trades margin for higher conversion and consistent pricing across touchpoints. The scrunchie's primary job is to bridge the free shipping threshold - the 9 zl net contribution is a bonus on top of the retained main product sale.

---

## Implementation phases

### Phase 1A: Metafield configuration (no code changes)

**Prerequisites:** Products exist in Shopify admin (even as drafts).

**Actions:**
1. Set `lusena_free_shipping_threshold` to `275` in theme settings (DONE 2026-03-29)
2. Set `lusena_cart_upsell_global_fallback` to scrunchie product
3. Set `lusena_cart_upsell_message_fallback` to "Idealne uzupelnienie z jedwabiu"
4. For each product, set metafield values per the matrix above:
   - `lusena.upsell_role`
   - `lusena.upsell_primary` (product reference)
   - `lusena.upsell_secondary` (product reference)
   - `lusena.upsell_message`
5. Remove the DEV-ONLY hardcoded fallback (`all_products['the-compare-at-price-snowboard']`) from both `cart-drawer.liquid` and `lusena-cart-items.liquid`
6. Remove the hardcoded color label (`'Beżowy'`) from both files
7. **Color matching:** Update upsell variant selection logic to match the trigger product's color. If the trigger product has a "Kolor" option (e.g., Gold), find the upsell product's variant with the same color value. Fallback: if matching color is unavailable, use the variant with the highest inventory quantity (maximizes chance of fulfillment at launch with limited stock). This keeps the cart visually cohesive (matching product photos) and feels curated rather than random.

**Effort:** ~1-2 hours (metafields in Shopify admin + code removals + color matching logic)

### Phase 1B: PDP cross-sell checkbox (dev work)

**Prerequisites:** Phase 1A complete.

**Actions:**
1. Build checkbox component in `lusena-main-product.liquid` buybox (poszewka PDP only)
2. JS: on checkbox check, add scrunchie to cart via `/cart/add.js`
3. Create Shopify BXGY automatic discount: "Buy poszewka -> 34% off 1 scrunchie"
4. Display crossed-out 59 zl + 39 zl price next to checkbox

**No free shipping line on PDP.** Deliberately dropped - showing "brakuje X zl" on PDPs other than poszewka would feel discouraging (bonnet: 50 zl gap, maska: 120 zl gap), and showing it only on poszewka is inconsistent. The free shipping bar in the cart drawer/page is sufficient. Keep the PDP clean.

**Effort:** ~2-4 hours

### Phase 2A: Bundle upgrade upsell (after bundles exist in Shopify)

**Prerequisites:** Phase 1 bundles created in Shopify admin via Bundles app.

**Actions:**
1. Update metafield values: `upsell_primary` on poszewka, bonnet, maska -> bundle products
2. Add `data-upsell-replaces="{cart-item-key}"` attribute to bundle upsell forms
3. Modify cart drawer JS: detect bundle upsell, chain add-bundle + remove-individual API calls
4. Add conditional label: "Uzupelnij do zestawu" when upsell is a bundle
5. Set `upsell_role = 'bundle'` on Nocna Rutyna and Piekny Sen only (suppresses upsell when these complete-routine bundles are in cart). **Scrunchie Trio does NOT get `upsell_role = 'bundle'`** - it's a low-value multi-pack (139 zl) that doesn't clear the 275 zl free shipping threshold. Scrunchie Trio gets `upsell_primary = poszewka` so the buyer sees poszewka as upsell (139 + 269 = 408, free shipping cleared).
6. **BXGY for bundles:** Create additional BXGY rules: "Buy Nocna Rutyna OR Piekny Sen bundle -> 34% off 1 scrunchie." This prevents the scrunchie price from jumping 39 -> 59 zl when a poszewka is swapped for a bundle (the original BXGY qualifying product disappears from cart, so a new rule is needed for bundles).
7. **Smart suppress rule:** Adjust the 2-distinct-product suppress rule: show bundle upgrade even with 2 items in cart, BUT only if the bundle contains the trigger product. This prevents incorrect suggestions (e.g., Scrunchie Trio shown when poszewka + scrunchie are in cart).
8. **Discount code + free shipping:** When creating any discount codes for the store, always bundle free shipping into the discount (Shopify supports combining order discounts with free shipping). This prevents a discount code from dropping the cart below the 275 zl threshold and frustrating customers who already qualified.

9. **PDP bundle detection ("Masz poszewke w koszyku?"):** When a customer views a PDP for product B and their cart already contains product A, and both A+B are components of the same bundle, show a banner near the buy box:

   ```
   ┌─────────────────────────────────────────────┐
   │  Masz poszewke w koszyku?                   │
   │  Razem tworza Nocna Rutyne - 399 zl         │
   │  zamiast 508 zl osobno                      │
   │                                             │
   │  [Dodaj do zestawu Nocna Rutyna]            │
   └─────────────────────────────────────────────┘
   ```

   The regular "Dodaj do koszyka" button remains available below - customer is fully informed and chooses freely. Clicking "Dodaj do zestawu" removes the individual item from cart and adds the bundle.

   **Implementation:** On PDP load, fetch cart contents via `/cart.js`. Check if any cart item is a component of a bundle that also contains the current PDP product. If yes, render the banner with the bundle name, price, and "zamiast X zl osobno" comparison. Use product metafields to define bundle membership (e.g., `lusena.bundle_parent` product reference on each component pointing to its bundle product).

   **Applies to these pairs:**
   - Poszewka PDP + bonnet in cart (or reverse) → Nocna Rutyna (399 zl vs 508 zl)
   - Poszewka PDP + maska in cart (or reverse) → Piekny Sen (349 zl vs 438 zl)

10. **Cart bundle merge ("Zamien na zestaw"):** Safety net for when both components end up in the cart separately. Instead of the regular upsell, show:

    > "Te produkty sa dostepne jako Nocna Rutyna - 399 zl zamiast 508 zl [Zamien na zestaw]"

    Clicking "Zamien na zestaw" removes both individual items and adds the bundle. This replaces the regular upsell zone when a mergeable pair is detected.

    **Implementation:** In the cart upsell resolution logic (both `cart-drawer.liquid` and `lusena-cart-items.liquid`), before the normal waterfall, check if any 2 cart items are components of the same bundle. If yes, show the merge suggestion instead of the regular upsell. Priority: merge suggestion > bundle upgrade > scrunchie cross-sell > fallback.

    **Why this matters:** A new premium brand with no reviews builds trust by being transparent about cheaper options. The customer thinks "this store saved me 109 zl" instead of quietly charging more. That earns repeat customers and word-of-mouth - worth far more than the 109 zl margin difference.

**Effort:** ~8-12 hours (items 1-8: ~4-6h, PDP bundle detection: ~2-3h, cart bundle merge: ~2-3h)

### Phase 2B: Post-purchase upsell (after 8+ weeks of data)

**Prerequisites:** Phase 1 data shows cart upsell conversion rates; enough order history for meaningful post-purchase offers.

**Actions:**
1. Install AfterSell or ReConvert
2. Configure post-purchase offers per the matrix above
3. A/B test acceptance rates

**Effort:** ~2 hours (app configuration)

### Phase 3: Tiered progress bar (Brooklinen model)

**Prerequisites:** Phase 2 data shows strong customer engagement; gift packaging ready.

**Actions:**
1. Add second tier to free shipping bar: e.g., "389 zl -> darmowy zestaw do prania jedwabiu" (small gift)
2. Visual: two-tier progress bar with milestone markers

**Effort:** ~3-4 hours

---

## KPIs and monitoring

Review weekly (every Monday), alongside bundle KPIs:

| KPI | Target | Warning signal | Action |
|-----|--------|---------------|--------|
| **Cart upsell conversion** | 3-5% add rate | <2% -> low relevance or bad placement | Review upsell product selection, messaging |
| **Scrunchie attach rate** | 15-25% of orders | <10% -> upsell not converting | Review messaging, consider discount in cart |
| **Free shipping qualification rate** | 60-70% of orders | >80% -> threshold too low | Raise threshold by 20-30 zl |
| | | <50% -> threshold too high | Lower threshold by 10-20 zl |
| **AOV** | 15-25% above baseline | Flat -> upsell not working | Review entire funnel |
| **Cart abandonment rate** | <70% (industry avg) | >75% -> shipping or upsell friction | Check threshold, check upsell relevance |
| **Bundle upgrade rate (Phase 2)** | 5-10% when shown | <3% -> poor framing | Review "Uzupelnij do zestawu" copy and pricing |
| **Post-purchase acceptance (Phase 2)** | 3-5% (conservative; no CEE-specific data) | <2% -> weak offer | Test different products, messaging |

---

## What was deliberately rejected and why

| Option | Decision | Research basis |
|--------|----------|---------------|
| **Gamified tiered rewards (Blissy model)** | Rejected | 8-step BOGO gamification commoditizes silk. Premium brands don't gamify cart. |
| **Percentage discount framing** | Rejected | "Oszczedzasz 21%" cheapens brand. Use absolute amounts as secondary info only. |
| **Multiple upsell products (2-3)** | Rejected | Jam study: more choices = lower conversion. 1 curated product is optimal. |
| **Different prices for PDP and cart upsell** | Rejected | Showing 39 zl on PDP then 59 zl in cart erodes trust. Consistent "with purchase" pricing (39 zl) everywhere the scrunchie appears alongside a qualifying product. |
| **Free shipping threshold 299 zl** | Rejected | Bonnet (239) + scrunchie (59) = 298 = 1 zl short. Catastrophic UX. |
| **Free shipping threshold 249/269 zl** | Rejected | Flagship poszewka (269) clears alone -> zero upsell incentive for core buyer. |
| **Free shipping threshold 329/349 zl** | Rejected | Poszewka (269) + scrunchie (59) = 328 = 1 zl short at 329. No single product clears 349. |
| **Discounting upsell products beyond the scrunchie** | Rejected | Only the scrunchie gets a "with purchase" price (39 zl with poszewka/bonnet). Higher-value products (bonnet, maska, curlers) always show at full price in upsell. |
| **Upselling when bundle is in cart** | Rejected | Bundle IS the upsell. Adding more feels pushy and fragments the "complete set" feeling. |
| **Algorithmic recommendations** | Rejected (Phase 1) | Product Recommendations API needs 50-200+ orders. Manual metafield config is superior for 5-product catalog. |
| **Loyalty program** | Deferred to Phase 3+ | Drives repeat purchase, not per-transaction AOV. Premature before building customer base. |
| **Returning customer detection** | Ignored for launch | A customer who already owns a poszewka might see "upgrade to Nocna Rutyna" when buying a bonnet. Shopify Liquid can't access order history in cart. Accept this limitation - post-purchase upsell app (Phase 2B) can handle this better. |
| **Free shipping line on PDP** | Dropped | Showing "brakuje X zl" only works for poszewka (20 zl gap). On bonnet (50 zl) it's awkward, on maska (120 zl) it's discouraging. Inconsistent to show on one PDP only. The cart drawer/page free shipping bar is sufficient. |

---

## Metafield definitions needed

These metafield definitions must exist in Shopify admin (under `lusena.*` namespace):

| Metafield | Type | Description |
|---|---|---|
| `lusena.upsell_role` | Single-line text | Product's role in upsell logic: `hero`, `bundle`, or empty |
| `lusena.upsell_primary` | Product reference | First-choice upsell product |
| `lusena.upsell_secondary` | Product reference | Fallback upsell product |
| `lusena.upsell_suppress` | Boolean | If true, suppress upsell when this product is in cart |
| `lusena.upsell_message` | Single-line text | Benefit message shown when this product appears as upsell |

These may already be defined from the cart drawer development. Verify in Shopify admin > Settings > Custom data > Products.

---

## Summary: complete upsell roadmap

| Phase | What | When | Effort |
|-------|------|------|--------|
| **1A** | Metafield config + free shipping 275 zl + remove dev-only code + color matching | DONE (2026-03-24) | — |
| **1B** | PDP cross-sell checkbox (scrunchie 39 zl, all PDPs + bundles) + scrunchie education | DONE (2026-03-29) | — |
| **2A** | Bundle upgrade upsell + cart bundle merge + BXGY rules + smart suppress | DONE (2026-03-28) | — |
| **2B** | Post-purchase upsell (AfterSell/ReConvert) | After 8+ weeks of order data | 2 hours |
| **3** | Tiered progress bar (shipping + gift) | After 3+ months, if data supports | 3-4 hours |
