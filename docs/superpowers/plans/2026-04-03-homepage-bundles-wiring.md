# Homepage Bundles Section — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the homepage bundles section from static text blocks to product-driven editorial cards with responsive mobile layout.

**Architecture:** The `lusena-bundles` section gets a new schema with product pickers (replacing hardcoded text), Liquid template reads real Shopify product data (prices, images, URLs) plus hand-crafted editorial copy from block settings. CSS adds mobile compact rows with SVG thumbnails. Template JSON wires up the 3 real bundle products.

**Tech Stack:** Shopify Liquid, CSS (standalone `lusena-bundles.css`), Shopify JSON templates

**Spec:** `docs/superpowers/specs/2026-04-03-homepage-bundles-section-design.md`

---

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| `sections/lusena-bundles.liquid` | Rewrite | Section template: product-driven blocks, responsive layout, image fallback chain, OOS handling |
| `assets/lusena-bundles.css` | Rewrite | All bundle card styles: desktop grid, mobile hero+compact, badge, SVG thumbnail, editorial line, OOS |
| `templates/index.json` | Modify | Wire 3 bundle products with editorial copy into the section |
| `assets/lusena-bundle-piekny-sen.svg` | Create | Owner-provided SVG for mobile compact row |
| `assets/lusena-bundle-scrunchie-trio.svg` | Create | Owner-provided SVG for mobile compact row |

---

### Task 1: Rewrite section schema with product pickers

**Files:**
- Modify: `sections/lusena-bundles.liquid` (lines 118-283 — the `{% schema %}` block)

- [ ] **Step 1: Replace the entire `{% schema %}` block**

Replace the schema starting at line 118 with:

```json
{% schema %}
{
  "name": "LUSENA Bundles",
  "tag": "section",
  "settings": [
    {
      "type": "header",
      "content": "Spacing overrides (0 = use global default)"
    },
    {
      "type": "range",
      "id": "padding_top",
      "label": "Padding top (desktop)",
      "min": 0,
      "max": 240,
      "step": 4,
      "unit": "px",
      "default": 0
    },
    {
      "type": "range",
      "id": "padding_bottom",
      "label": "Padding bottom (desktop)",
      "min": 0,
      "max": 240,
      "step": 4,
      "unit": "px",
      "default": 0
    },
    {
      "type": "range",
      "id": "padding_top_mobile",
      "label": "Padding top (mobile)",
      "min": 0,
      "max": 240,
      "step": 4,
      "unit": "px",
      "default": 0
    },
    {
      "type": "range",
      "id": "padding_bottom_mobile",
      "label": "Padding bottom (mobile)",
      "min": 0,
      "max": 240,
      "step": 4,
      "unit": "px",
      "default": 0
    },
    {
      "type": "text",
      "id": "kicker",
      "label": "Kicker",
      "default": "Zestawy Premium"
    },
    {
      "type": "textarea",
      "id": "heading",
      "label": "Heading",
      "default": "Zbuduj swoją nocną rutynę"
    },
    {
      "type": "text",
      "id": "body",
      "label": "Body",
      "default": "Każdy zestaw to gotowy pomysł - na nocną rutynę albo idealny prezent."
    }
  ],
  "blocks": [
    {
      "type": "bundle_card",
      "name": "Bundle card",
      "limit": 3,
      "settings": [
        {
          "type": "product",
          "id": "product",
          "label": "Bundle product"
        },
        {
          "type": "text",
          "id": "contents",
          "label": "What's inside",
          "default": "Poszewka jedwabna + Czepek do spania"
        },
        {
          "type": "text",
          "id": "editorial_line",
          "label": "Why together (italic teal line)",
          "default": "Twarz i włosy - kompletna ochrona na noc"
        },
        {
          "type": "text",
          "id": "mobile_svg",
          "label": "Mobile SVG filename (in assets/)",
          "info": "e.g. lusena-bundle-piekny-sen.svg. Leave blank for first block (hero card on mobile)."
        },
        {
          "type": "text",
          "id": "cta_label",
          "label": "Button label",
          "default": "Zobacz zestaw"
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "LUSENA Bundles",
      "settings": {
        "kicker": "Zestawy Premium",
        "heading": "Zbuduj swoją nocną rutynę",
        "body": "Każdy zestaw to gotowy pomysł - na nocną rutynę albo idealny prezent."
      },
      "blocks": [
        {
          "type": "bundle_card",
          "settings": {
            "contents": "Poszewka jedwabna + Czepek do spania",
            "editorial_line": "Twarz i włosy - kompletna ochrona na noc",
            "cta_label": "Zobacz zestaw"
          }
        },
        {
          "type": "bundle_card",
          "settings": {
            "contents": "Poszewka jedwabna + Maska 3D do spania",
            "editorial_line": "Gładkość dla skóry, ciemność dla oczu",
            "mobile_svg": "lusena-bundle-piekny-sen.svg",
            "cta_label": "Zobacz zestaw"
          }
        },
        {
          "type": "bundle_card",
          "settings": {
            "contents": "3× Scrunchie jedwabny w trzech kolorach",
            "editorial_line": "Kolor pod nastrój - idealny prezent",
            "mobile_svg": "lusena-bundle-scrunchie-trio.svg",
            "cta_label": "Zobacz zestaw"
          }
        }
      ]
    }
  ]
}
{% endschema %}
```

- [ ] **Step 2: Commit**

```bash
git add sections/lusena-bundles.liquid
git commit -m "feat(lusena): bundles section schema — product pickers replace text blocks"
```

---

### Task 2: Rewrite section Liquid template

**Files:**
- Modify: `sections/lusena-bundles.liquid` (lines 1-117 — everything above `{% schema %}`)

**Context:** The template must render two different card types based on `forloop.first` (mobile breakpoint). Desktop always renders full cards. Mobile renders the first block as a full card and subsequent blocks as compact rows. CSS handles the show/hide via media queries — the Liquid outputs BOTH markup variants for non-first blocks so CSS can toggle them.

- [ ] **Step 1: Replace lines 1-116 with the new template**

Replace everything above `{% schema %}` with:

```liquid
{{ 'lusena-bundles.css' | asset_url | stylesheet_tag }}

{%- liquid
  assign override_style = ''
  if section.settings.padding_top > 0
    assign override_style = override_style | append: '--lusena-section-padding-top-desktop:' | append: section.settings.padding_top | append: 'px;'
  endif
  if section.settings.padding_bottom > 0
    assign override_style = override_style | append: '--lusena-section-padding-bottom-desktop:' | append: section.settings.padding_bottom | append: 'px;'
  endif
  if section.settings.padding_top_mobile > 0
    assign override_style = override_style | append: '--lusena-section-padding-top-mobile:' | append: section.settings.padding_top_mobile | append: 'px;'
  endif
  if section.settings.padding_bottom_mobile > 0
    assign override_style = override_style | append: '--lusena-section-padding-bottom-mobile:' | append: section.settings.padding_bottom_mobile | append: 'px;'
  endif
-%}
<section
  class="lusena-bg-brand lusena-bundles lusena-spacing--spacious"
  {% if override_style != blank %}
    style="{{ override_style }}"
  {% endif %}
>
  <div class="lusena-container">
    <div class="lusena-text-center lusena-content-flow--tight lusena-gap-section-intro{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}">
      {%- if section.settings.kicker != blank -%}
        <span class="lusena-type-caption lusena-kicker">
          {{ section.settings.kicker | escape }}
        </span>
      {%- endif -%}

      <h2 class="lusena-type-h1">
        {{ section.settings.heading | newline_to_br }}
      </h2>
    </div>

    {%- if section.settings.body != blank -%}
      <p class="lusena-type-body lusena-text-center lusena-gap-body" style="max-width: 56rem; margin-inline: auto;">
        {{ section.settings.body | escape }}
      </p>
    {%- endif -%}

    {%- if section.blocks.size > 0 -%}
      <div class="lusena-bundles__grid" data-cascade>
        {%- for block in section.blocks -%}
          {%- liquid
            assign bundle_product = block.settings.product
            if bundle_product == blank
              continue
            endif

            assign is_first = forloop.first
            assign is_oos = false
            unless bundle_product.available
              assign is_oos = true
            endunless

            comment
              Savings calculation:
              lusena.bundle_original_price stores zł as integer (e.g. 508).
              product.price is in grosz/cents (e.g. 39900).
              Convert metafield to cents, then subtract.
            endcomment
            assign original_price_cents = 0
            assign savings_cents = 0
            assign has_savings = false
            assign mf_original = bundle_product.metafields.lusena.bundle_original_price
            if mf_original != blank and mf_original.value != blank
              assign original_price_cents = mf_original.value | times: 100
              assign savings_cents = original_price_cents | minus: bundle_product.price
              if savings_cents > 0
                assign has_savings = true
              endif
            endif

            assign has_badge = false
            assign mf_badge = bundle_product.metafields.lusena.badge_bestseller
            if mf_badge != blank and mf_badge.value == true
              assign has_badge = true
            endif
          -%}

          {%- comment -%} === FULL CARD (desktop always, mobile first-only) === {%- endcomment -%}
          <div
            class="lusena-bundles__card{% if is_oos %} lusena-bundles__card--oos{% endif %}{% unless is_first %} lusena-bundles__card--desktop-only{% endunless %}{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}"
            {{ block.shopify_attributes }}
            {% if settings.animations_reveal_on_scroll %}
              style="animation-delay: {{ forloop.index0 | times: 100 }}ms;"
            {% endif %}
          >
            {%- comment -%} Image area with fallback chain {%- endcomment -%}
            <div class="lusena-bundles__card-media">
              {%- if has_badge -%}
                <span class="lusena-bundles__badge">Bestseller</span>
              {%- endif -%}

              {%- if bundle_product.featured_image -%}
                {{
                  bundle_product.featured_image
                  | image_url: width: 800
                  | image_tag:
                    loading: 'lazy',
                    widths: '400, 600, 800',
                    sizes: '(min-width: 768px) 30vw, 90vw'
                }}
              {%- else -%}
                <div class="lusena-bundles__card-placeholder">
                  {{ 'product-1' | placeholder_svg_tag }}
                </div>
              {%- endif -%}
            </div>

            <div class="lusena-bundles__card-info">
              <h3 class="lusena-bundles__card-title">
                {{ bundle_product.title | escape }}
              </h3>

              {%- if block.settings.contents != blank -%}
                <p class="lusena-bundles__card-contents">
                  {{ block.settings.contents | escape }}
                </p>
              {%- endif -%}

              {%- if block.settings.editorial_line != blank -%}
                <p class="lusena-bundles__card-editorial">
                  {{ block.settings.editorial_line | escape }}
                </p>
              {%- endif -%}

              <div class="lusena-bundles__card-pricing">
                <span class="lusena-bundles__card-price">
                  {{ bundle_product.price | money_without_trailing_zeros }}
                </span>
                {%- if has_savings -%}
                  <span class="lusena-bundles__card-compare-price">
                    {{ original_price_cents | money_without_trailing_zeros }}
                  </span>
                {%- endif -%}
              </div>

              {%- if has_savings -%}
                <span class="lusena-bundles__card-savings">
                  Oszczędzasz {{ savings_cents | money_without_trailing_zeros }}
                </span>
              {%- endif -%}

              {%- if is_oos -%}
                <span class="lusena-bundles__card-cta lusena-bundles__card-cta--disabled">
                  Chwilowo niedostępny
                </span>
              {%- else -%}
                <a
                  href="{{ bundle_product.url }}"
                  class="lusena-bundles__card-cta"
                >
                  {{ block.settings.cta_label | default: 'Zobacz zestaw' | escape }}
                </a>
              {%- endif -%}
            </div>
          </div>

          {%- comment -%} === COMPACT ROW (mobile only, non-first blocks) === {%- endcomment -%}
          {%- unless is_first -%}
            <div
              class="lusena-bundles__compact-row{% if is_oos %} lusena-bundles__compact-row--oos{% endif %}"
              {{ block.shopify_attributes }}
            >
              {%- if block.settings.mobile_svg != blank -%}
                <div class="lusena-bundles__compact-thumb">
                  <img
                    src="{{ block.settings.mobile_svg | asset_url }}"
                    alt="{{ bundle_product.title | escape }}"
                    width="56"
                    height="56"
                    loading="lazy"
                  >
                </div>
              {%- endif -%}

              <div class="lusena-bundles__compact-body">
                <div class="lusena-bundles__compact-header">
                  <h3 class="lusena-bundles__compact-title">
                    {{ bundle_product.title | escape }}
                  </h3>
                  <div class="lusena-bundles__compact-pricing">
                    <span class="lusena-bundles__compact-price">
                      {{ bundle_product.price | money_without_trailing_zeros }}
                    </span>
                    {%- if has_savings -%}
                      <span class="lusena-bundles__card-compare-price">
                        {{ original_price_cents | money_without_trailing_zeros }}
                      </span>
                    {%- endif -%}
                  </div>
                </div>

                {%- if block.settings.contents != blank -%}
                  <p class="lusena-bundles__card-contents">
                    {{ block.settings.contents | escape }}
                  </p>
                {%- endif -%}

                <div class="lusena-bundles__compact-footer">
                  {%- if has_savings -%}
                    <span class="lusena-bundles__card-savings">
                      Oszczędzasz {{ savings_cents | money_without_trailing_zeros }}
                    </span>
                  {%- endif -%}

                  {%- if is_oos -%}
                    <span class="lusena-bundles__compact-cta lusena-bundles__compact-cta--disabled">
                      Niedostępny
                    </span>
                  {%- else -%}
                    <a href="{{ bundle_product.url }}" class="lusena-bundles__compact-cta">
                      {{ block.settings.cta_label | default: 'Zobacz zestaw' | escape }}
                      <span aria-hidden="true" class="lusena-link-arrow"></span>
                    </a>
                  {%- endif -%}
                </div>
              </div>
            </div>
          {%- endunless -%}

        {%- endfor -%}
      </div>
    {%- endif -%}
  </div>
</section>
```

- [ ] **Step 2: Commit**

```bash
git add sections/lusena-bundles.liquid
git commit -m "feat(lusena): bundles Liquid template — product-driven cards + mobile compact rows"
```

---

### Task 3: Rewrite CSS

**Files:**
- Rewrite: `assets/lusena-bundles.css`

- [ ] **Step 1: Replace the entire file contents**

```css
/* ==========================================================================
   LUSENA Bundles — Homepage bundle card grid
   Standalone CSS (loaded per-section to avoid compiled_assets truncation).
   Spec: docs/superpowers/specs/2026-04-03-homepage-bundles-section-design.md
   ========================================================================== */

/* --- Kicker (gold accent, matches all other section kickers) --- */
.lusena-bundles .lusena-kicker {
  color: var(--lusena-accent-2);
}

/* --- Grid: 1-col mobile → 3-col desktop --- */
.lusena-bundles__grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--lusena-space-3);
  margin-top: var(--lusena-space-6);
}

@media (min-width: 768px) {
  .lusena-bundles__grid {
    grid-template-columns: repeat(3, 1fr);
    gap: var(--lusena-space-5);
  }
}

/* ==========================================================================
   FULL CARD (desktop always, mobile first-only)
   ========================================================================== */

.lusena-bundles__card {
  display: flex;
  flex-direction: column;
}

/* Desktop-only cards: hidden on mobile, shown on desktop */
.lusena-bundles__card--desktop-only {
  display: none;
}

@media (min-width: 768px) {
  .lusena-bundles__card--desktop-only {
    display: flex;
  }
}

/* --- Card media --- */
.lusena-bundles__card-media {
  position: relative;
  overflow: hidden;
}

.lusena-bundles__card-media img {
  width: 100%;
  height: auto;
  aspect-ratio: 4 / 5;
  object-fit: cover;
}

.lusena-bundles__card-placeholder {
  aspect-ratio: 4 / 5;
  background: var(--lusena-color-n200);
  display: flex;
  align-items: center;
  justify-content: center;
}

.lusena-bundles__card-placeholder svg {
  width: 40%;
  opacity: 0.3;
}

/* --- Badge (Bestseller) --- */
.lusena-bundles__badge {
  position: absolute;
  top: 0.8rem;
  left: 0.8rem;
  z-index: 2;
  background: rgb(255 255 255 / 0.9);
  backdrop-filter: blur(4px);
  padding: 0.4rem 0.8rem;
  font-family: var(--lusena-font-ui);
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 500;
  color: var(--lusena-text-1);
}

/* --- Card info --- */
.lusena-bundles__card-info {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  gap: var(--lusena-space-1);
  padding-top: var(--lusena-space-3);
}

.lusena-bundles__card-title {
  font-family: var(--lusena-font-heading);
  font-size: 1.8rem;
  font-weight: 500;
  color: var(--lusena-text-1);
  margin: 0;
}

.lusena-bundles__card-contents {
  font-size: 1.4rem;
  color: var(--lusena-text-2);
  margin: 0;
}

/* --- Editorial "why together" line --- */
.lusena-bundles__card-editorial {
  font-size: 1.3rem;
  font-style: italic;
  color: var(--lusena-accent-cta);
  margin: 0;
}

/* --- Pricing row --- */
.lusena-bundles__card-pricing {
  display: flex;
  align-items: baseline;
  gap: var(--lusena-space-2);
  margin-top: var(--lusena-space-1);
}

.lusena-bundles__card-price {
  font-size: 1.8rem;
  font-weight: 600;
  color: var(--lusena-text-1);
}

.lusena-bundles__card-compare-price {
  font-size: 1.4rem;
  color: var(--lusena-text-2);
  text-decoration: line-through;
  text-decoration-color: color-mix(in srgb, currentColor 50%, transparent);
}

/* --- Savings (plain gold text) --- */
.lusena-bundles__card-savings {
  font-size: 1.3rem;
  font-weight: 500;
  color: var(--lusena-accent-2);
}

/* --- Card CTA (outline button) --- */
.lusena-bundles__card-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
  font-family: var(--lusena-font-ui);
  font-size: 1.4rem;
  font-weight: 500;
  height: 4rem;
  padding: 0 var(--lusena-space-4);
  background: transparent;
  color: var(--lusena-accent-cta);
  border: 1px solid var(--lusena-accent-cta);
  border-radius: var(--lusena-btn-radius);
  text-decoration: none;
  transition: background var(--lusena-transition-fast), color var(--lusena-transition-fast);
  margin-top: auto;
}

@media (hover: hover) {
  .lusena-bundles__card-cta:hover {
    background: var(--lusena-accent-cta);
    color: var(--lusena-color-n0);
  }
}

.lusena-bundles__card-cta:focus-visible {
  outline: 2px solid var(--lusena-accent-cta);
  outline-offset: 2px;
}

.lusena-bundles__card-cta--disabled {
  border-color: var(--lusena-color-n300);
  color: var(--lusena-text-2);
  cursor: default;
  pointer-events: none;
}

/* --- Out of stock --- */
.lusena-bundles__card--oos .lusena-bundles__card-media {
  opacity: 0.5;
  filter: grayscale(100%);
}

/* ==========================================================================
   COMPACT ROW (mobile only, non-first blocks)
   ========================================================================== */

.lusena-bundles__compact-row {
  display: flex;
  gap: var(--lusena-space-3);
  background: var(--lusena-surface-1);
  border-radius: var(--lusena-btn-radius);
  padding: var(--lusena-space-3);
}

/* Hidden on desktop (full cards shown instead) */
@media (min-width: 768px) {
  .lusena-bundles__compact-row {
    display: none;
  }
}

/* --- SVG thumbnail --- */
.lusena-bundles__compact-thumb {
  flex-shrink: 0;
  width: 5.6rem;
  height: 5.6rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lusena-bundles__compact-thumb img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

/* --- Compact body --- */
.lusena-bundles__compact-body {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  flex-grow: 1;
  min-width: 0;
}

.lusena-bundles__compact-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: var(--lusena-space-2);
}

.lusena-bundles__compact-title {
  font-family: var(--lusena-font-heading);
  font-size: 1.6rem;
  font-weight: 500;
  color: var(--lusena-text-1);
  margin: 0;
}

.lusena-bundles__compact-pricing {
  display: flex;
  align-items: baseline;
  gap: var(--lusena-space-1);
  flex-shrink: 0;
}

.lusena-bundles__compact-price {
  font-size: 1.6rem;
  font-weight: 600;
  color: var(--lusena-text-1);
}

.lusena-bundles__compact-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* --- Compact CTA (text link with arrow) --- */
.lusena-bundles__compact-cta {
  font-family: var(--lusena-font-ui);
  font-size: 1.3rem;
  font-weight: 500;
  color: var(--lusena-accent-cta);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  flex-shrink: 0;
}

@media (hover: hover) {
  .lusena-bundles__compact-cta:hover {
    text-decoration: underline;
  }
}

.lusena-bundles__compact-cta--disabled {
  color: var(--lusena-text-2);
  cursor: default;
  pointer-events: none;
}

/* --- Compact row OOS --- */
.lusena-bundles__compact-row--oos {
  opacity: 0.6;
}
```

- [ ] **Step 2: Commit**

```bash
git add assets/lusena-bundles.css
git commit -m "feat(lusena): bundles CSS — desktop grid, mobile compact rows, badge, OOS"
```

---

### Task 4: Update template JSON with real bundle products

**Files:**
- Modify: `templates/index.json` (the `"gift"` section, approximately lines 228-277)

- [ ] **Step 1: Replace the `"gift"` section in index.json**

Find the `"gift"` key (the bundles section) and replace its entire value with:

```json
    "gift": {
      "type": "lusena-bundles",
      "blocks": {
        "bundle-nocna-rutyna": {
          "type": "bundle_card",
          "settings": {
            "product": "nocna-rutyna",
            "contents": "Poszewka jedwabna + Czepek do spania",
            "editorial_line": "Twarz i włosy - kompletna ochrona na noc",
            "mobile_svg": "",
            "cta_label": "Zobacz zestaw"
          }
        },
        "bundle-piekny-sen": {
          "type": "bundle_card",
          "settings": {
            "product": "piekny-sen",
            "contents": "Poszewka jedwabna + Maska 3D do spania",
            "editorial_line": "Gładkość dla skóry, ciemność dla oczu",
            "mobile_svg": "lusena-bundle-piekny-sen.svg",
            "cta_label": "Zobacz zestaw"
          }
        },
        "bundle-scrunchie-trio": {
          "type": "bundle_card",
          "settings": {
            "product": "scrunchie-trio",
            "contents": "3× Scrunchie jedwabny w trzech kolorach",
            "editorial_line": "Kolor pod nastrój - idealny prezent",
            "mobile_svg": "lusena-bundle-scrunchie-trio.svg",
            "cta_label": "Zobacz zestaw"
          }
        }
      },
      "block_order": [
        "bundle-nocna-rutyna",
        "bundle-piekny-sen",
        "bundle-scrunchie-trio"
      ],
      "settings": {
        "kicker": "Zestawy Premium",
        "heading": "Zbuduj swoją nocną rutynę",
        "body": "Każdy zestaw to gotowy pomysł - na nocną rutynę albo idealny prezent."
      }
    }
```

**Note:** The `"product"` field uses the product handle as a string. Shopify resolves this to the full product object in the template. If the theme editor doesn't accept handle strings (some versions need the admin product URL format), the implementer should set the product via the theme editor UI instead of editing JSON directly. In that case, leave the `"product"` field empty in JSON and configure via Shopify admin > Online Store > Customize > Homepage > Bundles section.

- [ ] **Step 2: Commit**

```bash
git add templates/index.json
git commit -m "feat(lusena): wire 3 real bundle products into homepage bundles section"
```

---

### Task 5: Add SVG assets

**Files:**
- Create: `assets/lusena-bundle-piekny-sen.svg`
- Create: `assets/lusena-bundle-scrunchie-trio.svg`

**Note:** The owner has already generated these SVGs. This task is about placing them in the correct location.

- [ ] **Step 1: Add Piękny Sen SVG**

Place the owner-provided SVG file at `assets/lusena-bundle-piekny-sen.svg`. The SVG should have `viewBox="0 0 56 56"` and use the brand colors specified in the design spec (stroke `#2E2D2B`, gold accent `#8C6A3C`).

- [ ] **Step 2: Add Scrunchie Trio SVG**

Place the owner-provided SVG file at `assets/lusena-bundle-scrunchie-trio.svg`. The SVG should have `viewBox="0 0 56 56"` and use brand colors (Czarny `#2E2D2B`, Brudny róż `#C4A08A`, Szampan `#D4C9BD`, gold `#8C6A3C`).

- [ ] **Step 3: Commit**

```bash
git add assets/lusena-bundle-piekny-sen.svg assets/lusena-bundle-scrunchie-trio.svg
git commit -m "feat(lusena): add mobile SVG thumbnails for Piękny Sen and Scrunchie Trio"
```

---

### Task 6: Push to dev theme and verify

**Files:** None (verification only)

- [ ] **Step 1: Look up worktree theme ID**

Read `config/worktree-themes.json` and find the theme ID for this worktree slot number.

- [ ] **Step 2: Push to dev theme**

```bash
shopify theme push --theme <THEME_ID> --store lusena-dev.myshopify.com --nodelete
```

- [ ] **Step 3: Visual verification with `/lusena-preview-check`**

Use the `/lusena-preview-check` skill to verify:

1. **Desktop homepage** — navigate to homepage, scroll to bundles section:
   - 3-column grid visible
   - Each card shows: product title, contents text, italic teal editorial line, price + strikethrough, gold savings text, "Zobacz zestaw" button
   - Nocna Rutyna has "Bestseller" badge
   - Cards link to correct bundle PDP URLs
   - Section heading reads "Zbuduj swoją nocną rutynę"

2. **Mobile homepage** (resize to 375px width):
   - Nocna Rutyna renders as full card with image area
   - Piękny Sen renders as compact row with SVG thumbnail
   - Scrunchie Trio renders as compact row with SVG thumbnail
   - Compact rows show: name + price on same line, contents, savings + text link

3. **Click-through** — click each "Zobacz zestaw" to confirm it navigates to the correct bundle PDP

- [ ] **Step 4: Run theme check**

```bash
shopify theme check
```

Verify only known baseline warnings remain (listed in CLAUDE.md). No new warnings from the bundles section.

- [ ] **Step 5: Final commit if any fixes needed**

If visual verification reveals issues, fix them and commit:

```bash
git add -A
git commit -m "fix(lusena): homepage bundles visual fixes from QA"
```
