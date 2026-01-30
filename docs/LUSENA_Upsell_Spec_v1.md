# LUSENA Upsell Spec (Theme + Shopify Admin)
**Document type:** implementation + configuration guide (mockup → Shopify theme)  
**Applies to:** Shopify Online Store 2.0 theme (Dawn-based)  
**Primary upsell surface:** Cart drawer (1‑tap add‑on)  
**Secondary surface:** PDP “Pairs well with” (below the fold)  
**Brand constraints:** premium calm aesthetic, no aggressive sales UI, one primary action per viewport

---

## 1) Purpose & success criteria

### 1.1 Goals
- Increase **AOV** without harming conversion rate.
- Keep the experience **editorial + minimal** (no “salesy” patterns).
- Make upsell logic **easy to adjust in Shopify Admin** (no code changes for merchandising).

### 1.2 What “good” looks like
- Upsell is **contextual** (routine completion) and feels like part of the product story.
- Upsell adds in **one tap** (no page change, no modal pressure).
- Checkout remains the **dominant** action in the cart drawer.
- Upsell module never causes **layout shift** (CLS) or blocks primary interactions.

---

## 2) Upsell strategy (LUSENA logic)

### 2.1 “Routine completion” (core concept)
Recommend items that complete a sleep ritual, not generic “related products”.

**Primary pairings**
- **Heatless Curler → Bonnet** (protect style overnight)
- **Pillowcase → 3D Eye Mask** (same silk on skin + darkness/comfort)
- **Any hero item → Scrunchie** (low-friction add‑on)

**Practical second unit**
- **Pillowcase (single) → second pillowcase** (rotation for laundry)

### 2.2 Decision tree (priority order)
Show **max 1–2 items**. Prefer **1** for premium restraint.

1. If cart contains **Heatless Curler** and **no Bonnet** → offer **Bonnet**
2. Else if cart contains **Pillowcase** and **no 3D Eye Mask** → offer **3D Eye Mask**
3. Else if cart contains **any hero item** and **no Scrunchie** → offer **Scrunchie**
4. Else if cart contains **exactly 1× Pillowcase** → offer **second pillowcase** (same size/color if possible)

### 2.3 Suppression rules (keep it premium)
Suppress the upsell module if any is true:
- Cart already contains **2+ different LUSENA items** (avoid “nickel-and-diming”)
- Cart includes a **bundle/set** product (avoid stacking offers)
- Customer is in checkout / thank-you context (module is for cart + PDP only)

---

## 3) Frontend principles (must-follow)

### 3.1 Visual & UX principles
- **One primary action per viewport:** Checkout (or main CTA) must remain dominant.
- Upsell uses **secondary** button style (lower contrast, smaller).
- No urgency gimmicks: no timers, “only X left”, spin wheels, etc.
- Copy is calm, sensory, factual: “22 momme”, “mulberry silk”, “OEKO‑TEX”, “gift‑ready”.

### 3.2 Layout rules (cart drawer)
- Module appears **after** the main cart line items and **before** the cart CTA area, or
  as a subtle block **above** the CTA area (but never visually stronger than Checkout).
- Tile contents: image, title, one-line benefit, price, “Add”.
- Always show **stock state** (disable Add if unavailable).
- Never show more than **two** tiles; default is one.

### 3.3 Performance & accessibility
- No layout shift; reserve space for images and prices.
- All controls 44×44px minimum tap targets.
- Keyboard accessible; visible focus states.
- Respect `prefers-reduced-motion` (no movement; optional fade only).
- JS is progressive enhancement: cart should work even if JS fails.

### 3.4 Motion style (if used)
- Calm easing, 150–200ms for hover/focus; 250–400ms for drawer transitions.
- No bounce, no elastic/spring.
- Add-to-cart confirmation: subtle fade/slide only.

---

## 4) What belongs where (Theme vs Shopify Admin)

### 4.1 Implement in Theme (code)
**Theme owns:**
- Cart drawer upsell **UI component** + states (loading/added/error).
- Upsell **decision engine** (priority + suppression) that reads Admin-configured data.
- “Pairs well with” PDP block rendering + consistent styling.
- Add-to-cart via AJAX (no reload).
- Optional analytics events (see §8).

**Theme must not hardcode** specific product IDs for merchandising (use Admin-configured data).

### 4.2 Configure in Shopify Admin (no code)
**Admin owns:**
- Which products are upsells for each hero SKU (primary/secondary).
- Global fallback products (e.g., Scrunchie).
- Optional per-product copy overrides (if used).
- Bundles/sets configuration.
- Complementary products (if using Search & Discovery).

---

## 5) Shopify Admin configuration model (recommended)

### 5.1 Source of truth options
Choose **one** primary source:

**Option A — Product metafields (recommended for control)**
- Best for stable, editorial mapping and cart-drawer reuse.

**Option B — Search & Discovery complementary products**
- Fast for PDP recommendations; cart drawer reuse is possible but less controlled.

**Recommendation for LUSENA**
- Use **metafields** as the source of truth for cart drawer.
- Optionally also set complementary products in Search & Discovery for PDP.

---

## 6) Metafields spec (Admin-adjustable logic)

Create product metafields under namespace `lusena`:

### 6.1 Product-level metafields
1. `lusena.upsell_primary`  
   - **Type:** Product reference  
   - Meaning: the #1 recommended add-on for this product.

2. `lusena.upsell_secondary`  
   - **Type:** Product reference  
   - Meaning: fallback add-on if primary is in cart / unavailable.

3. `lusena.upsell_suppress`  
   - **Type:** True/false  
   - Meaning: never use this product to *trigger* upsells (useful for bundles/sets).

4. `lusena.upsell_role`  
   - **Type:** Single line text  
   - Allowed values (example): `hero`, `addon`, `bundle`  
   - Meaning: helps suppression logic and reporting.

5. `lusena.upsell_message` *(optional)*  
   - **Type:** Single line text (or rich text if preferred)  
   - Meaning: one-line editorial benefit for this upsell tile.

### 6.2 Theme-level settings (global defaults)
Add these as theme settings (Customize → Theme settings):

- Enable cart upsell: `enable_cart_upsell` (boolean)
- Max upsell tiles in cart: `cart_upsell_max_items` (1–2)
- Suppress if cart has ≥ N distinct LUSENA products: `cart_upsell_suppress_distinct_count` (default 2)
- Global fallback product (e.g., Scrunchie): `cart_upsell_global_fallback` (product reference)
- Enable PDP “Pairs well with”: `enable_pdp_pairs_well_with` (boolean)

*(If you prefer to avoid editing theme settings often, you can store these in a metaobject; see §7.3.)*

---

## 7) Integration into Shopify (step-by-step)

### 7.1 Admin setup steps
1. **Create metafields**
   - Shopify Admin → Settings → Custom data → Products → Add definitions (per §6.1)

2. **Assign metafields for hero SKUs**
   - For each hero product:
     - Set `upsell_primary` and `upsell_secondary` (examples below)
   - Example mapping:
     - Heatless Curler → primary: Bonnet, secondary: Scrunchie
     - Pillowcase → primary: 3D Eye Mask, secondary: Scrunchie

3. **Mark bundles/sets**
   - For bundle products: set `lusena.upsell_suppress = true` and `lusena.upsell_role = bundle`

4. *(Optional)* **Search & Discovery**
   - Install “Search & Discovery”
   - Set complementary products to match the same pairings for PDP

### 7.2 Theme integration steps (developer)
1. **Cart drawer module**
   - Add a new snippet or section used by cart drawer:
     - `snippets/cart-upsell.liquid` (recommended)
   - Render only if `enable_cart_upsell` is true and suppression rules pass.

2. **Decision engine**
   - Determine “trigger product”:
     - Prefer the first **hero** line item in cart.
   - Read its `lusena.upsell_primary` / `lusena.upsell_secondary`.
   - Apply suppression checks:
     - distinct LUSENA products count
     - bundle presence
   - Validate availability:
     - product exists, is published, variant available
   - Enforce max tiles (1–2).

3. **AJAX add**
   - Use `/cart/add.js` and then re-render cart drawer section (or update cart state).
   - Ensure no page refresh, no focus trap issues, and provide inline success feedback.

4. **PDP block**
   - Add a section block for “Pairs well with” (below the fold).
   - Data source:
     - either `recommendations` (Search & Discovery complementary) or metafields.

5. **Styling**
   - Reuse product-card system styles (ratio rules, typography).
   - Keep module subtle: border/background “common region”, not a banner.

### 7.3 Optional: Metaobject for global settings (advanced, cleaner ops)
If you want to edit global settings without theme settings:
- Create metaobject `upsell_config` with fields:
  - enabled (boolean)
  - max_items (number)
  - suppress_distinct_count (number)
  - global_fallback_product (product reference)
- Theme reads this metaobject (via `shop.metaobjects`) as a single config record.

---

## 8) Analytics hooks (optional but recommended)

Fire custom events to measure impact:
- `lusena_upsell_impression` (when module rendered with an offer)
- `lusena_upsell_add_click` (when user clicks Add)
- `lusena_upsell_added` (when add succeeds)
- Include payload:
  - trigger_product_handle
  - upsell_product_handle
  - placement (`cart_drawer` / `pdp`)
  - cart_value_before

Keep events lightweight and do not block UI.

---

## 9) Content guidelines (microcopy)

### 9.1 Module title options
- “Complete your night set”
- “Made to be used together”

### 9.2 One-line benefit examples
- Bonnet: “Protects hair while you sleep—silk on silk.”
- 3D Eye Mask: “Darkness + comfort, without pressure.”
- Scrunchie: “Gentle hold—no tugging, no creases.”

Buttons:
- Upsell button: “Add”
- Primary remains: “Checkout”

---

## 10) QA checklist (must pass)

### Functional
- Upsell respects priority + suppression logic
- Out-of-stock upsell is not shown (or shown disabled with clear state)
- 1‑tap add works and updates cart without reload
- No duplicate offers if upsell item already in cart

### UX
- Checkout remains visually dominant
- No CLS from module
- Mobile tap targets meet 44×44
- Keyboard navigation works
- Reduced-motion users are respected

### Performance
- Module does not add heavy scripts
- Images are sized with proper aspect ratio and lazy loading when appropriate

---

## 11) Implementation notes for mockup → Shopify
- In the mockup, represent upsell config as a JSON object matching §6–§7.
- When merging to Shopify, replace JSON with:
  - product metafields (`lusena.*`)
  - theme settings (or metaobject config)
- Keep the decision engine identical so behavior stays consistent across environments.

---

## Appendix A — Example product mapping
**Heatless Curler**
- `upsell_primary`: Bonnet
- `upsell_secondary`: Scrunchie
- `upsell_role`: hero

**Pillowcase**
- `upsell_primary`: 3D Eye Mask
- `upsell_secondary`: Scrunchie
- `upsell_role`: hero

**Bundle product**
- `upsell_suppress`: true
- `upsell_role`: bundle
