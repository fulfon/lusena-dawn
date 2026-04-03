# PDP Cross-sell Checkbox Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a cross-sell checkbox to all individual product PDPs offering the scrunchie at 39 zl, with color matching and dual-item ATC.

**Architecture:** New snippet (`lusena-pdp-cross-sell-checkbox.liquid`) renders a checkbox row in the buy-box between variant picker and ATC. JS intercepts form submit when checked, sending both items via `/cart/add.js` items array. Server-side Liquid does initial color matching; client-side JS updates on variant change.

**Tech Stack:** Shopify Liquid, vanilla JS, CSS (LUSENA design tokens)

**Spec:** `docs/superpowers/specs/2026-03-29-pdp-cross-sell-checkbox.md`

---

### Task 1: Section schema + buy-box render slot

**Files:**
- Modify: `sections/lusena-main-product.liquid` — schema settings + new div in buy-box

- [ ] **Step 1: Add cross-sell settings to the schema**

In `sections/lusena-main-product.liquid`, find the schema `settings` array. Add these settings before the closing `]` of the settings array (before the `blocks` definition):

```json
    {
      "type": "header",
      "content": "Cross-sell checkbox"
    },
    {
      "type": "checkbox",
      "id": "cross_sell_enabled",
      "label": "Pokazuj checkbox cross-sell w buy-boxie",
      "default": true
    },
    {
      "type": "product",
      "id": "cross_sell_product",
      "label": "Produkt cross-sell"
    },
    {
      "type": "number",
      "id": "cross_sell_price",
      "label": "Cena cross-sell (grosze)",
      "default": 3900,
      "info": "Cena wyswietlana na PDP. Musi odpowiadac rabatowi BXGY w Shopify admin (np. 3900 = 39 zl)."
    }
```

- [ ] **Step 2: Add the cross-sell checkbox render slot in the buy-box**

In `sections/lusena-main-product.liquid`, find the buy-box area. The variant picker div is at ~line 53 and the ATC div is at ~line 57. Insert a new div BETWEEN them:

After the closing `</div>` of `lusena-pdp-buy-box__variant` (line ~55) and before the opening `<div class="lusena-pdp-buy-box__atc">` (line ~57), add:

```liquid
      {%- comment -%} Cross-sell checkbox (between variant picker and ATC) {%- endcomment -%}
      {%- assign cs_product = section.settings.cross_sell_product -%}
      {%- if section.settings.cross_sell_enabled
            and cs_product != blank
            and product.handle != cs_product.handle
            and template.suffix != 'bundle'
            and cs_product.available -%}
        <div class="lusena-pdp-buy-box__cross-sell-checkbox">
          {%- render 'lusena-pdp-cross-sell-checkbox',
            cross_sell_product: cs_product,
            cross_sell_price: section.settings.cross_sell_price,
            current_variant: current_variant,
            product: product,
            section: section
          -%}
        </div>
      {%- endif -%}
```

- [ ] **Step 3: Run theme check**

Run: `shopify theme check`
Expected: Only known baseline warnings. No new errors related to `lusena-main-product.liquid`.

- [ ] **Step 4: Commit**

```
git add sections/lusena-main-product.liquid
git commit -m "feat(lusena): add cross-sell checkbox schema + render slot in buy-box"
```

---

### Task 2: Cross-sell checkbox snippet (Liquid)

**Files:**
- Create: `snippets/lusena-pdp-cross-sell-checkbox.liquid`

- [ ] **Step 1: Create the snippet**

Create `snippets/lusena-pdp-cross-sell-checkbox.liquid` with the full Liquid template. This handles:
- Color option detection for both products
- Server-side color matching (4-step: exact → highest inventory → first available)
- Checkbox row HTML with product image, title, prices, color label
- Embedded JSON for client-side variant data

```liquid
{%- comment -%}
  Cross-sell checkbox for PDP buy-box.
  Offers a discounted cross-sell product (e.g., scrunchie at 39 zl).
  Color-matches to the main product's selected variant.

  Required variables:
    cross_sell_product  - product object (from section setting)
    cross_sell_price    - discounted price in cents (e.g., 3900)
    current_variant     - selected variant of the main product
    product             - the main product
    section             - section object
{%- endcomment -%}

{%- comment -%} ── Find color option index on cross-sell product ── {%- endcomment -%}
{%- assign cs_color_index = 0 -%}
{%- for option in cross_sell_product.options_with_values -%}
  {%- assign opt_down = option.name | downcase -%}
  {%- if opt_down contains 'color' or opt_down contains 'colour' or opt_down contains 'kolor' -%}
    {%- assign cs_color_index = forloop.index -%}
  {%- endif -%}
{%- endfor -%}

{%- comment -%} ── Find color option index on main product ── {%- endcomment -%}
{%- assign main_color_index = 0 -%}
{%- for option in product.options_with_values -%}
  {%- assign opt_down = option.name | downcase -%}
  {%- if opt_down contains 'color' or opt_down contains 'colour' or opt_down contains 'kolor' -%}
    {%- assign main_color_index = forloop.index -%}
  {%- endif -%}
{%- endfor -%}

{%- comment -%} ── Get trigger color from current variant ── {%- endcomment -%}
{%- assign trigger_color = '' -%}
{%- if main_color_index == 1 -%}
  {%- assign trigger_color = current_variant.option1 -%}
{%- elsif main_color_index == 2 -%}
  {%- assign trigger_color = current_variant.option2 -%}
{%- elsif main_color_index == 3 -%}
  {%- assign trigger_color = current_variant.option3 -%}
{%- endif -%}

{%- comment -%} ── Color-match: find best cross-sell variant ── {%- endcomment -%}
{%- assign cs_variant = nil -%}
{%- assign cs_fallback = nil -%}
{%- assign cs_highest_inv = -1 -%}

{%- for variant in cross_sell_product.variants -%}
  {%- unless variant.available -%}{%- continue -%}{%- endunless -%}

  {%- if cs_color_index == 1 -%}
    {%- assign cs_var_color = variant.option1 -%}
  {%- elsif cs_color_index == 2 -%}
    {%- assign cs_var_color = variant.option2 -%}
  {%- elsif cs_color_index == 3 -%}
    {%- assign cs_var_color = variant.option3 -%}
  {%- else -%}
    {%- assign cs_var_color = '' -%}
  {%- endif -%}

  {%- if cs_var_color == trigger_color and cs_variant == nil -%}
    {%- assign cs_variant = variant -%}
  {%- endif -%}

  {%- if variant.inventory_quantity > cs_highest_inv -%}
    {%- assign cs_highest_inv = variant.inventory_quantity -%}
    {%- assign cs_fallback = variant -%}
  {%- endif -%}
{%- endfor -%}

{%- unless cs_variant -%}
  {%- if cs_fallback -%}
    {%- assign cs_variant = cs_fallback -%}
  {%- else -%}
    {%- assign cs_variant = cross_sell_product.selected_or_first_available_variant -%}
  {%- endif -%}
{%- endunless -%}

{%- comment -%} ── Guard: only render if we found an available variant ── {%- endcomment -%}
{%- if cs_variant and cs_variant.available -%}

{%- comment -%} ── Resolved color label ── {%- endcomment -%}
{%- assign cs_color_label = '' -%}
{%- if cs_color_index == 1 -%}
  {%- assign cs_color_label = cs_variant.option1 -%}
{%- elsif cs_color_index == 2 -%}
  {%- assign cs_color_label = cs_variant.option2 -%}
{%- elsif cs_color_index == 3 -%}
  {%- assign cs_color_label = cs_variant.option3 -%}
{%- endif -%}

{%- comment -%} ── Image: prefer variant-specific, fall back to product ── {%- endcomment -%}
{%- if cs_variant.featured_image -%}
  {%- assign cs_image = cs_variant.featured_image -%}
{%- else -%}
  {%- assign cs_image = cross_sell_product.featured_image -%}
{%- endif -%}

{%- comment -%} ── Prices ── {%- endcomment -%}
{%- assign cs_original_price = cs_variant.price -%}
{%- assign cs_display_price = cross_sell_price | default: cs_original_price -%}

<div class="lusena-pdp-cross-sell-cb"
     data-lusena-cross-sell-row
     data-main-color-index="{{ main_color_index }}">
  <label class="lusena-pdp-cross-sell-cb__label">
    <input
      type="checkbox"
      class="lusena-pdp-cross-sell-cb__input visually-hidden"
      data-lusena-cross-sell-checkbox
      data-variant-id="{{ cs_variant.id }}"
      autocomplete="off"
    >
    <span class="lusena-pdp-cross-sell-cb__check" aria-hidden="true"></span>

    {%- if cs_image -%}
      <span class="lusena-pdp-cross-sell-cb__image">
        <img
          src="{{ cs_image | image_url: width: 96 }}"
          alt="{{ cross_sell_product.title | escape }}"
          width="48"
          height="48"
          loading="lazy"
          data-lusena-cross-sell-image
        >
      </span>
    {%- endif -%}

    <span class="lusena-pdp-cross-sell-cb__info">
      <span class="lusena-pdp-cross-sell-cb__title">
        Dodaj {{ cross_sell_product.title | downcase }}
      </span>
      {%- if cs_color_label != blank -%}
        <span class="lusena-pdp-cross-sell-cb__color" data-lusena-cross-sell-color-label>
          Kolor: {{ cs_color_label }}
        </span>
      {%- endif -%}
    </span>

    <span class="lusena-pdp-cross-sell-cb__pricing">
      <span class="lusena-pdp-cross-sell-cb__price">
        {{- cs_display_price | money_without_trailing_zeros -}}
      </span>
      {%- if cs_original_price > cs_display_price -%}
        <span class="lusena-pdp-cross-sell-cb__was">
          {{- cs_original_price | money_without_trailing_zeros -}}
        </span>
      {%- endif -%}
    </span>
  </label>

  {%- comment -%} ── Variant data for JS color matching on variant change ── {%- endcomment -%}
  <script type="application/json" data-lusena-cross-sell-variants>
    [
      {%- for variant in cross_sell_product.variants -%}
        {%- if cs_color_index == 1 -%}
          {%- assign v_color = variant.option1 -%}
        {%- elsif cs_color_index == 2 -%}
          {%- assign v_color = variant.option2 -%}
        {%- elsif cs_color_index == 3 -%}
          {%- assign v_color = variant.option3 -%}
        {%- else -%}
          {%- assign v_color = '' -%}
        {%- endif -%}
        {
          "id": {{ variant.id }},
          "available": {{ variant.available }},
          "color": {{ v_color | json }},
          "inventory": {{ variant.inventory_quantity | default: 0 }},
          "image": {% if variant.featured_image %}{{ variant.featured_image | image_url: width: 96 | json }}{% else %}null{% endif %}
        }{% unless forloop.last %},{% endunless %}
      {%- endfor -%}
    ]
  </script>
</div>

{%- endif -%}
{%- comment -%} ── End guard: cs_variant available ── {%- endcomment -%}
```

- [ ] **Step 2: Run theme check**

Run: `shopify theme check`
Expected: Only known baseline warnings. No new errors.

- [ ] **Step 3: Commit**

```
git add snippets/lusena-pdp-cross-sell-checkbox.liquid
git commit -m "feat(lusena): cross-sell checkbox snippet with color matching"
```

---

### Task 3: CSS styles

**Files:**
- Modify: `assets/lusena-pdp.css`

- [ ] **Step 1: Adjust buy-box order values to make room for cross-sell slot**

The cross-sell checkbox takes the slot between variant and ATC. Bump ATC, guarantee, and payment order values by 1 on both mobile and desktop.

In `assets/lusena-pdp.css`, find and update these mobile base rules (around lines 37-47):

Change `.lusena-pdp .lusena-pdp-buy-box__atc` order from `5` to `6`.
Change `.lusena-pdp .lusena-pdp-buy-box__guarantee` order from `6` to `7`.
Change `.lusena-pdp .lusena-pdp-buy-box__payment` order from `7` to `8`.

Then find and update the desktop overrides inside `@media (min-width: 768px)` (around lines 461-471):

Change `.lusena-pdp .lusena-pdp-buy-box__atc` order from `7` to `8`.
Change `.lusena-pdp .lusena-pdp-buy-box__guarantee` order from `8` to `9`.
Change `.lusena-pdp .lusena-pdp-buy-box__payment` order from `9` to `10`.

- [ ] **Step 2: Add cross-sell checkbox row styles**

Add the following CSS at the end of the buy-box section in `assets/lusena-pdp.css` (after the existing buy-box child rules, before the `@media (min-width: 768px)` block — or in a clearly marked section):

```css
/* ── Cross-sell checkbox ── */

.lusena-pdp .lusena-pdp-buy-box__cross-sell-checkbox {
  order: 5;
}

.lusena-pdp-cross-sell-cb__label {
  display: flex;
  align-items: center;
  gap: var(--lusena-space-2);
  padding: var(--lusena-space-2);
  background: color-mix(in srgb, var(--lusena-accent-cta) 4%, var(--lusena-color-n0));
  border: 1px solid color-mix(in srgb, var(--lusena-color-n9) 10%, transparent);
  border-radius: var(--lusena-btn-radius);
  cursor: pointer;
  transition: border-color var(--lusena-transition-fast);
}

.lusena-pdp-cross-sell-cb__label:hover {
  border-color: color-mix(in srgb, var(--lusena-accent-cta) 30%, transparent);
}

/* Custom checkbox indicator */
.lusena-pdp-cross-sell-cb__check {
  flex-shrink: 0;
  width: 1.25rem;
  height: 1.25rem;
  border: 1.5px solid var(--lusena-color-n4);
  border-radius: 0.25rem;
  transition: background-color var(--lusena-transition-fast), border-color var(--lusena-transition-fast);
  position: relative;
}

.lusena-pdp-cross-sell-cb__input:checked ~ .lusena-pdp-cross-sell-cb__check {
  background-color: var(--lusena-accent-cta);
  border-color: var(--lusena-accent-cta);
}

.lusena-pdp-cross-sell-cb__check::after {
  content: '';
  position: absolute;
  top: 0.15rem;
  left: 0.35rem;
  width: 0.35rem;
  height: 0.6rem;
  border: solid var(--lusena-color-n0);
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
  opacity: 0;
  transition: opacity var(--lusena-transition-fast);
}

.lusena-pdp-cross-sell-cb__input:checked ~ .lusena-pdp-cross-sell-cb__check::after {
  opacity: 1;
}

/* When checked, highlight the row border */
.lusena-pdp-cross-sell-cb__input:checked ~ .lusena-pdp-cross-sell-cb__check ~ * {
  /* Handled by parent label border below */
}

.lusena-pdp-cross-sell-cb:has(.lusena-pdp-cross-sell-cb__input:checked) .lusena-pdp-cross-sell-cb__label {
  border-color: color-mix(in srgb, var(--lusena-accent-cta) 40%, transparent);
}

/* Product image */
.lusena-pdp-cross-sell-cb__image {
  flex-shrink: 0;
  width: 3rem;
  height: 3rem;
  border-radius: 0.375rem;
  overflow: hidden;
  border: 1px solid color-mix(in srgb, var(--lusena-color-n9) 8%, transparent);
}

.lusena-pdp-cross-sell-cb__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Text info */
.lusena-pdp-cross-sell-cb__info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}

.lusena-pdp-cross-sell-cb__title {
  font-size: var(--lusena-text-sm);
  font-weight: 500;
  line-height: 1.3;
}

.lusena-pdp-cross-sell-cb__color {
  font-size: var(--lusena-text-xs);
  color: var(--lusena-color-n4);
}

/* Pricing */
.lusena-pdp-cross-sell-cb__pricing {
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.125rem;
}

.lusena-pdp-cross-sell-cb__price {
  font-size: var(--lusena-text-sm);
  font-weight: 600;
  color: var(--lusena-accent-cta);
}

.lusena-pdp-cross-sell-cb__was {
  font-size: var(--lusena-text-xs);
  text-decoration: line-through;
  opacity: 0.5;
}
```

Then add the desktop order override inside the existing `@media (min-width: 768px)` block:

```css
.lusena-pdp .lusena-pdp-buy-box__cross-sell-checkbox {
  order: 7;
}
```

- [ ] **Step 3: Commit**

```
git add assets/lusena-pdp.css
git commit -m "feat(lusena): cross-sell checkbox CSS + buy-box order adjustment"
```

---

### Task 4: JS — ATC intercept, Buy Now, and variant change

**Files:**
- Modify: `snippets/lusena-pdp-scripts.liquid`

All JS goes inside the existing IIFE to access closure variables (`addToCartFormEl`, `variantIdInput`, `setStickyLoadingState`, `stickyLoadingStartedAt`, `PUB_SUB_EVENTS`, `publish`).

- [ ] **Step 1: Add the cross-sell variant update function**

Find the `updateUIForVariant` function call inside the variant change listener (~line 1401). After the call to `updateUIForVariant(variant)`, add a call to `updateCrossSellVariant(variant)`.

Then define the function earlier in the script (before the change listener, after the variable declarations at the top):

```js
    /* ── Cross-sell checkbox: update variant on color change ── */
    function updateCrossSellVariant(variant) {
      var row = root.querySelector('[data-lusena-cross-sell-row]');
      if (!row) return;
      var checkbox = row.querySelector('[data-lusena-cross-sell-checkbox]');
      if (!checkbox) return;

      var mainColorIndex = parseInt(row.dataset.mainColorIndex) || 0;
      var selectedColor = mainColorIndex > 0 ? variant['option' + mainColorIndex] : null;

      var jsonEl = row.querySelector('[data-lusena-cross-sell-variants]');
      if (!jsonEl) return;
      var variants = JSON.parse(jsonEl.textContent);

      var matched = null;
      var highestInv = null;

      for (var i = 0; i < variants.length; i++) {
        var v = variants[i];
        if (!v.available) continue;
        if (selectedColor && v.color === selectedColor && !matched) matched = v;
        if (!highestInv || v.inventory > highestInv.inventory) highestInv = v;
      }

      var chosen = matched || highestInv || variants[0];
      if (!chosen) return;

      checkbox.dataset.variantId = String(chosen.id);

      var colorLabel = row.querySelector('[data-lusena-cross-sell-color-label]');
      if (colorLabel) colorLabel.textContent = 'Kolor: ' + chosen.color;

      var img = row.querySelector('[data-lusena-cross-sell-image]');
      if (img && chosen.image) img.src = chosen.image;
    }
```

- [ ] **Step 2: Add the form submit intercept for dual-item ATC**

Find the existing form submit listener (~line 1406):
```js
    if (addToCartFormEl) {
      addToCartFormEl.addEventListener('submit', () => {
```

BEFORE this block, add the cross-sell intercept with `capture: true`:

```js
    /* ── Cross-sell checkbox: intercept ATC to add both items ── */
    if (addToCartFormEl) {
      addToCartFormEl.addEventListener('submit', function(event) {
        var checkbox = root.querySelector('[data-lusena-cross-sell-checkbox]');
        if (!checkbox || !checkbox.checked) return;

        event.preventDefault();
        event.stopImmediatePropagation();

        var mainId = parseInt(variantIdInput.value);
        var crossSellId = parseInt(checkbox.dataset.variantId);
        if (!mainId || !crossSellId) return;

        var productFormEl = addToCartFormEl.closest('product-form');
        if (productFormEl) productFormEl.classList.add('loading');
        setStickyLoadingState(true);
        stickyLoadingStartedAt = performance.now();

        fetch(window.routes.cart_add_url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
          },
          body: JSON.stringify({
            items: [
              { id: mainId, quantity: 1 },
              { id: crossSellId, quantity: 1 }
            ]
          })
        })
        .then(function(res) { return res.json(); })
        .then(function(data) {
          if (data.status) {
            publish(PUB_SUB_EVENTS.cartError, {
              source: 'product-form',
              productVariantId: mainId,
              errors: data.description || data.message
            });
            if (productFormEl) productFormEl.classList.remove('loading');
            setStickyLoadingState(false);
            return;
          }
          publish(PUB_SUB_EVENTS.cartUpdate, {
            source: 'product-form',
            productVariantId: mainId,
            cartData: data
          });
          var elapsed = performance.now() - stickyLoadingStartedAt;
          var minMs = parseInt(addToCartFormEl.dataset.loadingMinMs) || 500;
          var holdMs = parseInt(addToCartFormEl.dataset.loadingHoldMs) || 350;
          var remaining = Math.max(0, (minMs + holdMs) - elapsed);
          setTimeout(function() {
            if (productFormEl) productFormEl.classList.remove('loading');
            setStickyLoadingState(false);
          }, remaining);
        })
        .catch(function() {
          if (productFormEl) productFormEl.classList.remove('loading');
          setStickyLoadingState(false);
        });
      }, { capture: true });
    }
```

Key behavior: when checkbox is unchecked, the handler returns early and the event propagates normally to `product-form.js`. When checked, it prevents propagation and handles everything.

- [ ] **Step 3: Modify the Buy Now handler to include cross-sell**

Find the Buy Now click handler (~line 1439):
```js
      buyNowButton.addEventListener('click', async (event) => {
```

Inside this handler, after `const variantId = variantIdInput?.value;` (~line 1447), add the cross-sell check and modify the fetch to use items array when checked:

Find the section that builds config and FormData (~lines 1453-1461):
```js
        const config = fetchConfig('javascript');
        config.headers['X-Requested-With'] = 'XMLHttpRequest';
        delete config.headers['Content-Type'];

        const formData = addToCartFormEl ? new FormData(addToCartFormEl) : new FormData();
        formData.set('id', variantId);
        if (!formData.get('quantity')) formData.set('quantity', '1');

        config.body = formData;
```

Replace with:
```js
        const crossSellCheckbox = root.querySelector('[data-lusena-cross-sell-checkbox]');
        const crossSellChecked = crossSellCheckbox && crossSellCheckbox.checked;
        const crossSellVariantId = crossSellChecked ? crossSellCheckbox.dataset.variantId : null;

        let config;
        if (crossSellChecked && crossSellVariantId) {
          config = {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({
              items: [
                { id: parseInt(variantId), quantity: 1 },
                { id: parseInt(crossSellVariantId), quantity: 1 }
              ]
            })
          };
        } else {
          config = fetchConfig('javascript');
          config.headers['X-Requested-With'] = 'XMLHttpRequest';
          delete config.headers['Content-Type'];

          const formData = addToCartFormEl ? new FormData(addToCartFormEl) : new FormData();
          formData.set('id', variantId);
          if (!formData.get('quantity')) formData.set('quantity', '1');
          config.body = formData;
        }
```

The rest of the Buy Now handler (fetch, redirect to checkout) stays the same — it doesn't care about the body format.

- [ ] **Step 4: Run theme check**

Run: `shopify theme check`
Expected: Only known baseline warnings.

- [ ] **Step 5: Commit**

```
git add snippets/lusena-pdp-scripts.liquid
git commit -m "feat(lusena): cross-sell JS - ATC intercept, Buy Now, variant change"
```

---

### Task 5: Configuration + verification

**Files:**
- Modify: `templates/product.json` (via theme editor — sets the cross-sell product)

- [ ] **Step 1: Configure cross-sell product via theme editor**

Open the Shopify theme editor (or dev server customizer) for the product template. In the `lusena-main-product` section settings:
1. Enable "Pokazuj checkbox cross-sell w buy-boxie" (should be on by default)
2. Set "Produkt cross-sell" to "Scrunchie jedwabny"
3. Set "Cena cross-sell (grosze)" to `3900`

Save. This writes the product GID to `templates/product.json`.

- [ ] **Step 2: Verify checkbox appears on poszewka PDP**

Navigate to the poszewka PDP on dev server (`http://127.0.0.1:9292/products/poszewka-jedwabna`).

Verify:
- Checkbox row appears between variant picker and ATC button
- Shows scrunchie product image
- Shows "Dodaj scrunchie jedwabny"
- Shows "39 zl" with "59 zl" crossed out
- Shows "Kolor: {matching color}"
- Checkbox is unchecked by default

- [ ] **Step 3: Test color matching**

On the poszewka PDP, change the color swatch (e.g., from Czarny to Brudny roz).

Verify:
- The cross-sell color label updates to match
- The variant ID in `data-variant-id` updates (inspect element)

- [ ] **Step 4: Test ATC with checkbox checked**

1. Check the cross-sell checkbox
2. Click "Dodaj do koszyka"

Verify:
- Both items appear in the cart drawer
- Poszewka at 269 zl
- Scrunchie at 59 zl with BXGY discount showing (39 zl effective)
- Loading state shows and releases properly

- [ ] **Step 5: Test ATC with checkbox unchecked**

1. Clear cart
2. Leave checkbox unchecked
3. Click "Dodaj do koszyka"

Verify:
- Only the poszewka appears in cart
- Normal ATC flow unchanged

- [ ] **Step 6: Test Buy Now with checkbox checked**

1. Clear cart
2. Check the cross-sell checkbox
3. Click "Kup teraz"

Verify:
- Redirects to checkout
- Both items present in checkout

- [ ] **Step 7: Test sticky ATC**

1. Clear cart
2. Scroll down past the main ATC button (sticky bar appears)
3. Check the cross-sell checkbox (scroll back up briefly)
4. Scroll down and click the sticky ATC button

Verify:
- Both items added to cart

- [ ] **Step 8: Test scope rules**

Navigate to each PDP and verify checkbox visibility:

| URL | Expected |
|-----|----------|
| `/products/poszewka-jedwabna` | Checkbox visible |
| `/products/czepek-jedwabny` | Checkbox visible |
| `/products/jedwabna-maska-3d` | Checkbox visible |
| `/products/walek-do-lokow` | Checkbox visible |
| `/products/scrunchie-jedwabny` | Checkbox HIDDEN (self-exclusion) |
| `/products/nocna-rutyna` | Checkbox HIDDEN (bundle template) |
| `/products/piekny-sen` | Checkbox HIDDEN (bundle template) |
| `/products/scrunchie-trio` | Checkbox HIDDEN (bundle template) |

- [ ] **Step 9: Run theme check**

Run: `shopify theme check`
Expected: Only known baseline warnings.

- [ ] **Step 10: Commit configuration**

```
git add templates/product.json
git commit -m "feat(lusena): configure cross-sell product (scrunchie at 39 zl)"
```

---

### Task 6: Documentation updates

**Files:**
- Modify: `memory-bank/activeContext.md`
- Modify: `memory-bank/progress.md`
- Modify: `.claude/rules/bundle-system.md` — update threshold 289 → 275
- Modify: `memory-bank/doc/bundle-strategy.md` — update threshold references

- [ ] **Step 1: Update bundle-system rule**

In `.claude/rules/bundle-system.md`, update the free shipping threshold from 289 to 275 and update the cross-sell rules to reflect "all individual PDPs":

```
- Free shipping threshold: 275 zl
- Scrunchie cross-sell at 39 zl on ALL individual product PDPs (not just poszewka)
- Poszewka (269) + scrunchie (39) = 308 zl, clears 275 threshold
- Bonnet (239) + scrunchie (39) = 278 zl, clears 275 threshold
```

- [ ] **Step 2: Update activeContext.md**

Move "Phase 1B: PDP cross-sell checkbox" from "Next steps" to "Recent completed work". Add a summary of what was built and the strategic decisions (all PDPs, 275 threshold).

- [ ] **Step 3: Update progress.md**

Add to the "Infrastructure completed" section:
- PDP cross-sell checkbox (snippet, JS intercept, color matching, all individual PDPs)
- Free shipping threshold changed from 289 → 275 zl

Mark "Phase D: Cross-sell" items as complete.

- [ ] **Step 4: Update bundle-strategy.md threshold references**

Replace all references to "289 zl" threshold with "275 zl" in `memory-bank/doc/bundle-strategy.md`. Update the "Free shipping threshold" section heading and the cart-combo tables to reflect:
- Threshold: 275 zl (changed from 289)
- Cross-sell: all individual PDPs (changed from poszewka-only)

- [ ] **Step 5: Commit documentation**

```
git add memory-bank/ .claude/rules/bundle-system.md
git commit -m "docs: update memory bank + rules for cross-sell checkbox + 275 zl threshold"
```
