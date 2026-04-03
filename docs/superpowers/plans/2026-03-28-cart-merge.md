# #13 Cart Merge Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Show a merge card in cart when both bundle components are present, letting the customer combine them into a bundle and save money.

**Architecture:** Liquid-side merge detection runs before the existing nudge waterfall. If a merge pair is found, it renders a merge card (reusing the bundle nudge card structure) and skips the regular nudge. JS handler is extended with a merge-specific path that passes multiple remove keys and pre-filled color properties to `LusenaBundle.swap()`.

**Tech Stack:** Shopify Liquid, vanilla JS, existing `LusenaBundle.swap()`, section rendering API

**Spec:** `docs/superpowers/specs/2026-03-28-cart-merge-design.md`

---

## File structure

| File | Change | Responsibility |
|---|---|---|
| `snippets/cart-drawer.liquid` | Modify | Merge detection + card HTML + JS handler |
| `sections/lusena-cart-items.liquid` | Modify | Same changes for cart page |

No new files. No CSS changes (reuses existing `lusena-upsell-card__bn-*` classes).

---

### Task 1: Cart drawer - merge detection

**Files:**
- Modify: `snippets/cart-drawer.liquid:11-141` (initial Liquid block)

- [ ] **Step 1: Add merge handle detection to initial Liquid block**

Insert the following after line 29 (after the `endfor` of the suppress loop, before `assign trigger_product = nil`):

```liquid
  comment
    Merge detection: flag which bundle components are in cart.
    Checked later (before regular nudge) to offer bundle merge.
  endcomment
  assign merge_has_poszewka = false
  assign merge_has_bonnet = false
  assign merge_has_maska = false
  assign merge_has_nocna_rutyna = false
  assign merge_has_piekny_sen = false
  assign merge_poszewka_item = blank
  assign merge_bonnet_item = blank
  assign merge_maska_item = blank

  for item in cart.items
    case item.product.handle
      when 'poszewka-jedwabna'
        assign merge_has_poszewka = true
        assign merge_poszewka_item = item
      when 'czepek-jedwabny'
        assign merge_has_bonnet = true
        assign merge_bonnet_item = item
      when 'jedwabna-maska-3d'
        assign merge_has_maska = true
        assign merge_maska_item = item
      when 'nocna-rutyna'
        assign merge_has_nocna_rutyna = true
      when 'piekny-sen'
        assign merge_has_piekny_sen = true
    endcase
  endfor

  comment
    Resolve merge candidate. Highest savings first:
    Nocna Rutyna (poszewka+bonnet, 109 zl) > Piekny Sen (poszewka+maska, 89 zl).
    Skip if target bundle already in cart.
  endcomment
  assign show_merge = false
  assign merge_bundle_handle = ''
  assign merge_item_1 = blank
  assign merge_item_2 = blank

  if upsell_enabled
    if merge_has_poszewka and merge_has_bonnet and merge_has_nocna_rutyna == false
      assign show_merge = true
      assign merge_bundle_handle = 'nocna-rutyna'
      assign merge_item_1 = merge_poszewka_item
      assign merge_item_2 = merge_bonnet_item
    elsif merge_has_poszewka and merge_has_maska and merge_has_piekny_sen == false
      assign show_merge = true
      assign merge_bundle_handle = 'piekny-sen'
      assign merge_item_1 = merge_poszewka_item
      assign merge_item_2 = merge_maska_item
    endif
  endif
```

This goes inside the existing `{%- liquid ... -%}` block (lines 11-141), right after the suppress loop. The code uses indentation consistent with the rest of the block (2-space indent inside `liquid` tag).

- [ ] **Step 2: Verify the Liquid block still closes correctly**

Run: `shopify theme check snippets/cart-drawer.liquid`
Expected: Only pre-existing baseline warnings (no new errors about unclosed tags or syntax).

- [ ] **Step 3: Commit**

```bash
git add snippets/cart-drawer.liquid
git commit -m "feat(lusena): add merge detection flags to cart drawer"
```

---

### Task 2: Cart drawer - merge card HTML

**Files:**
- Modify: `snippets/cart-drawer.liquid:1128-1412` (upsell zone area)

- [ ] **Step 1: Insert merge card rendering block**

Insert the following AFTER line 1128 (`{%- endfor -%}` end of cart items loop) and BEFORE line 1130 (`{%- if upsell_product_1 != blank -%}`):

```liquid
        {%- if show_merge -%}
          {%- liquid
            assign merge_bundle = all_products[merge_bundle_handle]
            assign merge_variant = merge_bundle.selected_or_first_available_variant

            comment Extract color from merge_item_1 endcomment
            assign merge_color_1 = ''
            for option in merge_item_1.product.options_with_values
              assign opt_down = option.name | downcase
              assign is_color = false
              if opt_down contains 'color'
                assign is_color = true
              else
                if opt_down contains 'colour'
                  assign is_color = true
                else
                  if opt_down contains 'kolor'
                    assign is_color = true
                  endif
                endif
              endif
              if is_color
                assign cpos = forloop.index
                if cpos == 1
                  assign merge_color_1 = merge_item_1.variant.option1
                elsif cpos == 2
                  assign merge_color_1 = merge_item_1.variant.option2
                elsif cpos == 3
                  assign merge_color_1 = merge_item_1.variant.option3
                endif
                break
              endif
            endfor

            comment Extract color from merge_item_2 endcomment
            assign merge_color_2 = ''
            for option in merge_item_2.product.options_with_values
              assign opt_down = option.name | downcase
              assign is_color = false
              if opt_down contains 'color'
                assign is_color = true
              else
                if opt_down contains 'colour'
                  assign is_color = true
                else
                  if opt_down contains 'kolor'
                    assign is_color = true
                  endif
                endif
              endif
              if is_color
                assign cpos = forloop.index
                if cpos == 1
                  assign merge_color_2 = merge_item_2.variant.option1
                elsif cpos == 2
                  assign merge_color_2 = merge_item_2.variant.option2
                elsif cpos == 3
                  assign merge_color_2 = merge_item_2.variant.option3
                endif
                break
              endif
            endfor

            comment Build Simple Bundles properties JSON endcomment
            assign merge_props_json = ''
            assign merge_selection_parts = ''
            assign sb_options = merge_variant.metafields.simple_bundles.variant_options.value
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

                comment Match slot to cart item by title substring endcomment
                assign slot_lower = opt_clean | downcase
                assign title_1_lower = merge_item_1.product.title | downcase
                assign this_color = merge_color_2
                if title_1_lower contains slot_lower
                  assign this_color = merge_color_1
                endif

                assign prop_entry = '"' | append: opt_clean | append: '":"' | append: this_color | append: '"'
                if merge_props_json == ''
                  assign merge_props_json = prop_entry
                else
                  assign merge_props_json = merge_props_json | append: ',' | append: prop_entry
                endif

                if merge_selection_parts == ''
                  assign merge_selection_parts = this_color
                else
                  assign merge_selection_parts = merge_selection_parts | append: ' <> ' | append: this_color
                endif
              endfor

              assign merge_props_json = '{' | append: merge_props_json | append: ',"_bundle_selection":"' | append: merge_selection_parts | append: '"}'
            endif

            comment Calculate pricing endcomment
            assign merge_bundle_price = merge_variant.price
            assign merge_original_cents = merge_bundle.metafields.lusena.bundle_original_price.value | times: 100
            assign merge_savings = merge_original_cents | minus: merge_bundle_price

            comment Build replace keys JSON array endcomment
            assign merge_replace_keys = '["' | append: merge_item_1.key | append: '","' | append: merge_item_2.key | append: '"]'
          -%}
          <div class="lusena-cart-drawer__upsell" data-cart-upsell-zone aria-live="polite">
            <p class="lusena-cart-drawer__upsell-label">Korzystniej w zestawie</p>
            <div class="lusena-upsell-card"
                 data-bundle-nudge
                 data-bundle-variant-id="{{ merge_variant.id }}"
                 data-replace-keys="{{ merge_replace_keys | escape }}"
                 {%- if merge_props_json != '' %} data-properties="{{ merge_props_json | escape }}"{% endif -%}
                 aria-label="Propozycja zestawu">
              <p class="lusena-upsell-card__bn-headline">
                Zamień na zestaw i zaoszczędź {{ merge_savings | money_without_trailing_zeros }}
              </p>
              <div class="lusena-upsell-card__bn-tiles">
                <div class="lusena-upsell-card__bn-have">
                  <div class="lusena-upsell-card__bn-have-img">
                    {%- if merge_item_1.product.featured_image -%}
                      <img
                        src="{{ merge_item_1.product.featured_image | image_url: width: 120 }}"
                        alt="{{ merge_item_1.product.featured_image.alt | escape }}"
                        loading="lazy" width="38"
                        height="{{ 38 | divided_by: merge_item_1.product.featured_image.aspect_ratio | ceil }}"
                      >
                    {%- endif -%}
                    <span class="lusena-upsell-card__bn-check" aria-hidden="true">
                      {% render 'lusena-icon', name: 'check', stroke_width: 3 %}
                    </span>
                  </div>
                  <p class="lusena-upsell-card__bn-have-name">{{ merge_item_1.product.title | escape }}</p>
                  <p class="lusena-upsell-card__bn-have-status">W koszyku</p>
                </div>
                <span class="lusena-upsell-card__bn-plus" aria-hidden="true">+</span>
                <div class="lusena-upsell-card__bn-have">
                  <div class="lusena-upsell-card__bn-have-img">
                    {%- if merge_item_2.product.featured_image -%}
                      <img
                        src="{{ merge_item_2.product.featured_image | image_url: width: 120 }}"
                        alt="{{ merge_item_2.product.featured_image.alt | escape }}"
                        loading="lazy" width="38"
                        height="{{ 38 | divided_by: merge_item_2.product.featured_image.aspect_ratio | ceil }}"
                      >
                    {%- endif -%}
                    <span class="lusena-upsell-card__bn-check" aria-hidden="true">
                      {% render 'lusena-icon', name: 'check', stroke_width: 3 %}
                    </span>
                  </div>
                  <p class="lusena-upsell-card__bn-have-name">{{ merge_item_2.product.title | escape }}</p>
                  <p class="lusena-upsell-card__bn-have-status">W koszyku</p>
                </div>
              </div>
              <div class="lusena-upsell-card__bn-bottom">
                <div class="lusena-upsell-card__bn-pricing">
                  <span class="lusena-upsell-card__bn-price">{{ merge_bundle_price | money_without_trailing_zeros }}</span>
                  <span class="lusena-upsell-card__bn-was">{{ merge_original_cents | money_without_trailing_zeros }}</span>
                </div>
                <button type="button"
                        class="lusena-btn lusena-btn--outline lusena-btn--size-xs"
                        data-bundle-nudge-action>
                  <span class="lusena-btn__content">Zamień na zestaw</span>
                  <span class="loading__spinner hidden">
                    <span class="lusena-btn__loading-dots" aria-hidden="true">
                      <span></span><span></span><span></span>
                    </span>
                  </span>
                </button>
              </div>
            </div>
          </div>
        {%- endif -%}
```

- [ ] **Step 2: Wrap existing nudge in `unless show_merge`**

Find the existing nudge guard (currently at line 1130, but shifted by the insertion above):

```liquid
        {%- if upsell_product_1 != blank -%}
```

Wrap it and its closing `{%- endif -%}` (at line 1412, shifted) with:

```liquid
        {%- unless show_merge -%}
        {%- if upsell_product_1 != blank -%}
          ... (all existing nudge code, unchanged) ...
        {%- endif -%}
        {%- endunless -%}
```

The `{%- unless show_merge -%}` goes immediately before `{%- if upsell_product_1 != blank -%}`, and `{%- endunless -%}` goes immediately after the matching `{%- endif -%}`.

- [ ] **Step 3: Verify syntax**

Run: `shopify theme check snippets/cart-drawer.liquid`
Expected: Only pre-existing baseline warnings.

- [ ] **Step 4: Commit**

```bash
git add snippets/cart-drawer.liquid
git commit -m "feat(lusena): add merge card HTML to cart drawer"
```

---

### Task 3: Cart drawer - JS handler modification

**Files:**
- Modify: `snippets/cart-drawer.liquid` (JS block, around original line 1679-1750, shifted by earlier insertions)

- [ ] **Step 1: Replace the swap call and property logic in the click handler**

Find this code in the bundle nudge click handler:

```javascript
      var triggerColor = nudge.dataset.triggerColor;
      var propertyMapRaw = nudge.dataset.propertyMap;
      if (triggerColor && propertyMapRaw) {
        try {
          var components = JSON.parse(propertyMapRaw);
          var props = {};
          var selectionParts = [];

          // Detect multi-pack: all components have identical value lists
          var isMultiPack = components.length > 1 && components.every(function(c) {
            return c.values.join(',') === components[0].values.join(',');
          });

          if (isMultiPack) {
            // Distribute unique colors: trigger first, then remaining unused
            var usedColors = [];
            components.forEach(function(comp, idx) {
              var color;
              if (idx === 0) {
                color = comp.values.indexOf(triggerColor) !== -1 ? triggerColor : comp.values[0];
              } else {
                color = comp.values.find(function(v) { return usedColors.indexOf(v) === -1; });
                if (!color) color = comp.values[0];
              }
              usedColors.push(color);
              props[comp.key] = color;
              selectionParts.push(color);
            });
          } else {
            // Complementary: match trigger color per component (fallback to first available)
            components.forEach(function(comp) {
              var color = comp.values.indexOf(triggerColor) !== -1 ? triggerColor : comp.values[0];
              props[comp.key] = color;
              selectionParts.push(color);
            });
          }

          props['_bundle_selection'] = selectionParts.join(' <> ');
          swapOpts.properties = props;
        } catch (e) { /* ignore parse errors */ }
      }

      LusenaBundle.swap(nudge.dataset.bundleVariantId, [nudge.dataset.replaceKey], swapOpts)
```

Replace with:

```javascript
      // Merge path: pre-filled properties + multiple replace keys
      var removeKeys;
      if (nudge.dataset.replaceKeys) {
        removeKeys = JSON.parse(nudge.dataset.replaceKeys);
        if (nudge.dataset.properties) {
          try { swapOpts.properties = JSON.parse(nudge.dataset.properties); } catch(e) {}
        }
      } else {
        // Existing nudge path: single replace key + color matching
        removeKeys = [nudge.dataset.replaceKey];
        var triggerColor = nudge.dataset.triggerColor;
        var propertyMapRaw = nudge.dataset.propertyMap;
        if (triggerColor && propertyMapRaw) {
          try {
            var components = JSON.parse(propertyMapRaw);
            var props = {};
            var selectionParts = [];

            // Detect multi-pack: all components have identical value lists
            var isMultiPack = components.length > 1 && components.every(function(c) {
              return c.values.join(',') === components[0].values.join(',');
            });

            if (isMultiPack) {
              // Distribute unique colors: trigger first, then remaining unused
              var usedColors = [];
              components.forEach(function(comp, idx) {
                var color;
                if (idx === 0) {
                  color = comp.values.indexOf(triggerColor) !== -1 ? triggerColor : comp.values[0];
                } else {
                  color = comp.values.find(function(v) { return usedColors.indexOf(v) === -1; });
                  if (!color) color = comp.values[0];
                }
                usedColors.push(color);
                props[comp.key] = color;
                selectionParts.push(color);
              });
            } else {
              // Complementary: match trigger color per component (fallback to first available)
              components.forEach(function(comp) {
                var color = comp.values.indexOf(triggerColor) !== -1 ? triggerColor : comp.values[0];
                props[comp.key] = color;
                selectionParts.push(color);
              });
            }

            props['_bundle_selection'] = selectionParts.join(' <> ');
            swapOpts.properties = props;
          } catch (e) { /* ignore parse errors */ }
        }
      }

      LusenaBundle.swap(nudge.dataset.bundleVariantId, removeKeys, swapOpts)
```

The key changes are:
1. Added `removeKeys` variable — merge path parses `data-replace-keys` JSON array, nudge path wraps `data-replace-key` in single-element array
2. Added merge properties path — reads pre-filled `data-properties` directly
3. Existing color matching logic moved into the `else` branch (unchanged)
4. Swap call uses `removeKeys` variable instead of `[nudge.dataset.replaceKey]`

- [ ] **Step 2: Commit**

```bash
git add snippets/cart-drawer.liquid
git commit -m "feat(lusena): extend drawer JS handler for merge path"
```

---

### Task 4: Cart page - merge detection

**Files:**
- Modify: `sections/lusena-cart-items.liquid:15-134` (initial Liquid block)

- [ ] **Step 1: Add merge handle detection to initial Liquid block**

Insert the following after line 39 (after the `endfor` of the suppress loop, before `assign trigger_product = nil`):

```liquid
  comment
    Merge detection: flag which bundle components are in cart.
    Checked later (before regular nudge) to offer bundle merge.
  endcomment
  assign merge_has_poszewka = false
  assign merge_has_bonnet = false
  assign merge_has_maska = false
  assign merge_has_nocna_rutyna = false
  assign merge_has_piekny_sen = false
  assign merge_poszewka_item = blank
  assign merge_bonnet_item = blank
  assign merge_maska_item = blank

  for item in cart.items
    case item.product.handle
      when 'poszewka-jedwabna'
        assign merge_has_poszewka = true
        assign merge_poszewka_item = item
      when 'czepek-jedwabny'
        assign merge_has_bonnet = true
        assign merge_bonnet_item = item
      when 'jedwabna-maska-3d'
        assign merge_has_maska = true
        assign merge_maska_item = item
      when 'nocna-rutyna'
        assign merge_has_nocna_rutyna = true
      when 'piekny-sen'
        assign merge_has_piekny_sen = true
    endcase
  endfor

  assign show_merge = false
  assign merge_bundle_handle = ''
  assign merge_item_1 = blank
  assign merge_item_2 = blank

  if upsell_enabled
    if merge_has_poszewka and merge_has_bonnet and merge_has_nocna_rutyna == false
      assign show_merge = true
      assign merge_bundle_handle = 'nocna-rutyna'
      assign merge_item_1 = merge_poszewka_item
      assign merge_item_2 = merge_bonnet_item
    elsif merge_has_poszewka and merge_has_maska and merge_has_piekny_sen == false
      assign show_merge = true
      assign merge_bundle_handle = 'piekny-sen'
      assign merge_item_1 = merge_poszewka_item
      assign merge_item_2 = merge_maska_item
    endif
  endif
```

- [ ] **Step 2: Commit**

```bash
git add sections/lusena-cart-items.liquid
git commit -m "feat(lusena): add merge detection flags to cart page"
```

---

### Task 5: Cart page - merge card HTML

**Files:**
- Modify: `sections/lusena-cart-items.liquid:280-555` (upsell area)

- [ ] **Step 1: Insert merge card rendering block**

Insert the following AFTER line 281 (`</div>` closing the items container) and BEFORE line 283 (`{%- if upsell_product != blank -%}`):

```liquid
            {%- if show_merge -%}
              {%- liquid
                assign merge_bundle = all_products[merge_bundle_handle]
                assign merge_variant = merge_bundle.selected_or_first_available_variant

                comment Extract color from merge_item_1 endcomment
                assign merge_color_1 = ''
                for option in merge_item_1.product.options_with_values
                  assign opt_down = option.name | downcase
                  assign is_color = false
                  if opt_down contains 'color'
                    assign is_color = true
                  else
                    if opt_down contains 'colour'
                      assign is_color = true
                    else
                      if opt_down contains 'kolor'
                        assign is_color = true
                      endif
                    endif
                  endif
                  if is_color
                    assign cpos = forloop.index
                    if cpos == 1
                      assign merge_color_1 = merge_item_1.variant.option1
                    elsif cpos == 2
                      assign merge_color_1 = merge_item_1.variant.option2
                    elsif cpos == 3
                      assign merge_color_1 = merge_item_1.variant.option3
                    endif
                    break
                  endif
                endfor

                comment Extract color from merge_item_2 endcomment
                assign merge_color_2 = ''
                for option in merge_item_2.product.options_with_values
                  assign opt_down = option.name | downcase
                  assign is_color = false
                  if opt_down contains 'color'
                    assign is_color = true
                  else
                    if opt_down contains 'colour'
                      assign is_color = true
                    else
                      if opt_down contains 'kolor'
                        assign is_color = true
                      endif
                    endif
                  endif
                  if is_color
                    assign cpos = forloop.index
                    if cpos == 1
                      assign merge_color_2 = merge_item_2.variant.option1
                    elsif cpos == 2
                      assign merge_color_2 = merge_item_2.variant.option2
                    elsif cpos == 3
                      assign merge_color_2 = merge_item_2.variant.option3
                    endif
                    break
                  endif
                endfor

                comment Build Simple Bundles properties JSON endcomment
                assign merge_props_json = ''
                assign merge_selection_parts = ''
                assign sb_options = merge_variant.metafields.simple_bundles.variant_options.value
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

                    comment Match slot to cart item by title substring endcomment
                    assign slot_lower = opt_clean | downcase
                    assign title_1_lower = merge_item_1.product.title | downcase
                    assign this_color = merge_color_2
                    if title_1_lower contains slot_lower
                      assign this_color = merge_color_1
                    endif

                    assign prop_entry = '"' | append: opt_clean | append: '":"' | append: this_color | append: '"'
                    if merge_props_json == ''
                      assign merge_props_json = prop_entry
                    else
                      assign merge_props_json = merge_props_json | append: ',' | append: prop_entry
                    endif

                    if merge_selection_parts == ''
                      assign merge_selection_parts = this_color
                    else
                      assign merge_selection_parts = merge_selection_parts | append: ' <> ' | append: this_color
                    endif
                  endfor

                  assign merge_props_json = '{' | append: merge_props_json | append: ',"_bundle_selection":"' | append: merge_selection_parts | append: '"}'
                endif

                comment Calculate pricing endcomment
                assign merge_bundle_price = merge_variant.price
                assign merge_original_cents = merge_bundle.metafields.lusena.bundle_original_price.value | times: 100
                assign merge_savings = merge_original_cents | minus: merge_bundle_price

                comment Build replace keys JSON array endcomment
                assign merge_replace_keys = '["' | append: merge_item_1.key | append: '","' | append: merge_item_2.key | append: '"]'
              -%}
              <div class="lusena-cart-upsell" aria-live="polite">
                <p class="lusena-cart-upsell__label">Korzystniej w zestawie</p>
                <div class="lusena-upsell-card"
                     data-bundle-nudge
                     data-bundle-variant-id="{{ merge_variant.id }}"
                     data-replace-keys="{{ merge_replace_keys | escape }}"
                     {%- if merge_props_json != '' %} data-properties="{{ merge_props_json | escape }}"{% endif -%}
                     aria-label="Propozycja zestawu">
                  <p class="lusena-upsell-card__bn-headline">
                    Zamień na zestaw i zaoszczędź {{ merge_savings | money_without_trailing_zeros }}
                  </p>
                  <div class="lusena-upsell-card__bn-tiles">
                    <div class="lusena-upsell-card__bn-have">
                      <div class="lusena-upsell-card__bn-have-img">
                        {%- if merge_item_1.product.featured_image -%}
                          <img
                            src="{{ merge_item_1.product.featured_image | image_url: width: 120 }}"
                            alt="{{ merge_item_1.product.featured_image.alt | escape }}"
                            loading="lazy" width="38"
                            height="{{ 38 | divided_by: merge_item_1.product.featured_image.aspect_ratio | ceil }}"
                          >
                        {%- endif -%}
                        <span class="lusena-upsell-card__bn-check" aria-hidden="true">
                          {% render 'lusena-icon', name: 'check', stroke_width: 3 %}
                        </span>
                      </div>
                      <p class="lusena-upsell-card__bn-have-name">{{ merge_item_1.product.title | escape }}</p>
                      <p class="lusena-upsell-card__bn-have-status">W koszyku</p>
                    </div>
                    <span class="lusena-upsell-card__bn-plus" aria-hidden="true">+</span>
                    <div class="lusena-upsell-card__bn-have">
                      <div class="lusena-upsell-card__bn-have-img">
                        {%- if merge_item_2.product.featured_image -%}
                          <img
                            src="{{ merge_item_2.product.featured_image | image_url: width: 120 }}"
                            alt="{{ merge_item_2.product.featured_image.alt | escape }}"
                            loading="lazy" width="38"
                            height="{{ 38 | divided_by: merge_item_2.product.featured_image.aspect_ratio | ceil }}"
                          >
                        {%- endif -%}
                        <span class="lusena-upsell-card__bn-check" aria-hidden="true">
                          {% render 'lusena-icon', name: 'check', stroke_width: 3 %}
                        </span>
                      </div>
                      <p class="lusena-upsell-card__bn-have-name">{{ merge_item_2.product.title | escape }}</p>
                      <p class="lusena-upsell-card__bn-have-status">W koszyku</p>
                    </div>
                  </div>
                  <div class="lusena-upsell-card__bn-bottom">
                    <div class="lusena-upsell-card__bn-pricing">
                      <span class="lusena-upsell-card__bn-price">{{ merge_bundle_price | money_without_trailing_zeros }}</span>
                      <span class="lusena-upsell-card__bn-was">{{ merge_original_cents | money_without_trailing_zeros }}</span>
                    </div>
                    <button type="button"
                            class="lusena-btn lusena-btn--outline lusena-btn--size-xs"
                            data-bundle-nudge-action>
                      <span class="lusena-btn__content">Zamień na zestaw</span>
                      <span class="loading__spinner hidden">
                        <span class="lusena-btn__loading-dots" aria-hidden="true">
                          <span></span><span></span><span></span>
                        </span>
                      </span>
                    </button>
                  </div>
                </div>
              </div>
            {%- endif -%}
```

- [ ] **Step 2: Wrap existing nudge in `unless show_merge`**

Find the existing nudge guard (currently at line 283, shifted by insertion):

```liquid
            {%- if upsell_product != blank -%}
```

Wrap it and its closing `{%- endif -%}` (at line 555, shifted) with:

```liquid
            {%- unless show_merge -%}
            {%- if upsell_product != blank -%}
              ... (all existing nudge code, unchanged) ...
            {%- endif -%}
            {%- endunless -%}
```

- [ ] **Step 3: Verify syntax**

Run: `shopify theme check sections/lusena-cart-items.liquid`
Expected: Only pre-existing baseline warnings.

- [ ] **Step 4: Commit**

```bash
git add sections/lusena-cart-items.liquid
git commit -m "feat(lusena): add merge card HTML to cart page"
```

---

### Task 6: Cart page - JS handler modification

**Files:**
- Modify: `sections/lusena-cart-items.liquid` (JS block, around original line 628-695, shifted)

- [ ] **Step 1: Replace the swap call and property logic**

Find this code in the bundle nudge click handler (same pattern as drawer):

```javascript
      var triggerColor = nudge.dataset.triggerColor;
      var propertyMapRaw = nudge.dataset.propertyMap;
      if (triggerColor && propertyMapRaw) {
        try {
          var components = JSON.parse(propertyMapRaw);
          var props = {};
          var selectionParts = [];

          // Detect multi-pack: all components have identical value lists
          var isMultiPack = components.length > 1 && components.every(function(c) {
            return c.values.join(',') === components[0].values.join(',');
          });

          if (isMultiPack) {
            // Distribute unique colors: trigger first, then remaining unused
            var usedColors = [];
            components.forEach(function(comp, idx) {
              var color;
              if (idx === 0) {
                color = comp.values.indexOf(triggerColor) !== -1 ? triggerColor : comp.values[0];
              } else {
                color = comp.values.find(function(v) { return usedColors.indexOf(v) === -1; });
                if (!color) color = comp.values[0];
              }
              usedColors.push(color);
              props[comp.key] = color;
              selectionParts.push(color);
            });
          } else {
            // Complementary: match trigger color per component (fallback to first available)
            components.forEach(function(comp) {
              var color = comp.values.indexOf(triggerColor) !== -1 ? triggerColor : comp.values[0];
              props[comp.key] = color;
              selectionParts.push(color);
            });
          }

          props['_bundle_selection'] = selectionParts.join(' <> ');
          swapOpts.properties = props;
        } catch (e) { /* ignore parse errors */ }
      }

      try {
        var state = await LusenaBundle.swap(nudge.dataset.bundleVariantId, [nudge.dataset.replaceKey], swapOpts);
```

Replace with:

```javascript
      // Merge path: pre-filled properties + multiple replace keys
      var removeKeys;
      if (nudge.dataset.replaceKeys) {
        removeKeys = JSON.parse(nudge.dataset.replaceKeys);
        if (nudge.dataset.properties) {
          try { swapOpts.properties = JSON.parse(nudge.dataset.properties); } catch(e) {}
        }
      } else {
        // Existing nudge path: single replace key + color matching
        removeKeys = [nudge.dataset.replaceKey];
        var triggerColor = nudge.dataset.triggerColor;
        var propertyMapRaw = nudge.dataset.propertyMap;
        if (triggerColor && propertyMapRaw) {
          try {
            var components = JSON.parse(propertyMapRaw);
            var props = {};
            var selectionParts = [];

            // Detect multi-pack: all components have identical value lists
            var isMultiPack = components.length > 1 && components.every(function(c) {
              return c.values.join(',') === components[0].values.join(',');
            });

            if (isMultiPack) {
              // Distribute unique colors: trigger first, then remaining unused
              var usedColors = [];
              components.forEach(function(comp, idx) {
                var color;
                if (idx === 0) {
                  color = comp.values.indexOf(triggerColor) !== -1 ? triggerColor : comp.values[0];
                } else {
                  color = comp.values.find(function(v) { return usedColors.indexOf(v) === -1; });
                  if (!color) color = comp.values[0];
                }
                usedColors.push(color);
                props[comp.key] = color;
                selectionParts.push(color);
              });
            } else {
              // Complementary: match trigger color per component (fallback to first available)
              components.forEach(function(comp) {
                var color = comp.values.indexOf(triggerColor) !== -1 ? triggerColor : comp.values[0];
                props[comp.key] = color;
                selectionParts.push(color);
              });
            }

            props['_bundle_selection'] = selectionParts.join(' <> ');
            swapOpts.properties = props;
          } catch (e) { /* ignore parse errors */ }
        }
      }

      try {
        var state = await LusenaBundle.swap(nudge.dataset.bundleVariantId, removeKeys, swapOpts);
```

- [ ] **Step 2: Commit**

```bash
git add sections/lusena-cart-items.liquid
git commit -m "feat(lusena): extend cart page JS handler for merge path"
```

---

### Task 7: Manual testing

- [ ] **Step 1: Start dev server**

Run: `shopify theme dev` (if not already running)

- [ ] **Step 2: Test merge card appearance - Nocna Rutyna**

1. Add poszewka jedwabna to cart (any color)
2. Add silk bonnet to cart (any color)
3. Open cart drawer
Expected: Merge card appears with:
- Label "Korzystniej w zestawie"
- Headline "Zamień na zestaw i zaoszczędź 109,00 zł" (or computed savings)
- Two tiles: poszewka image + "W koszyku" and bonnet image + "W koszyku"
- Plus sign between tiles
- Bottom: bundle price + crossed-out original + "Zamień na zestaw" button
4. Navigate to /cart
Expected: Same merge card on cart page

- [ ] **Step 3: Test merge swap - Nocna Rutyna**

1. With poszewka + bonnet in cart, click "Zamień na zestaw" on the merge card
Expected:
- Both individual items removed from cart
- Nocna Rutyna bundle added
- Cart re-renders showing the bundle line item
- Bundle has correct color properties from the individual items

- [ ] **Step 4: Test merge card appearance - Piękny Sen**

1. Clear cart
2. Add poszewka jedwabna to cart
3. Add jedwabna maska 3D to cart
4. Open cart drawer
Expected: Merge card for Piękny Sen with savings ~89 zł

- [ ] **Step 5: Test conflict resolution (3 items)**

1. Clear cart
2. Add poszewka, bonnet, and maska to cart
3. Open cart drawer
Expected: Nocna Rutyna merge card (109 zł > 89 zł), NOT Piękny Sen

- [ ] **Step 6: Test no merge when bundle already in cart**

1. Clear cart
2. Add Nocna Rutyna bundle to cart
3. Add poszewka to cart
4. Add bonnet to cart
Expected: NO merge card (Nocna Rutyna already in cart, detected by handle check). Regular nudge suppressed by `upsell_role == 'bundle'`.

- [ ] **Step 7: Test regular nudge still works**

1. Clear cart
2. Add poszewka alone to cart
3. Open cart drawer
Expected: Regular bundle nudge "Dodaj bonnet i zaoszczędź 109 zł" (NOT merge card)

- [ ] **Step 8: Test bidirectional sync**

1. Add poszewka + bonnet to cart
2. On cart page, click "Zamień na zestaw"
Expected: Cart drawer updates (via pubsub sync) — no longer shows merge card, shows Nocna Rutyna bundle

- [ ] **Step 9: Run theme check**

Run: `shopify theme check`
Expected: Only pre-existing baseline warnings.

- [ ] **Step 10: Commit final state**

```bash
git add -A
git commit -m "feat(lusena): #13 cart merge - detect both bundle components and offer merge"
```

---

### Task 8: Update memory bank

- [ ] **Step 1: Update activeContext.md**

Update `memory-bank/activeContext.md`:
- Move #13 cart merge to "Recent completed work"
- Update "Next steps" to show Phase 1B PDP cross-sell checkbox as next
- Remove #13 from known issues (swap race condition now handled)

- [ ] **Step 2: Update progress.md**

Update `memory-bank/progress.md`:
- Mark #13 cart merge as DONE

- [ ] **Step 3: Commit docs**

```bash
git add memory-bank/activeContext.md memory-bank/progress.md
git commit -m "docs: update memory bank after #13 cart merge"
```
