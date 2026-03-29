# Scrunchie PDP Education Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Show discounted scrunchie price (39 zl) on the scrunchie PDP when a qualifying product is in the customer's cart, with a personalized hint naming the qualifying product.

**Architecture:** A self-contained Liquid snippet creates education DOM elements dynamically and manages state via JS. On page load and on every cart change (PubSub), it fetches `/cart.js`, checks for qualifying items, and toggles an education overlay that hides the original price row and shows crossed-out + discounted price plus a teal hint. A MutationObserver guards against variant-change scripts overwriting sticky ATC prices during active education.

**Tech Stack:** Shopify Liquid, vanilla JS (ES5, inline `<script>`), CSS with LUSENA design tokens

---

## File Structure

| Action | File | Responsibility |
|--------|------|----------------|
| Create | `snippets/lusena-scrunchie-education.liquid` | All education logic: Liquid guard, config data attribute, inline JS (cart check, PubSub subscriber, DOM manipulation, sticky sync) |
| Modify | `assets/lusena-pdp.css` | Education price row + hint line CSS (6 rules, ~20 lines) |
| Modify | `sections/lusena-main-product.liquid` | Render call for education snippet + schema setting for education price |

**Design note:** The spec suggested modifying `snippets/lusena-pdp-summary.liquid` to add data attributes, but all needed attributes (`data-lusena-price`, `data-lusena-compare-at`, `data-lusena-price-wrap`, `data-lusena-price-per-night`) already exist. Education DOM elements are created dynamically by JS to keep the shared summary snippet clean.

---

### Task 1: Create `snippets/lusena-scrunchie-education.liquid`

**Files:**
- Create: `snippets/lusena-scrunchie-education.liquid`

**Context:** This snippet is rendered from `sections/lusena-main-product.liquid` (wired in Task 3). It receives `product` and `education_price` as parameters. The inline script follows the same ES5 pattern used in `snippets/lusena-pdp-cross-sell-checkbox.liquid`: IIFE with idempotency guard, DOM lookups by data-attribute, `fetch('/cart.js')` for cart state.

**Key DOM elements the JS targets (already exist in the page):**
- `[data-lusena-product-section]` — section root
- `[data-lusena-price]` — main price `<span>` inside `.lusena-pdp-summary__price-row`
- `[data-lusena-price-per-night]` — per-night price
- `[data-lusena-sticky-price]` — sticky ATC prices (2 elements: mobile + desktop)
- `[data-lusena-sticky-price-per-night]` — sticky per-night prices (2 elements)

**Variant change interaction:** When the customer changes scrunchie color, `lusena-pdp-scripts.liquid`'s `updateUIForVariant()` directly overwrites `[data-lusena-price]` textContent and all `[data-lusena-sticky-price]` elements. Since all scrunchie variants cost 59 zl, the value doesn't change — but the text IS rewritten. The education handles this by:
1. Main price: hidden behind the education overlay row (`.lusena-pdp-summary__price-row` gets `hidden`), so overwrites are invisible.
2. Sticky prices: a MutationObserver detects overwrites and re-applies the education price. A `stickyGuard` flag prevents infinite observer loops.

- [ ] **Step 1: Create the snippet file**

Create `snippets/lusena-scrunchie-education.liquid` with the following content:

```liquid
{%- comment -%}
  Scrunchie PDP education — shows discounted price when qualifying product is in cart.
  Parameters: product (product object), education_price (integer, cents)
{%- endcomment -%}

{%- if product.handle == 'silk-scrunchie' and education_price != blank -%}
<span data-lusena-scrunchie-education
      data-education-price="{{ education_price | money_without_trailing_zeros }}"
      hidden></span>
<script>
(function lusenaScrunchieEducation() {
  var root = document.querySelector('[data-lusena-product-section]');
  if (!root) return;
  if (root.dataset.lusenaEducationInit) return;
  root.dataset.lusenaEducationInit = '1';

  /* ---- Config from Liquid ---- */
  var configEl = root.querySelector('[data-lusena-scrunchie-education]');
  if (!configEl) return;
  var eduPriceText = configEl.dataset.educationPrice;

  /* ---- Handle-to-label map (Polish instrumental case) ---- */
  var LABELS = {
    'poszewka-jedwabna': 'Taniej z poszewk\u0105 jedwabn\u0105 w koszyku',
    'silk-bonnet': 'Taniej z czepkiem jedwabnym w koszyku',
    'jedwabna-maska-do-spania-3d': 'Taniej z mask\u0105 do spania w koszyku',
    'jedwabny-walek-do-lokow': 'Taniej z wa\u0142kiem do lok\u00f3w w koszyku',
    'nocna-rutyna': 'Taniej z zestawem Nocna Rutyna w koszyku',
    'piekny-sen': 'Taniej z zestawem Pi\u0119kny Sen w koszyku'
  };
  var FALLBACK_LABEL = 'Taniej w komplecie';

  /* ---- DOM refs ---- */
  var priceEl = root.querySelector('[data-lusena-price]');
  var priceRow = priceEl ? priceEl.closest('.lusena-pdp-summary__price-row') : null;
  var perNightEl = root.querySelector('[data-lusena-price-per-night]');
  var stickyPrices = document.querySelectorAll('[data-lusena-sticky-price]');
  var stickyPerNights = document.querySelectorAll('[data-lusena-sticky-price-per-night]');

  if (!priceRow) return;

  /* ---- Build education elements ---- */
  var eduRow = document.createElement('div');
  eduRow.className = 'lusena-pdp-summary__education-row';
  eduRow.hidden = true;

  var eduCompare = document.createElement('span');
  eduCompare.className = 'lusena-pdp-summary__education-compare';

  var eduCurrent = document.createElement('span');
  eduCurrent.className = 'lusena-pdp-summary__education-current';
  eduCurrent.textContent = eduPriceText;

  eduRow.appendChild(eduCompare);
  eduRow.appendChild(eduCurrent);

  var hintEl = document.createElement('span');
  hintEl.className = 'lusena-pdp-summary__education-hint';
  hintEl.hidden = true;

  priceRow.after(eduRow);
  eduRow.after(hintEl);

  /* ---- State ---- */
  var isActive = false;
  var stickyGuard = false;

  /* ---- Sticky MutationObserver ---- */
  var stickyObs = null;
  if (stickyPrices.length > 0) {
    stickyObs = new MutationObserver(function() {
      if (stickyGuard || !isActive) return;
      applyStickyEducation();
    });
    stickyObs.observe(stickyPrices[0], { childList: true, characterData: true, subtree: true });
  }

  function applyStickyEducation() {
    stickyGuard = true;
    stickyPrices.forEach(function(el) { el.textContent = eduPriceText; });
    stickyPerNights.forEach(function(el) { el.hidden = true; });
    stickyGuard = false;
  }

  function revertStickyEducation() {
    stickyGuard = true;
    stickyPrices.forEach(function(el) { el.textContent = priceEl.textContent; });
    stickyPerNights.forEach(function(el) { el.hidden = false; });
    stickyGuard = false;
  }

  /* ---- Activate / Deactivate ---- */
  function activate(label) {
    isActive = true;
    eduCompare.textContent = priceEl.textContent;
    priceRow.hidden = true;
    eduRow.hidden = false;
    hintEl.textContent = label;
    hintEl.hidden = false;
    if (perNightEl) perNightEl.hidden = true;
    applyStickyEducation();
  }

  function deactivate() {
    isActive = false;
    priceRow.hidden = false;
    eduRow.hidden = true;
    hintEl.hidden = true;
    if (perNightEl) perNightEl.hidden = false;
    revertStickyEducation();
  }

  /* ---- Cart check ---- */
  function checkCart() {
    fetch('/cart.js', { credentials: 'same-origin' })
      .then(function(r) { return r.json(); })
      .then(function(cart) {
        var label = null;
        for (var i = 0; i < cart.items.length; i++) {
          var handle = cart.items[i].handle;
          if (handle.indexOf('scrunchie') === -1) {
            label = LABELS[handle] || FALLBACK_LABEL;
            break;
          }
        }
        if (label) {
          activate(label);
        } else if (isActive) {
          deactivate();
        }
      })
      .catch(function() { /* network error — silently ignore */ });
  }

  /* ---- PubSub subscriber (live cart sync) ---- */
  if (typeof subscribe === 'function' && typeof PUB_SUB_EVENTS !== 'undefined') {
    subscribe(PUB_SUB_EVENTS.cartUpdate, function() {
      checkCart();
    });
  }

  /* ---- Init ---- */
  checkCart();
})();
</script>
{%- endif -%}
```

- [ ] **Step 2: Verify file was created correctly**

Run: `shopify theme check snippets/lusena-scrunchie-education.liquid`

Expected: No new errors (some pre-existing baseline warnings are fine). The Liquid syntax and `<script>` tag should pass validation.

- [ ] **Step 3: Commit**

```bash
git add snippets/lusena-scrunchie-education.liquid
git commit -m "feat(lusena): add scrunchie PDP education snippet"
```

---

### Task 2: Add education CSS to `assets/lusena-pdp.css`

**Files:**
- Modify: `assets/lusena-pdp.css` (insert after the existing `.lusena-pdp-summary__per-night` rules, around line 383)

**Context:** The education creates three dynamic elements: `.lusena-pdp-summary__education-row` (flex row with compare + current price), `.lusena-pdp-summary__education-compare` (crossed-out original), `.lusena-pdp-summary__education-current` (bold discounted), and `.lusena-pdp-summary__education-hint` (teal text below). All selectors must use 0-2-0 specificity (`.lusena-pdp .lusena-pdp-summary__*`) per the CSS cascade rules.

- [ ] **Step 1: Add CSS rules**

Insert the following CSS block in `assets/lusena-pdp.css` after the existing `.lusena-pdp .lusena-pdp-summary__price` rule (line 381) and before the `[data-lusena-price-wrap]` margin rule (line 383):

```css
/* --- Scrunchie PDP education (price swap when qualifying product in cart) --- */
.lusena-pdp .lusena-pdp-summary__education-row {
  display: flex;
  align-items: baseline;
  gap: 0.8rem;
}

.lusena-pdp .lusena-pdp-summary__education-compare {
  font-size: 1.6rem;
  line-height: 1.4;
  color: var(--lusena-text-2);
  text-decoration: line-through;
  font-variant-numeric: tabular-nums;
}

.lusena-pdp .lusena-pdp-summary__education-current {
  font-variant-numeric: tabular-nums;
}

.lusena-pdp .lusena-pdp-summary__education-hint {
  display: block;
  margin-top: 0.2rem;
  font-family: var(--lusena-font-ui);
  font-size: 1.2rem;
  font-weight: 500;
  line-height: 1.4;
  color: var(--lusena-accent-cta);
}
```

**Why no font-size on `.education-current`:** It inherits from the parent `[data-lusena-price-wrap]` context, matching the regular `[data-lusena-price]` size exactly — same visual weight as the standard price.

- [ ] **Step 2: Commit**

```bash
git add assets/lusena-pdp.css
git commit -m "feat(lusena): add scrunchie education price CSS"
```

---

### Task 3: Wire education into `sections/lusena-main-product.liquid`

**Files:**
- Modify: `sections/lusena-main-product.liquid:190` (render call) and `:418` (schema setting)

**Context:** The render call goes just before the sticky ATC render (line 190). The snippet handles its own product-handle guard internally (`product.handle == 'silk-scrunchie'`), so no outer conditional is needed. The schema setting follows the same pattern as the cross-sell price setting at line 412-418.

- [ ] **Step 1: Add render call**

In `sections/lusena-main-product.liquid`, insert the education snippet render call at line 190, just before the sticky ATC render:

Find this block (lines 188-190):
```liquid
  {% render 'lusena-pdp-cross-sell', section: section %}

  {% render 'lusena-pdp-sticky-atc', product: product, current_variant: current_variant, section: section, product_form_id: product_form_id %}
```

Replace with:
```liquid
  {% render 'lusena-pdp-cross-sell', section: section %}

  {% render 'lusena-scrunchie-education', product: product, education_price: section.settings.scrunchie_education_price %}

  {% render 'lusena-pdp-sticky-atc', product: product, current_variant: current_variant, section: section, product_form_id: product_form_id %}
```

- [ ] **Step 2: Add schema setting**

In the `{% schema %}` block, insert a new header + setting after the existing `cross_sell_price` setting (line 418). Find:

```json
    {
      "type": "number",
      "id": "cross_sell_price",
      "label": "Cena cross-sell (grosze)",
      "default": 3900,
      "info": "Cena wyswietlana na PDP. Musi odpowiadac rabatowi BXGY w Shopify admin (np. 3900 = 39 zl)."
    }
```

Insert after it (before the `],` that closes the settings array):

```json
    ,
    {
      "type": "header",
      "content": "Scrunchie PDP education"
    },
    {
      "type": "number",
      "id": "scrunchie_education_price",
      "label": "Cena edukacyjna scrunchie (grosze)",
      "default": 3900,
      "info": "Cena wyswietlana na PDP scrunchie gdy kwalifikujacy produkt jest w koszyku (np. 3900 = 39 zl). Musi odpowiadac rabatowi BXGY."
    }
```

- [ ] **Step 3: Run theme check**

Run: `shopify theme check sections/lusena-main-product.liquid snippets/lusena-scrunchie-education.liquid`

Expected: No new errors beyond the known baseline (`main-product.liquid` warnings, `scheme_classes` in layouts).

- [ ] **Step 4: Commit**

```bash
git add sections/lusena-main-product.liquid
git commit -m "feat(lusena): wire scrunchie education into PDP section"
```

---

### Task 4: Manual verification

**Files:** None (browser testing only)

**Context:** The dev server must be running (`shopify theme dev`). Use `playwright-cli` with a named session for all browser work. The scrunchie product URL is `/products/silk-scrunchie`.

- [ ] **Step 1: Verify default state (empty cart)**

1. Clear the cart (or open incognito)
2. Navigate to `/products/silk-scrunchie`
3. Confirm: price shows **59 zl**, no hint text visible, no education overlay
4. Confirm: sticky ATC bar shows **59 zl** when scrolling down

- [ ] **Step 2: Verify educated state**

1. Navigate to a qualifying product PDP (e.g., `/products/poszewka-jedwabna`)
2. Add it to cart
3. Navigate to `/products/silk-scrunchie`
4. Confirm: price shows ~~59 zl~~ **39 zl** with education overlay
5. Confirm: teal hint reads **"Taniej z poszewka jedwabna w koszyku"** (with diacritics)
6. Confirm: sticky ATC bar shows **39 zl**
7. Confirm: per-night price is hidden (if it was visible)

- [ ] **Step 3: Verify live cart sync (deactivation)**

1. While on scrunchie PDP with education active, open cart drawer
2. Remove the qualifying product from cart
3. Confirm: price reverts to **59 zl** (education deactivates)
4. Confirm: hint text disappears
5. Confirm: sticky ATC reverts to **59 zl**

- [ ] **Step 4: Verify live cart sync (activation)**

1. While on scrunchie PDP with education inactive, use cart drawer to add a qualifying product (if possible via cart upsell) — OR simply navigate to another PDP, add to cart, come back
2. Confirm: education activates with correct product label

- [ ] **Step 5: Verify variant change doesn't break education**

1. With education active, change scrunchie color swatch
2. Confirm: education price (39 zl) stays visible, not reverted to 59 zl
3. Confirm: sticky price stays at 39 zl

- [ ] **Step 6: Verify other PDPs unaffected**

1. Navigate to `/products/poszewka-jedwabna`
2. Confirm: NO education elements visible, standard price display
3. Navigate to any bundle PDP
4. Confirm: NO education elements visible

---

### Task 5: Update documentation

**Files:**
- Modify: `memory-bank/activeContext.md`
- Modify: `memory-bank/progress.md`

- [ ] **Step 1: Update activeContext.md**

Update the "Current focus" section to reflect Phase 1B completion. Move scrunchie education from "Next steps" to "Recent completed work". Update the "Cross-sell checkbox architecture" note to include education.

- [ ] **Step 2: Update progress.md**

Add scrunchie PDP education to the Phase D cross-sell entries as completed.

- [ ] **Step 3: Commit**

```bash
git add memory-bank/activeContext.md memory-bank/progress.md
git commit -m "docs: update memory bank for scrunchie PDP education"
```
