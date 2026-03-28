# Homepage optimization: Benefit bridge + reorder + P/S refresh

**Date:** 2026-03-28
**Status:** Approved

## Summary

Three changes to the homepage:
1. New `lusena-benefit-bridge` section at position 3
2. Homepage section reorder in `templates/index.json`
3. Problem/Solution copy refresh (4 items rewritten)

## Motivation

All 4 customer personas + CRO research agreed: the Problem/Solution comparison is good content in the wrong position. Cold traffic from Instagram ads needs a short "why silk?" bridge before seeing products, not a heavy two-column lecture.

---

## Change 1: New section — `sections/lusena-benefit-bridge.liquid`

### Content (approved, legally checked)

**Heading:** "Co zmieni się po pierwszej nocy?"

| Card | Icon | Title | Description |
|------|------|-------|-------------|
| 1 (Skin) | `sparkles` | Gładka skóra o poranku | Jedwab sprzyja redukcji odcisków sennych - rano widzisz w lustrze wypoczętą, gładką twarz zamiast zagnieceń. |
| 2 (Hair) | `star` | Włosy bez porannego chaosu | Gładki jedwab pomaga zachować fryzurę przez noc - mniej puszenia, plątania i łamania delikatnych pasm. |
| 3 (Care) | `droplets` | Krem pracuje całą noc | Jedwab nie wchłania kosmetyków tak jak bawełna - Twój krem na noc zostaje na skórze, gdzie może działać. |

### Visual design spec

**Background:** `lusena-bg-brand` (`#F7F5F2` warm cream) — contrasts with white trust bar above.

**Spacing tier:** `lusena-spacing--standard` (mobile 48px / desktop 64px) — this is a bridge section, not a destination.

**Container:** `lusena-container` (max-width 120rem, centered).

**Heading:**
- Class: `lusena-type-h1` (Source Serif 4, 3.2rem mobile / 4.0rem desktop)
- Centered: `lusena-text-center`
- Bottom gap: `lusena-gap-section-intro` (32px)
- Animation: `scroll-trigger animate--slide-in` (gated by `settings.animations_reveal_on_scroll`)

**Card grid:**
- Class: `lusena-grid lusena-grid--3`
- Desktop: 3 columns with `--lusena-space-6` (48px) gap
- Mobile: stacked (1 column) with `--lusena-space-4` (32px) gap
- Animation: `data-cascade` on grid container for stagger, each card gets `scroll-trigger animate--slide-in`

**Card layout (each card):**
- `display: flex; flex-direction: column; align-items: center; text-align: center`
- Gap between elements: `--lusena-space-2` (16px)
- NO `lusena-content-card` class (no editorial top border — this section is lighter/airier than heritage)
- NO background, no shadow, no borders on cards

**Icon:**
- Use `lusena-icon-circle` from foundations (48px circle, 1px border `--lusena-color-n200`, transparent bg)
- Icon SVG inside: rendered via `{% render 'lusena-icon', name: block.settings.icon, stroke_width: 1.5 %}`
- Icon SVG size: `width: 2.4rem; height: 2.4rem` (matches heritage pattern)
- Icon color: `--lusena-accent-cta` (teal `#0E5E5A`) — these are USER BENEFIT icons (per brand tokens two-tier rule: "trust, process, or user benefits" = teal)

**Card title:**
- Class: `lusena-type-h2` (Source Serif 4, 2.0rem mobile / 2.4rem desktop)
- Color: `--lusena-text-1` (`#111111`)

**Card description:**
- Class: `lusena-type-body` (Inter, 1.6rem, line-height 2.4rem)
- Color: `--lusena-text-2` (`#4A4A4A`)

**Mobile behavior (< 768px):**
- Grid stacks to 1 column
- Cards remain centered
- Each card: icon circle, title, description — vertical stack
- Consider adding a thin separator between cards on mobile: `border-bottom: 1px solid var(--lusena-color-n200)` on all cards except last, with `padding-bottom: var(--lusena-space-4)` — this prevents the stacked cards from blending into a text wall. (Optional — implement and visual-check, remove if it looks busy.)

### Liquid structure (pseudocode)

```liquid
{%- comment -%} Padding override logic (same as heritage/P-S pattern) {%- endcomment -%}
<section class="lusena-bg-brand lusena-benefit-bridge lusena-spacing--standard" style="...overrides...">
  <div class="lusena-container">

    {%- if heading != blank -%}
    <div class="lusena-text-center lusena-gap-section-intro scroll-trigger animate--slide-in">
      <h2 class="lusena-type-h1">{{ heading }}</h2>
    </div>
    {%- endif -%}

    <div class="lusena-grid lusena-grid--3" data-cascade>
      {%- for block in section.blocks -%}
      <div class="lusena-benefit-bridge__card scroll-trigger animate--slide-in" {{ block.shopify_attributes }}>
        <div class="lusena-icon-circle lusena-benefit-bridge__icon">
          {% render 'lusena-icon', name: block.settings.icon, stroke_width: 1.5 %}
        </div>
        <h3 class="lusena-type-h2">{{ block.settings.title | escape }}</h3>
        <p class="lusena-type-body">{{ block.settings.text | escape }}</p>
      </div>
      {%- endfor -%}
    </div>

  </div>
</section>
```

### CSS (in `{% stylesheet %}` — estimated ~30 lines, well under 50-line threshold)

```css
/* Card centered layout */
.lusena-benefit-bridge__card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: var(--lusena-space-2);
}

/* Icon circle color — teal for user benefits */
.lusena-benefit-bridge .lusena-icon-circle {
  color: var(--lusena-accent-cta);
}

/* Icon SVG size (matches heritage pattern) */
.lusena-benefit-bridge__icon svg {
  width: 2.4rem;
  height: 2.4rem;
}

/* Mobile card separators (stacked cards need visual separation) */
@media (max-width: 767px) {
  .lusena-benefit-bridge__card:not(:last-child) {
    padding-bottom: var(--lusena-space-4);
    border-bottom: 1px solid var(--lusena-color-n200);
  }
}
```

### Schema

```json
{
  "name": "LUSENA Benefit Bridge",
  "tag": "section",
  "settings": [
    { "type": "header", "content": "Spacing overrides (0 = use global default)" },
    { "type": "range", "id": "padding_top", ... },
    { "type": "range", "id": "padding_bottom", ... },
    { "type": "range", "id": "padding_top_mobile", ... },
    { "type": "range", "id": "padding_bottom_mobile", ... },
    { "type": "text", "id": "heading", "label": "Heading", "default": "Co zmieni się po pierwszej nocy?" }
  ],
  "blocks": [
    {
      "type": "card",
      "name": "Benefit card",
      "settings": [
        { "type": "text", "id": "icon", "label": "Icon name", "default": "sparkles",
          "info": "Available: sparkles, star, droplets, layers, shield-check, heart, gift" },
        { "type": "text", "id": "title", "label": "Title (max 28 chars)", "default": "Gładka skóra o poranku" },
        { "type": "text", "id": "text", "label": "Description (1 sentence)", "default": "..." }
      ]
    }
  ],
  "presets": [ ... with 3 default blocks for skin/hair/care ... ]
}
```

---

## Change 2: Homepage section reorder

Edit `templates/index.json` to set the `order` array:

```
hero, trust, benefit_bridge, bestsellers, reviews, problem_solution, gift, heritage, faq, final_cta
```

Add the new `benefit_bridge` section with its 3 blocks and settings.

Positions 4-10 are all existing sections — just reordered. No content changes to bestsellers, testimonials, bundles, heritage, FAQ, or final CTA.

---

## Change 3: Problem/Solution copy refresh

Edit the `problem_solution` section block settings in `templates/index.json`:

| Item | Field | New value |
|------|-------|-----------|
| problem-0 | title | Tarcie tworzy zagniecenia |
| problem-0 | text | Włókna bawełny działają jak rzep - ciągną delikatną skórę twarzy i tworzą odciski, które z wiekiem znikają coraz wolniej. |
| problem-1 | title | Pielęgnacja znika w poduszce |
| problem-1 | text | Bawełna chłonie kosmetyki i naturalne nawilżenie skóry przez całą noc - Twój drogi krem pracuje dla poszewki, nie dla Ciebie. |
| solution-0 | title | Gładkość bez tarcia |
| solution-0 | text | Gładka powierzchnia jedwabiu 22 momme sprzyja redukcji porannych zagnieceń na twarzy i pomaga zachować fryzurę przez noc. |
| solution-1 | title | Twój krem wreszcie działa |
| solution-1 | text | Jedwab pomaga zachować nawilżenie i kosmetyki na skórze zamiast w poszewce - pielęgnacja pracuje dla Ciebie, nie dla poduszki. |

CTA link text stays: "Sprawdź dowody jakości →"
Section headings stay: "Bawełna chłonie. Tarcie i suchość." / "Jedwab chroni. Nawilżenie i gładkość."

---

## Files changed

| File | Action | Lines |
|------|--------|-------|
| `sections/lusena-benefit-bridge.liquid` | CREATE | ~90 |
| `templates/index.json` | EDIT | reorder + add section + update P/S copy |

No new CSS files needed. No JS needed. Section CSS is ~30 lines in `{% stylesheet %}`.

## Verification

After implementation:
1. Visual check desktop (1280px) + mobile (390px) via playwright-cli
2. Verify scroll animations trigger correctly (data-cascade stagger)
3. Check icon rendering (sparkles, star, droplets)
4. Check compiled_assets size stays under 55KB
5. Run `shopify theme check` — no new warnings
