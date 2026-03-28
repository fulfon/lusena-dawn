# Homepage Benefit Bridge Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a "benefit bridge" section to the homepage at position 3, reorder existing sections for optimal conversion flow, and refresh Problem/Solution copy.

**Architecture:** One new Liquid section file (`lusena-benefit-bridge.liquid`) using existing foundation classes. One template edit (`index.json`) to add the section, reorder, and update P/S copy. No new CSS files, no JS.

**Tech Stack:** Shopify Liquid, LUSENA foundations CSS, lusena-icon snippet

**Spec:** `docs/superpowers/specs/2026-03-28-homepage-benefit-bridge-design.md`

---

### Task 1: Create the benefit bridge section

**Files:**
- Create: `sections/lusena-benefit-bridge.liquid`

**References to read first:**
- `sections/lusena-heritage.liquid` — closest pattern (3-tile grid, icon circles, centered heading, same animation approach)
- `snippets/lusena-icon.liquid` — icon rendering (verify `sparkles`, `star`, `droplets` exist)
- `assets/lusena-foundations.css` lines ~386-407 — `lusena-grid` classes
- `assets/lusena-foundations.css` line ~826 — `lusena-icon-circle` class

**IMPORTANT:** Before writing any Liquid, call `learn_shopify_api` with `api: "liquid"` via the Shopify Dev MCP tool.

- [ ] **Step 1: Call learn_shopify_api**

Use the MCP tool `mcp__shopify-dev-mcp__learn_shopify_api` with `api: "liquid"` to load Liquid syntax context.

- [ ] **Step 2: Write the complete section file**

Create `sections/lusena-benefit-bridge.liquid` with the following exact content:

```liquid
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
  class="lusena-bg-brand lusena-benefit-bridge lusena-spacing--standard"
  {% if override_style != blank %}
    style="{{ override_style }}"
  {% endif %}
>
  <div class="lusena-container">
    {%- if section.settings.heading != blank -%}
      <div class="lusena-text-center lusena-gap-section-intro{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}">
        <h2 class="lusena-type-h1">
          {{ section.settings.heading | escape }}
        </h2>
      </div>
    {%- endif -%}

    {%- if section.blocks.size > 0 -%}
      <div
        class="lusena-grid lusena-grid--3"
        {% if settings.animations_reveal_on_scroll %}data-cascade{% endif %}
      >
        {%- for block in section.blocks -%}
          <div
            class="lusena-benefit-bridge__card{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}"
            {{ block.shopify_attributes }}
          >
            {%- if block.settings.icon != blank -%}
              <div class="lusena-icon-circle lusena-benefit-bridge__icon">
                {% render 'lusena-icon', name: block.settings.icon, class: 'lusena-benefit-bridge__icon-svg', stroke_width: 1.5 %}
              </div>
            {%- endif -%}
            {%- if block.settings.title != blank -%}
              <h3 class="lusena-type-h2">{{ block.settings.title | escape }}</h3>
            {%- endif -%}
            {%- if block.settings.text != blank -%}
              <p class="lusena-type-body">{{ block.settings.text | escape }}</p>
            {%- endif -%}
          </div>
        {%- endfor -%}
      </div>
    {%- endif -%}
  </div>
</section>

{% stylesheet %}
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
  .lusena-benefit-bridge__icon-svg {
    width: 2.4rem;
    height: 2.4rem;
  }

  /* Mobile card separators (stacked cards need visual separation) */
  @media (max-width: 767px) {
    .lusena-benefit-bridge .lusena-benefit-bridge__card:not(:last-child) {
      padding-bottom: var(--lusena-space-4);
      border-bottom: 1px solid var(--lusena-color-n200);
    }
  }
{% endstylesheet %}

{% schema %}
{
  "name": "LUSENA Benefit Bridge",
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
      "id": "heading",
      "label": "Heading",
      "default": "Co zmieni się po pierwszej nocy?"
    }
  ],
  "blocks": [
    {
      "type": "card",
      "name": "Benefit card",
      "settings": [
        {
          "type": "text",
          "id": "icon",
          "label": "Icon name",
          "default": "sparkles",
          "info": "Available: sparkles, star, droplets, layers, shield-check, heart, gift"
        },
        {
          "type": "text",
          "id": "title",
          "label": "Title (max 28 chars)",
          "default": "Benefit title"
        },
        {
          "type": "text",
          "id": "text",
          "label": "Description (1 sentence)",
          "default": "Benefit description."
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "LUSENA Benefit Bridge",
      "blocks": [
        {
          "type": "card",
          "settings": {
            "icon": "sparkles",
            "title": "Gładka skóra o poranku",
            "text": "Jedwab sprzyja redukcji odcisków sennych - rano widzisz w lustrze wypoczętą, gładką twarz zamiast zagnieceń."
          }
        },
        {
          "type": "card",
          "settings": {
            "icon": "star",
            "title": "Włosy bez porannego chaosu",
            "text": "Gładki jedwab pomaga zachować fryzurę przez noc - mniej puszenia, plątania i łamania delikatnych pasm."
          }
        },
        {
          "type": "card",
          "settings": {
            "icon": "droplets",
            "title": "Krem pracuje całą noc",
            "text": "Jedwab nie wchłania kosmetyków tak jak bawełna - Twój krem na noc zostaje na skórze, gdzie może działać."
          }
        }
      ]
    }
  ]
}
{% endschema %}
```

**CSS specificity notes:**
- `.lusena-benefit-bridge .lusena-icon-circle` is 0-2-0, wins over foundations' `.lusena-icon-circle` (0-1-0). Correct per cascade rule.
- `.lusena-benefit-bridge .lusena-benefit-bridge__card:not(:last-child)` is 0-3-0 for mobile separator. Safe.
- Icon SVG class `lusena-benefit-bridge__icon-svg` passed directly to `lusena-icon` render call via `class:` parameter.

- [ ] **Step 3: Commit**

```bash
git add sections/lusena-benefit-bridge.liquid
git commit -m "feat(lusena): add benefit bridge section for homepage"
```

---

### Task 2: Update homepage template (add section, reorder, refresh P/S copy)

**Files:**
- Modify: `templates/index.json`

- [ ] **Step 1: Read current index.json**

Read `templates/index.json` to confirm current structure before editing.

- [ ] **Step 2: Add the benefit_bridge section to the sections object**

Add a new `"benefit_bridge"` key to the `"sections"` object in `index.json`, after the `"trust"` section. Use the Edit tool to insert this block:

```json
    "benefit_bridge": {
      "type": "lusena-benefit-bridge",
      "blocks": {
        "card-skin": {
          "type": "card",
          "settings": {
            "icon": "sparkles",
            "title": "Gładka skóra o poranku",
            "text": "Jedwab sprzyja redukcji odcisków sennych - rano widzisz w lustrze wypoczętą, gładką twarz zamiast zagnieceń."
          }
        },
        "card-hair": {
          "type": "card",
          "settings": {
            "icon": "star",
            "title": "Włosy bez porannego chaosu",
            "text": "Gładki jedwab pomaga zachować fryzurę przez noc - mniej puszenia, plątania i łamania delikatnych pasm."
          }
        },
        "card-care": {
          "type": "card",
          "settings": {
            "icon": "droplets",
            "title": "Krem pracuje całą noc",
            "text": "Jedwab nie wchłania kosmetyków tak jak bawełna - Twój krem na noc zostaje na skórze, gdzie może działać."
          }
        }
      },
      "block_order": [
        "card-skin",
        "card-hair",
        "card-care"
      ],
      "settings": {
        "heading": "Co zmieni się po pierwszej nocy?"
      }
    },
```

- [ ] **Step 3: Reorder the sections array**

Replace the `"order"` array at the bottom of `index.json` with:

```json
  "order": [
    "hero",
    "trust",
    "benefit_bridge",
    "bestsellers",
    "reviews",
    "problem_solution",
    "gift",
    "heritage",
    "faq",
    "final_cta"
  ]
```

This moves:
- `benefit_bridge` to position 3 (NEW)
- `bestsellers` stays at 4
- `reviews` stays at 5
- `problem_solution` moves from 3 to 6

- [ ] **Step 4: Update Problem/Solution copy — problem items**

In the `"problem_solution"` section of `index.json`, update the block settings:

**problem-0:** Change `title` to `"Tarcie tworzy zagniecenia"` and `text` to `"Włókna bawełny działają jak rzep - ciągną delikatną skórę twarzy i tworzą odciski, które z wiekiem znikają coraz wolniej."`

**problem-1:** Change `title` to `"Pielęgnacja znika w poduszce"` and `text` to `"Bawełna chłonie kosmetyki i naturalne nawilżenie skóry przez całą noc - Twój drogi krem pracuje dla poszewki, nie dla Ciebie."`

- [ ] **Step 5: Update Problem/Solution copy — solution items**

**solution-0:** Keep `title` as `"Gładkość bez tarcia"`. Change `text` to `"Gładka powierzchnia jedwabiu 22 momme sprzyja redukcji porannych zagnieceń na twarzy i pomaga zachować fryzurę przez noc."`

**solution-1:** Change `title` to `"Twój krem wreszcie działa"` and `text` to `"Jedwab pomaga zachować nawilżenie i kosmetyki na skórze zamiast w poszewce - pielęgnacja pracuje dla Ciebie, nie dla poduszki."`

- [ ] **Step 6: Commit**

```bash
git add templates/index.json
git commit -m "feat(lusena): homepage reorder + benefit bridge + P/S copy refresh"
```

---

### Task 3: Visual verification

**Prerequisites:** Dev server running at `http://127.0.0.1:9292/`. If not, start with `shopify theme dev`.

**IMPORTANT:** Use `/playwright-cli` skill for ALL browser interactions. Use a unique session name `-s=benefit-bridge-verify`.

- [ ] **Step 1: Desktop screenshot (1280px)**

```bash
playwright-cli -s=benefit-bridge-verify open http://127.0.0.1:9292/
playwright-cli -s=benefit-bridge-verify resize 1280 900
```

Scroll to the benefit bridge section (below trust bar) and take a screenshot. Verify:
- Heading "Co zmieni się po pierwszej nocy?" is centered, serif font
- 3 cards in a row with icon circles above titles
- Icon circles have teal color (`#0E5E5A`)
- Icons render correctly (sparkles, star, droplets)
- Cream background (`#F7F5F2`)
- Adequate spacing from trust bar above and bestsellers below

- [ ] **Step 2: Desktop — verify section order**

Scroll through the full page and verify the section order:
1. Hero
2. Trust bar
3. **Benefit bridge** (NEW)
4. Bestsellers
5. Testimonials
6. **Problem/Solution** (refreshed copy, moved down)
7. Bundles
8. Heritage
9. FAQ
10. Final CTA

- [ ] **Step 3: Desktop — verify P/S copy refresh**

Scroll to the P/S section (now position 6). Verify:
- Problem titles: "Tarcie tworzy zagniecenia" / "Pielęgnacja znika w poduszce"
- Solution titles: "Gładkość bez tarcia" / "Twój krem wreszcie działa"
- No "roztocza" anywhere in the section
- CTA link "Sprawdź dowody jakości →" still present

- [ ] **Step 4: Mobile screenshot (390px)**

```bash
playwright-cli -s=benefit-bridge-verify resize 390 844
playwright-cli -s=benefit-bridge-verify goto http://127.0.0.1:9292/
```

Scroll to benefit bridge section. Verify:
- Cards stack vertically (1 column)
- Cards are centered
- Thin separator line between cards (not after last card)
- Text is readable, no overflow
- Icon circles render at correct size

- [ ] **Step 5: Check compiled_assets size**

Open DevTools Network tab or use playwright to check:

```bash
playwright-cli -s=benefit-bridge-verify eval "performance.getEntriesByType('resource').filter(e => e.name.includes('compiled_assets')).map(e => ({name: e.name.split('/').pop(), size: Math.round(e.transferSize/1024) + 'KB'}))"
```

Expected: compiled_assets < 55KB. The new section adds ~30 lines of CSS, so increase should be minimal.

- [ ] **Step 6: Run shopify theme check**

```bash
shopify theme check
```

Expected: Only known baseline warnings (listed in CLAUDE.md). No new warnings from `lusena-benefit-bridge.liquid`.

- [ ] **Step 7: Close browser and fix any issues**

```bash
playwright-cli -s=benefit-bridge-verify close
```

If visual issues found, fix and re-verify. Common issues to watch for:
- Icon SVG not rendering: check `snippets/lusena-icon.liquid` has the icon name in its `when` cases
- Spacing too tight/loose: adjust spacing tier or add override padding
- Mobile separators too heavy: remove the `border-bottom` rule if it looks cluttered
- Type hierarchy wrong: ensure `lusena-type-h1` on section heading, `lusena-type-h2` on card titles

- [ ] **Step 8: Final commit (if fixes needed)**

```bash
git add -A
git commit -m "fix(lusena): benefit bridge visual polish"
```

---

### Task 4: Update section catalog documentation

**Files:**
- Modify: `.claude/rules/section-catalog.md`

- [ ] **Step 1: Add benefit bridge to Homepage table**

In the Homepage (`index.json`) table, add the benefit bridge row between trust bar and problem_solution:

```markdown
| `lusena-benefit-bridge` | standard | - | 3 benefit cards, icons |
```

- [ ] **Step 2: Update problem_solution position note**

The problem_solution section is now at position 6 (was 3). No table change needed — the table doesn't track position. But if there's any positional note, update it.

- [ ] **Step 3: Commit**

```bash
git add .claude/rules/section-catalog.md
git commit -m "docs: add benefit bridge to section catalog"
```
