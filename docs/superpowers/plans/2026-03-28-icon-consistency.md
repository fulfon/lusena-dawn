# PDP Icon Consistency Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make all PDP feature highlight icons semantically consistent across 8 products — 9 icon reassignments, 1 new icon (`palette`), 1 new animation (`feather`).

**Architecture:** Icons are rendered via `snippets/lusena-icon.liquid` (static SVGs) and `snippets/lusena-icon-animated.liquid` (animated wrappers). Animations live in `assets/lusena-icon-animations.css`. Per-product icon values come from metafields (`lusena.pdp_feature_N_icon`) which override schema defaults. Product metafield docs in `memory-bank/doc/products/` are the source of truth for what gets pushed to Shopify.

**Tech Stack:** Liquid, inline SVG, CSS keyframe animations

**Spec:** `docs/superpowers/specs/2026-03-28-icon-consistency-strategy.md`

---

### Task 1: Add `palette` static SVG icon

**Files:**
- Modify: `snippets/lusena-icon.liquid:204-206` (insert new case before `moon`)

- [ ] **Step 1: Add `palette` icon case to lusena-icon.liquid**

Insert a new `when 'palette'` case before the `moon` case (line 204). The icon is three circles in a gentle arc — representing three color swatches. Design follows Lucide conventions: 24x24 viewBox, stroke-based, no fill.

```liquid
    {%- when 'palette' -%}
      <circle cx="7" cy="15" r="2.5"></circle>
      <circle cx="12" cy="9" r="2.5"></circle>
      <circle cx="17" cy="15" r="2.5"></circle>
```

Three circles arranged in an inverted-V arc. Clean, minimal, immediately reads as "three options/colors." Consistent stroke weight with all other LUSENA icons.

- [ ] **Step 2: Commit**

```
git add snippets/lusena-icon.liquid
git commit -m "feat(lusena): add palette static SVG icon"
```

---

### Task 2: Add `feather` animated icon

**Files:**
- Modify: `snippets/lusena-icon-animated.liquid:22` (add to animated set string)
- Modify: `snippets/lusena-icon-animated.liquid:119-121` (insert new case before endcase)
- Modify: `assets/lusena-icon-animations.css` (add keyframes + animation rules + reduced motion)

- [ ] **Step 1: Add `feather` to the animated set string**

In `snippets/lusena-icon-animated.liquid` line 22, change:

```liquid
  assign animated_icons = ',heart,layers,droplets,wind,shield-check,sparkles,gift,clock,moon,'
```

to:

```liquid
  assign animated_icons = ',heart,layers,droplets,wind,shield-check,sparkles,gift,clock,moon,feather,'
```

- [ ] **Step 2: Add `feather` animated SVG case**

In `snippets/lusena-icon-animated.liquid`, insert before the `{%- endcase -%}` (line 121):

```liquid
      {%- when 'feather' -%}
        <g class="lusena-anim-feather">
          <path d="M3 21h3.5C14 21 21 14 21 6v-3h-3.5C10 3 3 10 3 18v3z"></path>
          <path d="M3 21l18-18"></path>
          <path d="M9 15h4"></path>
          <path d="M15 9v-4"></path>
        </g>
```

- [ ] **Step 3: Add feather keyframes and animation rules to CSS**

In `assets/lusena-icon-animations.css`, add after the moon-glow keyframe block (after line 67):

```css
@keyframes lusena-feather-float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-2px) rotate(1deg); }
}
```

Add `.lusena-anim-feather` to the transform-box rule block. Change line 71-87 from:

```css
.lusena-anim-heart,
.lusena-anim-layers-top,
.lusena-anim-layers-bottom,
.lusena-anim-droplets-small,
.lusena-anim-droplets-large,
.lusena-anim-wind-1,
.lusena-anim-wind-2,
.lusena-anim-wind-3,
.lusena-anim-sparkles-1,
.lusena-anim-sparkles-2,
.lusena-anim-sparkles-3,
.lusena-anim-gift-lid,
.lusena-anim-gift-bow,
.lusena-anim-moon {
  transform-box: fill-box;
  transform-origin: center;
}
```

to:

```css
.lusena-anim-heart,
.lusena-anim-layers-top,
.lusena-anim-layers-bottom,
.lusena-anim-droplets-small,
.lusena-anim-droplets-large,
.lusena-anim-wind-1,
.lusena-anim-wind-2,
.lusena-anim-wind-3,
.lusena-anim-sparkles-1,
.lusena-anim-sparkles-2,
.lusena-anim-sparkles-3,
.lusena-anim-gift-lid,
.lusena-anim-gift-bow,
.lusena-anim-moon,
.lusena-anim-feather {
  transform-box: fill-box;
  transform-origin: center;
}
```

Add animation rule after the moon section (after line 186):

```css
/* ---------- Feather: gentle float + micro-rotation, 8s ---------- */

.lusena-anim-feather {
  animation: lusena-feather-float 8s ease-in-out infinite;
  animation-delay: var(--lusena-anim-stagger, 0s);
}
```

Add `.lusena-anim-feather` to the reduced-motion block. Change the selector list (lines 201-216) from:

```css
  .lusena-anim-heart,
  .lusena-anim-layers-top,
  .lusena-anim-layers-bottom,
  .lusena-anim-droplets-small,
  .lusena-anim-droplets-large,
  .lusena-anim-wind-1,
  .lusena-anim-wind-2,
  .lusena-anim-wind-3,
  .lusena-anim-sparkles-1,
  .lusena-anim-sparkles-2,
  .lusena-anim-sparkles-3,
  .lusena-anim-gift-lid,
  .lusena-anim-gift-bow,
  .lusena-anim-moon,
  .lusena-anim-clock-minute {
    animation: none !important;
  }
```

to:

```css
  .lusena-anim-heart,
  .lusena-anim-layers-top,
  .lusena-anim-layers-bottom,
  .lusena-anim-droplets-small,
  .lusena-anim-droplets-large,
  .lusena-anim-wind-1,
  .lusena-anim-wind-2,
  .lusena-anim-wind-3,
  .lusena-anim-sparkles-1,
  .lusena-anim-sparkles-2,
  .lusena-anim-sparkles-3,
  .lusena-anim-gift-lid,
  .lusena-anim-gift-bow,
  .lusena-anim-moon,
  .lusena-anim-feather,
  .lusena-anim-clock-minute {
    animation: none !important;
  }
```

- [ ] **Step 4: Commit**

```
git add snippets/lusena-icon-animated.liquid assets/lusena-icon-animations.css
git commit -m "feat(lusena): add feather icon animation"
```

---

### Task 3: Add `palette` animated icon

**Files:**
- Modify: `snippets/lusena-icon-animated.liquid:22` (add to animated set)
- Modify: `snippets/lusena-icon-animated.liquid` (insert new case)
- Modify: `assets/lusena-icon-animations.css` (add keyframes + animation rules + reduced motion)

- [ ] **Step 1: Add `palette` to the animated set string**

In `snippets/lusena-icon-animated.liquid` line 22, change (after Task 2):

```liquid
  assign animated_icons = ',heart,layers,droplets,wind,shield-check,sparkles,gift,clock,moon,feather,'
```

to:

```liquid
  assign animated_icons = ',heart,layers,droplets,wind,shield-check,sparkles,gift,clock,moon,feather,palette,'
```

- [ ] **Step 2: Add `palette` animated SVG case**

In `snippets/lusena-icon-animated.liquid`, insert before the `{%- endcase -%}`:

```liquid
      {%- when 'palette' -%}
        <g class="lusena-anim-palette-1">
          <circle cx="7" cy="15" r="2.5"></circle>
        </g>
        <g class="lusena-anim-palette-2">
          <circle cx="12" cy="9" r="2.5"></circle>
        </g>
        <g class="lusena-anim-palette-3">
          <circle cx="17" cy="15" r="2.5"></circle>
        </g>
```

- [ ] **Step 3: Add palette keyframes and animation rules to CSS**

In `assets/lusena-icon-animations.css`, add after the feather section:

```css
/* ---------- Palette: sequential opacity pulse across 3 swatches, 7s ---------- */

@keyframes lusena-palette-pulse {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 1; }
}
```

Add `.lusena-anim-palette-1`, `.lusena-anim-palette-2`, `.lusena-anim-palette-3` to the transform-box rule block (append after `.lusena-anim-feather`):

```css
.lusena-anim-palette-1,
.lusena-anim-palette-2,
.lusena-anim-palette-3,
```

Add animation rules:

```css
.lusena-anim-palette-1 {
  animation: lusena-palette-pulse 7s ease-in-out infinite;
  animation-delay: var(--lusena-anim-stagger, 0s);
}

.lusena-anim-palette-2 {
  animation: lusena-palette-pulse 7s ease-in-out infinite;
  animation-delay: calc(var(--lusena-anim-stagger, 0s) + 2.3s);
}

.lusena-anim-palette-3 {
  animation: lusena-palette-pulse 7s ease-in-out infinite;
  animation-delay: calc(var(--lusena-anim-stagger, 0s) + 4.6s);
}
```

Add to reduced-motion block (append after `.lusena-anim-feather,`):

```css
  .lusena-anim-palette-1,
  .lusena-anim-palette-2,
  .lusena-anim-palette-3,
```

- [ ] **Step 4: Commit**

```
git add snippets/lusena-icon-animated.liquid assets/lusena-icon-animations.css
git commit -m "feat(lusena): add palette icon with animation"
```

---

### Task 4: Add `palette` to section schema select options

**Files:**
- Modify: `sections/lusena-pdp-feature-highlights.liquid:319-329` (add option to select list)

- [ ] **Step 1: Add palette option to icon select**

In `sections/lusena-pdp-feature-highlights.liquid`, in the schema JSON block, change the options array from:

```json
          "options": [
            { "value": "sparkles", "label": "Sparkles" },
            { "value": "wind", "label": "Wind" },
            { "value": "shield-check", "label": "Shield Check" },
            { "value": "gift", "label": "Gift" },
            { "value": "droplets", "label": "Droplets" },
            { "value": "heart", "label": "Heart" },
            { "value": "map-pin", "label": "Map Pin" },
            { "value": "layers", "label": "Layers" },
            { "value": "package", "label": "Package" }
          ]
```

to:

```json
          "options": [
            { "value": "sparkles", "label": "Sparkles" },
            { "value": "wind", "label": "Wind" },
            { "value": "shield-check", "label": "Shield Check" },
            { "value": "gift", "label": "Gift" },
            { "value": "droplets", "label": "Droplets" },
            { "value": "heart", "label": "Heart" },
            { "value": "map-pin", "label": "Map Pin" },
            { "value": "layers", "label": "Layers" },
            { "value": "package", "label": "Package" },
            { "value": "palette", "label": "Palette" },
            { "value": "feather", "label": "Feather" },
            { "value": "moon", "label": "Moon" },
            { "value": "clock", "label": "Clock" }
          ]
```

This adds all icons actually used by products to the editor dropdown (previously `moon`, `clock`, `feather` were only available via metafield override).

- [ ] **Step 2: Commit**

```
git add sections/lusena-pdp-feature-highlights.liquid
git commit -m "feat(lusena): add palette, feather, moon, clock to icon schema select"
```

---

### Task 5: Update product metafield docs — Bonnet, Scrunchie, Heatless Curlers

**Files:**
- Modify: `memory-bank/doc/products/czepek-jedwabny.md` — C3 icon: `wind` -> `moon`, animation spec C3
- Modify: `memory-bank/doc/products/scrunchie-jedwabny.md` — C5 icon: `moon` -> `feather`, animation spec C5
- Modify: `memory-bank/doc/products/walek-do-lokow.md` — C5 icon: `heart` -> `feather`, animation spec C5

- [ ] **Step 1: Update Bonnet C3 icon**

In `memory-bank/doc/products/czepek-jedwabny.md`, in the Feature highlights table, change:

```
| `lusena.pdp_feature_3_icon` | wind | Done |
```

to:

```
| `lusena.pdp_feature_3_icon` | moon | **UPDATED** (icon consistency: "stays on all night" = overnight, not breathability) |
```

In the animation spec table, change the Card 3 row from:

```
| 3 | wind | Three curved wind lines. Lines gently wave from left to right in sequence (translateX 0→2px→0), staggered start times, over 7 seconds total. Feels like a soft, barely-there breeze - comforting, not chaotic. Easing: ease-in-out. Reinforces breathability and lightness of the bonnet. |
```

to:

```
| 3 | moon | Crescent moon with a very slow glow pulse (scale 1→1.04→1, opacity 1→0.82→1) over 8 seconds. Calm, protective nighttime feeling. Easing: ease-in-out. Reinforces that the bonnet stays on reliably all night. |
```

- [ ] **Step 2: Update Scrunchie C5 icon**

In `memory-bank/doc/products/scrunchie-jedwabny.md`, in the Feature highlights table, change:

```
| `lusena.pdp_feature_5_icon` | moon | **COMPLETED** (2026-03-28) |
```

to:

```
| `lusena.pdp_feature_5_icon` | feather | **UPDATED** (icon consistency: "no crease mark" = weightless/traceless, not nighttime) |
```

In the animation spec table, change the Card 5 row from:

```
| 5 | moon | Crescent moon with a small star beside it. The moon very slowly floats up 1px then back down over 7 seconds - a gentle hovering motion like it's suspended in the night sky. The small star has a very slow opacity blink (1.0 → 0.3 → 1.0 over 5 seconds, offset 2s from moon cycle). Serene, unhurried - reinforces the peaceful overnight angle. Easing: ease-in-out. |
```

to:

```
| 5 | feather | Single feather shape. Very slow, gentle float - subtle vertical drift (translateY 0→-2px→0) with barely perceptible rotation (±1°) over 8 seconds. The feather seems to hover weightlessly. Easing: ease-in-out. Reinforces the scrunchie being so light it leaves no trace. |
```

- [ ] **Step 3: Update Heatless Curlers C5 icon**

In `memory-bank/doc/products/walek-do-lokow.md`, in the Feature highlights table, change:

```
| `lusena.pdp_feature_5_icon` | heart | Done (2026-03-28) |
```

to:

```
| `lusena.pdp_feature_5_icon` | feather | **UPDATED** (icon consistency: "soft, no pressure" = weightless comfort, not body protection) |
```

In the animation spec table, change the Card 5 row from:

```
| 5 | heart | Heart shape with a very slow, gentle scale pulse (1.0→1.02→1.0) over 7 seconds. The heart seems to "breathe" - calm, the comforting idea that the curler won't hurt. Easing: ease-in-out. Barely perceptible. |
```

to:

```
| 5 | feather | Single feather shape. Very slow, gentle float - subtle vertical drift (translateY 0→-2px→0) with barely perceptible rotation (±1°) over 8 seconds. The feather seems to hover weightlessly. Easing: ease-in-out. Reinforces the soft, pressure-free comfort of sleeping with the curler. |
```

- [ ] **Step 4: Commit**

```
git add memory-bank/doc/products/czepek-jedwabny.md memory-bank/doc/products/scrunchie-jedwabny.md memory-bank/doc/products/walek-do-lokow.md
git commit -m "docs: update icon assignments for bonnet, scrunchie, heatless curlers"
```

---

### Task 6: Update product metafield docs — Nocna Rutyna, Piekny Sen, Scrunchie Trio

**Files:**
- Modify: `memory-bank/doc/products/nocna-rutyna.md` — C3 icon: `clock` -> `moon`, C5 icon: `wind` -> `sparkles`, animation specs
- Modify: `memory-bank/doc/products/piekny-sen.md` — C1 icon: `moon` -> `heart`, C3 icon: `heart` -> `sparkles`, animation specs
- Modify: `memory-bank/doc/products/scrunchie-trio.md` — C1 icon: `droplets` -> `palette`, C3 icon: `wind` -> `clock`, animation specs

- [ ] **Step 1: Update Nocna Rutyna C3 and C5 icons**

In `memory-bank/doc/products/nocna-rutyna.md`, Feature highlights table:

Change C3:
```
| `lusena.pdp_feature_3_icon` | clock | Done |
```
to:
```
| `lusena.pdp_feature_3_icon` | moon | **UPDATED** (icon consistency: "every night ritual" = overnight; echoes Bonnet C3) |
```

Change C5:
```
| `lusena.pdp_feature_5_icon` | wind | Done (2026-03-28) |
```
to:
```
| `lusena.pdp_feature_5_icon` | sparkles | **UPDATED** (icon consistency: "effortless morning" = radiant result; echoes Poszewka C5) |
```

In the animation spec table, change Card 3 from:
```
| 3 | clock | Clock face with hour and minute hands. Hands perform a gentle tick-tock motion - minute hand advances by a tiny increment then settles, hour hand barely moves. 8-second cycle. Easing: ease-in-out. Reinforces the nightly ritual and the 8-hour protection window. Calm, measured, never rushed. |
```
to:
```
| 3 | moon | Crescent moon with a very slow glow pulse (scale 1→1.04→1, opacity 1→0.82→1) over 8 seconds. Calm, protective nighttime feeling. Easing: ease-in-out. Reinforces the every-night ritual. |
```

Change Card 5 from:
```
| 5 | wind | 3 curved air-current lines with gentle rightward drift (translateX 0 → 2px → 0) over 7 seconds, staggered delays (0s, 0.7s, 1.4s). Evokes the fresh, light feeling of an unrushed morning - a gentle breeze through an open window. Easing: ease-in-out. Already implemented in lusena-icon-animations.css. |
```
to:
```
| 5 | sparkles | Three sparkle elements with sequential opacity pulse (0.4→1.0→0.4), staggered by 2.3s, over 7 seconds. Clean, radiant feeling. Easing: ease-in-out. Reinforces the radiant, effortless morning result. |
```

- [ ] **Step 2: Update Piekny Sen C1 and C3 icons**

In `memory-bank/doc/products/piekny-sen.md`, Feature highlights table:

Change C1:
```
| `lusena.pdp_feature_1_icon` | moon | Done |
```
to:
```
| `lusena.pdp_feature_1_icon` | heart | **UPDATED** (icon consistency: "full face protection" = gentle on body; echoes both component C1s) |
```

Change C3:
```
| `lusena.pdp_feature_3_icon` | heart | Done |
```
to:
```
| `lusena.pdp_feature_3_icon` | sparkles | **UPDATED** (icon consistency: "beautiful morning" = radiant result; echoes Poszewka C5) |
```

In the animation spec table, change Card 1 from:
```
| 1 | moon | Crescent moon with a very slow, gentle orbital drift (translate 0->1px->0) over 8 seconds. Subtle glow pulse on the inner curve (opacity 0.7->1->0.7). Calm, protective nighttime feeling. Easing: ease-in-out. |
```
to:
```
| 1 | heart | Heart shape with a very slow, gentle scale pulse (1.0→1.02→1.0) over 7 seconds. The heart seems to "breathe" - calm, protective feeling toward the entire face. Easing: ease-in-out. Barely perceptible. |
```

Change Card 3 from:
```
| 3 | heart | Heart shape with a very slow, gentle scale pulse (1.0->1.02->1.0) over 7 seconds. The heart seems to "breathe" - calm, the feeling of waking up refreshed and cared for. Easing: ease-in-out. Barely perceptible. |
```
to:
```
| 3 | sparkles | Three sparkle elements with sequential opacity pulse (0.4→1.0→0.4), staggered by 2.3s, over 7 seconds. Clean, radiant feeling. Easing: ease-in-out. Reinforces the beautiful, radiant morning result. |
```

- [ ] **Step 3: Update Scrunchie Trio C1 and C3 icons**

In `memory-bank/doc/products/scrunchie-trio.md`, Feature highlights table:

Change C1:
```
| `lusena.pdp_feature_1_icon` | droplets | Done |
```
to:
```
| `lusena.pdp_feature_1_icon` | palette | **UPDATED** (icon consistency: "color variety" requires dedicated icon, not moisture-retention droplets) |
```

Change C3:
```
| `lusena.pdp_feature_3_icon` | wind | Done |
```
to:
```
| `lusena.pdp_feature_3_icon` | clock | **UPDATED** (icon consistency: "always at hand" = everyday routine, not breathability) |
```

In the animation spec table, change Card 1 from:
```
| 1 | droplets | Three small droplets in a cluster. Each droplet gently pulses opacity in sequence (0.6->1->0.6), one at a time, left to right. 7-second full cycle. Easing: ease-in-out. The three drops represent three colors - calm, playful variety. |
```
to:
```
| 1 | palette | Three circles (color swatches) in a gentle arc. Each circle pulses opacity in sequence (0.5→1.0→0.5), staggered by 2.3s, over 7 seconds. Three swatches echo three scrunchies. Calm, playful variety. Easing: ease-in-out. |
```

Change Card 3 from:
```
| 3 | wind | Three curved wind lines. Lines gently wave from left to right in sequence (translateX 0->2px->0), staggered start times, over 6 seconds total. Feels like a soft breeze - lightness and freedom of always having silk at hand. Easing: ease-in-out. |
```
to:
```
| 3 | clock | Clock face with hour and minute hands. Minute hand performs a gentle tick-tock motion (rotate 60→65deg), hour hand static at 300deg. 7-second cycle. Easing: ease-in-out. Reinforces silk being part of every moment of your day. |
```

- [ ] **Step 4: Commit**

```
git add memory-bank/doc/products/nocna-rutyna.md memory-bank/doc/products/piekny-sen.md memory-bank/doc/products/scrunchie-trio.md
git commit -m "docs: update icon assignments for nocna-rutyna, piekny-sen, scrunchie-trio"
```

---

### Task 7: Update product-setup-checklist with icon vocabulary

**Files:**
- Modify: `memory-bank/doc/products/product-setup-checklist.md:115`

- [ ] **Step 1: Update available icons list and add semantic definitions**

In `memory-bank/doc/products/product-setup-checklist.md`, change line 115 from:

```
**Available icon names:** `sparkles`, `wind`, `shield-check`, `gift`, `droplets`, `heart`, `map-pin`, `layers`, `package`, `truck`, `clock`, `file-text`, `feather`, `scale`, `leaf`, `hourglass`, `smile`, `moon`
```

to:

```
**Available icon names:** `sparkles`, `wind`, `shield-check`, `gift`, `droplets`, `heart`, `map-pin`, `layers`, `package`, `truck`, `clock`, `file-text`, `feather`, `scale`, `leaf`, `hourglass`, `smile`, `moon`, `palette`

**Icon semantic definitions (variable cards 1/3/5 — one meaning per icon, no exceptions):**

| Icon | Meaning | Use for |
|------|---------|---------|
| `heart` | Gentle on your body | Silk reduces friction/pressure on skin, hair, or eyes |
| `wind` | Cool & gentle | Breathes, thermoregulates, no heat, smooth surface |
| `droplets` | Locks moisture in | Oils, serums, masks stay on you, not absorbed |
| `sparkles` | Radiant & fresh | Purity, clean surface, beautiful morning result |
| `moon` | All night, every night | Overnight benefit, stays on while you sleep |
| `clock` | Fits your routine | Zero effort, time does the work, everyday habit |
| `feather` | Weightless & traceless | No pressure, ultralight, forget you're wearing it |
| `palette` | Your colors | Color variety, personal choice |
```

- [ ] **Step 2: Commit**

```
git add memory-bank/doc/products/product-setup-checklist.md
git commit -m "docs: add icon semantic definitions to product-setup-checklist"
```

---

### Task 8: Update animated icon snippet doc comment

**Files:**
- Modify: `snippets/lusena-icon-animated.liquid:8` (update @param doc to include new icons)

- [ ] **Step 1: Update doc comment**

In `snippets/lusena-icon-animated.liquid`, change line 8 from:

```liquid
  @param {string} name - Icon name (heart, layers, droplets, wind, shield-check, sparkles, gift, clock, moon)
```

to:

```liquid
  @param {string} name - Icon name (heart, layers, droplets, wind, shield-check, sparkles, gift, clock, moon, feather, palette)
```

- [ ] **Step 2: Commit**

```
git add snippets/lusena-icon-animated.liquid
git commit -m "docs: update animated icon snippet doc comment"
```

---

### Task 9: Visual verification

**Files:** None (read-only verification)

- [ ] **Step 1: Start dev server if not running**

```
shopify theme dev
```

- [ ] **Step 2: Verify palette static icon renders**

Use `/playwright-cli` to navigate to a PDP and temporarily test the palette icon renders correctly by checking the icon snippet directly. Navigate to Scrunchie Trio PDP to verify.

- [ ] **Step 3: Verify feather animation works**

Navigate to Maska 3D PDP (which already uses `feather` on C5). Confirm the feather icon now animates instead of being static.

- [ ] **Step 4: Verify palette animation works**

After Scrunchie Trio metafields are pushed to Shopify, verify the palette icon animates with sequential opacity pulse on the three circles.

- [ ] **Step 5: Run theme check**

```
shopify theme check
```

Verify no new warnings beyond the known baseline listed in CLAUDE.md.
