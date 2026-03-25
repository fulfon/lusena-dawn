# Bundle Nudge Component — Design Spec

**Date:** 2026-03-24
**Status:** Approved

## Goal

A reusable bundle upgrade nudge that shows the specific added product, savings math, and incremental cost. Handles the swap (add bundle, remove individual) via shared JS logic. Used in cart drawer and cart page now, PDP later.

## Files

| File | Action | Purpose |
|---|---|---|
| `snippets/lusena-bundle-nudge.liquid` | Create | Visual card — Liquid/HTML only, no JS |
| `assets/lusena-bundle-swap.js` | Create | Shared swap logic — `window.LusenaBundle.swap()` |
| `assets/lusena-foundations.css` | Modify | Nudge CSS (~30-40 lines) |
| `snippets/cart-drawer.liquid` | Modify | Render nudge snippet for bundles, use shared swap JS, remove inline `swapToBundle` |
| `sections/lusena-cart-items.liquid` | Modify | Same changes mirrored for cart page |

## New Metafield

**`lusena.bundle_nudge_map`** — type: `json` — on each bundle product.

Maps trigger product handle to the added item's label in Polish accusative case.

Nocna Rutyna:
```json
{
  "poszewka-jedwabna": "czepek jedwabny",
  "silk-bonnet": "poszewkę jedwabną"
}
```

Piekny Sen:
```json
{
  "poszewka-jedwabna": "maskę 3D",
  "jedwabna-maska-3d": "poszewkę jedwabną"
}
```

Scrunchie Trio:
```json
{
  "silk-scrunchie": "dwie kolejne jedwabne gumki"
}
```

Lookup in Liquid:
```liquid
assign nudge_map = upsell_product.metafields.lusena.bundle_nudge_map.value
assign added_label = nudge_map[trigger_product.handle]
```

## The Nudge Card

### Visual

```
┌────────────────────────────────────────────┐
│  Dodaj czepek jedwabny do zestawu          │
│  Nocna Rutyna · 399 zł zam. 508 zł        │
│                                            │
│  [   Dodaj do zestawu · +130 zł   ]        │
└────────────────────────────────────────────┘
```

- **Headline:** "Dodaj {added_label} do zestawu" — specific product being added, accusative case
- **Pricing line:** Bundle name + bundle price (strong) + "zam." + crossed-out original total
- **Button:** Primary (filled, `lusena-btn--primary lusena-btn--size-sm`) — upgraded from the current outline/xs pattern to match the more prominent nudge card design. "Dodaj do zestawu · +{incremental} zl"
- **No image** — text-only, premium feel
- **No success overlay** — drawer re-renders with bundle in cart, which is self-evident confirmation. The existing cross-sell success animation ("Dodano do koszyka") stays for non-bundle upsells but is bypassed for the bundle nudge path.
- **Accessibility:** Container has `aria-label="Propozycja zestawu"` for screen readers

### Fallback

If `added_label` is blank (nudge map missing or handle not in map), headline falls back to "Uzupelnij do zestawu" without the specific item name. Pricing and button still work.

### Adaptations per bundle

| Trigger | Headline | Pricing | Button |
|---|---|---|---|
| Poszewka (269) → Nocna Rutyna | Dodaj czepek jedwabny do zestawu | Nocna Rutyna · 399 zl zam. 508 zl | +130 zl |
| Bonnet (239) → Nocna Rutyna | Dodaj poszewke jedwabna do zestawu | Nocna Rutyna · 399 zl zam. 508 zl | +160 zl |
| Poszewka (269) → Piekny Sen | Dodaj maske 3D do zestawu | Piekny Sen · 349 zl zam. 438 zl | +80 zl |
| Maska (169) → Piekny Sen | Dodaj poszewke jedwabna do zestawu | Piekny Sen · 349 zl zam. 438 zl | +180 zl |

The incremental cost is always `bundle_price - trigger_item_price`.

## Snippet Interface

`snippets/lusena-bundle-nudge.liquid` accepts:

```liquid
{% render 'lusena-bundle-nudge',
  added_label: added_label,
  bundle_name: upsell_product.title,
  bundle_price_cents: bundle_price_cents,
  original_total_cents: original_total_cents,
  incremental_cents: incremental_cents,
  bundle_variant_id: upsell_variant.id,
  replace_key: trigger_item.key
%}
```

| Parameter | Type | Description |
|---|---|---|
| `added_label` | string | "czepek jedwabny" — from nudge map. Blank triggers fallback headline. |
| `bundle_name` | string | "Nocna Rutyna" — bundle product title |
| `bundle_price_cents` | number | 39900 — bundle variant price in cents |
| `original_total_cents` | number | 50800 — sum of components at full price, in cents |
| `incremental_cents` | number | 13000 — extra cost to customer (bundle - trigger item price) |
| `bundle_variant_id` | number | Variant ID for the `/cart/add.js` call |
| `replace_key` | string | Cart line item key for the `/cart/change.js` removal |

### Output HTML

Prices are formatted with Shopify's `| money_without_trailing_zeros` filter (applied directly to cents values).

```html
<div class="lusena-bundle-nudge"
     data-bundle-nudge
     data-bundle-variant-id="{{ bundle_variant_id }}"
     data-replace-key="{{ replace_key }}"
     aria-label="Propozycja zestawu">
  <p class="lusena-bundle-nudge__added">
    {%- if added_label != blank -%}
      Dodaj {{ added_label }} do zestawu
    {%- else -%}
      Uzupełnij do zestawu
    {%- endif -%}
  </p>
  <p class="lusena-bundle-nudge__pricing">
    {{ bundle_name }} ·
    <strong>{{ bundle_price_cents | money_without_trailing_zeros }}</strong>
    {%- if original_total_cents > 0 -%}
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

## Shared JS — `assets/lusena-bundle-swap.js`

Exposes `window.LusenaBundle.swap()`:

```js
window.LusenaBundle = {
  async swap(bundleVariantId, removeKeys, options) {
    // options.sections — optional array of section IDs for re-render data

    // 1. POST /cart/add.js — add the bundle variant
    var addRes = await fetch('/cart/add.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ items: [{ id: parseInt(bundleVariantId), quantity: 1 }] })
    });
    if (!addRes.ok) throw new Error('Failed to add bundle');

    // 2. POST /cart/change.js per key — remove individual item(s)
    //    Last call includes sections param if provided
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

### What it does NOT do

- No loading states (caller manages button UI)
- No refresh/re-render (caller decides: drawer re-render vs page reload)
- No success overlay (not needed — cart re-render is the confirmation)
- No error UI (caller catches and handles)

### Script loading

Loaded with `<script src="{{ 'lusena-bundle-swap.js' | asset_url }}" defer>` only when `upsell_is_bundle` is true. Not loaded globally.

## Parent Wiring — Cart Drawer

In `snippets/cart-drawer.liquid`:

### Liquid (replacing current bundle upsell card)

```liquid
{%- if upsell_product_1 != blank and upsell_is_bundle -%}
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
{%- elsif upsell_product_1 != blank -%}
  ... existing cross-sell card (unchanged) ...
{%- endif -%}
```

### JS (simplified click handler)

This handler goes **inside the existing cart drawer `<script>` IIFE** where `drawer` is already bound to the `cart-drawer` element. It replaces the old `swapToBundle` function and `[data-cart-upsell] button[type="button"]` click listener, which are **deleted**.

```js
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

## Parent Wiring — Cart Page

In `sections/lusena-cart-items.liquid`:

### Liquid

Same pattern as drawer but using `upsell_product` (not `upsell_product_1`) and `upsell_variant` (not `upsell_variant_1`).

### JS

```js
container.addEventListener('click', async function(e) {
  var btn = e.target.closest('[data-bundle-nudge-action]');
  if (!btn) return;

  var nudge = btn.closest('[data-bundle-nudge]');
  if (!nudge) return;

  btn.disabled = true;
  // show loading dots

  try {
    await LusenaBundle.swap(nudge.dataset.bundleVariantId, [nudge.dataset.replaceKey]);
    window.location.reload();
  } catch (err) {
    btn.disabled = false;
    // restore button
  }
});
```

## CSS

Added to `assets/lusena-foundations.css` as a shared component:

```css
.lusena-bundle-nudge {
  /* Container: subtle border, padding, rounded corners */
  /* Sits inside the existing upsell zone positioning */
}
.lusena-bundle-nudge__added {
  /* Headline: product being added */
}
.lusena-bundle-nudge__pricing {
  /* Price line: bundle name + prices */
}
.lusena-bundle-nudge__was {
  /* Crossed-out original total */
}
```

Button uses existing `lusena-btn lusena-btn--primary lusena-btn--size-sm`. No new button CSS.

Placement/spacing CSS stays in each parent's stylesheet (cart drawer `<style>`, cart page `{% stylesheet %}`).

## Future PDP Reuse

When implementing #12 (PDP bundle detection banner):

1. **Visual:** Different layout on PDP (not the same compact card) — designed separately
2. **JS:** Same `LusenaBundle.swap()` call + different refresh (update cart badge, show confirmation)
3. **Data:** JS fetches `/cart.js` on PDP load, checks if any cart item's handle matches the current product's `bundle_nudge_map`, renders the banner if so

The shared `lusena-bundle-swap.js` and `lusena.bundle_nudge_map` metafield work identically.

## Edge Cases

| Scenario | Behavior |
|---|---|
| `bundle_nudge_map` not set on bundle | Fallback headline: "Uzupelnij do zestawu" (no specific item name) |
| Trigger handle not in nudge map | Same fallback |
| `bundle_original_price` not set | Hide "zam. X zl" — show only bundle price |
| Bundle variant out of stock | Waterfall skips to secondary (handled by existing upsell resolution) |
| Color matching | Already handled by existing Liquid color-matching logic (Step 2, built earlier) |
| Swap fails (add ok, remove fails) | Customer has both items in cart — known limitation, #13 (cart merge) will handle |
| Trigger item quantity > 1 | All units removed (quantity set to 0). Acceptable for launch — bundles are the upgrade path. Document for future improvement if needed. |
