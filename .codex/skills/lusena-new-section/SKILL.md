---
name: lusena-new-section
description: Scaffolds a new LUSENA section with correct boilerplate, spacing tier, CSS decision, and schema
argument-hint: "<section-name> [--tier=standard] [--bg=surface-1] [--js] [--standalone-css]"
allowed-tools: Write, Read, Glob, Bash(shopify theme check *)
---

# LUSENA Section Scaffolding

Generate a new `sections/lusena-<name>.liquid` file following the verified LUSENA section anatomy.

## Arguments

Parse `$ARGUMENTS` for:
- **Section name** (required): e.g., `my-feature` -> creates `sections/lusena-my-feature.liquid`
- **`--tier=`** (optional, default `standard`): `full-bleed`, `compact`, `standard`, `spacious`, `hero`
- **`--bg=`** (optional, default `surface-1`): `surface-1`, `surface-2`, `brand`
- **`--js`** (optional): include a `<script>` block with IIFE + idempotency guard
- **`--standalone-css`** (optional): create `assets/lusena-<name>.css` instead of inline `{% stylesheet %}`

## Pre-flight

1. Verify `sections/lusena-<name>.liquid` does not already exist
2. If `--standalone-css`, verify `assets/lusena-<name>.css` does not already exist

## Section template

Generate the file following this verified anatomy (based on analysis of 8 existing sections):

```liquid
{%- liquid
  assign padding_top = section.settings.padding_top
  assign padding_bottom = section.settings.padding_bottom
  assign padding_top_mobile = section.settings.padding_top_mobile
  assign padding_bottom_mobile = section.settings.padding_bottom_mobile

  assign override_style = ''
  if padding_top > 0
    assign override_style = override_style | append: '--lusena-section-pt: ' | append: padding_top | append: 'px; '
  endif
  if padding_bottom > 0
    assign override_style = override_style | append: '--lusena-section-pb: ' | append: padding_bottom | append: 'px; '
  endif
  if padding_top_mobile > 0
    assign override_style = override_style | append: '--lusena-section-pt-mobile: ' | append: padding_top_mobile | append: 'px; '
  endif
  if padding_bottom_mobile > 0
    assign override_style = override_style | append: '--lusena-section-pb-mobile: ' | append: padding_bottom_mobile | append: 'px; '
  endif

  -%}{%- comment -%} Section-specific variables go here {%- endcomment -%}{%- liquid
  -%}
```

If `--standalone-css`:
```liquid
{{ 'lusena-<name>.css' | asset_url | stylesheet_tag }}
```

Then the section markup:
```liquid
<section
  class="lusena-bg-<bg> lusena-<name>{% if <tier> != 'full-bleed' %} lusena-spacing--<tier>{% endif %}{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}"
  {% if override_style != blank %}style="{{ override_style }}"{% endif %}
  data-lusena-<name>
>
  <div class="lusena-container">
    {%- comment -%} Section content goes here {%- endcomment -%}
  </div>
</section>
```

If `--js`:
```html
<script>
(function() {
  if (window.__lusena<PascalName>Init) return;
  window.__lusena<PascalName>Init = true;

  // Section JS goes here

  // Re-initialize on section reload (theme editor)
  document.addEventListener('shopify:section:load', function(event) {
    if (event.detail.sectionId === '{{ section.id }}') {
      window.__lusena<PascalName>Init = false;
      // Re-run init
    }
  });
})();
</script>
```

The stylesheet block:
```liquid
{% stylesheet %}
  /* Section-scoped CSS — keep under 50 lines (compiled_assets 73KB truncation limit) */
  /* Use 0-2-0 specificity (.parent .child) for any rule competing with foundations */
{% endstylesheet %}
```

If `--standalone-css`, replace with:
```liquid
{% stylesheet %}
  /* CSS in assets/lusena-<name>.css */
{% endstylesheet %}
```

The schema block — always last:
```liquid
{% schema %}
{
  "name": "LUSENA <Readable Name>",
  "tag": "section",
  "class": "shopify-section",
  "settings": [
    {
      "type": "header",
      "content": "Spacing overrides (0 = use global default)"
    },
    {
      "type": "range",
      "id": "padding_top",
      "label": "Desktop: padding top (px)",
      "min": 0,
      "max": 200,
      "step": 4,
      "default": 0
    },
    {
      "type": "range",
      "id": "padding_bottom",
      "label": "Desktop: padding bottom (px)",
      "min": 0,
      "max": 200,
      "step": 4,
      "default": 0
    },
    {
      "type": "range",
      "id": "padding_top_mobile",
      "label": "Mobile: padding top (px)",
      "min": 0,
      "max": 120,
      "step": 4,
      "default": 0
    },
    {
      "type": "range",
      "id": "padding_bottom_mobile",
      "label": "Mobile: padding bottom (px)",
      "min": 0,
      "max": 120,
      "step": 4,
      "default": 0
    }
  ],
  "presets": [
    {
      "name": "LUSENA <Readable Name>"
    }
  ]
}
{% endschema %}
```

## If `--standalone-css`, also create `assets/lusena-<name>.css`:

```css
/* ==========================================================================
   LUSENA <Readable Name> — Section CSS
   Loaded via: {{ 'lusena-<name>.css' | asset_url | stylesheet_tag }}
   ========================================================================== */

/* Use 0-2-0 specificity (.parent .child) for any rule competing with foundations */
```

## Post-generation

1. Run `shopify theme check sections/lusena-<name>.liquid`
2. Report what was created and remind the user to add the section to the relevant template JSON (`order` array + `sections` object)

## Spacing tier guide (for when user doesn't specify)

| Use case | Tier |
|----------|------|
| Edge-to-edge media, hero images | `full-bleed` |
| Utility strips (trust bar, announcement) | `compact` (or no class + custom padding) |
| Informational content, FAQ, forms | `standard` (48/64px) |
| Trust-building, testimonials, CTAs | `spacious` (64/96px) |
| Page hero sections | `hero` (80/128px) |
