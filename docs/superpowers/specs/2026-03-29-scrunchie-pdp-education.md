# Scrunchie PDP Education

**Goal:** When a qualifying product is in the customer's cart, the scrunchie PDP shows the discounted price (39 zl instead of 59 zl) with a personalized hint naming the qualifying product.

**Context:** Final piece of Phase 1B cross-sell system. The BXGY automatic discount in Shopify admin already handles the real pricing - this feature educates the customer about the discount they qualify for, so they aren't surprised at checkout.

---

## What the customer sees

**Default state** (empty cart or only scrunchie/scrunchie-trio in cart):
- Price: **59 zl**
- No hint line
- Standard scrunchie PDP, no changes

**Educated state** (qualifying product in cart):
- Price: ~~59 zl~~ **39 zl** (crossed-out original + bold discounted)
- Teal hint line below price: "Taniej z poszewka jedwabna w koszyku"
- Sticky ATC bar price also shows 39 zl
- No ATC button label change (stays "Dodaj do koszyka")

The price swap is inline - no banners, no cards, no extra UI elements. The price itself IS the education. A small teal hint explains why. This matches how premium brands handle loyalty/status pricing: the price reflects your status with a subtle explanation.

---

## Qualifying products

Any cart item whose product handle does NOT contain "scrunchie" triggers the education. This covers all individual products (poszewka, bonnet, maska, walek) and bundles (Nocna Rutyna, Piekny Sen) while excluding scrunchie and scrunchie trio.

---

## Dynamic copy

The hint line names the specific qualifying product using Polish instrumental case (narzednik). A JS handle-to-label map provides the correct grammar:

| Handle | Hint text |
|--------|-----------|
| `poszewka-jedwabna` | Taniej z poszewką jedwabną w koszyku |
| `czepek-jedwabny` | Taniej z czepkiem jedwabnym w koszyku |
| `jedwabna-maska-do-spania-3d` | Taniej z maską do spania w koszyku |
| `jedwabny-walek-do-lokow` | Taniej z wałkiem do loków w koszyku |
| `nocna-rutyna` | Taniej z zestawem Nocna Rutyna w koszyku |
| `piekny-sen` | Taniej z zestawem Piękny Sen w koszyku |
| (any other handle) | Taniej w komplecie |

Multiple qualifying items: show the first qualifying product found in cart. If that one is removed but another remains, hint updates to the next qualifying product.

---

## Detection and live sync

**Page load:** JS fetches `/cart.js`. If any cart item's handle does not contain "scrunchie", activate education with that product's label.

**Live cart sync:** Subscribe to `PUB_SUB_EVENTS.cartUpdate`. On every cart change event:
1. Re-fetch `/cart.js`
2. Re-evaluate qualifying items
3. If qualifying product removed and none remain - revert to 59 zl, remove hint
4. If qualifying product added - show education
5. If qualifying product changed (e.g., poszewka removed but bonnet remains) - update hint text

Transitions are bidirectional. The education can activate and deactivate any number of times during a session.

---

## Scope

### In scope
- Price swap on scrunchie PDP main buy-box price area
- Teal hint line with dynamic product name (Polish instrumental case)
- Sticky ATC bar price update
- JS: fetch `/cart.js` on page load
- Live cart sync via `PUB_SUB_EVENTS.cartUpdate`
- Bidirectional transitions (activate and deactivate)
- Handle-to-label map (6 products + generic fallback)

### Not in scope
- ATC button label change (keeps "Dodaj do koszyka")
- Collection page price change (scrunchie stays 59 zl in product grids)
- Cart line-item education (already decided: skip)
- Animation on price swap (instant swap, no transition needed)

---

## Implementation footprint

**Modify:**
- `snippets/lusena-pdp-summary.liquid` - add data attributes to price elements for JS targeting, render the hidden hint element
- `assets/lusena-pdp.css` - hint line styling (teal color, font size, weight)

**Create:**
- `snippets/lusena-scrunchie-education.liquid` - inline `<script>` with: cart fetch, handle-to-label map, PubSub subscriber, bidirectional DOM swap logic

**Estimated size:** ~50-70 lines JS, ~15 lines CSS, ~20 lines Liquid.

---

## Edge cases

- **Scrunchie PDP loaded with empty cart, then product added via different tab:** No cross-tab sync. Education appears only after page refresh or in-page cart interaction that triggers `cartUpdate`.
- **Multiple scrunchies in cart:** The education still shows - the BXGY discount applies per qualifying product, not per scrunchie quantity.
- **Cart has qualifying product + scrunchie already:** Education still shows. Customer might be buying a second scrunchie at the discounted price, which is valid per BXGY rules.
