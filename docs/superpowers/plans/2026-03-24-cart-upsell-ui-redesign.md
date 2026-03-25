# Cart Upsell UI Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace both the cross-sell and bundle nudge UIs in cart drawer and cart page with a unified, gain-framed design using LUSENA tokens.

**Architecture:** Pure HTML/CSS/Liquid change - no JS logic changes. The existing upsell selection waterfall and `lusena-bundle-swap.js` stay untouched. We replace the rendered card HTML in two files (cart drawer, cart page), update CSS in their `{% stylesheet %}` blocks, delete the old bundle nudge snippet, and clean up foundations CSS.

**Tech Stack:** Shopify Liquid, CSS (LUSENA design tokens), existing `lusena-btn` component classes.

**Spec:** `docs/superpowers/specs/2026-03-24-cart-upsell-ui-redesign.md`

**Key references:**
- CSS tokens: `memory-bank/doc/patterns/brand-tokens.md`
- CLAUDE.md conventions (especially: `lusena-*` prefix, hyphens not em dashes, compiled_assets truncation guard)
- Cart drawer: `snippets/cart-drawer.liquid` (upsell zone starts ~line 849, CSS ~line 366)
- Cart page: `sections/lusena-cart-items.liquid` (upsell zone starts ~line 268, CSS ~line 827)
- Bundle nudge snippet: `snippets/lusena-bundle-nudge.liquid` (will be deleted)
- Foundations CSS: `assets/lusena-foundations.css` (bundle nudge styles ~lines 1209-1240)

---

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| `snippets/cart-drawer.liquid` | Modify | Replace upsell card HTML (lines ~940-1082) with unified cross-sell card + bundle two-tile card. Update `{% stylesheet %}` (lines ~366-674) with new `.lusena-upsell-card` and tile styles, remove old `.lusena-cart-drawer__upsell-card` styles. |
| `sections/lusena-cart-items.liquid` | Modify | Mirror drawer changes: replace upsell card HTML (lines ~358-482) with same unified markup. Update `{% stylesheet %}` (lines ~827-946) with matching styles. |
| `snippets/lusena-bundle-nudge.liquid` | Delete | No longer needed - markup is inline in drawer and cart page. |
| `assets/lusena-foundations.css` | Modify | Remove `.lusena-bundle-nudge` styles (lines ~1209-1240, ~30 lines). |

---

### Task 1: Update cart drawer CSS - replace old upsell styles with unified card + tile styles

**Files:**
- Modify: `snippets/cart-drawer.liquid` ({% stylesheet %} block, lines ~366-674)

This task replaces the old `.lusena-cart-drawer__upsell-*` CSS with the new unified `.lusena-upsell-card` system. Both cross-sell and bundle use the same card container, and the bundle gets the two-tile layout.

- [ ] **Step 1: Read the current CSS block**

Read `snippets/cart-drawer.liquid` lines 366-674 to understand the full existing upsell CSS. Note: lines 366-462 are the upsell zone + card styles. Lines 465-479 are the success state. These blocks will be replaced.

- [ ] **Step 2: Replace upsell zone CSS (lines ~366-462) with unified styles**

Replace the `/* === UPSELL ZONE === */` section with:

```css
/* === UPSELL ZONE === */
.lusena-cart-drawer__upsell :where(p) { margin: 0; }
.lusena-cart-drawer .lusena-cart-drawer__upsell .lusena-btn--size-xs { min-height: auto; }

.lusena-cart-drawer .lusena-cart-drawer__upsell {
  border-top: 1px solid color-mix(in srgb, var(--lusena-text-2) 10%, transparent);
  padding: var(--lusena-space-2) var(--lusena-space-3);
  background-color: color-mix(in srgb, var(--lusena-surface-2) 50%, transparent);
}

.lusena-cart-drawer .lusena-cart-drawer__upsell-label {
  font-family: var(--lusena-font-brand);
  font-size: 1.2rem;
  line-height: 1.4;
  color: var(--lusena-text-2);
  margin-bottom: 1rem;
}

/* --- Unified upsell card container --- */
.lusena-cart-drawer .lusena-upsell-card {
  padding: var(--lusena-space-2);
  background: var(--lusena-color-n0);
  border-radius: var(--lusena-btn-radius);
  border: 1px solid color-mix(in srgb, var(--lusena-text-2) 5%, transparent);
  box-shadow: 0 1px 2px rgba(0,0,0,0.03);
  border-left: 0.25rem solid color-mix(in srgb, var(--lusena-accent-cta) 40%, transparent);
}

/* --- Cross-sell card (horizontal layout) --- */
.lusena-upsell-card__xs-row {
  display: flex;
  gap: 1.2rem;
  align-items: center;
}

.lusena-upsell-card__xs-img {
  width: 5.6rem;
  height: 5.6rem;
  background-color: var(--lusena-surface-2);
  border-radius: var(--lusena-radius-sm);
  overflow: hidden;
  flex-shrink: 0;
}

.lusena-upsell-card__xs-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.lusena-upsell-card__xs-info {
  flex: 1;
  min-width: 0;
}

.lusena-upsell-card__xs-title {
  font-size: 1.3rem;
  font-weight: 500;
  color: var(--lusena-text-1);
  line-height: 1.25;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.lusena-upsell-card__xs-msg {
  font-size: 1.15rem;
  color: var(--lusena-text-2);
  margin-top: var(--lusena-space-05);
  line-height: 1.375;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.lusena-upsell-card__xs-color {
  font-size: 1.05rem;
  line-height: 1.5;
  color: color-mix(in srgb, var(--lusena-text-2) 70%, transparent);
  margin-top: var(--lusena-space-05);
}

.lusena-upsell-card__xs-color span {
  color: var(--lusena-text-1);
  font-weight: 500;
}

.lusena-upsell-card__xs-aside {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: space-between;
  flex-shrink: 0;
  gap: var(--lusena-space-1);
}

.lusena-upsell-card__xs-price {
  font-size: 1.35rem;
  line-height: 1.4;
  font-weight: 500;
  color: var(--lusena-text-1);
  font-variant-numeric: tabular-nums;
}

/* --- Bundle card (two-tile layout) --- */
.lusena-upsell-card__bn-headline {
  font-size: 1.35rem;
  font-weight: 500;
  color: var(--lusena-text-1);
  line-height: 1.35;
  margin-bottom: var(--lusena-space-1);
}

.lusena-upsell-card__bn-tiles {
  display: flex;
  gap: var(--lusena-space-1);
  align-items: stretch;
}

.lusena-upsell-card__bn-have {
  flex: 0 0 30%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: var(--lusena-space-1) var(--lusena-space-05);
  border-radius: var(--lusena-radius-sm);
  background: color-mix(in srgb, var(--lusena-surface-2) 40%, transparent);
}

.lusena-upsell-card__bn-have-img {
  width: 3.8rem;
  height: 3.8rem;
  border-radius: 0.4rem;
  overflow: hidden;
  margin-bottom: 0.5rem;
  position: relative;
  opacity: 0.75;
}

.lusena-upsell-card__bn-have-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.lusena-upsell-card__bn-check {
  position: absolute;
  top: -0.3rem;
  right: -0.3rem;
  width: 1.4rem;
  height: 1.4rem;
  background: var(--lusena-accent-cta);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 1;
}

.lusena-upsell-card__bn-check svg {
  width: 0.8rem;
  height: 0.8rem;
  color: #fff;
}

.lusena-upsell-card__bn-have-name {
  font-size: 1rem;
  font-weight: 500;
  color: #888;
  line-height: 1.2;
}

.lusena-upsell-card__bn-have-status {
  font-size: 0.9rem;
  color: var(--lusena-accent-cta);
  margin-top: 0.2rem;
  font-weight: 500;
}

.lusena-upsell-card__bn-plus {
  font-size: 1.6rem;
  color: var(--lusena-color-n300);
  font-weight: 300;
  flex-shrink: 0;
  align-self: center;
}

.lusena-upsell-card__bn-add {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: var(--lusena-space-1);
  border-radius: var(--lusena-radius-sm);
  background: color-mix(in srgb, var(--lusena-surface-2) 50%, transparent);
  border: 1px solid color-mix(in srgb, var(--lusena-text-2) 6%, transparent);
}

.lusena-upsell-card__bn-add-img {
  width: 5.6rem;
  height: 5.6rem;
  border-radius: var(--lusena-radius-sm);
  overflow: hidden;
  margin-bottom: 0.6rem;
}

.lusena-upsell-card__bn-add-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.lusena-upsell-card__bn-add-name {
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--lusena-text-1);
  line-height: 1.25;
}

.lusena-upsell-card__bn-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--lusena-space-1);
  margin-top: var(--lusena-space-1);
  padding-top: var(--lusena-space-1);
  border-top: 1px solid color-mix(in srgb, var(--lusena-text-2) 5%, transparent);
}

.lusena-upsell-card__bn-pricing {
  display: flex;
  align-items: baseline;
  gap: 0.6rem;
  flex-wrap: wrap;
}

.lusena-upsell-card__bn-price {
  font-size: 1.4rem;
  font-weight: 500;
  color: var(--lusena-text-1);
  font-variant-numeric: tabular-nums;
}

.lusena-upsell-card__bn-was {
  font-size: 1.1rem;
  color: var(--lusena-color-n300);
  text-decoration: line-through;
}

.lusena-upsell-card__bn-savings {
  display: inline-flex;
  background: rgba(140, 106, 60, 0.08);
  color: var(--lusena-accent-2);
  font-family: var(--lusena-font-ui);
  font-size: 1.15rem;
  font-weight: 500;
  padding: 0.3rem 0.8rem;
  border-radius: var(--lusena-btn-radius);
}
```

- [ ] **Step 3: Update the compact layout media query (lines ~636-661)**

In the `@media (max-height: 700px)` block, replace the old upsell compact rules with:

```css
.lusena-cart-drawer .lusena-cart-drawer__upsell {
  padding: var(--lusena-space-1) var(--lusena-space-2);
}

.lusena-cart-drawer .lusena-cart-drawer__upsell-label {
  margin-bottom: var(--lusena-space-1);
  font-size: 1.1rem;
}

.lusena-upsell-card__bn-have-img { width: 3rem; height: 3rem; }
.lusena-upsell-card__bn-add-img { width: 4.4rem; height: 4.4rem; }
.lusena-upsell-card__xs-img { width: 4rem; height: 4rem; }
```

- [ ] **Step 4: Verify the CSS is syntactically correct**

Read back the modified file's `{% stylesheet %}` block to check for unclosed braces or typos.

- [ ] **Step 5: Commit**

```bash
git add snippets/cart-drawer.liquid
git commit -m "feat(lusena): unified upsell card CSS in cart drawer"
```

---

### Task 2: Update cart drawer HTML - replace upsell card markup

**Files:**
- Modify: `snippets/cart-drawer.liquid` (lines ~940-1082)

Replace the upsell card HTML for both the cross-sell and bundle code paths with the new unified markup.

- [ ] **Step 1: Read lines 940-1082 for the full current card HTML**

Understand the existing structure: section label, card wrapper, image, info, aside, bundle nudge render call, and cross-sell product-form.

- [ ] **Step 2: Replace the upsell card HTML (lines ~940-1082)**

Replace everything from `<div class="lusena-cart-drawer__upsell"` through the closing `</div>` of the card (before the success div) with:

```liquid
<div class="lusena-cart-drawer__upsell" data-cart-upsell-zone aria-live="polite">
  <p class="lusena-cart-drawer__upsell-label">
    {%- if upsell_is_bundle -%}Korzystniej w zestawie{%- else -%}Pasuje do{%- endif -%}
  </p>

  {%- if upsell_is_bundle -%}
    {%- comment -%} Bundle two-tile card {%- endcomment -%}
    {%- assign nudge_map = upsell_product_1.metafields.lusena.bundle_nudge_map.value -%}
    {%- assign added_label = nudge_map[trigger_product.handle] -%}
    {%- assign bundle_price_cents = upsell_variant_1.price -%}
    {%- assign original_total_cents = upsell_product_1.metafields.lusena.bundle_original_price.value | times: 100 -%}
    {%- assign savings_cents = original_total_cents | minus: bundle_price_cents -%}
    {%- assign incremental_cents = bundle_price_cents | minus: trigger_item.variant.price -%}

    {%- liquid
      assign sb_options = upsell_variant_1.metafields.simple_bundles.variant_options.value
      assign nudge_prop_map = ''
      if sb_options != blank
        for opt in sb_options
          assign opt_product = opt.optionName | split: ' - Color' | first | split: ' - ' | first
          assign opt_clean = opt_product
          assign dim_parts = opt_product | split: '×'
          if dim_parts.size > 1
            assign opt_words = opt_product | split: ' '
            assign opt_clean = ''
            for w in opt_words
              assign w_dim = w | split: '×' | size
              if w_dim > 1
                break
              endif
              if opt_clean == ''
                assign opt_clean = w
              else
                assign opt_clean = opt_clean | append: ' ' | append: w
              endif
            endfor
          endif

          assign outer_idx = forloop.index
          assign same_total = 0
          assign same_so_far = 0
          for check in sb_options
            assign check_name = check.optionName | split: ' - Color' | first | split: ' - ' | first
            if check_name == opt_product
              assign same_total = same_total | plus: 1
              if forloop.index <= outer_idx
                assign same_so_far = same_so_far | plus: 1
              endif
            endif
          endfor
          if same_total > 1
            assign opt_clean = opt_clean | append: ' ' | append: same_so_far
          endif

          assign opt_vals_raw = opt.optionValues | split: ', '
          assign opt_vals_json = ''
          for v in opt_vals_raw
            if opt_vals_json == ''
              assign opt_vals_json = '"' | append: v | append: '"'
            else
              assign opt_vals_json = opt_vals_json | append: ',"' | append: v | append: '"'
            endif
          endfor
          assign entry = '{"key":"' | append: opt_clean | append: '","values":[' | append: opt_vals_json | append: ']}'
          if nudge_prop_map == ''
            assign nudge_prop_map = entry
          else
            assign nudge_prop_map = nudge_prop_map | append: ',' | append: entry
          endif
        endfor
        assign nudge_prop_map = '[' | append: nudge_prop_map | append: ']'
      endif
    -%}

    <div class="lusena-upsell-card"
         data-bundle-nudge
         data-bundle-variant-id="{{ upsell_variant_1.id }}"
         data-replace-key="{{ trigger_item.key | escape }}"
         {%- if trigger_color != blank %} data-trigger-color="{{ trigger_color | escape }}"{% endif -%}
         {%- if nudge_prop_map != blank %} data-property-map="{{ nudge_prop_map | escape }}"{% endif -%}
         aria-label="Propozycja zestawu">
      <p class="lusena-upsell-card__bn-headline">
        Dodaj {{ added_label }} i zaoszczedz {{ savings_cents | money_without_trailing_zeros }}
      </p>
      <div class="lusena-upsell-card__bn-tiles">
        <div class="lusena-upsell-card__bn-have">
          <div class="lusena-upsell-card__bn-have-img">
            {%- if trigger_product.featured_image -%}
              <img
                src="{{ trigger_product.featured_image | image_url: width: 120 }}"
                alt="{{ trigger_product.featured_image.alt | escape }}"
                loading="lazy"
                width="38"
                height="{{ 38 | divided_by: trigger_product.featured_image.aspect_ratio | ceil }}"
              >
            {%- endif -%}
            <span class="lusena-upsell-card__bn-check" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </span>
          </div>
          <p class="lusena-upsell-card__bn-have-name">{{ trigger_product.title | escape }}</p>
          <p class="lusena-upsell-card__bn-have-status">W koszyku</p>
        </div>
        <span class="lusena-upsell-card__bn-plus" aria-hidden="true">+</span>
        <div class="lusena-upsell-card__bn-add">
          <div class="lusena-upsell-card__bn-add-img">
            {%- if upsell_product_1.featured_image -%}
              <img
                src="{{ upsell_product_1.featured_image | image_url: width: 240 }}"
                alt="{{ upsell_product_1.featured_image.alt | escape }}"
                loading="lazy"
                width="56"
                height="{{ 56 | divided_by: upsell_product_1.featured_image.aspect_ratio | ceil }}"
              >
            {%- endif -%}
          </div>
          <p class="lusena-upsell-card__bn-add-name">{{ added_label | escape }}</p>
        </div>
      </div>
      <div class="lusena-upsell-card__bn-bottom">
        <div class="lusena-upsell-card__bn-pricing">
          <span class="lusena-upsell-card__bn-price">{{ bundle_price_cents | money_without_trailing_zeros }}</span>
          <span class="lusena-upsell-card__bn-was">{{ original_total_cents | money_without_trailing_zeros }}</span>
          <span class="lusena-upsell-card__bn-savings">Oszczedzasz {{ savings_cents | money_without_trailing_zeros }}</span>
        </div>
        <button type="button"
                class="lusena-btn lusena-btn--outline lusena-btn--size-xs"
                data-bundle-nudge-action>
          <span class="lusena-btn__content">Dodaj do zestawu</span>
          <span class="loading__spinner hidden">
            <span class="lusena-btn__loading-dots" aria-hidden="true">
              <span></span><span></span><span></span>
            </span>
          </span>
        </button>
      </div>
    </div>

  {%- else -%}
    {%- comment -%} Cross-sell card (horizontal) {%- endcomment -%}
    <div class="lusena-upsell-card">
      <div class="lusena-upsell-card__xs-row">
        <div class="lusena-upsell-card__xs-img">
          {%- if upsell_product_1.featured_image -%}
            <img
              src="{{ upsell_product_1.featured_image | image_url: width: 240 }}"
              alt="{{ upsell_product_1.featured_image.alt | escape }}"
              loading="lazy"
              width="56"
              height="{{ 56 | divided_by: upsell_product_1.featured_image.aspect_ratio | ceil }}"
            >
          {%- endif -%}
        </div>
        <div class="lusena-upsell-card__xs-info">
          <p class="lusena-upsell-card__xs-title">{{ upsell_display_title | escape }}</p>
          <p class="lusena-upsell-card__xs-msg">{{ upsell_display_message | escape }}</p>
          {%- if upsell_display_color != blank -%}
            <p class="lusena-upsell-card__xs-color">
              Kolor: <span>{{ upsell_display_color | escape }}</span>
            </p>
          {%- endif -%}
        </div>
        <div class="lusena-upsell-card__xs-aside">
          <p class="lusena-upsell-card__xs-price">{{ upsell_display_price | escape }}</p>
          <product-form class="product-form" data-hide-errors="true" data-cart-upsell>
            {%- form 'product',
              upsell_product_1,
              id: 'CartDrawer-Upsell-Form-1',
              class: 'form',
              novalidate: 'novalidate',
              data-type: 'add-to-cart-form'
            -%}
              <input type="hidden" name="id" value="{{ upsell_variant_1.id }}">
              <button type="submit" class="lusena-btn lusena-btn--outline lusena-btn--size-xs">
                <span class="lusena-btn__content">Dodaj</span>
                <span class="loading__spinner hidden">
                  <span class="lusena-btn__loading-dots" aria-hidden="true">
                    <span></span><span></span><span></span>
                  </span>
                </span>
              </button>
            {%- endform -%}
          </product-form>
        </div>
      </div>
    </div>
  {%- endif -%}
</div>
```

Note: The `data-bundle-nudge`, `data-bundle-nudge-action`, `data-replace-key`, `data-trigger-color`, and `data-property-map` attributes are preserved exactly as before - the JS click handler in the same file reads these. No JS changes needed.

- [ ] **Step 3: Verify the Liquid syntax**

Read back the modified HTML to check for unclosed tags, mismatched `if/endif`, and proper Liquid variable scoping.

- [ ] **Step 4: Commit**

```bash
git add snippets/cart-drawer.liquid
git commit -m "feat(lusena): unified upsell card HTML in cart drawer - two-tile bundle, gain-framed copy"
```

---

### Task 3: Update cart page - complete HTML and CSS

**Files:**
- Modify: `sections/lusena-cart-items.liquid` (HTML lines ~358-482, CSS lines ~827-946)

The cart page has different variable names and a different JS interaction model from the drawer. This task provides complete code for both CSS and HTML.

**Critical variable differences from drawer:**
- `upsell_product` (not `upsell_product_1`)
- `upsell_variant` (not `upsell_variant_1`)
- `upsell_message` (not `upsell_display_message` - cart page does NOT assign `upsell_display_message`)
- `upsell_color_label` (not `upsell_display_color`)
- Cross-sell uses `data-cart-page-upsell-add` + `data-variant-id` button (NOT `product-form`)
- Cross-sell button inner spans use `data-upsell-btn-text` and `data-upsell-loading` (required by JS handler at line ~578)

- [ ] **Step 1: Read the current cart page upsell HTML and CSS**

Read `sections/lusena-cart-items.liquid` lines 358-482 (HTML) and 827-946 (CSS).

- [ ] **Step 2: Replace upsell CSS (lines ~827-946)**

Replace the `/* === UPSELL ZONE === */` section and everything below it (upsell card, dots, responsive) with the complete cart page CSS. This duplicates the unified card classes from the drawer (since `{% stylesheet %}` blocks are section-scoped and NOT shared):

```css
/* === UPSELL ZONE (cart page) === */
.lusena-cart-upsell :where(p) { margin: 0; }
.lusena-cart-upsell .lusena-btn--size-xs { min-height: auto; }

.lusena-cart-upsell {
  padding: var(--lusena-space-2);
  border-top: 1px solid color-mix(in srgb, var(--lusena-text-2) 10%, transparent);
  background-color: color-mix(in srgb, var(--lusena-surface-2) 50%, transparent);
  margin-left: calc(-1 * var(--lusena-space-2));
  margin-right: calc(-1 * var(--lusena-space-2));
}
@media (min-width: 768px) {
  .lusena-cart-upsell {
    margin-left: calc(-1 * var(--lusena-space-4));
    margin-right: calc(-1 * var(--lusena-space-4));
    padding-left: var(--lusena-space-4);
    padding-right: var(--lusena-space-4);
  }
}

.lusena-cart-upsell__label {
  font-family: var(--lusena-font-brand);
  font-size: 1.2rem;
  line-height: 1.4;
  color: var(--lusena-text-2);
  margin: 0 0 1rem;
}

/* --- Unified card container (same as drawer) --- */
.lusena-upsell-card {
  padding: var(--lusena-space-2);
  background: var(--lusena-color-n0);
  border-radius: var(--lusena-btn-radius);
  border: 1px solid color-mix(in srgb, var(--lusena-text-2) 5%, transparent);
  box-shadow: 0 1px 2px rgba(0,0,0,0.03);
  border-left: 0.25rem solid color-mix(in srgb, var(--lusena-accent-cta) 40%, transparent);
}

/* --- Cross-sell card (horizontal) --- */
.lusena-upsell-card__xs-row { display: flex; gap: 1.2rem; align-items: center; }
.lusena-upsell-card__xs-img { width: 5.6rem; height: 5.6rem; background-color: var(--lusena-surface-2); border-radius: var(--lusena-radius-sm); overflow: hidden; flex-shrink: 0; }
.lusena-upsell-card__xs-img img { width: 100%; height: 100%; object-fit: cover; }
.lusena-upsell-card__xs-info { flex: 1; min-width: 0; }
.lusena-upsell-card__xs-title { font-size: 1.3rem; font-weight: 500; color: var(--lusena-text-1); line-height: 1.25; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.lusena-upsell-card__xs-msg { font-size: 1.15rem; color: var(--lusena-text-2); margin-top: var(--lusena-space-05); line-height: 1.375; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.lusena-upsell-card__xs-color { font-size: 1.05rem; line-height: 1.5; color: color-mix(in srgb, var(--lusena-text-2) 70%, transparent); margin-top: var(--lusena-space-05); }
.lusena-upsell-card__xs-color span { color: var(--lusena-text-1); font-weight: 500; }
.lusena-upsell-card__xs-aside { display: flex; flex-direction: column; align-items: flex-end; justify-content: space-between; flex-shrink: 0; gap: var(--lusena-space-1); }
.lusena-upsell-card__xs-price { font-size: 1.35rem; line-height: 1.4; font-weight: 500; color: var(--lusena-text-1); font-variant-numeric: tabular-nums; }

/* --- Bundle card (two-tile) --- */
.lusena-upsell-card__bn-headline { font-size: 1.35rem; font-weight: 500; color: var(--lusena-text-1); line-height: 1.35; margin-bottom: var(--lusena-space-1); }
.lusena-upsell-card__bn-tiles { display: flex; gap: var(--lusena-space-1); align-items: stretch; }
.lusena-upsell-card__bn-have { flex: 0 0 30%; display: flex; flex-direction: column; align-items: center; text-align: center; padding: var(--lusena-space-1) var(--lusena-space-05); border-radius: var(--lusena-radius-sm); background: color-mix(in srgb, var(--lusena-surface-2) 40%, transparent); }
.lusena-upsell-card__bn-have-img { width: 3.8rem; height: 3.8rem; border-radius: 0.4rem; overflow: hidden; margin-bottom: 0.5rem; position: relative; opacity: 0.75; }
.lusena-upsell-card__bn-have-img img { width: 100%; height: 100%; object-fit: cover; }
.lusena-upsell-card__bn-check { position: absolute; top: -0.3rem; right: -0.3rem; width: 1.4rem; height: 1.4rem; background: var(--lusena-accent-cta); border-radius: 50%; display: flex; align-items: center; justify-content: center; opacity: 1; }
.lusena-upsell-card__bn-check svg { width: 0.8rem; height: 0.8rem; color: #fff; }
.lusena-upsell-card__bn-have-name { font-size: 1rem; font-weight: 500; color: #888; line-height: 1.2; }
.lusena-upsell-card__bn-have-status { font-size: 0.9rem; color: var(--lusena-accent-cta); margin-top: 0.2rem; font-weight: 500; }
.lusena-upsell-card__bn-plus { font-size: 1.6rem; color: var(--lusena-color-n300); font-weight: 300; flex-shrink: 0; align-self: center; }
.lusena-upsell-card__bn-add { flex: 1; display: flex; flex-direction: column; align-items: center; text-align: center; padding: var(--lusena-space-1); border-radius: var(--lusena-radius-sm); background: color-mix(in srgb, var(--lusena-surface-2) 50%, transparent); border: 1px solid color-mix(in srgb, var(--lusena-text-2) 6%, transparent); }
.lusena-upsell-card__bn-add-img { width: 5.6rem; height: 5.6rem; border-radius: var(--lusena-radius-sm); overflow: hidden; margin-bottom: 0.6rem; }
.lusena-upsell-card__bn-add-img img { width: 100%; height: 100%; object-fit: cover; }
.lusena-upsell-card__bn-add-name { font-size: 1.2rem; font-weight: 500; color: var(--lusena-text-1); line-height: 1.25; }
.lusena-upsell-card__bn-bottom { display: flex; align-items: center; justify-content: space-between; gap: var(--lusena-space-1); margin-top: var(--lusena-space-1); padding-top: var(--lusena-space-1); border-top: 1px solid color-mix(in srgb, var(--lusena-text-2) 5%, transparent); }
.lusena-upsell-card__bn-pricing { display: flex; align-items: baseline; gap: 0.6rem; flex-wrap: wrap; }
.lusena-upsell-card__bn-price { font-size: 1.4rem; font-weight: 500; color: var(--lusena-text-1); font-variant-numeric: tabular-nums; }
.lusena-upsell-card__bn-was { font-size: 1.1rem; color: var(--lusena-color-n300); text-decoration: line-through; }
.lusena-upsell-card__bn-savings { display: inline-flex; background: rgba(140, 106, 60, 0.08); color: var(--lusena-accent-2); font-family: var(--lusena-font-ui); font-size: 1.15rem; font-weight: 500; padding: 0.3rem 0.8rem; border-radius: var(--lusena-btn-radius); }

/* --- Cross-sell loading dots (cart page specific) --- */
.lusena-upsell-card__dots { display: inline-flex; gap: 0.3rem; align-items: center; justify-content: center; }
.lusena-upsell-card__dots.hidden { display: none; }
.lusena-upsell-card__dots span { width: 0.4rem; height: 0.4rem; border-radius: 50%; background: currentColor; animation: lusena-dot-pulse 1.2s infinite ease-in-out; }
.lusena-upsell-card__dots span:nth-child(2) { animation-delay: 0.2s; }
.lusena-upsell-card__dots span:nth-child(3) { animation-delay: 0.4s; }
@keyframes lusena-dot-pulse {
  0%, 80%, 100% { opacity: 0.3; transform: scale(0.8); }
  40% { opacity: 1; transform: scale(1); }
}
```

Note: The mobile `margin-top: auto` rule at line ~647 must be preserved. It is scoped to `.lusena-cart-upsell` which is the zone wrapper class we keep. Verify this rule is NOT inside the replaced block.

- [ ] **Step 3: Replace upsell HTML (lines ~358-482)**

Replace the entire `{%- if upsell_is_bundle -%}...{%- else -%}...{%- endif -%}` block with this complete cart page HTML:

```liquid
{%- if upsell_is_bundle -%}
  {%- comment -%} Bundle two-tile card {%- endcomment -%}
  {%- assign nudge_map = upsell_product.metafields.lusena.bundle_nudge_map.value -%}
  {%- assign added_label = nudge_map[trigger_product.handle] -%}
  {%- assign bundle_price_cents = upsell_variant.price -%}
  {%- assign original_total_cents = upsell_product.metafields.lusena.bundle_original_price.value | times: 100 -%}
  {%- assign savings_cents = original_total_cents | minus: bundle_price_cents -%}
  {%- assign incremental_cents = bundle_price_cents | minus: trigger_item.variant.price -%}

  {%- liquid
    assign sb_options = upsell_variant.metafields.simple_bundles.variant_options.value
    assign nudge_prop_map = ''
    if sb_options != blank
      for opt in sb_options
        assign opt_product = opt.optionName | split: ' - Color' | first | split: ' - ' | first
        assign opt_clean = opt_product
        assign dim_parts = opt_product | split: '×'
        if dim_parts.size > 1
          assign opt_words = opt_product | split: ' '
          assign opt_clean = ''
          for w in opt_words
            assign w_dim = w | split: '×' | size
            if w_dim > 1
              break
            endif
            if opt_clean == ''
              assign opt_clean = w
            else
              assign opt_clean = opt_clean | append: ' ' | append: w
            endif
          endfor
        endif

        assign outer_idx = forloop.index
        assign same_total = 0
        assign same_so_far = 0
        for check in sb_options
          assign check_name = check.optionName | split: ' - Color' | first | split: ' - ' | first
          if check_name == opt_product
            assign same_total = same_total | plus: 1
            if forloop.index <= outer_idx
              assign same_so_far = same_so_far | plus: 1
            endif
          endif
        endfor
        if same_total > 1
          assign opt_clean = opt_clean | append: ' ' | append: same_so_far
        endif

        assign opt_vals_raw = opt.optionValues | split: ', '
        assign opt_vals_json = ''
        for v in opt_vals_raw
          if opt_vals_json == ''
            assign opt_vals_json = '"' | append: v | append: '"'
          else
            assign opt_vals_json = opt_vals_json | append: ',"' | append: v | append: '"'
          endif
        endfor
        assign entry = '{"key":"' | append: opt_clean | append: '","values":[' | append: opt_vals_json | append: ']}'
        if nudge_prop_map == ''
          assign nudge_prop_map = entry
        else
          assign nudge_prop_map = nudge_prop_map | append: ',' | append: entry
        endif
      endfor
      assign nudge_prop_map = '[' | append: nudge_prop_map | append: ']'
    endif
  -%}

  <div class="lusena-cart-upsell" aria-live="polite">
    <p class="lusena-cart-upsell__label">Korzystniej w zestawie</p>
    <div class="lusena-upsell-card"
         data-bundle-nudge
         data-bundle-variant-id="{{ upsell_variant.id }}"
         data-replace-key="{{ trigger_item.key | escape }}"
         {%- if trigger_color != blank %} data-trigger-color="{{ trigger_color | escape }}"{% endif -%}
         {%- if nudge_prop_map != blank %} data-property-map="{{ nudge_prop_map | escape }}"{% endif -%}
         aria-label="Propozycja zestawu">
      <p class="lusena-upsell-card__bn-headline">
        Dodaj {{ added_label }} i zaoszczedz {{ savings_cents | money_without_trailing_zeros }}
      </p>
      <div class="lusena-upsell-card__bn-tiles">
        <div class="lusena-upsell-card__bn-have">
          <div class="lusena-upsell-card__bn-have-img">
            {%- if trigger_product.featured_image -%}
              <img
                src="{{ trigger_product.featured_image | image_url: width: 120 }}"
                alt="{{ trigger_product.featured_image.alt | escape }}"
                loading="lazy" width="38"
                height="{{ 38 | divided_by: trigger_product.featured_image.aspect_ratio | ceil }}"
              >
            {%- endif -%}
            <span class="lusena-upsell-card__bn-check" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </span>
          </div>
          <p class="lusena-upsell-card__bn-have-name">{{ trigger_product.title | escape }}</p>
          <p class="lusena-upsell-card__bn-have-status">W koszyku</p>
        </div>
        <span class="lusena-upsell-card__bn-plus" aria-hidden="true">+</span>
        <div class="lusena-upsell-card__bn-add">
          <div class="lusena-upsell-card__bn-add-img">
            {%- if upsell_product.featured_image -%}
              <img
                src="{{ upsell_product.featured_image | image_url: width: 240 }}"
                alt="{{ upsell_product.featured_image.alt | escape }}"
                loading="lazy" width="56"
                height="{{ 56 | divided_by: upsell_product.featured_image.aspect_ratio | ceil }}"
              >
            {%- endif -%}
          </div>
          <p class="lusena-upsell-card__bn-add-name">{{ added_label | escape }}</p>
        </div>
      </div>
      <div class="lusena-upsell-card__bn-bottom">
        <div class="lusena-upsell-card__bn-pricing">
          <span class="lusena-upsell-card__bn-price">{{ bundle_price_cents | money_without_trailing_zeros }}</span>
          <span class="lusena-upsell-card__bn-was">{{ original_total_cents | money_without_trailing_zeros }}</span>
          <span class="lusena-upsell-card__bn-savings">Oszczedzasz {{ savings_cents | money_without_trailing_zeros }}</span>
        </div>
        <button type="button"
                class="lusena-btn lusena-btn--outline lusena-btn--size-xs"
                data-bundle-nudge-action>
          <span class="lusena-btn__content">Dodaj do zestawu</span>
          <span class="loading__spinner hidden">
            <span class="lusena-btn__loading-dots" aria-hidden="true">
              <span></span><span></span><span></span>
            </span>
          </span>
        </button>
      </div>
    </div>
  </div>

{%- else -%}
  {%- comment -%} Cross-sell card (horizontal) - cart page version {%- endcomment -%}
  <div class="lusena-cart-upsell" data-cart-page-upsell aria-live="polite">
    <p class="lusena-cart-upsell__label">Pasuje do</p>
    <div class="lusena-upsell-card">
      <div class="lusena-upsell-card__xs-row">
        <div class="lusena-upsell-card__xs-img">
          {%- if upsell_product.featured_image -%}
            <img
              src="{{ upsell_product.featured_image | image_url: width: 240 }}"
              alt="{{ upsell_product.featured_image.alt | escape }}"
              loading="lazy" width="56"
              height="{{ 56 | divided_by: upsell_product.featured_image.aspect_ratio | ceil }}"
            >
          {%- endif -%}
        </div>
        <div class="lusena-upsell-card__xs-info">
          <p class="lusena-upsell-card__xs-title">{{ upsell_product.title | escape }}</p>
          {%- if upsell_message != blank -%}
            <p class="lusena-upsell-card__xs-msg">{{ upsell_message | escape }}</p>
          {%- endif -%}
          {%- if upsell_color_label != blank -%}
            <p class="lusena-upsell-card__xs-color">
              Kolor: <span>{{ upsell_color_label | escape }}</span>
            </p>
          {%- endif -%}
        </div>
        <div class="lusena-upsell-card__xs-aside">
          <p class="lusena-upsell-card__xs-price">{{ upsell_display_price | escape }}</p>
          <button
            type="button"
            class="lusena-btn lusena-btn--outline lusena-btn--size-xs"
            data-cart-page-upsell-add
            data-variant-id="{{ upsell_variant.id }}"
          >
            <span class="lusena-btn__content" data-upsell-btn-text>Dodaj</span>
            <span class="lusena-upsell-card__dots hidden" data-upsell-loading aria-hidden="true">
              <span></span><span></span><span></span>
            </span>
          </button>
        </div>
      </div>
    </div>
  </div>
{%- endif -%}
```

Key differences from drawer version:
- Uses `upsell_product` / `upsell_variant` (not `_1` suffix)
- Cross-sell uses `upsell_message` (not `upsell_display_message`) and `upsell_color_label` (not `upsell_display_color`)
- Cross-sell uses `upsell_display_price` (this IS assigned in cart page at line ~355)
- Cross-sell button uses `data-cart-page-upsell-add` + `data-variant-id` + `data-upsell-btn-text` + `data-upsell-loading` (cart page JS handler pattern)
- Cross-sell uses custom dots class `lusena-upsell-card__dots` (not `loading__spinner` - matches cart page JS)
- Bundle zone wrapper uses `lusena-cart-upsell` class (for mobile `margin-top: auto` rule at line ~647)
- Bundle uses `data-bundle-nudge` / `data-bundle-nudge-action` (same as drawer - cart page JS handler at line ~507 reads these)

- [ ] **Step 4: Verify no broken Liquid or HTML**

Read back the modified sections to verify syntax. Check that the mobile `margin-top: auto` rule (inside `@media (max-width: 767px)` block at line ~647) still targets `.lusena-cart-upsell` correctly.

- [ ] **Step 5: Commit**

```bash
git add sections/lusena-cart-items.liquid
git commit -m "feat(lusena): unified upsell card in cart page - complete HTML and CSS"
```

---

### Task 4: Delete bundle nudge snippet and clean up foundations CSS

**Files:**
- Delete: `snippets/lusena-bundle-nudge.liquid`
- Modify: `assets/lusena-foundations.css` (remove lines ~1209-1240)

- [ ] **Step 1: Delete the bundle nudge snippet**

```bash
git rm snippets/lusena-bundle-nudge.liquid
```

- [ ] **Step 2: Remove `.lusena-bundle-nudge` styles from foundations CSS**

Read `assets/lusena-foundations.css` lines 1209-1240. Remove the entire `/* -- Bundle nudge -- */` block (~30 lines, from the comment through `.lusena-bundle-nudge .lusena-btn`).

- [ ] **Step 3: Verify no other files reference the deleted snippet**

Search the codebase for `lusena-bundle-nudge` to ensure no remaining `{% render %}` calls. After Tasks 2 and 3, there should be zero references.

- [ ] **Step 4: Commit**

```bash
git add snippets/lusena-bundle-nudge.liquid assets/lusena-foundations.css
git commit -m "chore(lusena): delete lusena-bundle-nudge snippet and foundations CSS - replaced by inline upsell card"
```

---

### Task 5: Visual verification and compiled_assets check

**Files:** None (testing only)

- [ ] **Step 1: Start the dev server if not running**

```bash
shopify theme dev --port 9292
```

- [ ] **Step 2: Test cross-sell in cart drawer**

Use `/playwright-cli` skill with a named session (e.g., `-s=upsell-ui-test`):
1. Navigate to a product page (e.g., poszewka)
2. Add to cart - drawer should open
3. Verify the cross-sell card shows with:
   - "Pasuje do" label
   - White card with teal left border
   - Product image, title, message, color, price
   - Outline "Dodaj" button
4. Click "Dodaj" and verify it adds the item and shows success state

- [ ] **Step 3: Test bundle nudge in cart drawer**

1. Clear cart, add a czepek (bonnet)
2. Verify the bundle card shows with:
   - "Korzystniej w zestawie" label
   - Headline: "Dodaj poszewke i zaoszczedz 109 zl"
   - Two tiles: small muted czepek (with check + "W koszyku") + larger poszewka image
   - Pricing row: "399 zl" / crossed-out "508 zl" / gold "Oszczedzasz 109 zl" chip
   - Outline "Dodaj do zestawu" button
3. Click "Dodaj do zestawu" and verify the swap works (czepek replaced by Nocna Rutyna bundle)

- [ ] **Step 4: Test bundle nudge for Piekny Sen**

1. Clear cart, add a poszewka
2. Verify the bundle card shows Nocna Rutyna or Piekny Sen (depends on upsell waterfall config)
3. Verify the headline names the correct missing item

- [ ] **Step 5: Test Scrunchie Trio**

1. Clear cart, add a scrunchie
2. Verify the headline says "Dodaj 2 scrunchie i zaoszczedz 38 zl"
3. Verify the swap works

- [ ] **Step 6: Test cart page**

1. Navigate to `/cart` page
2. Verify the same card designs appear
3. Verify cross-sell add works (page reloads)
4. Verify bundle swap works (page reloads)

- [ ] **Step 7: Check compiled_assets size**

Open DevTools Network tab, filter for `compiled_assets`. The file must be under 55KB. If it exceeds 55KB, extract the largest `{% stylesheet %}` block into a standalone asset (see `memory-bank/doc/patterns/css-architecture.md`).

- [ ] **Step 8: Run theme check**

```bash
shopify theme check
```

Only known baseline warnings should appear (listed in CLAUDE.md). No new warnings.

- [ ] **Step 9: Commit any fixes from testing**

If any visual or functional issues were found and fixed during testing:

```bash
git add -A
git commit -m "fix(lusena): upsell card visual/functional adjustments from testing"
```
