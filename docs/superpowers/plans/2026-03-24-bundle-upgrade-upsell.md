# Bundle Upgrade Upsell (S2 + #11) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** When a bundle component (poszewka, bonnet, maska) is in the cart, show a bundle upgrade upsell that **swaps** the individual product for the bundle — not adds alongside it.

**Architecture:** The existing cart upsell waterfall (Liquid) already resolves bundle products via `upsell_primary` metafields. We add: (1) a conditional "Uzupelnij do zestawu" label when the resolved upsell has `upsell_role == 'bundle'`, (2) a `data-upsell-replaces` attribute carrying the trigger item's cart key, (3) JS swap logic that chains `/cart/add.js` + `/cart/change.js` before refreshing, and (4) a relaxed suppress rule that allows bundle upsells even with 2+ distinct items in cart.

**Tech Stack:** Shopify Liquid, vanilla JS, Shopify Cart API (`/cart/add.js`, `/cart/change.js`), Dawn's `product-form.js` + `cart-drawer.js` custom elements, Shopify Sections Rendering API.

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `snippets/cart-drawer.liquid` | Modify | Liquid: label, data attrs, smart suppress. JS: swap intercept in drawer upsell. |
| `sections/lusena-cart-items.liquid` | Modify | Liquid: label, data attrs, smart suppress. JS: swap intercept in cart page upsell. |

No new files. Both surfaces (drawer + page) are self-contained with inline JS.

---

## Current Flow (before changes)

**Cart Drawer upsell "Dodaj" click:**
```
click <button type="submit"> inside <product-form data-cart-upsell>
  -> product-form.js: onSubmitHandler()
  -> fetch POST /cart/add (with sections=[cart-drawer, cart-icon-bubble])
  -> publish PUB_SUB_EVENTS.cartUpdate
  -> cart-drawer.renderContents(response)  // replaces #CartDrawer innerHTML
  -> upsell success overlay (sessionStorage bridge)
```

**Cart Page upsell "Dodaj" click:**
```
click <button data-cart-page-upsell-add data-variant-id="...">
  -> event delegation on #main-cart-items
  -> fetch POST /cart/add.js (JSON body)
  -> window.location.reload()
```

## Target Flow (after changes)

**Cart Drawer — bundle swap:**
```
click <button type="submit"> inside <product-form data-cart-upsell data-upsell-replaces="KEY">
  -> drawer submit listener intercepts BEFORE product-form.js
  -> e.preventDefault() + e.stopPropagation()
  -> fetch POST /cart/add.js (bundle variant)
  -> fetch POST /cart/change.js (trigger item key, quantity: 0)
  -> fetch GET /?sections=cart-drawer,cart-icon-bubble
  -> drawer.renderContents(sectionsResponse)
  -> upsell success overlay
```

**Cart Page — bundle swap:**
```
click <button data-cart-page-upsell-add data-variant-id="..." data-upsell-replaces="KEY">
  -> event delegation detects data-upsell-replaces
  -> fetch POST /cart/add.js (bundle variant)
  -> fetch POST /cart/change.js (trigger item key, quantity: 0)
  -> window.location.reload()
```

---

## Task 1: Liquid — Smart Suppress Rule (both files)

**Files:**
- Modify: `snippets/cart-drawer.liquid` — the `{%- liquid ... -%}` header block (lines 10-104)
- Modify: `sections/lusena-cart-items.liquid` — the `{%- liquid ... -%}` header block (lines 12-94)

The current code sets `suppress_upsell = true` when `distinct_count >= 2`, which prevents bundle upsells from showing when the customer has 2+ items. We need to split this into "hard suppress" (bundle in cart, explicit suppress) vs "soft suppress" (distinct count — only blocks non-bundle upsells).

### Current logic (both files):
```liquid
assign suppress_upsell = false
if distinct_count >= suppress_distinct_threshold
  assign suppress_upsell = true
endif
for item in cart.items
  if item.product.metafields.lusena.upsell_suppress == true or item.product.metafields.lusena.upsell_role == 'bundle'
    assign suppress_upsell = true
    break
  endif
endfor
```

### Target logic (both files):
```liquid
assign suppress_upsell = false
for item in cart.items
  if item.product.metafields.lusena.upsell_suppress == true or item.product.metafields.lusena.upsell_role == 'bundle'
    assign suppress_upsell = true
    break
  endif
endfor
```
Then AFTER the upsell candidate is resolved:
```liquid
comment
  Soft suppress: 2+ distinct items blocks cross-sells but allows bundle upgrades.
  This lets "Uzupelnij do zestawu" show even when cart has 2 items.
endcomment
if distinct_count >= suppress_distinct_threshold and upsell_product != blank
  if upsell_product.metafields.lusena.upsell_role != 'bundle'
    assign upsell_product = blank
  endif
endif
```

- [ ] **Step 1:** In `snippets/cart-drawer.liquid`, remove the `distinct_count >= suppress_distinct_threshold` block from the initial suppress logic. The variable name is `upsell_product_1` in this file.

- [ ] **Step 2:** In `snippets/cart-drawer.liquid`, add the soft suppress check AFTER the upsell candidate resolution (after the `endif` that closes the waterfall). Check `upsell_product_1.metafields.lusena.upsell_role`.

- [ ] **Step 3:** Repeat steps 1-2 in `sections/lusena-cart-items.liquid`. The variable name is `upsell_product` in this file.

- [ ] **Step 4:** Validate both files with `mcp__shopify-dev-mcp__validate_theme`.

---

## Task 2: Liquid — Conditional Label + Data Attributes (both files)

**Files:**
- Modify: `snippets/cart-drawer.liquid` — upsell card HTML (~line 852+)
- Modify: `sections/lusena-cart-items.liquid` — upsell card HTML (~line 270+)

### 2A: Conditional label

Replace the hardcoded "Pasuje do" label with a conditional:
```liquid
{%- assign upsell_is_bundle = false -%}
{%- if upsell_product.metafields.lusena.upsell_role == 'bundle' -%}
  {%- assign upsell_is_bundle = true -%}
{%- endif -%}
<p class="...label">{{ upsell_is_bundle | if: 'Uzupełnij do zestawu', 'Pasuje do' }}</p>
```

Note: Liquid doesn't have a ternary. Use `{% if %}`:
```liquid
<p class="...label">
  {%- if upsell_is_bundle -%}Uzupełnij do zestawu{%- else -%}Pasuje do{%- endif -%}
</p>
```

### 2B: `data-upsell-replaces` attribute

**Cart drawer:** Add to the `<form>` element inside `<product-form>`:
```liquid
{%- form 'product', upsell_product_1,
  id: 'CartDrawer-Upsell-Form-1',
  class: 'form',
  novalidate: 'novalidate',
  data-type: 'add-to-cart-form'
-%}
```
Liquid's `form` tag doesn't support arbitrary data attributes directly. Instead, add to the `<product-form>` wrapper:
```liquid
<product-form
  class="product-form"
  data-hide-errors="true"
  data-cart-upsell
  {% if upsell_is_bundle %}data-upsell-replaces="{{ trigger_item.key | escape }}"{% endif %}
>
```

**Cart page:** Add to the `<button>`:
```liquid
<button
  type="button"
  class="lusena-btn lusena-btn--outline lusena-btn--size-xs"
  data-cart-page-upsell-add
  data-variant-id="{{ upsell_variant.id }}"
  {% if upsell_is_bundle %}data-upsell-replaces="{{ trigger_item.key | escape }}"{% endif %}
>
```

- [ ] **Step 1:** In `snippets/cart-drawer.liquid`, add `upsell_is_bundle` assignment in the Liquid block (after upsell candidate is resolved, near the display variables). Change the label. Add `data-upsell-replaces` to `<product-form>`.

- [ ] **Step 2:** In `sections/lusena-cart-items.liquid`, add `upsell_is_bundle` assignment. Change the label. Add `data-upsell-replaces` to the `<button>`.

- [ ] **Step 3:** Validate both files with `mcp__shopify-dev-mcp__validate_theme`.

---

## Task 3: JS — Swap Logic in Cart Drawer

**File:** `snippets/cart-drawer.liquid` — the inline `<script>` block (~lines 1052-1250)

The existing submit listener (line 1193) already intercepts form submits inside the drawer. We need to add swap detection BEFORE `product-form.js` processes the submit.

### Implementation

Inside the existing `drawer.addEventListener('submit', function(e) {...})`, at the top (before `markPendingUpsell`):

```js
// Check if this is a bundle swap upsell
var upsellForm = form.closest('[data-cart-upsell][data-upsell-replaces]');
if (upsellForm) {
  e.preventDefault();
  e.stopImmediatePropagation(); // prevent product-form.js from also handling

  var bundleVariantId = variantInput.value;
  var replaceKey = upsellForm.dataset.upsellReplaces;
  var submitBtn = form.querySelector('[type="submit"]');

  // Show loading state
  if (submitBtn) {
    submitBtn.disabled = true;
    var content = submitBtn.querySelector('.lusena-btn__content');
    var spinner = submitBtn.querySelector('.loading__spinner');
    if (content) content.classList.add('hidden');
    if (spinner) spinner.classList.remove('hidden');
  }

  swapToBundle(bundleVariantId, [replaceKey])
    .then(function() {
      markPendingUpsell(bundleVariantId);
      writeUpsellAddedFlag();
    })
    .catch(function(err) {
      console.error('Bundle swap failed:', err);
      if (submitBtn) {
        submitBtn.disabled = false;
        if (content) content.classList.remove('hidden');
        if (spinner) spinner.classList.add('hidden');
      }
    });

  return;
}
```

### The `swapToBundle` function (shared helper, defined in the same IIFE):

```js
async function swapToBundle(bundleVariantId, removeKeys) {
  // 1. Add the bundle
  var addRes = await fetch('/cart/add.js', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ items: [{ id: parseInt(bundleVariantId), quantity: 1 }] })
  });
  if (!addRes.ok) throw new Error('Failed to add bundle');

  // 2. Remove individual item(s)
  for (var i = 0; i < removeKeys.length; i++) {
    var changeRes = await fetch('/cart/change.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: removeKeys[i], quantity: 0 })
    });
    if (!changeRes.ok) throw new Error('Failed to remove item ' + removeKeys[i]);
  }

  // 3. Fetch updated sections for drawer re-render
  var sectionsParam = drawer.getSectionsToRender
    ? drawer.getSectionsToRender().map(function(s) { return s.id || s.section; }).join(',')
    : 'cart-drawer,cart-icon-bubble';

  var sectionsRes = await fetch('/?sections=' + sectionsParam);
  var sectionsData = await sectionsRes.json();

  // 4. Re-render the drawer
  var parsedState = { sections: sectionsData };
  drawer.renderContents(parsedState);
}
```

- [ ] **Step 1:** Add the `swapToBundle` function inside the existing IIFE, before the event listeners.

- [ ] **Step 2:** Modify the existing `drawer.addEventListener('submit', ...)` to check for `[data-upsell-replaces]` at the top and run swap logic if found. The existing `markPendingUpsell` flow handles the success overlay.

- [ ] **Step 3:** Validate with `mcp__shopify-dev-mcp__validate_theme`.

---

## Task 4: JS — Swap Logic in Cart Page

**File:** `sections/lusena-cart-items.liquid` — the inline `<script>` block (~lines 411-441)

The existing click handler checks for `[data-cart-page-upsell-add]`. We add a check for `data-upsell-replaces` on the same button.

### Implementation

Inside the existing click handler, after getting `btn`:

```js
var btn = e.target.closest('[data-cart-page-upsell-add]');
if (!btn || btn.disabled) return;

btn.disabled = true;
// show loading, hide text (existing code)

var replaceKey = btn.dataset.upsellReplaces;

try {
  // Add the new product (bundle or regular)
  var addRes = await fetch('/cart/add.js', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ items: [{ id: parseInt(btn.dataset.variantId), quantity: 1 }] })
  });
  if (!addRes.ok) throw new Error('Add failed');

  // If bundle swap, remove the individual item
  if (replaceKey) {
    var changeRes = await fetch('/cart/change.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: replaceKey, quantity: 0 })
    });
    if (!changeRes.ok) throw new Error('Remove failed');
  }

  window.location.reload();
} catch (e) {
  // existing error handling
}
```

- [ ] **Step 1:** Read the existing inline JS in `lusena-cart-items.liquid` to get the exact code.

- [ ] **Step 2:** Modify the click handler to read `data-upsell-replaces`, and if present, chain a `/cart/change.js` call after the add. The `window.location.reload()` happens after both calls complete.

- [ ] **Step 3:** Validate with `mcp__shopify-dev-mcp__validate_theme`.

---

## Task 5: Verification

**Prerequisites:** Dev server running (`shopify theme dev`), products configured with upsell metafields.

- [ ] **Step 1: Bundle upgrade shows correct label.** Add poszewka to cart. Open cart drawer. Verify upsell shows "Uzupelnij do zestawu" (not "Pasuje do") with Nocna Rutyna as the upsell product.

- [ ] **Step 2: Swap works in drawer.** Click "Dodaj" on the Nocna Rutyna upsell. Verify: poszewka is REMOVED from cart, Nocna Rutyna bundle is ADDED. Cart total should be 399 zl (not 269 + 399 = 668).

- [ ] **Step 3: Regular cross-sell still works.** Add curlers to cart. Verify upsell shows "Pasuje do" with scrunchie. Click "Dodaj". Verify scrunchie is ADDED alongside curlers (no swap). Cart total = 219 + 59 = 278.

- [ ] **Step 4: Smart suppress allows bundles with 2 items.** Add poszewka + scrunchie to cart (2 distinct items). Verify: bundle upsell (Nocna Rutyna) still shows with "Uzupelnij do zestawu" label.

- [ ] **Step 5: Cart page mirror.** Navigate to `/cart`. Verify same label, same swap behavior, same suppress rules as the drawer.

- [ ] **Step 6: Color matching.** Add Brudny roz poszewka. Verify the Nocna Rutyna upsell shows the Brudny roz variant (not Czarny).

---

## Edge Cases to Watch

| Scenario | Expected behavior |
|---|---|
| Bundle product is out of stock | Waterfall falls to secondary (Piekny Sen or scrunchie) |
| Trigger item is the only item in cart | Normal swap — cart goes from 1 individual to 1 bundle |
| Both bundle components in cart (poszewka + bonnet) | Smart suppress allows bundle upsell. Swap removes trigger only. Second item stays. #13 (cart merge, future) will handle this better. |
| Bundle already in cart (Nocna Rutyna) | Hard suppress — no upsell shown (upsell_role = 'bundle' triggers suppress) |
| Scrunchie Trio as upsell for scrunchie | NOT a swap (Scrunchie Trio has no `upsell_role = 'bundle'`). Regular "Pasuje do" + add behavior. |
