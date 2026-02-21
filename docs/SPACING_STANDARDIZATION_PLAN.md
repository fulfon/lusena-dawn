# LUSENA Spacing Standardization — Implementation Plan

> **Purpose:** Centralize all vertical spacing across the LUSENA theme into a single, token-based system. Eliminate per-section hardcoded padding, ensure consistent gaps between sections and content elements, and add automatic same-background adjacency detection.
>
> **Created:** 2026-02-21
> **Status:** Implemented (theme code + core docs updated on 2026-02-21)

---

## Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Architecture Overview](#2-architecture-overview)
3. [Spacing Token Scale](#3-spacing-token-scale)
4. [Spacing Tier System (4 Tiers)](#4-spacing-tier-system-4-tiers)
5. [Same-bg vs Different-bg Section Gap](#5-same-bg-vs-different-bg-section-gap)
6. [Intra-Section Content Spacing Tokens](#6-intra-section-content-spacing-tokens)
7. [Per-Section Schema Override (Option B)](#7-per-section-schema-override-option-b)
8. [File-by-File Changes](#8-file-by-file-changes)
9. [Current State Audit (Source of Truth)](#9-current-state-audit-source-of-truth)
10. [Migration Checklist](#10-migration-checklist)
11. [Verification](#11-verification)
12. [Future Sections](#12-future-sections)

---

## 1. Problem Statement

### What's wrong today

1. **No single source of truth.** Each of the 28 LUSENA sections independently sets its own `padding-top` / `padding-bottom` via 4 schema range sliders. The visual gap between two adjacent sections is the **sum** of Section A's `padding_bottom` + Section B's `padding_top` — unpredictable and manually managed.

2. **No same-bg vs different-bg awareness.** When two adjacent sections share the same background color, their content visually merges. When backgrounds differ, the color boundary provides visual separation. Currently both cases get the same combined padding — there's no logic to adapt.

3. **Inconsistent intra-section spacing.** Kicker→heading, heading→content, content→CTA gaps use a mix of `space-y-3`, `space-y-4`, `space-y-6`, `space-y-8`, `mb-4`, `mb-8`, `mb-12`, `mb-16`, `mt-4`, `mt-12`, `mt-16`, `pt-4` — with no governing rule.

4. **Two CSS variable naming conventions.** 26 sections use `--lusena-section-padding-*-*`; 2 sections (`lusena-science`, `lusena-comparison`) use `--padding-*-*`. Both achieve the same thing.

5. **Changing spacing requires editing every section.** To shift standard padding from 56px to 64px, you'd need to update 20+ section schemas AND clear any template JSON overrides.

### What we want

- **One snippet** defines all spacing tokens as CSS custom properties.
- **Each section declares a "role"** (tier class), not raw pixel values.
- **Between-section gap** is automatically managed: 0 extra gap when backgrounds differ, a defined gap when they match.
- **Intra-section spacing** uses semantic CSS classes instead of ad-hoc Tailwind margins.
- **Per-section overrides** are still available (theme editor sliders defaulting to 0 = "use global").

---

## 2. Architecture Overview

### New files to create

| File | Purpose |
|---|---|
| `snippets/lusena-spacing-system.liquid` | Single source of truth for all spacing CSS custom properties, tier classes, and intra-section spacing utility classes. |
| `snippets/lusena-section-gap-detector.liquid` | Small JS script that detects adjacent sections with the same background color and adds `lusena-section-gap-same` class. |

### Files to modify

| File | Change |
|---|---|
| `layout/theme.liquid` | Add `{% render 'lusena-spacing-system' %}` and `{% render 'lusena-section-gap-detector' %}`. |
| All 28 `sections/lusena-*.liquid` files | Replace per-section padding CSS with tier class; update schema defaults to 0; update intra-section spacing classes. |

### Files NOT to modify

| File | Reason |
|---|---|
| `sections/lusena-header.liquid` | Uses fixed `py-4`, no section padding. Leave as-is. |
| `sections/lusena-footer.liquid` | Uses fixed `py-16`, no section padding. Leave as-is. |
| `sections/lusena-hero.liquid` | Full-bleed viewport hero, no section padding system. Leave as-is. |
| `sections/lusena-page-about.liquid` | Legacy monolithic section. Not used by any active template. Ignore. |
| `sections/lusena-page-quality.liquid` | Legacy monolithic section. Not used by any active template. Ignore. |
| `sections/lusena-page-returns.liquid` | Legacy monolithic section. Not used by any active template. Ignore. |
| Template JSON files (`templates/*.json`) | No padding overrides exist. Section defaults will change but JSONs stay untouched. |

---

## 3. Spacing Token Scale

All tokens follow the existing 4px grid from the brandbook. Values are mobile-first with desktop overrides at `min-width: 768px`.

```
Token Name              Mobile    Desktop    Purpose
──────────────────────  ────────  ─────────  ────────────────────────────────────
--lusena-space-xs       8px       8px        Kicker → heading
--lusena-space-sm       12px      16px       Heading → subheading/body
--lusena-space-md       20px      24px       Body → CTA, general content gap
--lusena-space-lg       32px      48px       Heading block → content grid
--lusena-space-xl       40px      64px       Section internal padding (standard)
--lusena-space-2xl      64px      96px       Section internal padding (hero)
--lusena-space-3xl      80px      128px      Section internal padding (landing — NOT USED, reserved)

--lusena-section-gap         0px       0px        Gap between different-bg sections
--lusena-section-gap-same    24px      32px       Gap between same-bg sections
```

> **Note on dual-purpose tokens:** `--lusena-space-lg` (32/48px) is used by both the **compact** tier section padding and the **`lusena-gap-section-intro`** utility class. Changing this token's value affects both simultaneously. If these ever need to diverge, introduce a dedicated `--lusena-space-section-intro` token.

> **Note on `--lusena-space-3xl`:** This token is defined but NOT assigned to any tier in the 4-tier system. It's reserved for future use or ad-hoc overrides. All returns-* sections that currently use 128/96 will be reassigned to the `hero` tier (96/64). The visual impact is a reduction from 128→96px desktop and 96→64px mobile on returns sections. If after visual review this feels too tight, the `--lusena-space-2xl` values can be increased, or a 5th tier can be introduced.

---

## 4. Spacing Tier System (4 Tiers)

Each section gets ONE tier class on its outermost element. The tier class applies `padding-top` and `padding-bottom` using the tokens from Section 3.

### Tier definitions

| Tier | CSS Class | Desktop Padding T/B | Mobile Padding T/B | When to use |
|---|---|---|---|---|
| **Full-bleed** | `lusena-spacing--full-bleed` | 0 / 0 | 0 / 0 | Viewport-height heroes with background images. Only `lusena-hero`. |
| **Hero** | `lusena-spacing--hero` | 96px / 96px | 64px / 64px | Page intro sections, landing CTAs, any section needing generous breathing room. |
| **Standard** | `lusena-spacing--standard` | 64px / 64px | 40px / 40px | Regular content sections — the vast majority. |
| **Compact** | `lusena-spacing--compact` | 48px / 48px | 32px / 32px | Utility / transactional sections (trust bar, PDP main, collection grid). |

### CSS implementation (conceptual)

> **Note:** This is the simplified conceptual model. The **actual CSS implementation** uses intermediate `--lusena-tier-pt` / `--lusena-tier-pb` custom properties plus a shared selector with `var()` fallback chains to support per-section overrides. See **Section 7** for the final CSS that should be written.

```css
/* Conceptual — do NOT copy this verbatim; see Section 7 for real implementation */
.lusena-spacing--full-bleed {
  padding-top: 0;
  padding-bottom: 0;
}
.lusena-spacing--compact {
  padding-top: var(--lusena-space-lg);    /* 32px mobile, 48px desktop */
  padding-bottom: var(--lusena-space-lg);
}
.lusena-spacing--standard {
  padding-top: var(--lusena-space-xl);    /* 40px mobile, 64px desktop */
  padding-bottom: var(--lusena-space-xl);
}
.lusena-spacing--hero {
  padding-top: var(--lusena-space-2xl);   /* 64px mobile, 96px desktop */
  padding-bottom: var(--lusena-space-2xl);
}
```

### Tier assignments for every section

| # | Section file | Current defaults (dt/db/mt/mb) | Assigned tier | Tier defaults (dt/db/mt/mb) | Delta |
|---|---|---|---|---|---|
| 1 | `lusena-hero` | N/A (viewport) | `full-bleed` *(conceptual only — file NOT modified, no class added)* | 0/0/0/0 | No change |
| 2 | `lusena-trust-bar` | 32/32/24/24 | `compact` | 48/48/32/32 | +16dt, +16db, +8mt, +8mb |
| 3 | `lusena-problem-solution` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 4 | `lusena-bestsellers` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 5 | `lusena-heritage` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 6 | `lusena-testimonials` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 7 | `lusena-bundles` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 8 | `lusena-faq` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 9 | `lusena-about-hero` | 96/96/64/64 | `hero` | 96/96/64/64 | No change |
| 10 | `lusena-about-story` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 11 | `lusena-about-values` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 12 | `lusena-quality-hero` | 96/96/64/64 | `hero` | 96/96/64/64 | No change |
| 13 | `lusena-quality-momme` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 14 | `lusena-quality-fire-test` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 15 | `lusena-quality-origin` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 16 | `lusena-quality-qc` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 17 | `lusena-quality-certificates` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 18 | `lusena-main-product` | 48/96/32/48 | `compact` | 48/48/32/32 | 0dt, -48db, 0mt, -16mb |
| 19 | `lusena-main-collection` | 48/48/32/32 | `compact` | 48/48/32/32 | No change |
| 20 | `lusena-pdp-feature-highlights` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 21 | `lusena-pdp-quality-evidence` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 22 | `lusena-pdp-details` | 56/56/40/40 | `standard` | 64/64/40/40 | +8dt, +8db |
| 23 | `lusena-returns-hero` | 128/128/96/96 | `hero` | 96/96/64/64 | -32dt, -32db, -32mt, -32mb |
| 24 | `lusena-returns-steps` | 128/128/96/96 | `hero` ⚠️ | 96/96/64/64 | -32dt, -32db, -32mt, -32mb |
| 25 | `lusena-returns-editorial` | 128/128/96/96 | `standard` | 64/64/40/40 | -64dt, -64db, -56mt, -56mb |
| 26 | `lusena-returns-faq` | 128/128/96/96 | `standard` | 64/64/40/40 | -64dt, -64db, -56mt, -56mb |
| 27 | `lusena-returns-final-cta` | 128/128/96/96 | `hero` | 96/96/64/64 | -32dt, -32db, -32mt, -32mb |
| 28 | `lusena-science` | 48/48/32/32 | `compact` | 48/48/32/32 | No change |
| 29 | `lusena-comparison` | 48/48/32/32 | `compact` | 48/48/32/32 | No change |

> ⚠️ **`lusena-returns-steps`** is assigned to `hero` tier because it serves as a primary content section on the returns page and currently uses the spacious 128/128/96/96 values — `hero` (96/64) is the closest fit. After visual review, this could be changed to `standard` if it feels right.
>
> ⚠️ **`lusena-main-product`** currently has an asymmetric padding (48/96/32/48). The `compact` tier will make it symmetric (48/48/32/32). The extra bottom padding was likely there to create distance from the next PDP section. After migration, the same-bg gap detector may add `--lusena-section-gap-same` (32px desktop) which partially compensates. **Visual review needed.**

---

## 5. Same-bg vs Different-bg Section Gap

### Concept

When two adjacent sections have the **same background color**, extra margin is needed to visually separate them. When backgrounds **differ**, the color change itself provides separation.

### Implementation: JS-based background detection

A small script (`snippets/lusena-section-gap-detector.liquid`) runs after DOM load and:

1. Gets all `.shopify-section` children of `#MainContent`.
2. For each adjacent pair, computes the `backgroundColor` of the first matching child element (the section's outermost `<section>` or `<div>` with a background).
3. If backgrounds match → adds `lusena-section-gap-same` class to the second section's outermost element (adds extra `padding-top`).
4. If backgrounds differ → adds `lusena-section-gap-different` class (no extra padding, tier default is sufficient).

### CSS

```css
/* Doubled class selector → specificity 0,2,0 beats tier's 0,1,0 */
.lusena-section-gap-same.lusena-section-gap-same {
  padding-top: calc(var(--lusena-section-gap-same) + var(--lusena-section-padding-top-mobile, var(--lusena-tier-pt)));
}
.lusena-section-gap-different {
  /* No extra padding — tier padding is sufficient */
}

@media (min-width: 768px) {
  .lusena-section-gap-same.lusena-section-gap-same {
    padding-top: calc(var(--lusena-section-gap-same) + var(--lusena-section-padding-top-desktop, var(--lusena-tier-pt)));
  }
}
```

> **Why `calc()` and doubled selector?** The tier class already sets `padding-top`. The gap class must **add** the gap on top of the existing tier padding, not replace it. `calc(gap + tier-padding)` achieves this. The doubled class selector (`.lusena-section-gap-same.lusena-section-gap-same`) gives specificity 0,2,0 — always beating the tier selector's 0,1,0 regardless of source order. This is robust and doesn't break if CSS is reordered.
>
> **With a schema override active:** If `--lusena-section-padding-top-mobile` is set via inline style (e.g., 80px), the `calc()` correctly picks it up: `calc(24px + 80px) = 104px`. The override and gap are additive.

### JS logic (pseudocode)

```javascript
function normalizeColor(bgColor) {
  // Convert rgb/rgba string to comparable "r,g,b" format
  // Treat 'transparent' and 'rgba(0,0,0,0)' as null
}

function detect() {
  const main = document.getElementById('MainContent');
  const sections = main.querySelectorAll(':scope > .shopify-section');

  for (let i = 1; i < sections.length; i++) {
    const prevEl = sections[i-1].querySelector('section, [class*="lusena-"]');
    const currEl = sections[i].querySelector('section, [class*="lusena-"]');

    const prevBg = normalizeColor(getComputedStyle(prevEl).backgroundColor);
    const currBg = normalizeColor(getComputedStyle(currEl).backgroundColor);

    if (prevBg && currBg && prevBg === currBg) {
      currEl.classList.add('lusena-section-gap-same');
    } else {
      currEl.classList.add('lusena-section-gap-different');
    }
  }
}

// Run on DOMContentLoaded + requestAnimationFrame (so styles are computed)
// Re-run on shopify:section:load (theme editor support)
```

### Edge cases

- **First section** on a page never gets a gap class (no previous sibling).
- **`lusena-hero` (full-bleed):** Its background is an image, not a CSS color. `getComputedStyle` will return `transparent` or `rgba(0,0,0,0)`. The normalizer treats this as `null` — so the next section will get `lusena-section-gap-different` (0 gap), which is correct.
- **`lusena-pdp-quality-evidence`:** Uses inline `background-color: rgb(247 245 242 / 1)` instead of a Tailwind class. `getComputedStyle` will still pick this up correctly.
- **Sections with `border-t`:** `lusena-bestsellers` and `lusena-quality-certificates` have `border-t border-brand-bg`. The border serves as a visual separator already. The gap system is additive — if the border is sufficient, the same-bg gap adds a small extra space which is fine.

### Gap color behavior (padding-top approach)

The same-bg gap is implemented via **extra `padding-top`** on the inner `<section>` element (added on top of the tier padding). Because padding is inside the element, the gap area inherits the section's own background color:

- **Two adjacent white sections** (e.g., PDP main-product → feature-highlights): the gap is **white** — invisible, just extra breathing room.
- **Two adjacent beige sections** (e.g., Zwroty editorial → faq): the gap is **beige** — invisible, just extra breathing room.

This is intentional: same-bg gaps create seamless extra spacing without visible dividers, consistent with the premium LUSENA aesthetic.

### Shopify theme editor support

When a section is reloaded in the theme editor (drag-and-drop, settings change), the `shopify:section:load` event fires. The detector re-runs to recalculate gaps.

---

## 6. Intra-Section Content Spacing Tokens

These utility classes replace ad-hoc Tailwind margin classes inside sections. They are defined in `snippets/lusena-spacing-system.liquid`.

### Utility classes

| Class | CSS | Mobile | Desktop | Replaces |
|---|---|---|---|---|
| `.lusena-gap-kicker` | `margin-bottom: var(--lusena-space-xs)` | 8px | 8px | `mb-2`, `mb-3`, `space-y-3` (kicker element) |
| `.lusena-gap-heading` | `margin-bottom: var(--lusena-space-sm)` | 12px | 16px | `mb-4`, `space-y-4` (heading element) |
| `.lusena-gap-body` | `margin-bottom: var(--lusena-space-md)` | 20px | 24px | `mb-6`, `space-y-6`, `mt-8`, `pt-4` (body/CTA spacing) |
| `.lusena-gap-section-intro` | `margin-bottom: var(--lusena-space-lg)` | 32px | 48px | `mb-12`, `mb-16`, `margin: 0 0 48px` (heading block → content) |

### Migration mapping for each intra-section pattern

#### Kicker → Heading gap

| Section | Current | New |
|---|---|---|
| `lusena-heritage` | `space-y-8` on parent wrapper | Remove `space-y-8`, add `lusena-gap-kicker` on kicker `<span>` |
| `lusena-about-hero` | `space-y-8` on parent wrapper | Remove `space-y-8`, add `lusena-gap-kicker` on kicker `<span>` |
| `lusena-problem-solution` | `space-y-8` on parent wrapper | Remove `space-y-8`, add `lusena-gap-kicker` on kicker `<span>` |
| `lusena-bundles` | `space-y-6` on parent wrapper | Remove `space-y-6`, add `lusena-gap-kicker` on kicker `<span>` |
| `lusena-quality-hero` | `space-y-6` on parent wrapper | Remove `space-y-6`, add `lusena-gap-kicker` on kicker `<span>` |
| `lusena-returns-hero` | `space-y-6` on parent wrapper | Remove `space-y-6`, add `lusena-gap-kicker` on kicker `<span>` |
| `lusena-returns-steps` | `space-y-3` on parent wrapper | Remove `space-y-3`, add `lusena-gap-kicker` on kicker `<span>` |
| `lusena-about-values` | `mt-4` on `<h2>` | Remove `mt-4` from `<h2>`, add `lusena-gap-kicker` on kicker element |

> **When migrating `space-y-*` patterns:** The parent wrapper uses `space-y-*` to space ALL children evenly. When converting, you must remove `space-y-*` from the parent and add individual `lusena-gap-*` classes to each child element. This gives more control per element.

#### Heading → Body/Subheading gap

| Section | Current | New |
|---|---|---|
| `lusena-bestsellers` | `space-y-4` on parent → h2→subheading | Add `lusena-gap-heading` on `<h2>` |
| `lusena-testimonials` | `space-y-4` on parent → h2→subheading | Add `lusena-gap-heading` on `<h2>` |
| `lusena-faq` | `mb-4` on `<h2>` | Replace `mb-4` with `lusena-gap-heading` |
| `lusena-quality-momme` | `space-y-6` on parent | Add `lusena-gap-heading` on `<h2>` |

#### Heading block → Content grid gap

| Section | Current | New |
|---|---|---|
| `lusena-faq` | `mb-16` | Replace `mb-16` with `lusena-gap-section-intro` |
| `lusena-bestsellers` | `mb-12` | Replace `mb-12` with `lusena-gap-section-intro` |
| `lusena-testimonials` | `mb-16` | Replace `mb-16` with `lusena-gap-section-intro` |
| `lusena-about-values` | `mb-16` | Replace `mb-16` with `lusena-gap-section-intro` |
| `lusena-returns-steps` | `mb-16` | Replace `mb-16` with `lusena-gap-section-intro` |
| `lusena-pdp-quality-evidence` | CSS `margin: 0 0 48px` | Replace with `lusena-gap-section-intro` |
| `lusena-pdp-details` | `mb-8 md:mb-12` | Replace with `lusena-gap-section-intro` |

#### Body → CTA gap

| Section | Current | New |
|---|---|---|
| `lusena-bestsellers` | `mt-12` on CTA wrapper | Replace `mt-12` with `lusena-gap-body` on the element before CTA |
| `lusena-testimonials` | `mt-12` on CTA wrapper | Replace `mt-12` with `lusena-gap-body` on the element before CTA |
| `lusena-problem-solution` | `mt-16` on CTA wrapper | Replace `mt-16` with `lusena-gap-body` on the element before CTA |
| `lusena-heritage` | `pt-4` on CTA wrapper | Replace `pt-4` with `lusena-gap-body` |

### Content grid gaps — DO NOT CHANGE

Content grid `gap-*` values (e.g., `gap-8`, `gap-12`, `gap-x-4 gap-y-12`) are **horizontal + vertical layout concerns** specific to each section's content type. These are NOT part of the vertical spacing standardization. Leave them as-is.

---

## 7. Per-Section Schema Override (Option B)

### Concept

The 4 padding range sliders remain in each section's `{% schema %}` but their **defaults change to `0`**. A value of `0` means "use the tier class default." A non-zero value means "override the tier for this specific section instance."

### Liquid logic change (per section)

**BEFORE:**
```liquid
<section
  class="bg-brand-bg lusena-faq"
  style="
    --lusena-section-padding-top-mobile: {{ section.settings.padding_top_mobile }}px;
    --lusena-section-padding-bottom-mobile: {{ section.settings.padding_bottom_mobile }}px;
    --lusena-section-padding-top-desktop: {{ section.settings.padding_top }}px;
    --lusena-section-padding-bottom-desktop: {{ section.settings.padding_bottom }}px;
  "
>
```

**AFTER:**
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
  class="bg-surface-1 lusena-faq lusena-spacing--standard"
  {% if override_style != blank %}
    style="{{ override_style }}"
  {% endif %}
>
```

### Override CSS (in `lusena-spacing-system.liquid`)

The override mechanism uses CSS custom property fallback chains:

```css
/* Each tier sets its own --lusena-tier-pt and --lusena-tier-pb */
.lusena-spacing--compact {
  --lusena-tier-pt: var(--lusena-space-lg);
  --lusena-tier-pb: var(--lusena-space-lg);
}
.lusena-spacing--standard {
  --lusena-tier-pt: var(--lusena-space-xl);
  --lusena-tier-pb: var(--lusena-space-xl);
}
.lusena-spacing--hero {
  --lusena-tier-pt: var(--lusena-space-2xl);
  --lusena-tier-pb: var(--lusena-space-2xl);
}
.lusena-spacing--full-bleed {
  --lusena-tier-pt: 0px;
  --lusena-tier-pb: 0px;
}

/* All tier classes apply padding via one rule — override vars win if set */
.lusena-spacing--compact,
.lusena-spacing--standard,
.lusena-spacing--hero,
.lusena-spacing--full-bleed {
  padding-top: var(--lusena-section-padding-top-mobile, var(--lusena-tier-pt));
  padding-bottom: var(--lusena-section-padding-bottom-mobile, var(--lusena-tier-pb));
}

@media (min-width: 768px) {
  .lusena-spacing--compact,
  .lusena-spacing--standard,
  .lusena-spacing--hero,
  .lusena-spacing--full-bleed {
    padding-top: var(--lusena-section-padding-top-desktop, var(--lusena-tier-pt));
    padding-bottom: var(--lusena-section-padding-bottom-desktop, var(--lusena-tier-pb));
  }
}
```

**How this works:**
- If `--lusena-section-padding-top-mobile` is **not set** (no inline style), CSS `var()` falls through to `--lusena-tier-pt` (the tier default).
- If `--lusena-section-padding-top-mobile` **is set** (via inline style, because schema override > 0), it takes precedence.

This is clean, requires no `!important`, and keeps the override mechanism entirely in CSS.

### Schema setting changes

For each section, the 4 range settings change:

```json
{
  "type": "header",
  "content": "Spacing overrides (0 = use global default)"
},
{
  "type": "range",
  "id": "padding_top",
  "label": "Padding top override – desktop",
  "min": 0,
  "max": 300,
  "step": 4,
  "unit": "px",
  "default": 0
},
{
  "type": "range",
  "id": "padding_bottom",
  "label": "Padding bottom override – desktop",
  "min": 0,
  "max": 300,
  "step": 4,
  "unit": "px",
  "default": 0
},
{
  "type": "range",
  "id": "padding_top_mobile",
  "label": "Padding top override – mobile",
  "min": 0,
  "max": 300,
  "step": 4,
  "unit": "px",
  "default": 0
},
{
  "type": "range",
  "id": "padding_bottom_mobile",
  "label": "Padding bottom override – mobile",
  "min": 0,
  "max": 300,
  "step": 4,
  "unit": "px",
  "default": 0
}
```

Key changes from current:
- `default` changes from current value to `0`
- `max` standardized to `300` for all sections
- `label` updated to include "override" and "(0 = use global default)"
- The `"header"` content explains the override behavior

> **Limitation:** Because `0` means "use global default," a merchant cannot override a section's padding to exactly 0px via the schema slider. The minimum possible override is 4px (first step). To get 0px section padding, use the `full-bleed` tier. This is an acceptable trade-off for the vast majority of use cases.

---

## 8. File-by-File Changes

### Phase 1: Add the spacing system (non-breaking)

These changes add the new system without affecting any existing section. The new CSS classes exist but nothing uses them yet.

#### 8.1 Create `snippets/lusena-spacing-system.liquid`

Create this file with:

1. A `{% doc %}` tag explaining the snippet's purpose.
2. A `{% stylesheet %}` block containing (in this exact order):
   1. `:root` with all `--lusena-space-*` token definitions (mobile-first)
   2. `@media (min-width: 768px)` override block for desktop token values
   3. Tier classes (`.lusena-spacing--full-bleed`, `--compact`, `--standard`, `--hero`) that set `--lusena-tier-pt`/`--lusena-tier-pb` intermediate variables
   4. Shared tier padding rule with CSS fallback chain (Section 7) + desktop `@media` override
   5. Gap classes (`.lusena-section-gap-same.lusena-section-gap-same` with doubled selector for specificity, `.lusena-section-gap-different`) — MUST come after tier rules
   6. Intra-section utility classes (`.lusena-gap-kicker`, `.lusena-gap-heading`, `.lusena-gap-body`, `.lusena-gap-section-intro`)

#### 8.2 Create `snippets/lusena-section-gap-detector.liquid`

Create this file with:

1. A `{% doc %}` tag.
2. A `<script>` block implementing the background detection logic from Section 5.
3. Re-run on `shopify:section:load` for theme editor support.

#### 8.3 Modify `layout/theme.liquid`

Add two render calls:

```liquid
{% render 'lusena-missing-utilities' %}
{% render 'lusena-button-system' %}
{% render 'lusena-spacing-system' %}    <!-- ADD THIS LINE -->
```

And before `</body>`:

```liquid
    {% render 'lusena-section-gap-detector' %}    <!-- ADD THIS LINE -->
  </body>
</html>
```

**Exact insertion points:**
- `{% render 'lusena-spacing-system' %}` → after line 302 (after `{% render 'lusena-button-system' %}`)
- `{% render 'lusena-section-gap-detector' %}` → before `</body>` tag (approximately line 415-420, verify exact line)

---

### Phase 2: Migrate sections one-by-one

For each section, the following changes are needed. They are listed in the recommended order of migration (homepage first, then subpages, then PDP).

**Repeat this exact pattern for each section:**

#### A. Remove per-section padding CSS from `{% stylesheet %}` block

**Delete** the CSS rules that apply `padding-top` / `padding-bottom` using the section's custom properties:

```css
/* DELETE THIS BLOCK */
.lusena-SECTION {
    padding-top: var(--lusena-section-padding-top-mobile);
    padding-bottom: var(--lusena-section-padding-bottom-mobile);
}
@media (min-width: 768px) {
    .lusena-SECTION {
        padding-top: var(--lusena-section-padding-top-desktop);
        padding-bottom: var(--lusena-section-padding-bottom-desktop);
    }
}
```

#### B. Add tier class to outermost element

```liquid
<!-- BEFORE -->
<section class="bg-surface-1 lusena-faq" style="--lusena-section-padding-top-mobile: ...">

<!-- AFTER -->
<section class="bg-surface-1 lusena-faq lusena-spacing--standard" {% if override_style != blank %}style="{{ override_style }}"{% endif %}>
```

#### C. Add override logic at top of section

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
```

#### D. Update schema settings

Change the 4 padding settings to match the new defaults (Section 7).

#### E. Update intra-section spacing classes

Replace ad-hoc Tailwind margin/space classes with semantic `lusena-gap-*` classes per the mapping in Section 6.

---

### Section migration details

Below is the specific tier + intra-section changes for each section. The override logic (step C) and schema update (step D) are identical for all sections — only the tier class and intra-section classes differ.

#### Homepage sections

| Section | Tier class | Intra-section changes |
|---|---|---|
| `lusena-hero` | None (leave as-is — no padding system) | No changes |
| `lusena-trust-bar` | `lusena-spacing--compact` | No intra-section heading/kicker changes needed (trust bar has no heading block pattern) |
| `lusena-problem-solution` | `lusena-spacing--standard` | Remove `space-y-8` from the 2 column header wrappers (lines ~12 and ~34). Leave `space-y-8` and `pt-4` on the items list containers (lines ~19 and ~41) — those are content grid gaps. Add `lusena-gap-kicker` on kicker, `lusena-gap-heading` on heading in both columns. Replace `mt-16` on CTA wrapper with `lusena-gap-body`. |
| `lusena-bestsellers` | `lusena-spacing--standard` | Remove `space-y-4` from heading wrapper block; add `lusena-gap-heading` on `<h2>`. Replace `mb-12` with `lusena-gap-section-intro`. Replace `mt-12` on CTA with `lusena-gap-body`. |
| `lusena-heritage` | `lusena-spacing--standard` | Remove `space-y-8` from wrapper; add `lusena-gap-kicker` on kicker, `lusena-gap-heading` on heading. Replace `pt-4` on CTA with `lusena-gap-body`. |
| `lusena-testimonials` | `lusena-spacing--standard` | Remove `space-y-4` from heading wrapper; add `lusena-gap-heading` on `<h2>`. Replace `mb-16` with `lusena-gap-section-intro`. Replace `mt-12` on CTA with `lusena-gap-body`. |
| `lusena-bundles` | `lusena-spacing--standard` | Remove `space-y-6` from text wrapper (~line 29); add `lusena-gap-kicker` on kicker, `lusena-gap-heading` on heading, `lusena-gap-body` on body paragraphs. Leave `space-y-3` on benefits `<ul>` (~line 47) as-is (list internal gap). |
| `lusena-faq` | `lusena-spacing--standard` | Replace `mb-4` on `<h2>` with `lusena-gap-heading`. Replace `mb-16` on heading wrapper with `lusena-gap-section-intro`. |

#### About page sections

| Section | Tier class | Intra-section changes |
|---|---|---|
| `lusena-about-hero` | `lusena-spacing--hero` | Remove `space-y-8` from wrapper; add `lusena-gap-kicker` on kicker, `lusena-gap-heading` on heading. |
| `lusena-about-story` | `lusena-spacing--standard` | Remove `space-y-12` from outer container wrapper (~line 11). Add `lusena-gap-section-intro` on the heading/title element to create gap before body content. Leave `space-y-6` on richtext paragraph wrapper (~line 15) as-is (body internal gap). |
| `lusena-about-values` | `lusena-spacing--standard` | Remove `mt-4` from `<h2>`; add `lusena-gap-kicker` on kicker element. Replace `mb-16` with `lusena-gap-section-intro`. |

#### Quality page sections

| Section | Tier class | Intra-section changes |
|---|---|---|
| `lusena-quality-hero` | `lusena-spacing--hero` | Remove `space-y-6` from wrapper; add `lusena-gap-kicker` on kicker, `lusena-gap-heading` on heading. |
| `lusena-quality-momme` | `lusena-spacing--standard` | Remove `space-y-6` from text column wrapper (~line 28); add `lusena-gap-heading` on `<h2>`. Leave `space-y-4` on richtext wrapper (~line 32), `mt-4` on benefits `<ul>` (~line 35), and `space-y-2` on list items as-is (body/list internal gaps). |
| `lusena-quality-fire-test` | `lusena-spacing--standard` | Replace `mb-12` on `<h2>` (~line 13) with `lusena-gap-section-intro`. Replace `mt-8` on `<p>` body text (~line 33) with `lusena-gap-body`. |
| `lusena-quality-origin` | `lusena-spacing--standard` | Remove `space-y-6` from text column wrapper (~line 14); add `lusena-gap-kicker` on kicker, `lusena-gap-heading` on heading. Leave `space-y-4` on richtext wrapper (~line 20) as-is (body internal gap). |
| `lusena-quality-qc` | `lusena-spacing--standard` | Remove `space-y-12` from outer container (~line 12); add `lusena-gap-section-intro` on the heading element. Leave `mb-4` and `mb-2` inside cards (~lines 22-23) as-is (card internal gaps). |
| `lusena-quality-certificates` | `lusena-spacing--standard` | Replace `mb-6` on `<h2>` (~line 16) with `lusena-gap-heading`. Replace `mb-8` on body text wrapper (~line 19) with `lusena-gap-body`. |

#### PDP sections

| Section | Tier class | Intra-section changes |
|---|---|---|
| `lusena-main-product` | `lusena-spacing--compact` | No intra-section heading changes (PDP has its own layout). Verify bottom padding reduction (96→48px desktop) is acceptable — may need schema override. |
| `lusena-pdp-feature-highlights` | `lusena-spacing--standard` | No heading block. Grid gaps stay as-is (CSS `gap: 32px` / `48px`). |
| `lusena-pdp-quality-evidence` | `lusena-spacing--standard` | Replace CSS `margin: 0 0 48px` on heading with `lusena-gap-section-intro` class. |
| `lusena-pdp-details` | `lusena-spacing--standard` | Replace `mb-8 md:mb-12` on heading with `lusena-gap-section-intro`. |

#### Returns page sections

| Section | Tier class | Intra-section changes |
|---|---|---|
| `lusena-returns-hero` | `lusena-spacing--hero` | Remove `space-y-6` from wrapper; add `lusena-gap-kicker` on kicker, `lusena-gap-heading` on heading. |
| `lusena-returns-steps` | `lusena-spacing--hero` | Remove `space-y-3` from wrapper; add `lusena-gap-kicker` on kicker. Replace `mb-16` with `lusena-gap-section-intro`. |
| `lusena-returns-editorial` | `lusena-spacing--standard` | Remove `space-y-6` from left column wrapper (~line 12); add `lusena-gap-heading` on heading element. Leave `space-y-4` on right column (~line 34), `mb-2` (~line 35), and `mb-4` (~line 47) as-is (image grid layout gaps). |
| `lusena-returns-faq` | `lusena-spacing--standard` | Remove `space-y-3` from header block wrapper (~line 12); add `lusena-gap-kicker` on kicker. Replace `mb-12` on header block (~line 12) with `lusena-gap-section-intro`. Leave `py-4` on accordion wrapper (~line 22), CSS accordion padding, `mt-12` on contact prompt (~line 63), and `mb-4` on prompt text (~line 64) as-is (accordion/CTA internal layout). |
| `lusena-returns-final-cta` | `lusena-spacing--hero` | Remove `space-y-6` from container wrapper (~line 12); add `lusena-gap-kicker` on icon/kicker element, `lusena-gap-heading` on heading, `lusena-gap-body` on body text. Leave CSS `padding-top: 1.6rem` on actions div as-is (button layout). |

#### Outlier sections (Pattern B)

| Section | Tier class | Additional changes |
|---|---|---|
| `lusena-science` | `lusena-spacing--compact` | Also change CSS variable names from `--padding-*-*` to `--lusena-section-padding-*-*` for consistency. Update inline style template. |
| `lusena-comparison` | `lusena-spacing--compact` | Same as above. |

---

### Phase 3: Cleanup

After all sections are migrated and visually verified:

1. **Remove dead CSS**: Each section's `{% stylesheet %}` block will have the old padding rules deleted as part of migration.
2. **Update brandbook**: Update `docs/theme-brandbook-uiux.md` sections 5.2 and 8.2 to reference the new spacing system instead of the old per-section pattern.
3. **Update AGENTS.md**: Add note about the spacing system to the architecture section.

---

## 9. Current State Audit (Source of Truth)

This section records the exact current state of every spacing value for reference during migration.

### 9.1 Section padding defaults (current, pre-migration)

| Section | dt | db | mt | mb | max | CSS var pattern |
|---|---|---|---|---|---|---|
| `lusena-trust-bar` | 32 | 32 | 24 | 24 | 200 | `--lusena-section-padding-*` |
| `lusena-bestsellers` | 56 | 56 | 40 | 40 | 240 | `--lusena-section-padding-*` |
| `lusena-testimonials` | 56 | 56 | 40 | 40 | 240 | `--lusena-section-padding-*` |
| `lusena-problem-solution` | 56 | 56 | 40 | 40 | 240 | `--lusena-section-padding-*` |
| `lusena-bundles` | 56 | 56 | 40 | 40 | 240 | `--lusena-section-padding-*` |
| `lusena-faq` | 56 | 56 | 40 | 40 | 240 | `--lusena-section-padding-*` |
| `lusena-heritage` | 56 | 56 | 40 | 40 | 240 | `--lusena-section-padding-*` |
| `lusena-main-product` | 48 | 96 | 32 | 48 | 240 | `--lusena-section-padding-*` |
| `lusena-main-collection` | 48 | 48 | 32 | 32 | 240 | `--lusena-section-padding-*` |
| `lusena-about-hero` | 96 | 96 | 64 | 64 | 300 | `--lusena-section-padding-*` |
| `lusena-about-story` | 56 | 56 | 40 | 40 | 300 | `--lusena-section-padding-*` |
| `lusena-about-values` | 56 | 56 | 40 | 40 | 300 | `--lusena-section-padding-*` |
| `lusena-pdp-details` | 56 | 56 | 40 | 40 | 240 | `--lusena-section-padding-*` |
| `lusena-pdp-feature-highlights` | 56 | 56 | 40 | 40 | 240 | `--lusena-section-padding-*` |
| `lusena-pdp-quality-evidence` | 56 | 56 | 40 | 40 | 240 | `--lusena-section-padding-*` |
| `lusena-returns-hero` | 128 | 128 | 96 | 96 | 300 | `--lusena-section-padding-*` |
| `lusena-returns-steps` | 128 | 128 | 96 | 96 | 300 | `--lusena-section-padding-*` |
| `lusena-returns-faq` | 128 | 128 | 96 | 96 | 300 | `--lusena-section-padding-*` |
| `lusena-returns-editorial` | 128 | 128 | 96 | 96 | 300 | `--lusena-section-padding-*` |
| `lusena-returns-final-cta` | 128 | 128 | 96 | 96 | 300 | `--lusena-section-padding-*` |
| `lusena-quality-hero` | 96 | 96 | 64 | 64 | 300 | `--lusena-section-padding-*` |
| `lusena-quality-momme` | 56 | 56 | 40 | 40 | 300 | `--lusena-section-padding-*` |
| `lusena-quality-fire-test` | 56 | 56 | 40 | 40 | 300 | `--lusena-section-padding-*` |
| `lusena-quality-origin` | 56 | 56 | 40 | 40 | 300 | `--lusena-section-padding-*` |
| `lusena-quality-qc` | 56 | 56 | 40 | 40 | 300 | `--lusena-section-padding-*` |
| `lusena-quality-certificates` | 56 | 56 | 40 | 40 | 300 | `--lusena-section-padding-*` |
| `lusena-science` | 48 | 48 | 32 | 32 | 100 | `--padding-*-*` |
| `lusena-comparison` | 48 | 48 | 32 | 32 | 100 | `--padding-*-*` |

*Legend: dt = desktop top, db = desktop bottom, mt = mobile top, mb = mobile bottom, max = schema range max*

### 9.2 Template JSON section order (current)

**`templates/index.json`:**
1. `lusena-hero`
2. `lusena-trust-bar`
3. `lusena-problem-solution`
4. `lusena-bestsellers`
5. `lusena-heritage`
6. `lusena-testimonials` (key: `reviews`)
7. `lusena-bundles` (key: `gift`)
8. `lusena-faq`

**`templates/page.o-nas.json`:**
1. `lusena-about-hero`
2. `lusena-about-story`
3. `lusena-about-values`

**`templates/page.nasza-jakosc.json`:**
1. `lusena-quality-hero`
2. `lusena-quality-momme`
3. `lusena-quality-fire-test`
4. `lusena-quality-origin`
5. `lusena-quality-qc`
6. `lusena-quality-certificates`
7. `lusena-trust-bar`

**`templates/product.json`:**
1. `lusena-main-product`
2. `lusena-pdp-feature-highlights`
3. `lusena-pdp-quality-evidence`
4. `lusena-pdp-details` (key: `pdp_details_questions`)

**`templates/page.zwroty.json`:**
1. `lusena-returns-hero`
2. `lusena-returns-steps`
3. `lusena-returns-editorial`
4. `lusena-returns-faq`
5. `lusena-returns-final-cta`

### 9.3 Background color per section (current)

| Section | BG class / method | Resolved color |
|---|---|---|
| `lusena-hero` | Background image | N/A (image) |
| `lusena-trust-bar` | `bg-surface-2` | `#F0EEEB` |
| `lusena-problem-solution` | `bg-brand-bg` | `#F7F5F2` |
| `lusena-bestsellers` | `bg-surface-1` + `border-t border-brand-bg` | `#FFFFFF` |
| `lusena-heritage` | `bg-brand-bg` | `#F7F5F2` |
| `lusena-testimonials` | `bg-surface-1` | `#FFFFFF` |
| `lusena-bundles` | `bg-surface-2` | `#F0EEEB` |
| `lusena-faq` | `bg-surface-1` | `#FFFFFF` |
| `lusena-about-hero` | `bg-white` | `#FFFFFF` |
| `lusena-about-story` | `bg-brand-bg` | `#F7F5F2` |
| `lusena-about-values` | `bg-white` | `#FFFFFF` |
| `lusena-quality-hero` | `bg-brand-bg` | `#F7F5F2` |
| `lusena-quality-momme` | `bg-white` | `#FFFFFF` |
| `lusena-quality-fire-test` | `bg-brand-bg` | `#F7F5F2` |
| `lusena-quality-origin` | `bg-white` | `#FFFFFF` |
| `lusena-quality-qc` | `bg-brand-bg` | `#F7F5F2` |
| `lusena-quality-certificates` | `bg-white` + `border-t` | `#FFFFFF` |
| `lusena-main-product` | None (white implied) | `#FFFFFF` |
| `lusena-pdp-feature-highlights` | None (white implied) | `#FFFFFF` |
| `lusena-pdp-quality-evidence` | Inline CSS `rgb(247 245 242 / 1)` | `#F7F5F2` |
| `lusena-pdp-details` | `border-t` (white implied) | `#FFFFFF` |
| `lusena-returns-hero` | `bg-brand-bg` | `#F7F5F2` |
| `lusena-returns-steps` | `bg-white` | `#FFFFFF` |
| `lusena-returns-editorial` | `bg-brand-bg` | `#F7F5F2` |
| `lusena-returns-faq` | `bg-brand-bg` | `#F7F5F2` |
| `lusena-returns-final-cta` | `bg-accent-cta` | `#0E5E5A` |

### 9.4 Adjacent same-bg pairs (current, by page)

Based on background colors above:

**Homepage:** No same-bg adjacent pairs (colors alternate correctly).

**O nas:** No same-bg adjacent pairs.

**Nasza jakość:**
- `lusena-quality-certificates` (`bg-white`) → `lusena-trust-bar` (`bg-surface-2`) — different.
- All others alternate `bg-brand-bg` ↔ `bg-white` — no same-bg pairs.

**PDP:**
- `lusena-main-product` (white) → `lusena-pdp-feature-highlights` (white) — **SAME BG** ✹
- `lusena-pdp-feature-highlights` (white) → `lusena-pdp-quality-evidence` (`#F7F5F2`) — different (barely).
- `lusena-pdp-quality-evidence` (`#F7F5F2`) → `lusena-pdp-details` (white) — different.

**Zwroty:**
- `lusena-returns-editorial` (`bg-brand-bg`) → `lusena-returns-faq` (`bg-brand-bg`) — **SAME BG** ✹
- All others alternate or use unique colors.

> ✹ These are the pairs where the gap detector will add `lusena-section-gap-same` (32px desktop / 24px mobile extra padding-top, in the section's own background color).

---

## 10. Migration Checklist

Use this checklist to track progress. Mark each item when complete.

### Phase 1: Infrastructure (non-breaking)

- [ ] Create `snippets/lusena-spacing-system.liquid` with all tokens, tier classes, gap classes, utility classes
- [ ] Create `snippets/lusena-section-gap-detector.liquid` with JS background detection
- [ ] Add `{% render 'lusena-spacing-system' %}` to `layout/theme.liquid` after `{% render 'lusena-button-system' %}`
- [ ] Add `{% render 'lusena-section-gap-detector' %}` to `layout/theme.liquid` before `</body>`
- [ ] Visual check: no changes should be visible (new classes exist but nothing uses them yet)

### Phase 2: Section migration

**Homepage:**
- [ ] `sections/lusena-trust-bar.liquid` → `lusena-spacing--compact`
- [ ] `sections/lusena-problem-solution.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-bestsellers.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-heritage.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-testimonials.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-bundles.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-faq.liquid` → `lusena-spacing--standard`

**About page:**
- [ ] `sections/lusena-about-hero.liquid` → `lusena-spacing--hero`
- [ ] `sections/lusena-about-story.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-about-values.liquid` → `lusena-spacing--standard`

**Quality page:**
- [ ] `sections/lusena-quality-hero.liquid` → `lusena-spacing--hero`
- [ ] `sections/lusena-quality-momme.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-quality-fire-test.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-quality-origin.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-quality-qc.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-quality-certificates.liquid` → `lusena-spacing--standard`

**PDP:**
- [ ] `sections/lusena-main-product.liquid` → `lusena-spacing--compact`
- [ ] `sections/lusena-pdp-feature-highlights.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-pdp-quality-evidence.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-pdp-details.liquid` → `lusena-spacing--standard`

**Returns page:**
- [ ] `sections/lusena-returns-hero.liquid` → `lusena-spacing--hero`
- [ ] `sections/lusena-returns-steps.liquid` → `lusena-spacing--hero`
- [ ] `sections/lusena-returns-editorial.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-returns-faq.liquid` → `lusena-spacing--standard`
- [ ] `sections/lusena-returns-final-cta.liquid` → `lusena-spacing--hero`

**Collection:**
- [ ] `sections/lusena-main-collection.liquid` → `lusena-spacing--compact`

**Outliers:**
- [ ] `sections/lusena-science.liquid` → `lusena-spacing--compact` + rename CSS vars
- [ ] `sections/lusena-comparison.liquid` → `lusena-spacing--compact` + rename CSS vars

### Phase 3: Cleanup & documentation

- [x] Update `docs/theme-brandbook-uiux.md` section 5.2 (spacing)
- [x] Update `docs/theme-brandbook-uiux.md` section 8.2 (new section recipe)
- [x] Update `docs/theme-brandbook-uiux.md` do/don't checklist
- [ ] Add entry to `docs/THEME_CHANGES.md`
- [ ] Commit with message: `feat: global spacing standardization system`

---

## 11. Verification

After each migration phase, verify visually on the Shopify dev server (`http://127.0.0.1:9292/`):

### Visual checks per page

| Page | URL path | What to verify |
|---|---|---|
| Homepage | `/` | All section gaps look consistent. Trust bar feels compact. No excessive gaps between alternating backgrounds. |
| O nas | `/pages/o-nas` | Hero has generous padding. Story and values sections match standard spacing. |
| Nasza jakość | `/pages/nasza-jakosc` | Hero has generous padding. All quality sections have consistent spacing. Trust bar at bottom is compact. |
| PDP | `/products/[any]` | Main product is compact. Feature highlights / quality evidence / details have consistent standard spacing. **Critical:** Check gap between main-product and feature-highlights (same-bg pair). |
| Zwroty | `/pages/zwroty` | Returns hero has generous padding. **Critical:** Check gap between returns-editorial and returns-faq (same-bg pair). Final CTA has generous padding. |

### Specific things to watch for

1. **PDP main-product bottom:** Currently 96px desktop / 48px mobile. After migration to `compact` tier: 48px desktop / 32px mobile + potential 32px/24px same-bg gap. Check if this feels too tight.
2. **Returns sections:** Currently 128/96. After migration to `hero` tier: 96/64. This is a noticeable reduction — verify it doesn't feel cramped.
3. **Same-bg gap detection:** On PDP (main-product → feature-highlights) and Zwroty (editorial → faq), verify the extra padding-top appears and looks right. The gap should be invisible (same bg color as the section) — just extra breathing room.
4. **Header → first section:** The first section's top padding is now governed by the tier class, not per-section override. On pages where `--lusena-header-height` padding-top is applied to `<main>`, verify the header doesn't overlap content.
5. **Last section → footer:** The last section's bottom padding is now governed by the tier class. Verify there's adequate space before the footer.

### Automated checks

- Run `shopify theme check` — no new warnings beyond the known baseline.
- Check browser console for JS errors from the gap detector script.

---

## 12. Future Sections

When creating a new LUSENA section after this system is in place:

### Required pattern

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
  class="bg-brand-bg lusena-NEW-SECTION lusena-spacing--standard"
  {% if override_style != blank %}
    style="{{ override_style }}"
  {% endif %}
>
  <div class="container max-w-4xl mx-auto">
    {% if section.settings.kicker != blank %}
      <p class="text-xs uppercase tracking-widest text-secondary lusena-gap-kicker">
        {{ section.settings.kicker }}
      </p>
    {% endif %}

    <h2 class="text-3xl md:text-4xl font-serif text-primary lusena-gap-heading">
      {{ section.settings.heading }}
    </h2>

    {% if section.settings.body != blank %}
      <div class="text-secondary max-w-2xl lusena-gap-section-intro">
        {{ section.settings.body }}
      </div>
    {% endif %}

    <!-- Content grid/blocks here -->

    {% if section.settings.button_label != blank %}
      <div class="lusena-gap-body">
        <a href="{{ section.settings.button_link }}"
           class="lusena-btn lusena-btn--primary lusena-btn--size-default">
          {{ section.settings.button_label }}
        </a>
      </div>
    {% endif %}
  </div>
</section>
```

### Schema template (spacing section)

```json
{
  "type": "header",
  "content": "Spacing overrides (0 = use global default)"
},
{
  "type": "range",
  "id": "padding_top",
  "label": "Padding top override – desktop",
  "min": 0,
  "max": 300,
  "step": 4,
  "unit": "px",
  "default": 0
},
{
  "type": "range",
  "id": "padding_bottom",
  "label": "Padding bottom override – desktop",
  "min": 0,
  "max": 300,
  "step": 4,
  "unit": "px",
  "default": 0
},
{
  "type": "range",
  "id": "padding_top_mobile",
  "label": "Padding top override – mobile",
  "min": 0,
  "max": 300,
  "step": 4,
  "unit": "px",
  "default": 0
},
{
  "type": "range",
  "id": "padding_bottom_mobile",
  "label": "Padding bottom override – mobile",
  "min": 0,
  "max": 300,
  "step": 4,
  "unit": "px",
  "default": 0
}
```

### Choosing a tier

| Your section is... | Use tier |
|---|---|
| A full-viewport hero with background image | `lusena-spacing--full-bleed` |
| A page intro, landing hero, or generous CTA section | `lusena-spacing--hero` |
| A regular content section (most sections) | `lusena-spacing--standard` |
| A utility bar, PDP main, collection grid, or compact row | `lusena-spacing--compact` |

### Intra-section spacing classes to use

| Between... | Use class on the TOP element |
|---|---|
| Kicker → Heading | `lusena-gap-kicker` on the kicker element |
| Heading → Subheading/body | `lusena-gap-heading` on the heading element |
| Body text → CTA / Content block → next block | `lusena-gap-body` on the element above |
| Heading block (kicker+heading+subtext) → Content grid | `lusena-gap-section-intro` on the last element of the heading block |

### What NOT to do

- ❌ Do NOT add per-section padding CSS in `{% stylesheet %}`.
- ❌ Do NOT use `mb-12`, `mb-16`, `mt-8`, `space-y-8` for vertical content spacing — use `lusena-gap-*` classes.
- ❌ Do NOT set padding schema defaults to any value other than `0` (unless you have a specific reason to force an override).
- ❌ Do NOT use `--padding-*-*` CSS variable names (legacy Pattern B) — always use `--lusena-section-padding-*-*`.

---

*Implementation completed on 2026-02-21. Active spacing source of truth is now `docs/theme-brandbook-uiux.md` plus `snippets/lusena-spacing-system.liquid` and `snippets/lusena-section-gap-detector.liquid`. Keep this file as implementation history/reference.*
