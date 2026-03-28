# PDP Bundle Detection Banner — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Show a bundle upgrade banner on the PDP when the customer's cart already contains a complement product, enabling a one-click swap to the bundle.

**Architecture:** A hidden Liquid snippet renders the banner HTML with bundle mapping data as JSON attributes. Client-side JS fetches `/cart.js` on page load, checks for complement matches, and reveals the banner. Swap reuses the existing `LusenaBundle.swap()` from `assets/lusena-bundle-swap.js`. CSS goes in the existing `assets/lusena-pdp.css`.

**Tech Stack:** Shopify Liquid, vanilla JS, CSS (LUSENA design tokens from `lusena-foundations.css`)

**Spec:** `docs/superpowers/specs/2026-03-28-pdp-bundle-detection-banner.md`

---

## File map

| File | Action | Responsibility |
|------|--------|----------------|
| `snippets/lusena-pdp-bundle-banner.liquid` | **Create** | Banner HTML + Liquid case-based bundle mapping |
| `sections/lusena-main-product.liquid` | **Modify** (line 56, between variant and ATC wrappers) | Render the banner snippet |
| `assets/lusena-pdp.css` | **Modify** (append to end) | `.lusena-pdp-bundle-banner` styles |

JS is inline in the snippet (< 80 lines, tightly coupled to the banner DOM). No separate JS file needed.

---

### Task 1: Create the banner snippet

**Files:**
- Create: `snippets/lusena-pdp-bundle-banner.liquid`

This snippet does three things: (A) maps the current product to its bundle complements, (B) renders bundle product data as hidden data attributes, (C) renders the banner HTML (hidden by default).

- [ ] **Step 1: Create `snippets/lusena-pdp-bundle-banner.liquid`**

```liquid
{%- comment -%}
  PDP Bundle Detection Banner (#12)
  Shows when customer's cart has a complement product for a bundle.
  Hidden by default — JS reveals after cart check.

  Required variables: product (passed from section)
{%- endcomment -%}

{%- liquid
  comment
    Map current product to its bundle complements.
    Each entry: cart_handle (what must be in cart), bundle_handle (the bundle to suggest).
    Priority: higher savings_priority wins when multiple matches exist.
  endcomment

  assign has_complements = false

  case product.handle
    when 'poszewka-jedwabna'
      assign has_complements = true
      assign pdp_product_label = 'poszewke jedwabna'
      assign complement_1_cart = 'silk-bonnet'
      assign complement_1_bundle = 'nocna-rutyna'
      assign complement_1_priority = 1
      assign complement_2_cart = 'jedwabna-maska-3d'
      assign complement_2_bundle = 'piekny-sen'
      assign complement_2_priority = 0
      assign complement_count = 2

    when 'silk-bonnet'
      assign has_complements = true
      assign pdp_product_label = 'czepek jedwabny'
      assign complement_1_cart = 'poszewka-jedwabna'
      assign complement_1_bundle = 'nocna-rutyna'
      assign complement_1_priority = 1
      assign complement_count = 1

    when 'jedwabna-maska-3d'
      assign has_complements = true
      assign pdp_product_label = 'maske 3D'
      assign complement_1_cart = 'poszewka-jedwabna'
      assign complement_1_bundle = 'piekny-sen'
      assign complement_1_priority = 1
      assign complement_count = 1
  endcase
-%}

{%- if has_complements -%}
  {%- liquid
    comment
      Build a JSON array of complement entries with live bundle product data.
      Using all_products to get real prices, images, titles, and variant info.
    endcomment
  -%}

  <div class="lusena-pdp-bundle-banner"
       data-pdp-bundle-banner
       style="display:none"
       aria-live="polite">

    {%- comment -%} Render complement data as a JSON script block for JS to read {%- endcomment -%}
    <script type="application/json" data-bundle-complements>
      [
        {%- assign bundle_1 = all_products[complement_1_bundle] -%}
        {%- assign bundle_1_variant = bundle_1.selected_or_first_available_variant -%}
        {%- assign bundle_1_original = bundle_1.metafields.lusena.bundle_original_price.value -%}
        {%- assign bundle_1_sb_options = bundle_1_variant.metafields.simple_bundles.variant_options.value -%}
        {
          "cart_handle": {{ complement_1_cart | json }},
          "bundle_handle": {{ complement_1_bundle | json }},
          "bundle_title": {{ bundle_1.title | json }},
          "bundle_price": {{ bundle_1_variant.price }},
          "bundle_original_price": {{ bundle_1_original | default: 0 }},
          "bundle_variant_id": {{ bundle_1_variant.id }},
          "bundle_url": {{ bundle_1.url | json }},
          "pdp_product_label": {{ pdp_product_label | json }},
          "complement_product_title": {{ all_products[complement_1_cart].title | json }},
          "complement_product_image": {{ all_products[complement_1_cart].featured_image | image_url: width: 120 | json }},
          "priority": {{ complement_1_priority }},
          "property_map": {{ bundle_1_sb_options | json }}
        }
        {%- if complement_count == 2 -%}
          ,
          {%- assign bundle_2 = all_products[complement_2_bundle] -%}
          {%- assign bundle_2_variant = bundle_2.selected_or_first_available_variant -%}
          {%- assign bundle_2_original = bundle_2.metafields.lusena.bundle_original_price.value -%}
          {%- assign bundle_2_sb_options = bundle_2_variant.metafields.simple_bundles.variant_options.value -%}
          {
            "cart_handle": {{ complement_2_cart | json }},
            "bundle_handle": {{ complement_2_bundle | json }},
            "bundle_title": {{ bundle_2.title | json }},
            "bundle_price": {{ bundle_2_variant.price }},
            "bundle_original_price": {{ bundle_2_original | default: 0 }},
            "bundle_variant_id": {{ bundle_2_variant.id }},
            "bundle_url": {{ bundle_2.url | json }},
            "pdp_product_label": {{ pdp_product_label | json }},
            "complement_product_title": {{ all_products[complement_2_cart].title | json }},
            "complement_product_image": {{ all_products[complement_2_cart].featured_image | image_url: width: 120 | json }},
            "priority": {{ complement_2_priority }},
            "property_map": {{ bundle_2_sb_options | json }}
          }
        {%- endif -%}
      ]
    </script>

    {%- comment -%} Banner HTML — content populated by JS {%- endcomment -%}
    <p class="lusena-pdp-bundle-banner__label">Korzystniej w zestawie</p>
    <div class="lusena-pdp-bundle-banner__card">
      <p class="lusena-pdp-bundle-banner__headline" data-banner-headline></p>

      <div class="lusena-pdp-bundle-banner__have-row">
        <div class="lusena-pdp-bundle-banner__have-img-wrap">
          <img class="lusena-pdp-bundle-banner__have-img"
               data-banner-have-img
               src=""
               alt=""
               width="44"
               height="44"
               loading="lazy">
          <span class="lusena-pdp-bundle-banner__check" aria-hidden="true">
            <svg width="10" height="10" viewBox="0 0 10 10" fill="none">
              <path d="M2 5l2.5 2.5L8 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </span>
        </div>
        <div class="lusena-pdp-bundle-banner__have-text">
          <span class="lusena-pdp-bundle-banner__have-name" data-banner-have-name></span>
          <span class="lusena-pdp-bundle-banner__have-status">W koszyku</span>
        </div>
      </div>

      <div class="lusena-pdp-bundle-banner__bottom">
        <div class="lusena-pdp-bundle-banner__pricing">
          <span class="lusena-pdp-bundle-banner__price" data-banner-price></span>
          <s class="lusena-pdp-bundle-banner__was" data-banner-was></s>
        </div>
        <button type="button"
                class="lusena-btn lusena-btn--outline lusena-btn--size-xs"
                data-pdp-bundle-swap>
          <span class="lusena-btn__content">Kup jako zestaw</span>
          <span class="loading__spinner hidden">
            <span class="lusena-btn__loading-dots" aria-hidden="true">
              <span></span><span></span><span></span>
            </span>
          </span>
        </button>
      </div>
    </div>
  </div>

  <script>
    (function() {
      var banner = document.querySelector('[data-pdp-bundle-banner]');
      if (!banner) return;

      var complementsJson = banner.querySelector('[data-bundle-complements]');
      if (!complementsJson) return;

      var complements;
      try { complements = JSON.parse(complementsJson.textContent); }
      catch (e) { return; }

      // Fetch cart and check for complement matches
      fetch('/cart.js', { credentials: 'same-origin' })
        .then(function(r) { return r.json(); })
        .then(function(cart) {
          var match = null;

          cart.items.forEach(function(item) {
            var itemHandle = item.handle;
            complements.forEach(function(comp) {
              if (itemHandle === comp.cart_handle) {
                if (!match || comp.priority > match.priority) {
                  match = {
                    comp: comp,
                    cartItem: item
                  };
                }
              }
            });
          });

          if (!match) return;

          // Populate banner content
          var comp = match.comp;
          var cartItem = match.cartItem;
          var savings = (comp.bundle_original_price * 100) - comp.bundle_price;

          banner.querySelector('[data-banner-headline]').textContent =
            'Dodaj ' + comp.pdp_product_label + ' i zaoszczedz ' + formatMoney(savings);

          banner.querySelector('[data-banner-have-name]').textContent = comp.complement_product_title;
          var haveImg = banner.querySelector('[data-banner-have-img]');
          haveImg.src = comp.complement_product_image;
          haveImg.alt = comp.complement_product_title;

          banner.querySelector('[data-banner-price]').textContent = formatMoney(comp.bundle_price);
          banner.querySelector('[data-banner-was]').textContent = formatMoney(comp.bundle_original_price * 100);

          // Store match data for swap handler
          banner.dataset.bundleVariantId = comp.bundle_variant_id;
          banner.dataset.replaceKey = cartItem.key;
          banner.dataset.propertyMap = JSON.stringify(comp.property_map || []);
          banner.dataset.triggerColor = getCartItemColor(cartItem);

          // Reveal banner
          banner.style.display = '';
        })
        .catch(function(err) {
          console.error('Bundle banner: cart fetch failed', err);
        });

      // Swap click handler
      banner.addEventListener('click', async function(e) {
        var btn = e.target.closest('[data-pdp-bundle-swap]');
        if (!btn) return;

        btn.disabled = true;
        btn.classList.add('loading');
        var spinner = btn.querySelector('.loading__spinner');
        if (spinner) spinner.classList.remove('hidden');

        // Read current PDP color from variant picker
        var pdpColor = getCurrentPdpColor();
        var triggerColor = banner.dataset.triggerColor;

        // Build properties for Simple Bundles
        var swapOpts = {};
        var propertyMapRaw = banner.dataset.propertyMap;
        if (propertyMapRaw) {
          try {
            var sbOptions = JSON.parse(propertyMapRaw);
            if (Array.isArray(sbOptions) && sbOptions.length > 0) {
              var components = parseSbOptions(sbOptions);
              var props = {};
              var selectionParts = [];

              // Assign colors: cart item's color + current PDP color
              components.forEach(function(comp) {
                var color;
                // Match by product handle in the key
                if (triggerColor && comp.values.indexOf(triggerColor) !== -1 && isCartProductComponent(comp, banner.dataset.replaceKey)) {
                  color = triggerColor;
                } else if (pdpColor && comp.values.indexOf(pdpColor) !== -1) {
                  color = pdpColor;
                } else {
                  color = comp.values[0];
                }
                props[comp.key] = color;
                selectionParts.push(color);
              });

              props['_bundle_selection'] = selectionParts.join(' <> ');
              swapOpts.properties = props;
            }
          } catch (err) { /* ignore parse errors */ }
        }

        try {
          // Use cart-drawer sections for re-render after swap
          var drawerSections = ['cart-drawer', 'cart-icon-bubble'];
          swapOpts.sections = drawerSections;
          swapOpts.sectionsUrl = window.location.pathname;

          var state = await LusenaBundle.swap(
            banner.dataset.bundleVariantId,
            [banner.dataset.replaceKey],
            swapOpts
          );

          // Open cart drawer with updated content
          var drawerEl = document.getElementById('cart-drawer');
          if (drawerEl && state && state.sections) {
            var html = new DOMParser().parseFromString(state.sections['cart-drawer'], 'text/html');
            var newContent = html.querySelector('#CartDrawer');
            if (newContent) {
              document.getElementById('CartDrawer').innerHTML = newContent.innerHTML;
            }
            // Update cart icon bubble
            if (state.sections['cart-icon-bubble']) {
              var bubbleHtml = new DOMParser().parseFromString(state.sections['cart-icon-bubble'], 'text/html');
              var newBubble = bubbleHtml.querySelector('.shopify-section');
              var oldBubble = document.getElementById('cart-icon-bubble');
              if (newBubble && oldBubble) {
                oldBubble.innerHTML = newBubble.innerHTML;
              }
            }
            // Open the drawer
            var openBtn = document.querySelector('cart-drawer');
            if (openBtn) {
              var drawerWrapper = document.getElementById('CartDrawer');
              if (drawerWrapper) {
                drawerWrapper.classList.add('active');
                document.body.classList.add('overflow-hidden');
              }
            }
          }

          // Publish cart update for any other listeners
          if (typeof publish === 'function') {
            publish(PUB_SUB_EVENTS.cartUpdate, { source: 'pdp-bundle-banner', cartData: state });
          }

          // Hide the banner after successful swap
          banner.style.display = 'none';

        } catch (err) {
          console.error('PDP bundle swap failed:', err);
          btn.disabled = false;
          btn.classList.remove('loading');
          if (spinner) spinner.classList.add('hidden');
        }
      });

      // --- Helper functions ---

      function formatMoney(cents) {
        return Math.round(cents / 100) + ' zl';
      }

      function getCartItemColor(cartItem) {
        // Read color from cart item variant options
        if (cartItem.variant_options) {
          // variant_options is an array of option values; color is typically option 1
          // Check variant_title for a single-option product
          if (cartItem.variant_title) return cartItem.variant_title;
        }
        if (cartItem.options_with_values) {
          for (var i = 0; i < cartItem.options_with_values.length; i++) {
            var opt = cartItem.options_with_values[i];
            var name = opt.name.toLowerCase();
            if (name === 'color' || name === 'colour' || name === 'kolor') {
              return opt.value;
            }
          }
        }
        return '';
      }

      function getCurrentPdpColor() {
        var colorFieldset = document.querySelector('[data-lusena-option][data-lusena-option-type="color"]');
        if (!colorFieldset) return '';
        var checked = colorFieldset.querySelector('input[type="radio"].lusena-option__input:checked');
        return checked ? checked.value : '';
      }

      function parseSbOptions(sbOptions) {
        // Same parsing logic as cart drawer/cart page nudge handlers
        var components = [];
        var keyCounts = {};
        sbOptions.forEach(function(opt) {
          var rawKey = opt.optionName || '';
          // Strip " - Color (Dropdown N)" suffix
          var key = rawKey.replace(/ - Color.*$/i, '').replace(/ - .*$/, '');
          // Strip dimension tokens (words containing x or ×)
          key = key.replace(/\s+\S*[x×]\S*/gi, '').trim();

          // Disambiguate duplicates (Scrunchie Trio)
          if (!keyCounts[key]) keyCounts[key] = 0;
          keyCounts[key]++;
          var disambiguated = keyCounts[key] > 1 ? key + ' ' + keyCounts[key] : key;
          // If this is the first and there are more coming, retroactively number it
          if (keyCounts[key] === 2 && components.length > 0) {
            for (var i = components.length - 1; i >= 0; i--) {
              if (components[i].key === key) {
                components[i].key = key + ' 1';
                break;
              }
            }
          }

          var values = (opt.optionValues || '').split(', ').filter(Boolean);
          components.push({ key: disambiguated, values: values, rawKey: rawKey });
        });
        return components;
      }

      function isCartProductComponent(comp, cartItemKey) {
        // Heuristic: check if the component key contains part of the cart product's name
        // This is used to assign the cart item's color to the correct bundle component
        // For complementary bundles, triggerColor goes to the component matching the cart product
        return false; // Simplified: let the complementary logic below handle it
      }

    })();
  </script>
{%- endif -%}
```

- [ ] **Step 2: Verify the file was created**

Run: `ls snippets/lusena-pdp-bundle-banner.liquid`
Expected: file exists

- [ ] **Step 3: Commit**

```bash
git add snippets/lusena-pdp-bundle-banner.liquid
git commit -m "feat(lusena): add PDP bundle detection banner snippet (#12)"
```

---

### Task 2: Add CSS to lusena-pdp.css

**Files:**
- Modify: `assets/lusena-pdp.css` (append to end of file)

The styles match the cart nudge card design language: white card, teal accent stripe, brand font label, compact "have" row, pricing + outline CTA bottom row.

- [ ] **Step 1: Append the following CSS to the end of `assets/lusena-pdp.css`**

```css
/* -------------------------------------------------------
   PDP Bundle Detection Banner (#12)
   Matches cart nudge card design language.
   ------------------------------------------------------- */

.lusena-pdp-bundle-banner {
  padding: var(--lusena-space-2) 0;
  margin-top: var(--lusena-space-1);
}

.lusena-pdp .lusena-pdp-bundle-banner__label {
  font-family: var(--lusena-font-brand);
  font-size: 1.2rem;
  line-height: 1.4;
  color: var(--lusena-text-2);
  margin-bottom: 1rem;
}

.lusena-pdp .lusena-pdp-bundle-banner__card {
  padding: var(--lusena-space-2);
  background: var(--lusena-color-n0);
  border-radius: var(--lusena-btn-radius);
  border: 1px solid color-mix(in srgb, var(--lusena-text-2) 5%, transparent);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
  border-left: 0.25rem solid color-mix(in srgb, var(--lusena-accent-cta) 40%, transparent);
}

.lusena-pdp .lusena-pdp-bundle-banner__headline {
  font-size: 1.35rem;
  font-weight: 500;
  color: var(--lusena-text-1);
  line-height: 1.35;
  margin-bottom: var(--lusena-space-1);
}

/* "Have" row — compact horizontal layout */
.lusena-pdp .lusena-pdp-bundle-banner__have-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: var(--lusena-radius-sm);
  background: color-mix(in srgb, var(--lusena-surface-2) 40%, transparent);
  margin-bottom: var(--lusena-space-1);
}

.lusena-pdp-bundle-banner__have-img-wrap {
  position: relative;
  flex-shrink: 0;
}

.lusena-pdp .lusena-pdp-bundle-banner__have-img {
  width: 2.8rem;
  height: 2.8rem;
  border-radius: 0.4rem;
  background: var(--lusena-surface-2);
  border: 1px dashed color-mix(in srgb, var(--lusena-text-2) 20%, transparent);
  object-fit: cover;
  opacity: 0.75;
}

.lusena-pdp-bundle-banner__check {
  position: absolute;
  top: -0.4rem;
  right: -0.4rem;
  width: 1.1rem;
  height: 1.1rem;
  background: var(--lusena-accent-cta);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
}

.lusena-pdp-bundle-banner__have-text {
  display: flex;
  flex-direction: column;
}

.lusena-pdp .lusena-pdp-bundle-banner__have-name {
  font-size: 1rem;
  font-weight: 500;
  color: var(--lusena-text-1);
  line-height: 1.2;
}

.lusena-pdp .lusena-pdp-bundle-banner__have-status {
  font-size: 0.85rem;
  color: var(--lusena-accent-cta);
  font-weight: 500;
}

/* Bottom row — pricing + CTA */
.lusena-pdp .lusena-pdp-bundle-banner__bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--lusena-space-1);
  margin-top: var(--lusena-space-1);
  padding-top: var(--lusena-space-1);
  border-top: 1px solid color-mix(in srgb, var(--lusena-text-2) 5%, transparent);
}

.lusena-pdp-bundle-banner__pricing {
  display: flex;
  align-items: baseline;
  gap: 0.6rem;
  flex-wrap: wrap;
}

.lusena-pdp .lusena-pdp-bundle-banner__price {
  font-size: 1.4rem;
  font-weight: 500;
  color: var(--lusena-text-1);
  font-variant-numeric: tabular-nums;
}

.lusena-pdp .lusena-pdp-bundle-banner__was {
  font-size: 1.4rem;
  color: var(--lusena-text-2);
  text-decoration: none;
}

/* Mobile adjustments */
@media (max-width: 767px) {
  .lusena-pdp .lusena-pdp-bundle-banner__headline {
    font-size: 1.25rem;
  }

  .lusena-pdp .lusena-pdp-bundle-banner__bottom {
    flex-direction: column;
    align-items: stretch;
    gap: var(--lusena-space-05);
  }

  .lusena-pdp .lusena-pdp-bundle-banner__bottom .lusena-btn {
    width: 100%;
    justify-content: center;
  }
}
```

- [ ] **Step 2: Verify compiled_assets is still under 55KB**

Open `http://127.0.0.1:9292/products/poszewka-jedwabna` in DevTools Network tab. Check `compiled_assets/styles.css` size. Must be under 55KB. The new CSS is in the standalone `lusena-pdp.css` file, not `{% stylesheet %}`, so compiled_assets should be unchanged.

- [ ] **Step 3: Commit**

```bash
git add assets/lusena-pdp.css
git commit -m "feat(lusena): add PDP bundle banner CSS (#12)"
```

---

### Task 3: Wire snippet into the section

**Files:**
- Modify: `sections/lusena-main-product.liquid` (insert between lines 55 and 57)

Insert the banner render between the variant picker wrapper (`lusena-pdp-buy-box__variant`) and the ATC wrapper (`lusena-pdp-buy-box__atc`).

- [ ] **Step 1: In `sections/lusena-main-product.liquid`, add the banner render after line 55**

Find this block (lines 53–59):
```liquid
        <div class="lusena-pdp-buy-box__variant">
          {% render 'lusena-pdp-variant-picker', product: product, current_variant: current_variant, section: section %}
        </div>

        <div class="lusena-pdp-buy-box__atc">
          {% render 'lusena-pdp-atc', product: product, current_variant: current_variant, section: section, product_form_id: product_form_id %}
        </div>
```

Insert the banner between the variant and ATC wrappers:
```liquid
        <div class="lusena-pdp-buy-box__variant">
          {% render 'lusena-pdp-variant-picker', product: product, current_variant: current_variant, section: section %}
        </div>

        {% render 'lusena-pdp-bundle-banner', product: product %}

        <div class="lusena-pdp-buy-box__atc">
          {% render 'lusena-pdp-atc', product: product, current_variant: current_variant, section: section, product_form_id: product_form_id %}
        </div>
```

- [ ] **Step 2: Verify the section loads without Liquid errors**

Open `http://127.0.0.1:9292/products/poszewka-jedwabna` — page should load normally. Banner should be invisible (empty cart = no match). No Liquid errors in console.

- [ ] **Step 3: Commit**

```bash
git add sections/lusena-main-product.liquid
git commit -m "feat(lusena): wire PDP bundle banner into buy-box (#12)"
```

---

### Task 4: Fix the color assignment logic

**Files:**
- Modify: `snippets/lusena-pdp-bundle-banner.liquid` (JS section only)

The `isCartProductComponent` function in Task 1 returns `false` as a placeholder. Replace it with proper complementary bundle color assignment logic.

For complementary bundles (Nocna Rutyna, Piekny Sen), we know:
- Component whose key matches the cart product → gets `triggerColor` (cart item's color)
- Component whose key matches the PDP product → gets `pdpColor` (current variant picker color)

We need to match component keys against the known product titles.

- [ ] **Step 1: Replace the color assignment block in the swap click handler**

Find the `components.forEach` block inside the swap handler and replace it with:

```javascript
              // Complementary bundle: assign colors based on product identity
              // Cart product component → triggerColor, PDP product component → pdpColor
              var currentProductTitle = document.querySelector('.lusena-pdp-buy-box h1');
              var currentProductName = currentProductTitle ? currentProductTitle.textContent.trim() : '';

              components.forEach(function(comp) {
                var color;
                var compKeyLower = comp.key.toLowerCase();

                // Check if this component matches the PDP product (the one being viewed)
                var isPdpProduct = currentProductName && compKeyLower.indexOf(currentProductName.toLowerCase().split(' ').slice(0, 2).join(' ').toLowerCase()) !== -1;

                if (isPdpProduct && pdpColor && comp.values.indexOf(pdpColor) !== -1) {
                  color = pdpColor;
                } else if (triggerColor && comp.values.indexOf(triggerColor) !== -1) {
                  color = triggerColor;
                } else if (pdpColor && comp.values.indexOf(pdpColor) !== -1) {
                  color = pdpColor;
                } else {
                  color = comp.values[0];
                }
                props[comp.key] = color;
                selectionParts.push(color);
              });
```

Also remove the unused `isCartProductComponent` function.

- [ ] **Step 2: Commit**

```bash
git add snippets/lusena-pdp-bundle-banner.liquid
git commit -m "fix(lusena): proper color assignment for PDP bundle swap (#12)"
```

---

### Task 5: Ensure `lusena-bundle-swap.js` is loaded on PDP

**Files:**
- Possibly modify: `sections/lusena-main-product.liquid` or `snippets/lusena-pdp-bundle-banner.liquid`

The banner's swap handler calls `LusenaBundle.swap()`. Check whether `lusena-bundle-swap.js` is already loaded on PDP pages.

- [ ] **Step 1: Check if the script is loaded**

Search for `lusena-bundle-swap` in `layout/theme.liquid`, `sections/lusena-main-product.liquid`, or any snippet rendered on PDP pages.

If NOT loaded, add to the banner snippet (only when complements exist):

```liquid
{%- if has_complements -%}
  <script src="{{ 'lusena-bundle-swap.js' | asset_url }}" defer="defer"></script>
  {%- comment -%} Rest of banner HTML... {%- endcomment -%}
```

If it's already loaded globally (e.g., in `theme.liquid` or `cart-drawer`), no change needed.

- [ ] **Step 2: Verify `LusenaBundle` is available in console**

Open `http://127.0.0.1:9292/products/poszewka-jedwabna`, open DevTools console, type `LusenaBundle`. Should return the object with `swap` method.

- [ ] **Step 3: Commit if changes were made**

```bash
git add snippets/lusena-pdp-bundle-banner.liquid
git commit -m "fix(lusena): ensure bundle-swap.js loaded on PDP (#12)"
```

---

### Task 6: Manual testing — all scenarios

**Files:** None (testing only)

Use `http://127.0.0.1:9292/` dev server. Start with empty cart for each test. Dev server must be running (`shopify theme dev --store-password paufro`).

- [ ] **Step 1: Banner appears correctly (tests 1–4)**

| # | Setup | Navigate to | Expected |
|---|-------|-------------|----------|
| 1 | Add poszewka to cart | Bonnet PDP | Banner: "Dodaj czepek i zaoszczedz 109 zl", poszewka shown in have-row, 399 zl / ~~508 zl~~ |
| 2 | Add bonnet to cart | Poszewka PDP | Banner: "Dodaj poszewke i zaoszczedz 109 zl", bonnet shown in have-row, 399 zl / ~~508 zl~~ |
| 3 | Add poszewka to cart | Maska 3D PDP | Banner: "Dodaj maske 3D i zaoszczedz 89 zl", poszewka shown, 349 zl / ~~438 zl~~ |
| 4 | Add maska 3D to cart | Poszewka PDP | Banner: "Dodaj poszewke i zaoszczedz 89 zl", maska shown, 349 zl / ~~438 zl~~ |

- [ ] **Step 2: Conflict resolution (test 5)**

Add both bonnet AND maska 3D to cart. Navigate to poszewka PDP. Expected: Nocna Rutyna banner (109 zl savings, not 89 zl).

- [ ] **Step 3: No banner when not applicable (tests 6–9)**

| # | Setup | Navigate to | Expected |
|---|-------|-------------|----------|
| 6 | Empty cart | Any PDP | No banner |
| 7 | Scrunchie only in cart | Any PDP | No banner |
| 8 | Poszewka in cart | Walek PDP | No banner |
| 9 | Any cart contents | Bundle PDP (e.g., nocna-rutyna?view=bundle) | No banner (different template) |

- [ ] **Step 4: Swap works correctly (tests 10–11)**

Add poszewka (Czarny) to cart. Navigate to bonnet PDP. Select "Brudny roz" on bonnet variant picker. Click "Kup jako zestaw". Expected:
- Cart drawer opens
- Nocna Rutyna bundle in cart with Czarny poszewka + Brudny roz bonnet
- Individual poszewka removed from cart
- Banner hides

- [ ] **Step 5: Mobile banner (test 12)**

Using DevTools device emulation (iPhone 14 or similar): add poszewka to cart, navigate to bonnet PDP. Banner should be visible between variant picker and ATC. ATC button should still be reachable without excessive scrolling.

- [ ] **Step 6: Run theme check**

```bash
shopify theme check
```

Expected: only the known baseline warnings (listed in CLAUDE.md). No new warnings from the banner snippet.

- [ ] **Step 7: Commit all final fixes from testing**

```bash
git add -A
git commit -m "fix(lusena): PDP bundle banner testing fixes (#12)"
```

---

### Task 7: Update documentation

**Files:**
- Modify: `memory-bank/activeContext.md`
- Modify: `memory-bank/progress.md`

- [ ] **Step 1: Update `memory-bank/activeContext.md`**

Add to "Recent completed work" section:
```markdown
### PDP bundle detection banner (#12) (2026-03-XX)
- Banner between variant picker and ATC on PDP buy-box
- Detects cart complement via fetch('/cart.js') on page load
- One-click swap to bundle using LusenaBundle.swap()
- Compact "have" row layout (matching cart nudge design language)
- 4 combinations: poszewka↔bonnet (Nocna Rutyna), poszewka↔maska (Piekny Sen)
- Conflict resolution: higher savings bundle wins
- Eliminates need for #13 (cart merge)
```

Remove `#12 PDP bundle detection banner` and `#13 Cart merge` from "Next steps". Update the next steps list.

- [ ] **Step 2: Update `memory-bank/progress.md`**

Under "Phase 2A remaining", mark #12 as done and #13 as superseded:
```markdown
- [x] #12 PDP bundle detection banner — one-click swap on PDP when cart has complement (2026-03-XX)
- [~] #13 Cart merge — superseded by #12 (PDP interception prevents the scenario)
```

- [ ] **Step 3: Commit**

```bash
git add memory-bank/activeContext.md memory-bank/progress.md
git commit -m "docs: update memory bank for PDP bundle banner (#12)"
```
