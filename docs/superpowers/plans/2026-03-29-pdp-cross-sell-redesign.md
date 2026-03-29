# PDP Cross-sell Checkbox UI/UX Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the PDP cross-sell checkbox to match LUSENA's premium aesthetic — white card with teal left accent, compact single row, no color text, educational hint.

**Architecture:** Pure CSS replacement (~115 lines) + minor Liquid template edit (swap color label for hint, adjust image size) + 2-line JS cleanup. No new files, no structural changes. Functional behavior unchanged.

**Tech Stack:** Liquid, CSS (LUSENA design tokens), inline JS

**Spec:** `docs/superpowers/specs/2026-03-29-pdp-cross-sell-redesign.md`

---

### Task 1: Replace cross-sell CSS styles

**Files:**
- Modify: `assets/lusena-pdp.css:51-166` (replace cross-sell block)

- [ ] **Step 1: Replace the cross-sell CSS block**

Replace lines 51-166 in `assets/lusena-pdp.css` (from `/* ── Cross-sell checkbox ── */` through `.lusena-pdp-cross-sell-cb__was` closing brace, stopping before `.lusena-pdp .lusena-pdp-buy-box__proof`).

Old code starts at line 51:
```css
/* ── Cross-sell checkbox ── */

.lusena-pdp .lusena-pdp-buy-box__cross-sell-checkbox {
  order: 5;
}

.lusena-pdp-cross-sell-cb__label {
  ...
```

Replace with:
```css
/* ── Cross-sell checkbox ── */

.lusena-pdp .lusena-pdp-buy-box__cross-sell-checkbox {
  order: 5;
}

.lusena-pdp-cross-sell-cb {
  background: var(--lusena-color-n0);
  border: 1px solid color-mix(in srgb, var(--lusena-text-2) 6%, transparent);
  border-left: 3px solid color-mix(in srgb, var(--lusena-accent-cta) 40%, transparent);
  border-radius: var(--lusena-btn-radius);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
  cursor: pointer;
  transition: border-color var(--lusena-transition-fast), box-shadow var(--lusena-transition-fast);
}

.lusena-pdp-cross-sell-cb:hover {
  border-left-color: var(--lusena-accent-cta);
}

.lusena-pdp-cross-sell-cb:has(.lusena-pdp-cross-sell-cb__input:checked) {
  border-left-color: var(--lusena-accent-cta);
  box-shadow: 0 1px 3px rgba(14, 94, 90, 0.08);
}

.lusena-pdp-cross-sell-cb__label {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.2rem;
  cursor: pointer;
}

/* Custom checkbox indicator */
.lusena-pdp-cross-sell-cb__check {
  flex-shrink: 0;
  width: 1.6rem;
  height: 1.6rem;
  border: 1.5px solid #b8b8b8;
  border-radius: 3px;
  background: var(--lusena-color-n0);
  position: relative;
  transition: background-color var(--lusena-transition-fast), border-color var(--lusena-transition-fast);
}

.lusena-pdp-cross-sell-cb__input:checked ~ .lusena-pdp-cross-sell-cb__check {
  background-color: var(--lusena-accent-cta);
  border-color: var(--lusena-accent-cta);
}

.lusena-pdp-cross-sell-cb__check::after {
  content: '';
  position: absolute;
  top: 0.15rem;
  left: 0.4rem;
  width: 0.45rem;
  height: 0.8rem;
  border: solid var(--lusena-color-n0);
  border-width: 0 1.5px 1.5px 0;
  transform: rotate(45deg);
  opacity: 0;
  transition: opacity var(--lusena-transition-fast);
}

.lusena-pdp-cross-sell-cb__input:checked ~ .lusena-pdp-cross-sell-cb__check::after {
  opacity: 1;
}

/* Product image */
.lusena-pdp-cross-sell-cb__image {
  flex-shrink: 0;
  width: 4rem;
  height: 4rem;
  border-radius: var(--lusena-btn-radius);
  overflow: hidden;
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
}

.lusena-pdp-cross-sell-cb__title {
  font-size: 1.25rem;
  font-weight: 500;
  color: var(--lusena-text-1);
  line-height: 1.3;
}

.lusena-pdp-cross-sell-cb__hint {
  font-size: 1.05rem;
  color: var(--lusena-text-2);
  opacity: 0.6;
  margin-top: 0.1rem;
}

/* Pricing */
.lusena-pdp-cross-sell-cb__pricing {
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.lusena-pdp-cross-sell-cb__price {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--lusena-text-1);
  font-variant-numeric: tabular-nums;
}

.lusena-pdp-cross-sell-cb__was {
  font-size: 1.05rem;
  color: var(--lusena-text-2);
  text-decoration: line-through;
  opacity: 0.45;
}
```

The desktop order rule at line 577-579 (`.lusena-pdp .lusena-pdp-buy-box__cross-sell-checkbox { order: 7; }`) stays unchanged.

- [ ] **Step 2: Commit CSS changes**

```bash
git add assets/lusena-pdp.css
git commit -m "fix(lusena): cross-sell checkbox CSS redesign — white card, teal left accent, compact layout"
```

---

### Task 2: Update Liquid template — remove color label, add hint, adjust image

**Files:**
- Modify: `snippets/lusena-pdp-cross-sell-checkbox.liquid:115-148` (HTML block)

- [ ] **Step 1: Update the HTML inside the label**

In `snippets/lusena-pdp-cross-sell-checkbox.liquid`, replace the image + info + pricing block (lines 115-148).

Replace:
```liquid
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
```

With:
```liquid
    {%- if cs_image -%}
      <span class="lusena-pdp-cross-sell-cb__image">
        <img
          src="{{ cs_image | image_url: width: 80 }}"
          alt="{{ cross_sell_product.title | escape }}"
          width="40"
          height="40"
          loading="lazy"
          data-lusena-cross-sell-image
        >
      </span>
    {%- endif -%}

    <span class="lusena-pdp-cross-sell-cb__info">
      <span class="lusena-pdp-cross-sell-cb__title">
        Dodaj {{ cross_sell_product.title | downcase }}
      </span>
      <span class="lusena-pdp-cross-sell-cb__hint">Taniej w komplecie</span>
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
```

Changes:
- Image: `width: 96` -> `width: 80`, HTML `width/height` 48 -> 40
- Removed: `cs__color` span with `data-lusena-cross-sell-color-label` and "Kolor:" text
- Added: `cs__hint` span with "Taniej w komplecie"

- [ ] **Step 2: Update variant image URL in JSON block**

In the same file, line 169, update the image URL width in the variants JSON to match the new size:

Replace:
```liquid
          "image": {% if variant.featured_image %}{{ variant.featured_image | image_url: width: 96 | json }}{% else %}null{% endif %}
```

With:
```liquid
          "image": {% if variant.featured_image %}{{ variant.featured_image | image_url: width: 80 | json }}{% else %}null{% endif %}
```

- [ ] **Step 3: Remove color label update from JS**

In the same file, in the variant change handler (around line 356-357), remove the two lines that update the color label:

Remove:
```js
        var label = row.querySelector('[data-lusena-cross-sell-color-label]');
        if (label) label.textContent = 'Kolor: ' + chosen.color;
```

The image update line below it (`var img = row.querySelector(...)`) stays.

- [ ] **Step 4: Commit Liquid/JS changes**

```bash
git add snippets/lusena-pdp-cross-sell-checkbox.liquid
git commit -m "fix(lusena): cross-sell Liquid — remove color label, add hint, 40px image"
```

---

### Task 3: Visual verification

- [ ] **Step 1: Check PDP in browser**

Open a product PDP (e.g., `http://127.0.0.1:9292/products/silk-pillowcase`) using `/playwright-cli` with a unique session name. Verify:

1. Cross-sell card renders with white background and teal left accent
2. Checkbox unchecked by default, fills teal on click
3. "Dodaj scrunchie" title visible, "Taniej w komplecie" hint below it
4. Price shows correctly (39 zl with 59 zl crossed out)
5. No "Kolor:" text anywhere
6. Image is ~40px, shows correct color variant

- [ ] **Step 2: Test color switching**

Switch the main product color swatch. Verify the scrunchie image updates to match (no text label change — just the image).

- [ ] **Step 3: Test ATC with checkbox**

Check the checkbox, click ATC. Verify:
1. Button shows loading animation (shimmer + spinner)
2. Cart drawer opens with both items
3. Only 1 of each item added (not doubled)

- [ ] **Step 4: Check mobile viewport**

Resize browser to 375px width. Verify the card is compact and doesn't crowd the ATC button.
