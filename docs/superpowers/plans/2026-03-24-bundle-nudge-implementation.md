# Bundle Nudge Component — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `lusena-bundle-nudge` snippet and `lusena-bundle-swap.js` shared file, then refactor cart drawer and cart page to use them — replacing the current inline bundle swap code.

**Architecture:** Visual snippet (`lusena-bundle-nudge.liquid`) renders the upgrade card with pricing. Shared JS (`lusena-bundle-swap.js`) exposes `window.LusenaBundle.swap()`. Each parent (cart drawer, cart page) computes data from metafields, renders the snippet, and wires a click handler that calls the shared swap function. CSS lives in `lusena-foundations.css`.

**Tech Stack:** Shopify Liquid, vanilla JS, Shopify Cart API, Dawn custom elements.

**Spec:** `docs/superpowers/specs/2026-03-24-bundle-nudge-design.md`

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `assets/lusena-bundle-swap.js` | Create | Shared swap: add bundle + remove individual via Cart API |
| `snippets/lusena-bundle-nudge.liquid` | Create | Visual nudge card with pricing, data attributes, loading state |
| `assets/lusena-foundations.css` | Modify | Add `.lusena-bundle-nudge` component styles (~30-40 lines) |
| `snippets/cart-drawer.liquid` | Modify | Render nudge snippet for bundles, new click handler, delete old swap code |
| `sections/lusena-cart-items.liquid` | Modify | Same changes mirrored for cart page |

---

## Task 1: Create `assets/lusena-bundle-swap.js`

**Files:**
- Create: `assets/lusena-bundle-swap.js`

- [ ] **Step 1: Create the shared swap JS file**

```js
/**
 * LUSENA Bundle Swap — shared cart API logic for bundle upgrades.
 *
 * Usage:
 *   var state = await LusenaBundle.swap(bundleVariantId, [removeKey], { sections: [...] });
 *
 * - Adds the bundle variant via /cart/add.js
 * - Removes individual item(s) via /cart/change.js
 * - Last removal includes `sections` param (if provided) for re-render data
 * - Returns parsed JSON response from the last /cart/change.js call
 * - Throws on failure — caller handles errors and UI
 */
window.LusenaBundle = {
  async swap(bundleVariantId, removeKeys, options) {
    var addRes = await fetch('/cart/add.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ items: [{ id: parseInt(bundleVariantId), quantity: 1 }] })
    });
    if (!addRes.ok) throw new Error('Failed to add bundle');

    var lastIdx = removeKeys.length - 1;
    var lastState = null;
    for (var i = 0; i < removeKeys.length; i++) {
      var body = { id: removeKeys[i], quantity: 0 };
      if (i === lastIdx && options && options.sections) {
        body.sections = options.sections;
      }
      var changeRes = await fetch('/cart/change.js', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      });
      if (!changeRes.ok) throw new Error('Failed to remove item');
      if (i === lastIdx) {
        lastState = await changeRes.json();
      }
    }

    return lastState;
  }
};
```

- [ ] **Step 2: Verify the file exists and is valid JS**

Run: `node -c assets/lusena-bundle-swap.js` — should print "ok" (syntax check only).

---

## Task 2: Create `snippets/lusena-bundle-nudge.liquid`

**Files:**
- Create: `snippets/lusena-bundle-nudge.liquid`

**Context:** This snippet is a pure visual component. It accepts parameters and renders the nudge card HTML. No JS inside. The parent computes all data before calling `{% render %}`.

- [ ] **Step 1: Create the snippet**

The snippet must include:
- A `{% doc %}` LiquidDoc header documenting all parameters
- The nudge card HTML with data attributes for JS
- Fallback: if `added_label` is blank, show "Uzupelnij do zestawu" instead
- Conditional: if `original_total_cents` is 0 or blank, hide the "zam." price
- Prices formatted with `| money_without_trailing_zeros`
- `aria-label="Propozycja zestawu"` on the container
- Loading spinner inside the button (`.loading__spinner` + `.lusena-btn__loading-dots` pattern)

Full snippet content:

```liquid
{% doc %}
  Renders a bundle upgrade nudge card with pricing math and swap action.

  @param {string} [added_label] - "czepek jedwabny" — item being added. Blank shows fallback headline.
  @param {string} bundle_name - "Nocna Rutyna" — bundle product title
  @param {number} bundle_price_cents - Bundle variant price in cents (e.g. 39900)
  @param {number} [original_total_cents] - Sum of components at full price, in cents (e.g. 50800). 0 hides "zam." line.
  @param {number} incremental_cents - Extra cost to customer in cents (bundle - trigger price)
  @param {number} bundle_variant_id - Variant ID for /cart/add.js
  @param {string} replace_key - Cart line item key for /cart/change.js removal

  @example
  {% render 'lusena-bundle-nudge',
    added_label: "czepek jedwabny",
    bundle_name: "Nocna Rutyna",
    bundle_price_cents: 39900,
    original_total_cents: 50800,
    incremental_cents: 13000,
    bundle_variant_id: variant.id,
    replace_key: trigger_item.key
  %}
{% enddoc %}

<div class="lusena-bundle-nudge"
     data-bundle-nudge
     data-bundle-variant-id="{{ bundle_variant_id }}"
     data-replace-key="{{ replace_key | escape }}"
     aria-label="Propozycja zestawu">
  <p class="lusena-bundle-nudge__added">
    {%- if added_label != blank -%}
      Dodaj {{ added_label }} do zestawu
    {%- else -%}
      Uzupełnij do zestawu
    {%- endif -%}
  </p>
  <p class="lusena-bundle-nudge__pricing">
    {{ bundle_name }}
    · <strong>{{ bundle_price_cents | money_without_trailing_zeros }}</strong>
    {%- if original_total_cents != blank and original_total_cents > 0 -%}
      <span class="lusena-bundle-nudge__was">zam. {{ original_total_cents | money_without_trailing_zeros }}</span>
    {%- endif -%}
  </p>
  <button type="button"
          class="lusena-btn lusena-btn--primary lusena-btn--size-sm"
          data-bundle-nudge-action>
    <span class="lusena-btn__content">Dodaj do zestawu · +{{ incremental_cents | money_without_trailing_zeros }}</span>
    <span class="loading__spinner hidden">
      <span class="lusena-btn__loading-dots" aria-hidden="true">
        <span></span><span></span><span></span>
      </span>
    </span>
  </button>
</div>
```

- [ ] **Step 2: Validate with Shopify Theme Check**

Run: `mcp__shopify-dev-mcp__validate_theme` with conversationId `86a3f6e0-ebd9-4650-a202-f6d24a8d7d13`, path `snippets/lusena-bundle-nudge.liquid`.

---

## Task 3: Add nudge CSS to `assets/lusena-foundations.css`

**Files:**
- Modify: `assets/lusena-foundations.css` (add at end, before any closing comment)

**Context:** Follow the existing component pattern in this file (`.lusena-accordion`, `.lusena-trust-bar`, etc.). The nudge sits inside existing upsell zones, so it needs only its own internal styling — positioning comes from the parent.

- [ ] **Step 1: Read the end of `lusena-foundations.css`** to find the right insertion point (after the last component block).

- [ ] **Step 2: Add the nudge CSS**

```css
/* ── Bundle nudge ────────────────────────────── */

.lusena-bundle-nudge {
  border: 1px dashed var(--lusena-color-n300);
  border-radius: var(--lusena-btn-radius);
  padding: var(--lusena-space-1) var(--lusena-space-2);
  margin-top: var(--lusena-space-1);
}

.lusena-bundle-nudge__added {
  font-family: var(--lusena-font-ui);
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--lusena-text-1);
  margin: 0 0 0.4rem 0;
}

.lusena-bundle-nudge__pricing {
  font-family: var(--lusena-font-ui);
  font-size: 1.2rem;
  color: var(--lusena-text-2);
  margin: 0 0 var(--lusena-space-1) 0;
}

.lusena-bundle-nudge__was {
  text-decoration: line-through;
  opacity: 0.65;
}

.lusena-bundle-nudge .lusena-btn {
  width: 100%;
}
```

Design tokens used: `--lusena-color-n300` (border), `--lusena-btn-radius` (6px), `--lusena-space-1`/`--lusena-space-2`, `--lusena-text-1`/`--lusena-text-2` (colors), `--lusena-font-ui` (Inter). All defined in `lusena-foundations.css` `:root`. Append at the end of the file.

- [ ] **Step 3: Verify the file is valid CSS** — no syntax errors after insertion.

---

## Task 4: Refactor cart drawer to use nudge snippet + shared swap

**Files:**
- Modify: `snippets/cart-drawer.liquid`

**Context:** This is the largest task. The file currently has:
- A conditional bundle vs non-bundle upsell card (Liquid, ~line 940-1010)
- An inline `swapToBundle` async function (~line 1178-1206)
- A click listener for `[data-cart-upsell] button[type="button"]` (~line 1246-1279)

All three need to change. The cross-sell (non-bundle) upsell path stays unchanged.

### Liquid changes

- [ ] **Step 1: Read the current upsell card HTML** in `snippets/cart-drawer.liquid`. Find the `{%- if upsell_is_bundle -%}` block that renders the bundle `<div data-cart-upsell>` card.

- [ ] **Step 2: Replace the bundle upsell card HTML** with the nudge snippet render, including the script load tag. The `<script>` tag goes inside the `{%- if upsell_is_bundle -%}` block (where the variable is available). Replace the entire `{%- if upsell_is_bundle -%}...{%- else -%}` bundle path with:

```liquid
{%- if upsell_is_bundle -%}
  <script src="{{ 'lusena-bundle-swap.js' | asset_url }}" defer="defer"></script>
  {%- assign nudge_map = upsell_product_1.metafields.lusena.bundle_nudge_map.value -%}
  {%- assign added_label = nudge_map[trigger_product.handle] -%}
  {%- assign bundle_price_cents = upsell_variant_1.price -%}
  {%- assign original_total_cents = upsell_product_1.metafields.lusena.bundle_original_price.value | times: 100 -%}
  {%- assign incremental_cents = bundle_price_cents | minus: trigger_item.variant.price -%}

  {%- render 'lusena-bundle-nudge',
    added_label: added_label,
    bundle_name: upsell_product_1.title,
    bundle_price_cents: bundle_price_cents,
    original_total_cents: original_total_cents,
    incremental_cents: incremental_cents,
    bundle_variant_id: upsell_variant_1.id,
    replace_key: trigger_item.key
  -%}
{%- else -%}
```

Keep the `{%- else -%}` and everything after it (the non-bundle cross-sell card) unchanged.

### JS changes

- [ ] **Step 4: Delete the inline `swapToBundle` function.** Find `async function swapToBundle(bundleVariantId, removeKeys)` in the IIFE and delete the entire function (~28 lines). This is replaced by `LusenaBundle.swap()` from the shared JS file.

- [ ] **Step 5: Replace the old bundle click listener** with the new nudge click handler. Find the existing `drawer.addEventListener('click', function(e) {` that targets `[data-cart-upsell] button[type="button"]` and replace with the handler below. **Important:** The new handler deliberately omits `markPendingUpsell` / `writeUpsellAddedFlag` — the bundle nudge bypasses the success overlay entirely (per spec: drawer re-render is the confirmation). The existing success overlay functions stay for the cross-sell path.

```js
// Bundle nudge: click handler using shared LusenaBundle.swap()
drawer.addEventListener('click', function(e) {
  var btn = e.target.closest('[data-bundle-nudge-action]');
  if (!btn) return;

  var nudge = btn.closest('[data-bundle-nudge]');
  if (!nudge) return;

  btn.disabled = true;
  var content = btn.querySelector('.lusena-btn__content');
  var spinner = btn.querySelector('.loading__spinner');
  if (content) content.classList.add('hidden');
  if (spinner) spinner.classList.remove('hidden');

  var sections = drawer.getSectionsToRender().map(function(s) { return s.id || s.section; });

  LusenaBundle.swap(nudge.dataset.bundleVariantId, [nudge.dataset.replaceKey], { sections: sections })
    .then(function(state) {
      drawer.renderContents(state);
    })
    .catch(function(err) {
      console.error('Bundle swap failed:', err);
      btn.disabled = false;
      if (content) content.classList.remove('hidden');
      if (spinner) spinner.classList.add('hidden');
    });
});
```

- [ ] **Step 6: Validate with Shopify Theme Check.**

Run: `mcp__shopify-dev-mcp__validate_theme` with `snippets/cart-drawer.liquid`.

---

## Task 5: Refactor cart page to use nudge snippet + shared swap

**Files:**
- Modify: `sections/lusena-cart-items.liquid`

**Context:** Mirror the cart drawer changes. The cart page has:
- A conditional bundle vs non-bundle upsell card (Liquid, inside `{%- if upsell_product != blank -%}`)
- An inline click handler in a `<script>` block that chains `/cart/add.js` + `/cart/change.js`

### Liquid changes

- [ ] **Step 1: Read the current upsell card HTML** in `sections/lusena-cart-items.liquid`. Find the `{%- if upsell_is_bundle -%}` / `{%- else -%}` pattern. Note: the variable names differ from the drawer: `upsell_product` (not `upsell_product_1`), `upsell_variant` (not `upsell_variant_1`).

- [ ] **Step 2: Replace the bundle upsell path** with the nudge snippet render. Use the same pattern as Task 4 but with cart page variable names:

```liquid
{%- if upsell_is_bundle -%}
  <script src="{{ 'lusena-bundle-swap.js' | asset_url }}" defer="defer"></script>
  {%- assign nudge_map = upsell_product.metafields.lusena.bundle_nudge_map.value -%}
  {%- assign added_label = nudge_map[trigger_product.handle] -%}
  {%- assign bundle_price_cents = upsell_variant.price -%}
  {%- assign original_total_cents = upsell_product.metafields.lusena.bundle_original_price.value | times: 100 -%}
  {%- assign incremental_cents = bundle_price_cents | minus: trigger_item.variant.price -%}

  {%- render 'lusena-bundle-nudge',
    added_label: added_label,
    bundle_name: upsell_product.title,
    bundle_price_cents: bundle_price_cents,
    original_total_cents: original_total_cents,
    incremental_cents: incremental_cents,
    bundle_variant_id: upsell_variant.id,
    replace_key: trigger_item.key
  -%}
{%- else -%}
```

### JS changes

- [ ] **Step 3: Add a nudge click handler** in the existing inline `<script>` block. This runs alongside the existing `[data-cart-page-upsell-add]` handler (which stays for non-bundle upsells). Add BEFORE the existing handler:

```js
// Bundle nudge: click handler using shared LusenaBundle.swap()
container.addEventListener('click', async function(e) {
  var btn = e.target.closest('[data-bundle-nudge-action]');
  if (!btn) return;

  var nudge = btn.closest('[data-bundle-nudge]');
  if (!nudge) return;

  btn.disabled = true;
  var contentEl = btn.querySelector('.lusena-btn__content');
  var spinnerEl = btn.querySelector('.loading__spinner');
  if (contentEl) contentEl.classList.add('hidden');
  if (spinnerEl) spinnerEl.classList.remove('hidden');

  try {
    await LusenaBundle.swap(nudge.dataset.bundleVariantId, [nudge.dataset.replaceKey]);
    window.location.reload();
  } catch (err) {
    console.error('Bundle swap failed:', err);
    btn.disabled = false;
    if (contentEl) contentEl.classList.remove('hidden');
    if (spinnerEl) spinnerEl.classList.add('hidden');
  }
});
```

- [ ] **Step 4: Clean up the old bundle path** in the existing `[data-cart-page-upsell-add]` click handler. The old handler has a `replaceKey` check that chains `/cart/change.js` for bundle swaps. Remove this — bundle clicks are now handled by the new nudge handler above. The old handler should only handle non-bundle adds:

Find and remove the `var replaceKey = btn.dataset.upsellReplaces;` block and the subsequent `if (replaceKey) { ... }` fetch call. The old handler becomes a simple add-only handler again.

- [ ] **Step 5: Validate with Shopify Theme Check.**

Run: `mcp__shopify-dev-mcp__validate_theme` with `sections/lusena-cart-items.liquid`.

---

## Task 6: Verification

**Prerequisites:** Dev server running at `http://127.0.0.1:9292`. Products configured with `upsell_primary`/`upsell_secondary` metafields. `lusena.bundle_nudge_map` metafield set on bundle products (must be done by the owner in Shopify admin before this test).

Use `/playwright-cli` skill with session name `-s=nudge-verify`.

- [ ] **Step 1: Verify nudge card renders.** Navigate to poszewka PDP. Add to cart. Check cart drawer shows the nudge card with: "Dodaj czepek jedwabny do zestawu", pricing line with bundle name + prices, "+130 zl" button.

- [ ] **Step 2: Verify swap works.** Click the nudge button. Verify: poszewka removed from cart, Nocna Rutyna added, drawer re-renders showing bundle at 399 zl, no JS errors in console.

- [ ] **Step 3: Verify non-bundle cross-sell unchanged.** Clear cart. Add curlers. Check drawer shows "Pasuje do" with scrunchie (old card style, not nudge). Click "Dodaj". Verify scrunchie added alongside curlers (regular add, no swap).

- [ ] **Step 4: Verify cart page.** Navigate to `/cart`. If a bundle upsell is showing, verify same nudge card and swap behavior with page reload.

- [ ] **Step 5: Verify smart suppress.** Add poszewka + scrunchie to cart (2 distinct items). Verify bundle nudge still shows (smart suppress allows bundles).

---

## Admin Prerequisite (owner action, not code)

Before Task 6 verification, the owner must create the `lusena.bundle_nudge_map` metafield definition (type: json) in Shopify admin and set values on each bundle product:

**Nocna Rutyna:**
```json
{"poszewka-jedwabna": "czepek jedwabny", "silk-bonnet": "poszewkę jedwabną"}
```

**Piekny Sen:**
```json
{"poszewka-jedwabna": "maskę 3D", "jedwabna-maska-3d": "poszewkę jedwabną"}
```

**Scrunchie Trio:**
```json
{"silk-scrunchie": "dwie kolejne jedwabne gumki"}
```

After setting metafields, update `docs/product-metafields-reference.md` with the new `lusena.bundle_nudge_map` definition (type: json, purpose: maps trigger product handle to added item label for nudge card).
