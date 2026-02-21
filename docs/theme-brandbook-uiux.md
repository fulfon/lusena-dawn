# LUSENA Theme Brandbook — UI/UX & Implementation Guide

> **Generated:** 2026-02-20 · **Theme base:** Dawn v15.4.1 · **Brand:** LUSENA (PL-first, premium silk)

---

## 1. Purpose & How to Use This Document

### Who this is for

- **Developers** adding new sections, templates, or theme features.
- **Designers** creating mockups that will be implemented in the theme.
- **Future contractors** who need to ship work that looks like it belongs.

### What problems it prevents

| Problem | How this doc helps |
|---|---|
| Visual drift between pages | Defines validated tokens, component patterns, and composition rules |
| Inconsistent button/interaction styles | Documents the canonical button system and its variants |
| Broken responsive behavior | Lists the dual breakpoint system and responsive conventions |
| Accessibility regressions | Provides checklists for focus, contrast, touch targets, reduced motion |
| "It works but doesn't feel LUSENA" | Translates the brand personality into concrete CSS/HTML rules |

### Source of truth chain

1. **Brand rules:** `docs/LUSENA_BrandBook_v1.md` — colors, tone, photography, personality.
2. **Theme implementation guide:** **This document** — how brand rules are realized in code.
3. **Code:** The `lusena-*` prefixed files in `sections/`, `snippets/`, and `assets/`.

### Validated surfaces vs. repo leftovers

This document was built by deep-diving **only** these five surfaces:

| Surface | Template | Key section files |
|---|---|---|
| **Homepage** | `templates/index.json` | `lusena-hero`, `lusena-trust-bar`, `lusena-problem-solution`, `lusena-bestsellers`, `lusena-heritage`, `lusena-testimonials`, `lusena-bundles`, `lusena-faq` |
| **Page: /nasza-jakosc** | `templates/page.nasza-jakosc.json` | `lusena-quality-hero`, `lusena-quality-momme`, `lusena-quality-fire-test`, `lusena-quality-origin`, `lusena-quality-qc`, `lusena-quality-certificates`, `lusena-trust-bar` |
| **Page: /o-nas** | `templates/page.o-nas.json` | `lusena-about-hero`, `lusena-about-story`, `lusena-about-values` |
| **PDP** | `templates/product.json` | `lusena-main-product`, `lusena-pdp-feature-highlights`, `lusena-pdp-quality-evidence`, `lusena-pdp-details` |
| **Cart drawer** | `layout/theme.liquid` (global) | `snippets/cart-drawer.liquid` |

Patterns from **other** templates/sections (Dawn defaults, `lusena-page-returns`, `lusena-comparison`, `lusena-science`, etc.) are marked **"unvalidated / repo leftover"** and should not be treated as reference for new work.

---

## 2. Theme Architecture Overview (Dawn / OS 2.0)

### 2.1 Repository structure

```
lusena-dawn/
├── assets/          # Global CSS (base.css, lusena-shop.css), JS (global.js, cart-drawer.js, etc.)
├── config/          # settings_schema.json (theme editor schema), settings_data.json (current values)
├── layout/          # theme.liquid (main layout), password.liquid
├── locales/         # en.default.json, en.default.schema.json, pl.json, etc.
├── sections/        # lusena-*.liquid (custom), Dawn defaults (main-product, etc.)
├── snippets/        # lusena-*.liquid (custom), Dawn defaults (meta-tags, etc.)
├── templates/       # .json files mapping URLs to section compositions
└── docs/            # LUSENA_BrandBook_v1.md, THEME_CHANGES.md, this file
```

### 2.2 How the rendering pipeline works

```
layout/theme.liquid                      ← HTML shell, <head>, global CSS/JS
  ├── sections/header-group.json         ← header section group
  │     └── sections/lusena-header.liquid
  ├── {{ content_for_layout }}           ← page content injected here
  │     └── templates/{name}.json        ← maps URL to ordered section list
  │           └── sections/lusena-{X}.liquid
  │                 ├── snippets/lusena-{Y}.liquid   ← reusable fragments
  │                 └── {% stylesheet %} / {% javascript %}  ← scoped CSS/JS
  ├── sections/footer-group.json
  │     └── sections/lusena-footer.liquid
  └── snippets/cart-drawer.liquid        ← rendered globally when cart_type == 'drawer'
```

### 2.3 Naming convention

**All LUSENA-custom files use the `lusena-` prefix.** This clearly separates them from Dawn defaults.

| File type | Pattern | Example |
|---|---|---|
| Section | `sections/lusena-{name}.liquid` | `sections/lusena-hero.liquid` |
| Snippet | `snippets/lusena-{name}.liquid` | `snippets/lusena-icon.liquid` |
| PDP snippet | `snippets/lusena-pdp-{name}.liquid` | `snippets/lusena-pdp-atc.liquid` |
| Page template | `templates/page.{handle}.json` | `templates/page.nasza-jakosc.json` |
| CSS | `assets/lusena-{name}.css` | `assets/lusena-shop.css` |
| JS | `assets/lusena-{name}.js` | `assets/lusena-animations.js` |

### 2.4 Global assets loaded on every page

Defined in `layout/theme.liquid`:

| Asset | Purpose |
|---|---|
| `assets/base.css` | Dawn's base styles, CSS custom properties, typography scale, page-width |
| `assets/lusena-shop.css` | Tailwind-like utility classes (colors, spacing, responsive, typography) |
| `snippets/lusena-missing-utilities.liquid` | Additional utility classes not in main CSS file |
| `snippets/lusena-button-system.liquid` | Global button component styles |
| `assets/global.js` | Dawn web components, scroll behavior, section rendering |
| `assets/constants.js` | JS constants |
| `assets/pubsub.js` | PubSub event system for cart updates |
| `assets/lusena-animations.js` | LUSENA scroll-reveal IntersectionObserver (when animations enabled) |
| `assets/animations.js` | Dawn scroll-trigger animations (when animations enabled) |
| Google Fonts | Inter (body), Source Serif 4 (headings) — loaded via `<link>` |

### 2.5 Key global settings

From `config/settings_data.json`:

| Setting | Value | Purpose |
|---|---|---|
| `page_width` | `1300` (px) | Dawn's `--page-width` variable |
| `spacing_sections` | `36` (px) | Default spacing between Dawn sections |
| `cart_type` | `"drawer"` | Uses slide-out cart drawer |
| `buttons_radius` | `6` (px) | Global button corner radius |
| `variant_pills_radius` | `8` (px) | Variant selector pill corners |
| `type_header_font` | `source_serif_4_n4` | Heading font family |
| `type_body_font` | `inter_n4` | Body font family |
| `heading_scale` / `body_scale` | `100` / `100` | 1:1 scale (no multiplier) |
| `lusena_free_shipping_threshold` | `"269"` (zł) | Free shipping progress bar target |
| `lusena_primary_add_to_cart_label` | `"Dodaj do koszyka – wysyłka w 24 h"` | Primary ATC button text |

---

## 3. Design Tokens (As Implemented)

### 3.1 Color System

#### 3.1.1 Brand primitives (CSS custom properties)

Defined in `assets/lusena-shop.css` `:root`:

```css
--brand-bg:   #F7F5F2;   /* porcelain warm off-white */
--primary:    #111111;   /* near-black text */
--accent-cta: #0E5E5A;   /* deep teal — CTA & accents */
```

#### 3.1.2 Semantic Tailwind classes

| Class | RGB | Hex | Role |
|---|---|---|---|
| `.text-primary` / `.bg-primary` | `17 17 17` | `#111111` | Primary text, dark backgrounds |
| `.text-secondary` | `74 74 74` | `#4A4A4A` | Body copy, captions, muted text |
| `.text-accent-cta` / `.bg-accent-cta` | `14 94 90` | `#0E5E5A` | CTA fills, links, active states |
| `.text-accent-gold` / `.bg-accent-gold` | `140 106 60` | `#8C6A3C` | Badges, highlight accents |
| `.bg-brand-bg` | `247 245 242` | `#F7F5F2` | Primary page background |
| `.bg-surface-1` | `255 255 255` | `#FFFFFF` | White card/section backgrounds |
| `.bg-surface-2` | `240 238 235` | `#F0EEEB` | Slightly darker off-white backgrounds |
| `.text-neutral-400` | `185 183 180` | `#B9B7B4` | Disabled, placeholder text |
| `.text-neutral-700` | `90 88 85` | `#5A5855` | Muted labels |
| `.text-status-success` / `.bg-status-success` | `47 125 78` | `#2F7D4E` | In-stock indicators, success |

**Sources:** `assets/lusena-shop.css`, `snippets/lusena-missing-utilities.liquid`

#### 3.1.3 Color schemes (Shopify admin)

| Scheme | Background | Text | Button | Used for |
|---|---|---|---|---|
| scheme-1 | `#F7F5F2` | `#111111` | `#0E5E5A` | Primary (most pages) |
| scheme-2 | `#F0EEEB` | `#111111` | `#0E5E5A` | Card backgrounds |
| scheme-3 | `#2E2D2B` | `#FFFFFF` | `#0E5E5A` | Dark mode, sold-out badge |
| scheme-4 | `#111111` | `#FFFFFF` | `#0E5E5A` | Footer, darkest contexts |
| scheme-5 | `#8C6A3C` | `#FFFFFF` | `#FFFFFF` | Sale badges (gold) |

#### 3.1.4 Hardcoded section colors (validated)

| Hex | Context | File |
|---|---|---|
| `#2f7d4e` | Stock-available green dot | `snippets/lusena-pdp-styles.liquid` |
| `#b91c1c` | Stock-unavailable red dot | `snippets/lusena-pdp-styles.liquid` |
| `rgba(0,0,0,0.92)` | Lightbox overlay | `snippets/lusena-pdp-styles.liquid` |
| `rgb(14 94 90)` | Cart count badge bg | `sections/lusena-header.liquid` |

#### 3.1.5 Usage rules

- **CTA color is always `#0E5E5A`** — never change it between pages (brandbook rule).
- **Max 1–2 color accents per screen** — teal for CTA, optional gold for badges.
- **Backgrounds alternate** between `bg-brand-bg` / `bg-white` / `bg-surface-1` / `bg-surface-2` to visually separate section bands.
- **Status colors** — green `#2F7D4E` for success/in-stock, red `#B91C1C` for error/out-of-stock.
- **Contrast:** All key text/bg pairs meet WCAG AA (4.5:1 minimum). White on `#0E5E5A` passes AA for CTA text.

---

### 3.2 Typography System

#### 3.2.1 Font families

| Role | Font | CSS class | Source |
|---|---|---|---|
| Headings / brand | Source Serif 4, serif | `.font-serif` | Google Fonts link in `layout/theme.liquid` |
| Body / UI | Inter, sans-serif | `.font-sans` (default) | Google Fonts link in `layout/theme.liquid` |

#### 3.2.2 Size scale

The theme uses **two overlapping systems**: Dawn's heading scale (via `--font-heading-scale`) and LUSENA's Tailwind utility classes.

**LUSENA Tailwind scale** (validated sizes, `1rem = 10px` in Dawn):

| Class | Size | Line-height | Used where |
|---|---|---|---|
| `.text-[8px]` | 8px | — | Minor decorative UI |
| `.text-[10px]` | 10px | — | Cart count badge |
| `.text-[11px]` | 11px | 1.5 | Payment secure label |
| `.text-xs` | 12px | 16px | Proof chips, badges, captions |
| `.text-sm` | 14px | 20px | Trust bar, accordion body, prices |
| `.text-base` | 16px | 24px | Body text, FAQ summary, large buttons |
| `.text-lg` | 18px | 28px | PDP eyebrow, footer headings |
| `.text-xl` | 20px | 28px | Cart drawer title |
| `.text-2xl` | 24px | 32px | PDP title (mobile), section headings |
| `.text-3xl` | 30px | 36px | Section headings |
| `.text-4xl` | 36px | 40px | Large section headings, PDP title (desktop) |
| `.text-5xl` | 48px | 1 | Hero headline (mobile) |
| `.md:text-7xl` | 72px | 1 | Hero headline (tablet) |
| `.lg:text-8xl` | 96px | 1 | Hero headline (desktop) |

**Dawn heading scale** (from `assets/base.css`):

```css
h1, .h1 { font-size: calc(var(--font-heading-scale) * 3rem); }   /* 30px → 40px @750px */
h2, .h2 { font-size: calc(var(--font-heading-scale) * 2rem); }   /* 20px → 28px @750px */
h3, .h3 { font-size: calc(var(--font-heading-scale) * 1.7rem); }  /* 17px → 20px @750px */
```

> **Recommendation for new LUSENA sections:** Use the Tailwind utility classes (`.text-*`) rather than Dawn's heading scale. All five validated surfaces use Tailwind classes exclusively.

#### 3.2.3 Weights

| Class | Value | Usage |
|---|---|---|
| `.font-normal` (default) | 400 | Body text, headings |
| `.font-medium` | 500 | Buttons, FAQ summary, bold inline labels |
| `.font-semibold` | 600 | Links with icons, breadcrumb current page |

> The brandbook prescribes only 400 (regular) and 500 (medium). `font-semibold` is only used sparingly for breadcrumb current item and link-with-icon patterns.

#### 3.2.4 Letter spacing & text transform

| Token | Value | Use case |
|---|---|---|
| `.tracking-tight` | −0.025em | Large hero headlines |
| `.tracking-normal` | 0 | Body text (default) |
| `.tracking-wider` | 0.05em | Kicker labels, uppercase captions |
| `.tracking-widest` | 0.1em | Small uppercase labels |
| `.uppercase` | — | Kickers, option labels, badge text |

#### 3.2.5 Line-height

| Token | Value |
|---|---|
| `.leading-tight` | 1.25 |
| `.leading-snug` | 1.375 |
| default | 1.5 |
| `.leading-relaxed` | 1.625 |

**Brandbook rule:** Minimum 1.4× line-height for text blocks > 3 lines.

---

### 3.3 Spacing & Layout Scale

#### 3.3.1 Spacing scale

Based on a 4px (0.4rem) increment Tailwind grid:

```
4 → 6 → 8 → 12 → 16 → 20 → 24 → 32 → 48 → 64 → 96 → 128 px
```

Common gap classes: `.gap-1` (4px), `.gap-2` (8px), `.gap-3` (12px), `.gap-4` (16px), `.gap-6` (24px), `.gap-8` (32px), `.gap-12` (48px).

#### 3.3.2 Container padding

Defined in `assets/lusena-shop.css`:

```css
.container { padding: 0 2rem; }                /* mobile: 20px */
@media (min-width: 768px)  { padding: 0 3.2rem; }   /* 32px */
@media (min-width: 1024px) { padding: 0 6.4rem; }   /* 64px */
@media (min-width: 1280px) { padding: 0 9.6rem; }   /* 96px */
```

Container `max-width: 1440px` at the `2xl` breakpoint.

Dawn's `.page-width` (from `assets/base.css`): `max-width: var(--page-width)` (1300px), padding `0 1.5rem` → `0 5rem` at 750px.

> **Validated pattern:** LUSENA sections use `.container`, not `.page-width`. Use `.container` for new work.

#### 3.3.3 Section padding convention

Every standard LUSENA section exposes 4 schema range settings and applies them via CSS variables:

**Schema (in `{% schema %}`):**
```json
{
  "type": "range", "id": "padding_top",          "label": "Padding top (desktop)",
  "min": 0, "max": 240, "step": 4, "unit": "px", "default": 56
},
{
  "type": "range", "id": "padding_bottom",       "label": "Padding bottom (desktop)",
  "min": 0, "max": 240, "step": 4, "unit": "px", "default": 56
},
{
  "type": "range", "id": "padding_top_mobile",   "label": "Padding top (mobile)",
  "min": 0, "max": 240, "step": 4, "unit": "px", "default": 40
},
{
  "type": "range", "id": "padding_bottom_mobile", "label": "Padding bottom (mobile)",
  "min": 0, "max": 240, "step": 4, "unit": "px", "default": 40
}
```

**Inline style on `<section>`:**
```liquid
style="
  --lusena-section-padding-top-mobile: {{ section.settings.padding_top_mobile }}px;
  --lusena-section-padding-bottom-mobile: {{ section.settings.padding_bottom_mobile }}px;
  --lusena-section-padding-top-desktop: {{ section.settings.padding_top }}px;
  --lusena-section-padding-bottom-desktop: {{ section.settings.padding_bottom }}px;
"
```

**CSS consumption (in `{% stylesheet %}`):**
```css
.lusena-SECTION-NAME {
  padding-top: var(--lusena-section-padding-top-mobile);
  padding-bottom: var(--lusena-section-padding-bottom-mobile);
}
@media (min-width: 768px) {
  .lusena-SECTION-NAME {
    padding-top: var(--lusena-section-padding-top-desktop);
    padding-bottom: var(--lusena-section-padding-bottom-desktop);
  }
}
```

**Default values:**
- Standard sections: desktop 56px, mobile 40px
- Hero / landing sections: desktop 96px, mobile 64px
- PDP below-fold: hardcoded 96px desktop / 64px mobile (no schema settings)

#### 3.3.4 Content width narrowing

Sections use `.container` for outer constraint, then optionally narrow content with `max-w-*`:

| Class | Max width | When to use |
|---|---|---|
| `max-w-xl` | ~576px | Narrow centered text (hero overlay text) |
| `max-w-2xl` | ~672px | Centered prose (heritage, about-story) |
| `max-w-3xl` | ~768px | Centered body text, accordions (FAQ, PDP details) |
| `max-w-4xl` | ~896px | Medium-width content blocks |
| `max-w-5xl` | ~1024px | Wide 2-column grids (about-hero) |
| _(no narrowing)_ | container width | Full section grids (bestsellers, testimonials) |

---

### 3.4 Grid & Breakpoints

#### 3.4.1 Breakpoint system

The theme has **two coexisting breakpoint systems**:

| System | Breakpoints | Used in |
|---|---|---|
| **Dawn** | `749px` (max), `750px`, `990px` (min-width) | `assets/base.css`, Dawn sections |
| **LUSENA (Tailwind)** | `640px` (sm), `768px` (md), `1024px` (lg), `1280px` (xl), `1440px` (2xl) | `assets/lusena-shop.css`, all `lusena-*` sections |

> **For new sections:** Use the Tailwind breakpoints (`md:`, `lg:`, `xl:`). The `768px` breakpoint is the primary mobile→desktop switch in LUSENA sections.

#### 3.4.2 Common grid patterns (validated)

| Pattern | Classes | Used in |
|---|---|---|
| 2-column equal | `grid grid-cols-1 md:grid-cols-2 gap-12 items-center` | bundles, quality-momme, about-hero |
| 2-column wide gap | `grid grid-cols-1 md:grid-cols-2 gap-24` | problem-solution |
| 3-column cards | `grid grid-cols-1 md:grid-cols-3 gap-8` | testimonials |
| 4-column cards | `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8` | about-values |
| Product grid | `grid grid-cols-2 lg:grid-cols-3 gap-x-4 gap-y-12` | bestsellers |
| PDP above-fold | `grid grid-cols-1 md:grid-cols-12 gap-8 lg:gap-16` (7+5 cols) | main-product |
| Stacked / narrow | `max-w-3xl mx-auto` (no grid) | heritage, quality-hero, FAQ, PDP details |

**Brandbook grid:** Desktop 12-col (24px gutter), tablet 8-col (20px), mobile 4-col (16px).

---

### 3.5 Radius, Borders, Shadows

#### 3.5.1 Border radius tokens

| Token / value | Purpose | Files |
|---|---|---|
| `rounded-brand` (0.6rem / 6px) | **Brand standard** — buttons, inputs, cart items | `snippets/lusena-missing-utilities.liquid` |
| `rounded-sm` (0.2rem / 2px) | Subtle rounding — payment badges, media thumbnails | `assets/lusena-shop.css` |
| `rounded-full` (9999px) | Circles — icon buttons, color swatches, dots, cart badge | `assets/lusena-shop.css` |
| `0` | Sharp — media containers, product cards | `config/settings_data.json` |

> **Theme setting:** `buttons_radius: 6`, `variant_pills_radius: 8`, `inputs_radius: 6`, `card_corner_radius: 0`, `media_radius: 0`.

#### 3.5.2 Border patterns

| Pattern | Value | Context |
|---|---|---|
| Section dividers | `1px solid rgba(74,74,74, 0.1)` | Between buybox areas |
| Proof chips/pills | `1px solid rgba(74,74,74, 0.15)` | Subtle chip outlines |
| Hover accent | `border-color: rgba(14,94,90, 0.3)` | Chip/pill hover state |
| Sticky ATC divider | `1px solid rgba(74,74,74, 0.15)` | Top border of sticky bar |
| Cart badge | `2px solid rgb(255 255 255)` | White ring around teal badge |
| Swatch selected | `box-shadow: 0 0 0 2px #fff, 0 0 0 4px var(--accent-cta)` | Double-ring selection indicator |

#### 3.5.3 Shadows

| Token | Value | When to use |
|---|---|---|
| `.shadow-sm` | `0 1px 2px 0 rgb(0 0 0 / .05)` | Proof chips, swatch swatches |
| `.shadow-xl` | `0 20px 25px -5px rgb(0 0 0 / .1), 0 8px 10px -6px rgb(0 0 0 / .1)` | (available but rarely used on validated surfaces) |
| `.shadow-2xl` | `0 25px 50px -12px rgb(0 0 0 / .25)` | Cart drawer panel |
| Focus ring | `0 0 0 2px rgb(14 94 90), 0 0 0 4px rgb(255 255 255)` | `:focus-visible` on buttons/links |
| Sticky ATC top | `0 -4px 6px -1px rgba(0,0,0,.05)` | Top shadow on sticky bar |

> **Brandbook alignment:** "Shadows sparingly." The theme respects this — most `shadow_opacity` settings are `0` in `config/settings_data.json`.

---

### 3.6 Motion & Interaction

#### 3.6.1 Duration tokens

Defined in `assets/base.css` `:root`:

```css
--duration-short:      150ms;
--duration-default:    200ms;
--duration-medium:     300ms;
--duration-long:       500ms;
--duration-extra-long: 600ms;
--ease-out-slow:       cubic-bezier(0, 0, 0.3, 1);
```

LUSENA custom (also in `assets/base.css` `:root`):

```css
--lusena-motion-duration: 420ms;
--lusena-motion-ease:     cubic-bezier(0.2, 0, 0, 1);
--lusena-motion-distance: 14px;
```

#### 3.6.2 Scroll-reveal animations

**LUSENA system** (`assets/lusena-animations.js`, `assets/base.css`):
- Classes: `.lusena-animate-fade-up`, `.lusena-animate-scale-in`
- Start state: `opacity: 0; transform: translateY(14px)` — transitions to `opacity: 1; transform: none`
- Stagger: `[data-lusena-stagger]` on container — children get `--lusena-delay` (70ms per child)
- IntersectionObserver threshold: `rootMargin: 0px 0px -12% 0px`

**Dawn system** (`assets/animations.js`, `assets/base.css`):
- Classes: `.scroll-trigger` + `.animate--slide-in` (or `.animate--fade-in`)
- Gated by `settings.animations_reveal_on_scroll`
- Stagger: `data-cascade` on container

Both systems coexist. LUSENA sections use both — typically Dawn's `scroll-trigger` for block-level reveals and LUSENA's custom system for finer effects.

**Gating pattern (required in all sections):**
```liquid
{% if settings.animations_reveal_on_scroll %}
  scroll-trigger animate--slide-in
{% endif %}
```

#### 3.6.3 Transition conventions

| Context | Properties | Duration | Easing |
|---|---|---|---|
| Button hover/focus | color, background, border, opacity | 150ms | ease |
| Accordion open/close | height | 200ms | ease-out |
| Cart drawer slide | transform | 280ms | cubic-bezier(0.22, 1, 0.36, 1) |
| Header auto-hide | transform | 220ms | ease |
| Mobile menu | grid-template-rows, opacity | 260ms | cubic-bezier(0.2, 0.9, 0.2, 1) |
| Image hover scale | transform | 300ms | ease-in-out |
| Proof chip hover | border-color, color | 150ms | ease |
| Gallery dots | background-color | 200ms | ease |
| Hero image entry | scale 1.04→1 | 900ms | ease-out-slow |
| Hero text entry | translateY + opacity | 650ms | ease-out-slow (120ms/220ms delay) |

**Brandbook alignment:**
- UI hover/focus: 150–200ms ✓
- Modals/hero: 250–400ms ✓
- Easing: calm ease-in-out, no springy/bouncy ✓
- `prefers-reduced-motion`: All animations respect it ✓

#### 3.6.4 Hover states (validated)

| Element | Hover effect |
|---|---|
| `.lusena-btn--primary` | `background: rgb(14 94 90 / 0.9)` — slight fade (≈10% lighten) |
| `.lusena-btn--outline` | `background: rgb(14 94 90 / 0.05)` — teal tint 5% |
| `.lusena-btn--ghost` | `background: rgb(240 238 235)` — surface-2 fill |
| Icon buttons | Ghost: `bg: #F0EEEB`; Overlay: `opacity → 1`; Subtle: `bg: 10% gray` |
| Product card image | `transform: scale(1.05)` (with pointer:fine media query) |
| Links | `text-decoration: underline` on `.hover\:underline` |
| FAQ summary | `color: var(--accent-cta)` |

#### 3.6.5 Reduced motion

All LUSENA code includes `@media (prefers-reduced-motion: reduce)` blocks:
- CSS transitions → `0.15s` or `none`
- CSS animations → `none` or reduced to simple opacity fade
- JS (`lusena-animations.js`): Early return, no IntersectionObserver setup
- Hero: Image starts at final state (no scale), text visible immediately

---

## 4. Core UI Components & Patterns (As Implemented)

### 4.1 Buttons & Links

**File:** `snippets/lusena-button-system.liquid` (global — loaded on every page via `layout/theme.liquid`)

#### Button variants

| Variant | Class | Visual | Usage |
|---|---|---|---|
| **Primary** | `.lusena-btn--primary` | Teal fill, white text | Main CTA (Add to cart, Checkout) |
| **Outline** | `.lusena-btn--outline` | Teal border, transparent bg | Secondary CTA (Buy now) |
| **Ghost** | `.lusena-btn--ghost` | No border/bg, dark text | Tertiary actions |
| **Link** | `.lusena-btn--link` | Underlined dark text | Inline text links as buttons |
| **Text** | `.lusena-btn--text` | No padding/height, teal | Minimal inline actions |
| **Text-secondary** | `.lusena-btn--text-secondary` | Gray, underlined | Dismiss / "Continue shopping" |

#### Button sizes

| Size | Class | Height | Padding | Font |
|---|---|---|---|---|
| XS | `.lusena-btn--size-xs` | 3.2rem | 1.4rem | 1.2rem |
| SM | `.lusena-btn--size-sm` | 4.4rem | 1.6rem | 1.2rem |
| Default | `.lusena-btn--size-default` | 4.8rem | 3.2rem | 1.4rem |
| PDP | `.lusena-btn--size-pdp` | 4.8rem | 4rem | — |
| LG | `.lusena-btn--size-lg` | 5.6rem | 4rem | 1.6rem |
| Icon | `.lusena-btn--size-icon` | 4.4rem square | 0 | — |

#### Button states

- **Disabled:** Gray bg (`#B9B7B4`), no pointer events.
- **Loading:** Content hidden, centered dot-wave or shimmer animation, cursor `wait`.
- **Focus-visible:** `box-shadow: 0 0 0 2px rgb(14 94 90), 0 0 0 4px rgb(255 255 255)`.

#### Icon buttons

| Variant | Class | Usage |
|---|---|---|
| Ghost | `.lusena-icon-button--ghost` | Header icons, mobile actions |
| Overlay | `.lusena-icon-button--overlay` | Gallery lightbox controls (white on dark) |
| Subtle | `.lusena-icon-button--subtle` | Cart drawer close, quantity controls |
| Sizes | `--md` (4.4rem / 44px min), `--sm` (3.6rem / 36px min) | |

**Full-width modifier:** `.lusena-btn--full-width` → `width: 100%`.

#### Usage rules

- **Max 2 CTAs per section:** 1 primary + 1 secondary (brandbook rule).
- **CTA stacking:** On mobile, full-width stacked. Never 3+ side-by-side.
- **Loading state:** Must be implemented on all form-submit buttons (min 500ms visible duration).
- **Touch targets:** All buttons meet 44×44px minimum.

---

### 4.2 Forms & Inputs

#### Variant picker (`snippets/lusena-pdp-variant-picker.liquid`)

**Color swatches:**
- `.lusena-option__swatch` — 4.4rem circle, `rounded-full`, background from swatch color.
- Selected: Double-ring via `box-shadow: 0 0 0 2px #fff, 0 0 0 4px var(--accent-cta)`.
- Unavailable: `opacity-40`, `cursor-not-allowed`, input `disabled`.

**Size/option pills:**
- `.lusena-option__pill` — Rectangle, `px-6 py-2`, `border border-secondary/30`, `min-w-[6.4rem]`.
- Selected: Highlighted border. Hover: `border-accent-cta`.

**Accessibility:**
- `<fieldset>` + `<legend>` grouping per option.
- Hidden `<input type="radio">` (`.visually-hidden`) → native keyboard/screen reader support.
- `.visually-hidden` text label on each swatch.

#### Quantity stepper (in `snippets/cart-drawer.liquid`)

```html
<div class="flex items-center border border-secondary/20 rounded-brand">
  <button class="lusena-icon-button lusena-icon-button--subtle lusena-icon-button--sm">−</button>
  <span data-cart-qty>1</span>
  <button class="lusena-icon-button lusena-icon-button--subtle lusena-icon-button--sm">+</button>
</div>
```

Minus button disabled when `qty <= 1`. Both buttons have `aria-label` in Polish.

#### Newsletter input (`sections/lusena-footer.liquid`)

Minimal style: `bg-transparent border-b border-gray-700` with `focus:outline-none focus:border-white`. Submit button is `sr-only`.

---

### 4.3 Cards (Product / Collection / Content)

#### Product card (`snippets/lusena-product-card.liquid`)

**Structure:** Entire card is a single `<a>` link for accessibility.

```html
<a class="lusena-product-card block cursor-pointer">
  <div class="relative aspect-[4/5] bg-surface-2 overflow-hidden mb-4">
    <span class="absolute top-2 left-2 z-10 … uppercase">Badge</span>
    <img class="lusena-product-card__image--primary …" loading="lazy"/>
    <img class="lusena-product-card__image--secondary opacity-0 …"/>
  </div>
  <div class="space-y-1 text-center md:text-left">
    <h3 class="text-sm font-medium text-primary">Title</h3>
    <div>
      <span class="text-secondary">Price</span>
      <span class="text-secondary/50 line-through text-xs">Compare-at</span>
    </div>
  </div>
</a>
```

**Key details:**
- Image ratio: `aspect-[4/5]` (4:5, matching brandbook PLP spec).
- Badge: Auto-detected from product tags (`bestseller`, `new`), or explicit param. Styled `bg-white/90 backdrop-blur-sm`.
- Hover image: Secondary image crossfades in on hover (gated by `pointer: fine` media query).
- Responsive images: `widths: '360, 540, 720, 900, 1080, 1200'`.
- Used in: `sections/lusena-bestsellers.liquid`, `snippets/lusena-pdp-cross-sell.liquid`.

#### Content cards

No standalone content-card snippet exists. Sections like `lusena-testimonials`, `lusena-about-values` render cards inline with consistent patterns:
- `bg-neutral-50` or `bg-white` card background
- `p-6` to `p-8` padding
- Consistent text hierarchy: small kicker → heading → body

---

### 4.4 Navigation (Header / Menus / Footer)

#### Header (`sections/lusena-header.liquid`)

**Structure:** Fixed, transparent-blurred bar at top.

```
<header class="fixed top-0 left-0 right-0 z-50 bg-brand-bg/95 backdrop-blur-sm py-4">
  [mobile menu toggle] [logo] [desktop nav] [icon actions: search, account, cart]
</header>
```

**Key behaviors:**
- **Auto-hide on scroll (mobile):** Scrolling down > 8px delta hides header (`translateY(-110%)`); scrolling up shows it. Controlled by `data-lusena-auto-hide-on-scroll-mobile`.
- **Mobile menu:** Native `<details>/<summary>` with animated CSS grid expansion (`0fr → 1fr`, 260ms). Panel has `inert` attribute toggled for accessibility.
- **Cart count badge:** Absolute-positioned teal circle with white text, 2px white border ring.
- **CSS variable sync:** `--lusena-header-height` and `--header-height` set via ResizeObserver on `:root`.

**Accessibility:**
- All icon actions have `aria-label`.
- Mobile menu: `aria-controls`, `aria-hidden`, `inert` toggling.
- Focus-visible inherited from button system.

#### Breadcrumbs (`snippets/lusena-breadcrumbs.liquid`)

```html
<nav aria-label="Breadcrumb" class="py-4">
  <ol class="flex items-center gap-1.5 text-xs text-neutral-700">
    <li><a href="/">Strona główna</a> <chevron-right/></li>
    <li><a href="/collections/jedwab">Collection</a> <chevron-right/></li>
    <li class="text-primary font-semibold truncate max-w-[200px]">Product Title</li>
  </ol>
</nav>
```

Used on: PDP only. Semantic `<ol>`, current page has no link.

#### Footer (`sections/lusena-footer.liquid`)

Dark background (`bg-primary text-white`), 4-column grid (`md:grid-cols-4`):
1. Brand logo + description
2. Shop links (`link_list` setting)
3. Help links (`link_list` setting)
4. Newsletter

Copyright bar: `border-t border-gray-800`, centered, `text-xs text-gray-500`.

---

### 4.5 Product Page Patterns (PDP)

**Template:** `templates/product.json`
**Main section:** `sections/lusena-main-product.liquid`

#### Above-fold layout

```
┌─────────────────────────────────────────────────────────┐
│  Breadcrumbs (full width)                                │
├──────────────────────┬──────────────────────────────────┤
│  Media Gallery       │  Buybox                          │
│  (7 cols)            │  (5 cols)                        │
│  ┌──────┬──────────┐ │  ┌─ Summary (title, price)      │
│  │ Thumb│ Main     │ │  ├─ Proof Chips (5 badges)      │
│  │ strip│ stage    │ │  ├─ Variant Picker               │
│  │      │          │ │  ├─ ATC Button + Buy Now        │
│  │      │ (zoom)   │ │  ├─ Guarantee Box               │
│  │      │          │ │  ├─ Payment Badges               │
│  └──────┴──────────┘ │  ├─ Buybox Accordion (Specs/Care)│
│                      │  └─ Cross-sell                   │
└──────────────────────┴──────────────────────────────────┘
```

Mobile: Stacked vertically — horizontal scroll gallery with dots, then buybox.

#### Below-fold sections

| Section | File | Content |
|---|---|---|
| Feature Highlights | `sections/lusena-pdp-feature-highlights.liquid` | 3–6 icon cards (responsive 1→2→3 col grid) |
| Quality Evidence | `sections/lusena-pdp-quality-evidence.liquid` | Expandable accordion cards with icon, title, detail |
| Details & Questions | `sections/lusena-pdp-details.liquid` | FAQ-style accordion, centered narrow width |

#### Key PDP snippets

| Snippet | Purpose |
|---|---|
| `lusena-pdp-media` | Gallery: thumbnails + main stage (desktop), horizontal scroll (mobile), lightbox with zoom/pinch |
| `lusena-pdp-summary` | Title (serif), price (with compare-at line-through), eyebrow text |
| `lusena-pdp-proof-chips` | 5 trust badges: OEKO-TEX, 22 momme, 24h shipping, 60-day returns, gifting |
| `lusena-pdp-variant-picker` | Color swatches + size pills with `<fieldset>` a11y |
| `lusena-pdp-atc` | Primary CTA + Buy Now + stock indicator |
| `lusena-pdp-guarantee` | Shield icon guarantee line with "learn more" link |
| `lusena-pdp-payment` | Payment method badges with lock icon |
| `lusena-pdp-buybox-panels` | Accordion with Specs (metafield-driven table) and Care (bullet list) |
| `lusena-pdp-cross-sell` | Recommended product cards grid |
| `lusena-pdp-sticky-atc` | Fixed bottom bar on scroll (product title + price + ATC button) |
| `lusena-pdp-styles` | All PDP CSS (inline `{% stylesheet %}`) |
| `lusena-pdp-scripts` | All PDP JS (inline `{% javascript %}` — ~1835 lines) |

#### Sticky ATC bar (`snippets/lusena-pdp-sticky-atc.liquid`)

Appears when main ATC scrolls out of view. Fixed to bottom, `max-width: 1280px`, top shadow. Contains product image thumbnail, title, price, and "Add to cart" button. Hides via `transform: translateY(110%)`.

---

### 4.6 Collection / List Patterns (PLP)

> **Status: NOT VALIDATED.** `sections/lusena-main-collection.liquid` exists but is not one of the five source-of-truth surfaces. Treat its patterns as unverified.

The product card component (`snippets/lusena-product-card.liquid`) is validated. Use it with grid patterns from section 3.4.2 for any collection layout.

---

### 4.7 Cart Patterns

**File:** `snippets/cart-drawer.liquid`

#### Drawer structure

| Zone | Content |
|---|---|
| **Header** | "Twój koszyk" (serif heading) + close button |
| **Empty state** | Shopping bag icon, "Twój koszyk jest pusty", browse CTA, close button |
| **Line items** | Scrollable area with product thumbnails, titles, variant options, quantity steppers, remove buttons |
| **Upsell zone** | "Pasuje do" label, product card with "Dodaj" outline button, success toast |
| **Footer** | Subtotal, free shipping progress bar (teal fill → green when qualified), checkout CTA (primary, full-width, LG), 60-day return trust line, "Kontynuuj zakupy" link |

#### Shipping progress bar

```html
<div class="lusena-cart-drawer__shipping-track">  <!-- 0.6rem h, gray bg, rounded pill -->
  <span class="lusena-cart-drawer__shipping-fill" style="width: N%"></span>
</div>
```

- Fill color: Teal → green (`rgb(47 125 78)`) via `--qualified` modifier when threshold met.
- Width transition: 500ms.
- Threshold: configurable via `lusena_free_shipping_threshold` setting (default: 269 zł).

#### JS behavior

- `<cart-drawer>` web component extending `HTMLElement`.
- Quantity changes via Fetch to `routes.cart_change_url`.
- Section rendering: Uses `getSectionsToRender()` for AJAX partial updates.
- Upsell: `product-form` web component, pending variant tracked in `sessionStorage`, 2.2s success toast.
- Focus trap: `role="dialog"`, `aria-modal="true"`, `tabindex="-1"`.

#### Accessibility

- `role="dialog"`, `aria-modal="true"`, `tabindex="-1"` on drawer.
- `aria-live="polite"` on upsell zone and success toast.
- All quantity buttons have `aria-label` (Polish).
- Overlay click closes drawer.

---

### 4.8 Drawers / Modals / Accordions

#### Accordion patterns (two implementations)

| Type | File | Mechanism | Used on |
|---|---|---|---|
| **FAQ accordion** | `sections/lusena-faq.liquid` | Native `<details>/<summary>` + JS animated height | Homepage |
| **Buybox accordion** | `snippets/lusena-pdp-buybox-panels.liquid` | `data-lusena-accordion-*` attributes + JS | PDP |

**FAQ accordion:**
- Native `<details>` elements — accessible by default (keyboard + screen reader).
- JS adds animated height transitions: `height: 0` → `scrollHeight` on open, reverse on close.
- Chevron rotation: `transform: rotate(180deg)` on `details[open]`.
- Only one item open at a time (accordion mode).
- 200ms ease-out.

**Buybox accordion:**
- Custom `data-lusena-accordion-*` data-attribute system.
- `data-lusena-accordion-single`: Only one panel open at a time.
- `data-lusena-accordion-collapsible`: All panels can be closed.
- `aria-expanded` toggled on trigger buttons.
- Contains inline term definitions (`data-lusena-spec-def-toggle`) that expand rows within the specs table.

#### Cart drawer

See section 4.7. Slide-in from right, 280ms cubic-bezier easing, backdrop overlay with blur.

#### Mobile menu drawer

See section 4.4. CSS grid `0fr → 1fr` expansion, `inert` toggling.

#### PDP lightbox (in `snippets/lusena-pdp-media.liquid`)

- Full-screen overlay (`rgba(0,0,0,0.92)`).
- Zoom + pinch support.
- Keyboard navigation (arrow keys, Escape to close).
- Close button (icon-button overlay variant).

---

### 4.9 Media (Images / Video) Rules

#### Image loading strategy

| Context | `loading` | `fetchpriority` | `widths` |
|---|---|---|---|
| Hero image | `eager` | `high` | Up to `3000` |
| Everything else | `lazy` | — | Varies (see below) |

#### Responsive image pattern

```liquid
{{ image
  | image_url: width: 1400
  | image_tag:
    class: 'w-full h-full object-cover',
    loading: 'lazy',
    widths: '600, 900, 1200, 1400',
    sizes: '(min-width: 768px) 45vw, 90vw'
}}
```

**Width sets by context:**

| Context | `widths` | `sizes` |
|---|---|---|
| 2-column content | `'600, 900, 1200, 1400'` | `'(min-width: 768px) 45vw, 90vw'` |
| Full-bleed hero | Up to `'1920, 2400, 3000'` | `'100vw'` |
| Product card (grid) | `'360, 540, 720, 900, 1080, 1200'` | Responsive based on columns |
| PDP gallery main | `'600, 800, 1000, 1200'` | `'(min-width: 768px) 50vw, 100vw'` |
| PDP thumbnails | `'120, 180, 240, 300'` | `'72px'` |

**All images use `object-cover`** for consistent cropping.

#### Image ratios (brandbook-aligned)

| Context | Ratio |
|---|---|
| Product cards / PLP | `aspect-[4/5]` (4:5) |
| PDP main gallery | 1:1 (implicit via container) |
| Details/lifestyle | 3:2 |
| Hero (desktop) | 16:9 (via viewport height) |
| Hero (mobile) | 4:5 (via `<source>` art direction) |

#### Hero image art direction

Uses `<picture>` with `<source>` for desktop/mobile breakpoints, allowing different crops per device.

#### Weight budgets (brandbook)

| Context | Max size |
|---|---|
| Hero (desktop) | 250–300 KB (WebP/AVIF) |
| Hero (mobile) | 150–200 KB |
| PLP card | 120–160 KB |
| PDP gallery (first 2–3 frames) | 180–220 KB each |

---

### 4.10 Rich Text / Content Sections

#### Validated content section types

| Pattern | Section | Layout |
|---|---|---|
| **Full-bleed hero** | `lusena-hero` | Viewport-height, overlay text on image, animated entry |
| **Centered text column** | `lusena-heritage`, `lusena-quality-hero` | Narrow `max-w-2xl`–`max-w-4xl`, centered, serif heading + body text |
| **2-column image + text** | `lusena-bundles`, `lusena-quality-momme`, `lusena-about-hero` | `grid-cols-2` on desktop, stacked on mobile, image side configurable |
| **Problem/solution split** | `lusena-problem-solution` | 2-column with distinct block types per column |
| **Card grid** | `lusena-testimonials` (3-col), `lusena-about-values` (4-col) | Block-based cards with consistent spacing |
| **Trust bar** | `lusena-trust-bar` | Horizontal icon + text chips |
| **FAQ** | `lusena-faq` | Centered narrow column, accordion items |

#### Common content hierarchy within sections

```
┌─ Kicker (small uppercase .tracking-wider .text-secondary, optional)
├─ Heading (.font-serif, size varies by section importance)
├─ Subheading or body (.text-secondary, 1–3 sentences)
└─ CTA (lusena-btn, optional)
```

#### Background alternation pattern (homepage example)

```
Hero         → image background (dark overlay)
Trust bar    → bg-brand-bg
Problem/Sol  → bg-brand-bg
Bestsellers  → bg-surface-1
Heritage     → bg-brand-bg
Testimonials → bg-surface-1
Bundles      → bg-surface-2
FAQ          → bg-surface-1
```

This creates a subtle visual rhythm that separates sections without hard borders.

---

## 5. Page-Level Composition Rules

### 5.1 Section ordering conventions

| Surface | Order pattern |
|---|---|
| **Homepage** | Hero → Trust → Problem/Solution → Products → Story → Social proof → Gift/Bundle → FAQ |
| **Quality page** | Hero → Detail evidence (multiple sections) → Trust bar |
| **About page** | Hero → Story → Values |
| **PDP** | Main (gallery + buybox) → Feature highlights → Quality evidence → Details/FAQ |

**Common pattern:** Start with hero/hook → evidence/proof → social proof → CTA.

This matches the brandbook's message hierarchy:
1. Short benefit + parameter
2. Proof/concrete
3. CTA with operational promise
4. Reassurance (delivery/returns)

### 5.2 Default spacing between sections

- Sections handle their own top/bottom padding via the 4 CSS variables (section 3.3.3).
- Dawn's `spacing_sections: 36px` applies to Dawn sections but LUSENA sections override with their own padding.
- **Typical defaults:** 56px desktop / 40px mobile between content sections.
- **Hero sections:** 96px desktop / 64px mobile.
- Sections alternate backgrounds instead of using separators.

### 5.3 Content density rules

- **Max 70–80 characters per line** (desktop), **38–45** (mobile) — enforced by `max-w-*` constraints.
- **Max 2 CTAs per visible screen area.**
- **Min 24px white space** between content blocks within a section.
- **Product grids:** 2 columns mobile, 3 columns desktop (PDP cross-sell / bestsellers).
- **Card grids:** 1→2→3 or 1→2→4 columns depending on card complexity.

### 5.4 CTA placement conventions

- **Hero:** Central, below headline and subheading.
- **Content sections:** Below body text, either centered or left-aligned depending on layout.
- **PDP above-fold:** Sticky within the buybox column. Secondary "Buy now" below primary ATC.
- **PDP below-fold sections:** At the bottom of each evidence section, linking to ATC or relevant page.
- **Cart drawer footer:** Full-width checkout CTA, always visible.

---

## 6. Copy & Microcopy Conventions

### 6.1 Tone of voice

From the brandbook: **Expert, calm, empathetic, precise.**

| Rule | Example |
|---|---|
| Speak plainly about specifics | "22 momme, kontrola jakości każdej partii" not "Najwyższa jakość!" |
| Max 18–22 words per sentence | Keep short for scanning |
| Fewer adjectives, more proof | Pair claims with data: "precyzyjne szwy – odstęp ~3 mm" |
| Calm, don't rush | "Wysyłamy w 24 h" not "Kup teraz, bo zniknie!" |
| No exclamation marks in headings | Period or no punctuation |

### 6.2 CTA labels (validated examples)

| Context | Current label (PL) | Principle |
|---|---|---|
| PDP primary | "Dodaj do koszyka – wysyłka w 24 h" | Benefit + operational promise |
| PDP secondary | "Kup teraz i zapłać" | Direct action |
| Cart checkout | "Przejdź do kasy" | Clear next step |
| Cart upsell | "Dodaj" | Minimal, no pressure |
| Empty cart | "Przeglądaj produkty" | Exploratory, not pushy |
| Empty cart dismiss | "Zamknij" | Simple action |

### 6.3 Microcopy patterns

| Context | Pattern |
|---|---|
| Stock available | "W magazynie – gotowe do wysyłki" |
| Stock unavailable | "Chwilowo niedostępne" |
| Guarantee | "60 Dni Gwarancji Przespanych Nocy" |
| Shipping progress | "Darmowa dostawa za X zł" / "Darmowa dostawa! ✓" |
| Cart upsell success | "✓ Dodano do koszyka" |
| Proof chips | "OEKO-TEX® 100", "22 momme", "Wysyłka 24h z PL", "60 dni na zwrot", "Na prezent" |

### 6.4 PL localization rules (from brandbook)

| Rule | Format |
|---|---|
| Currency | "1 249,00 zł" (full) or "249 zł" (short) |
| Dates | DD.MM.RRRR |
| Decimal separator | Comma ("22,0 momme") |
| Numbers always in digits | "22 momme" not "dwadzieścia dwa" |
| Forbidden anglicisms | "premium look" → "eleganckie wykończenie" |

### 6.5 Hardcoded text (by design)

> LUSENA targets the Polish market only. All sections use hardcoded Polish text directly in Liquid files rather than `{{ 'key' | t }}` translation filters. **This is intentional** — there is no multi-language requirement. New sections should follow the same pattern: write Polish copy directly in the template.

---

## 7. Do/Don't Checklist

### Do

- [ ] **Name files** with `lusena-` prefix: `sections/lusena-{name}.liquid`, `snippets/lusena-{name}.liquid`.
- [ ] **Use `.container`** (not `.page-width`) for horizontal content constraint.
- [ ] **Use Tailwind breakpoints** (`md:`, `lg:`, `xl:`) for responsive — not Dawn's 750/990px.
- [ ] **Use semantic color classes** (`.text-primary`, `.bg-accent-cta`) — not hardcoded hex in HTML.
- [ ] **Use `.lusena-btn--{variant}`** for all buttons — never create ad-hoc button styles.
- [ ] **Use `{% render 'lusena-icon', name: '…' %}`** for all icons — never paste raw SVG.
- [ ] **Include 4 padding schema settings** (top/bottom × desktop/mobile) in every section.
- [ ] **Gate animations** with `{% if settings.animations_reveal_on_scroll %}`.
- [ ] **Respect `prefers-reduced-motion`** in all custom CSS/JS.
- [ ] **Use `font-serif`** (Source Serif 4) for headings, `font-sans` (Inter) for body/UI.
- [ ] **Use `rounded-brand`** (6px) for buttons and inputs, `rounded-full` for circles.
- [ ] **Keep touch targets ≥ 44×44px** on all interactive elements.
- [ ] **Use `data-lusena-*`** namespace for JS hooks — never couple JS to CSS classes.
- [ ] **Write CSS in `{% stylesheet %}`** tag (inline) — not in separate `.css` asset files.
- [ ] **Write JS in `{% javascript %}`** tag or via `<script>` + asset_url — not inline `<script>` in HTML.
- [ ] **Alternate section backgrounds** (brand-bg / white / surface-1 / surface-2) for visual rhythm.
- [ ] **Add `loading="lazy"`** to all images except hero (which gets `loading="eager"` + `fetchpriority="high"`).
- [ ] **Use `{{ block.shopify_attributes }}`** on all block-rendered elements for theme editor highlighting.
- [ ] **Use Tailwind breakpoints** (`md: 768px`, `lg: 1024px`) — not Dawn's 750/990px — for all responsive switches in new sections.
- [ ] **Hardcode Polish text** directly in templates — no `{{ 'key' | t }}` needed (PL-only market).

### Don't

- [ ] Don't hardcode hex colors in HTML `style` attributes — use CSS variables or Tailwind classes.
- [ ] Don't introduce new font sizes outside the existing scale (section 3.2.2).
- [ ] Don't add more than 2 font weights to any single block.
- [ ] Don't use Dawn's `.button` class — use `.lusena-btn--{variant}` instead.
- [ ] Don't use `.page-width` — use `.container` for LUSENA sections.
- [ ] Don't create icon fonts or reference icons by URL — use the `lusena-icon` snippet.
- [ ] Don't add shadows beyond `shadow-sm` unless specifically needed — the brandbook says "shadows sparingly."
- [ ] Don't use springy/bouncy/flashy animations — keep motion calm (ease, ease-out, ease-in-out).
- [ ] Don't exceed 80 characters per line width (use `max-w-*` to constrain).
- [ ] Don't place 3+ CTAs side-by-side.
- [ ] Don't mix 3+ image aspect ratios in a single view.
- [ ] Don't use `all-caps` for anything longer than 2–3 words.
- [ ] Don't skip `aria-label` on icon-only buttons.
- [ ] Don't use color schemes 3 or 4 (dark backgrounds) in LUSENA sections — no dark mode by brand decision.
- [ ] Don't use Dawn breakpoints (750/990px) in new LUSENA sections — use Tailwind (768/1024px) unless syncing with Dawn layout classes.

---

## 8. "How To" Recipes

### 8.1 How to Add a New Page Template

**Example:** Creating a `/kontakt` (contact) page.

**Step 1:** Create the template JSON.
```
templates/page.kontakt.json
```

```json
{
  "sections": {
    "contact_hero": {
      "type": "lusena-contact-hero",
      "settings": {
        "heading": "Skontaktuj się z nami",
        "subheading": "Odpowiadamy w ciągu 24 godzin."
      }
    },
    "contact_form": {
      "type": "lusena-contact-form",
      "settings": {}
    },
    "trust": {
      "type": "lusena-trust-bar",
      "settings": {}
    }
  },
  "order": ["contact_hero", "contact_form", "trust"]
}
```

**Step 2:** Create sections (if needed), reusing existing ones where possible.

```
sections/lusena-contact-hero.liquid
sections/lusena-contact-form.liquid
```

**Step 3:** In Shopify admin, assign the template to the page:
- Online Store → Pages → Kontakt → Template: `page.kontakt`

**Step 4:** Reuse existing sections when possible — `lusena-trust-bar`, `lusena-faq` can be added to any page template.

---

### 8.2 How to Add a New Section Consistently

**Step 1:** Create the file: `sections/lusena-{name}.liquid`

**Step 2:** Follow this canonical structure:

```liquid
<section
  class="bg-brand-bg lusena-{name}"
  style="
    --lusena-section-padding-top-mobile: {{ section.settings.padding_top_mobile }}px;
    --lusena-section-padding-bottom-mobile: {{ section.settings.padding_bottom_mobile }}px;
    --lusena-section-padding-top-desktop: {{ section.settings.padding_top }}px;
    --lusena-section-padding-bottom-desktop: {{ section.settings.padding_bottom }}px;
  "
>
  <div class="container max-w-4xl mx-auto">
    {% comment %} Optional kicker {% endcomment %}
    {% if section.settings.kicker != blank %}
      <p class="text-xs uppercase tracking-widest text-secondary mb-4">
        {{ section.settings.kicker }}
      </p>
    {% endif %}

    {% comment %} Heading {% endcomment %}
    <h2 class="text-3xl md:text-4xl font-serif text-primary mb-4
      {%- if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif -%}
    ">
      {{ section.settings.heading }}
    </h2>

    {% comment %} Body {% endcomment %}
    {% if section.settings.body != blank %}
      <div class="text-secondary max-w-2xl
        {%- if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif -%}
      ">
        {{ section.settings.body }}
      </div>
    {% endif %}

    {% comment %} Blocks (if applicable) {% endcomment %}
    {% for block in section.blocks %}
      <div {{ block.shopify_attributes }}
        class="{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}"
      >
        {{ block.settings.text }}
      </div>
    {% endfor %}

    {% comment %} CTA {% endcomment %}
    {% if section.settings.button_label != blank %}
      <a href="{{ section.settings.button_link }}"
         class="lusena-btn lusena-btn--primary lusena-btn--size-default mt-8">
        {{ section.settings.button_label }}
      </a>
    {% endif %}
  </div>
</section>

{% stylesheet %}
  .lusena-{name} {
    padding-top: var(--lusena-section-padding-top-mobile);
    padding-bottom: var(--lusena-section-padding-bottom-mobile);
  }
  @media (min-width: 768px) {
    .lusena-{name} {
      padding-top: var(--lusena-section-padding-top-desktop);
      padding-bottom: var(--lusena-section-padding-bottom-desktop);
    }
  }
{% endstylesheet %}

{% schema %}
{
  "name": "LUSENA {Name}",
  "settings": [
    {
      "type": "text",
      "id": "kicker",
      "label": "Kicker text"
    },
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Section heading"
    },
    {
      "type": "richtext",
      "id": "body",
      "label": "Body text"
    },
    {
      "type": "text",
      "id": "button_label",
      "label": "Button label"
    },
    {
      "type": "url",
      "id": "button_link",
      "label": "Button link"
    },
    {
      "type": "header",
      "content": "Spacing"
    },
    {
      "type": "range",
      "id": "padding_top",
      "label": "Padding top (desktop)",
      "min": 0,
      "max": 240,
      "step": 4,
      "unit": "px",
      "default": 56
    },
    {
      "type": "range",
      "id": "padding_bottom",
      "label": "Padding bottom (desktop)",
      "min": 0,
      "max": 240,
      "step": 4,
      "unit": "px",
      "default": 56
    },
    {
      "type": "range",
      "id": "padding_top_mobile",
      "label": "Padding top (mobile)",
      "min": 0,
      "max": 240,
      "step": 4,
      "unit": "px",
      "default": 40
    },
    {
      "type": "range",
      "id": "padding_bottom_mobile",
      "label": "Padding bottom (mobile)",
      "min": 0,
      "max": 240,
      "step": 4,
      "unit": "px",
      "default": 40
    }
  ],
  "presets": [
    {
      "name": "LUSENA {Name}"
    }
  ]
}
{% endschema %}
```

**Step 3:** Add the section to a template JSON file, or let merchants add it via the theme editor.

**Checklist for new sections:**
- [ ] `lusena-` prefix in filename
- [ ] `.container` for width constraint
- [ ] 4 padding CSS variables + schema ranges
- [ ] `bg-{brand-bg|surface-1|surface-2|white}` on the `<section>` tag
- [ ] Animations gated by `settings.animations_reveal_on_scroll`
- [ ] `{{ block.shopify_attributes }}` on block elements
- [ ] CSS in `{% stylesheet %}` (not external file)
- [ ] Images with `loading="lazy"`, responsive `widths` and `sizes`
- [ ] Touch targets ≥ 44px on interactive elements
- [ ] Semantic HTML tags (`<section>`, `<nav>`, `<h2>`)

---

### 8.3 How to Add a New Component Variant

#### Adding a new button variant

**File to edit:** `snippets/lusena-button-system.liquid`

1. Add the CSS rule in the `{% stylesheet %}` block, following naming convention:
   ```css
   .lusena-btn--{new-variant} {
     /* styles following existing patterns */
   }
   .lusena-btn--{new-variant}:hover {
     /* hover state */
   }
   ```

2. Document the variant in this file (section 4.1).

3. Test with reduced motion, focus-visible, and disabled states.

#### Adding a new icon

**File to edit:** `snippets/lusena-icon.liquid`

1. Add a new `{% when '{icon-name}' %}` case in the icon case/when block.
2. Use a 24×24 viewBox SVG, `fill="none"`, `stroke="currentColor"`, consistent stroke width (1.5px default).
3. The icon inherits color from parent via `currentColor`.

#### Adding a new utility class

**File to edit:** `snippets/lusena-missing-utilities.liquid`

Add the class in the `{% stylesheet %}` block, following Tailwind naming conventions. Use the existing responsive/state patterns as reference.

---

## 9. Maintenance Guardrails (Quality)

### 9.1 Performance checklist

- [ ] Hero images use `loading="eager"` + `fetchpriority="high"`.
- [ ] All other images use `loading="lazy"`.
- [ ] Images include `widths` and `sizes` attributes for responsive srcset.
- [ ] Image weight budgets: hero ≤300KB, cards ≤160KB, gallery ≤220KB each.
- [ ] CSS is scoped via `{% stylesheet %}` (deferred loading, deduped by Shopify).
- [ ] No render-blocking JS — use `{% javascript %}` tag or `defer`/`async` on script tags.
- [ ] No unused CSS/JS left in the page (check for leftover Dawn component files).
- [ ] Video embeds are deferred (click-to-play) — never autoplay with sound.

### 9.2 Accessibility checklist

- [ ] All interactive elements have `:focus-visible` styles (teal ring: `0 0 0 2px rgb(14 94 90), 0 0 0 4px rgb(255 255 255)`).
- [ ] Touch targets ≥ 44×44px on mobile.
- [ ] 8px minimum gap between touch targets.
- [ ] Text contrast meets WCAG AA (4.5:1 for body, 3:1 for large text/UI).
- [ ] Icon-only buttons have `aria-label`.
- [ ] Drawers/modals use `role="dialog"`, `aria-modal="true"`, `tabindex="-1"`.
- [ ] Accordions use `aria-expanded` on trigger buttons.
- [ ] `prefers-reduced-motion` respected — all animations/transitions have reduced-motion fallbacks.
- [ ] Breadcrumbs wrapped in `<nav aria-label="Breadcrumb">`.
- [ ] Interactive areas that toggle visibility use `aria-hidden` and/or `inert`.
- [ ] Form fields grouped with `<fieldset>` and `<legend>`.
- [ ] Every swipe/drag gesture has a click/tap equivalent.

### 9.3 Theme editor UX checklist

- [ ] Schema setting labels are clear and descriptive (English is fine).
- [ ] All settings have sensible defaults.
- [ ] Range sliders have appropriate min/max/step/unit.
- [ ] Section has a `presets` entry so merchants can add it via the theme editor.
- [ ] Block types have clear names and reasonable limits.

### 9.4 Testing checklist

- [ ] Run `shopify theme check` — ignore warnings listed in the known baseline (AGENTS.md).
- [ ] Quick Lighthouse pass: Performance > 80, Accessibility > 90 on key pages.
- [ ] Responsive spot-checks at 375px (mobile), 768px (tablet), 1280px (desktop), 1440px+ (wide).
- [ ] Test with cart drawer: add item, remove item, quantity change, upsell.
- [ ] Test reduced motion: verify `prefers-reduced-motion: reduce` removes animations.
- [ ] Test keyboard navigation: Tab through all interactive elements on the page.

### 9.5 Known theme check warnings (baseline)

These have been present since the beginning and are not bugs:
- `layout/password.liquid`: UndefinedObject `scheme_classes`
- `layout/theme.liquid`: UndefinedObject `scheme_classes`
- `sections/featured-product.liquid`: UnusedAssign `seo_media`
- `sections/main-article.liquid`: VariableName `anchorId`
- `sections/main-list-collections.liquid`: VariableName `moduloResult`
- `sections/main-product.liquid`: UnusedAssign `seo_media`
- `sections/main-product.liquid`: UndefinedObject `continue`
- `sections/main-search.liquid`: UnusedAssign `product_settings`

---

## 10. Appendix

### 10.1 Component Inventory Table

| Component | File | Used on surfaces |
|---|---|---|
| Button system | `snippets/lusena-button-system.liquid` | All (global) |
| Icon system | `snippets/lusena-icon.liquid` | All (global) |
| Missing utilities | `snippets/lusena-missing-utilities.liquid` | All (global) |
| Product card | `snippets/lusena-product-card.liquid` | Homepage (bestsellers), PDP (cross-sell) |
| Breadcrumbs | `snippets/lusena-breadcrumbs.liquid` | PDP |
| PDP media gallery | `snippets/lusena-pdp-media.liquid` | PDP |
| PDP summary | `snippets/lusena-pdp-summary.liquid` | PDP |
| PDP proof chips | `snippets/lusena-pdp-proof-chips.liquid` | PDP |
| PDP variant picker | `snippets/lusena-pdp-variant-picker.liquid` | PDP |
| PDP add-to-cart | `snippets/lusena-pdp-atc.liquid` | PDP |
| PDP guarantee | `snippets/lusena-pdp-guarantee.liquid` | PDP |
| PDP payment badges | `snippets/lusena-pdp-payment.liquid` | PDP |
| PDP buybox panels | `snippets/lusena-pdp-buybox-panels.liquid` | PDP |
| PDP cross-sell | `snippets/lusena-pdp-cross-sell.liquid` | PDP |
| PDP sticky ATC | `snippets/lusena-pdp-sticky-atc.liquid` | PDP |
| PDP styles | `snippets/lusena-pdp-styles.liquid` | PDP |
| PDP scripts | `snippets/lusena-pdp-scripts.liquid` | PDP |
| Cart drawer | `snippets/cart-drawer.liquid` | All (global when cart=drawer) |
| Header | `sections/lusena-header.liquid` | All (global) |
| Footer | `sections/lusena-footer.liquid` | All (global) |
| Hero | `sections/lusena-hero.liquid` | Homepage |
| Trust bar | `sections/lusena-trust-bar.liquid` | Homepage, Quality page |
| Problem/Solution | `sections/lusena-problem-solution.liquid` | Homepage |
| Bestsellers | `sections/lusena-bestsellers.liquid` | Homepage |
| Heritage | `sections/lusena-heritage.liquid` | Homepage |
| Testimonials | `sections/lusena-testimonials.liquid` | Homepage |
| Bundles | `sections/lusena-bundles.liquid` | Homepage |
| FAQ | `sections/lusena-faq.liquid` | Homepage |
| Quality hero | `sections/lusena-quality-hero.liquid` | Quality page |
| Quality momme | `sections/lusena-quality-momme.liquid` | Quality page |
| Quality fire test | `sections/lusena-quality-fire-test.liquid` | Quality page |
| Quality origin | `sections/lusena-quality-origin.liquid` | Quality page |
| Quality QC | `sections/lusena-quality-qc.liquid` | Quality page |
| Quality certificates | `sections/lusena-quality-certificates.liquid` | Quality page |
| About hero | `sections/lusena-about-hero.liquid` | About page |
| About story | `sections/lusena-about-story.liquid` | About page |
| About values | `sections/lusena-about-values.liquid` | About page |
| PDP feature highlights | `sections/lusena-pdp-feature-highlights.liquid` | PDP |
| PDP quality evidence | `sections/lusena-pdp-quality-evidence.liquid` | PDP |
| PDP details | `sections/lusena-pdp-details.liquid` | PDP |
| Main product | `sections/lusena-main-product.liquid` | PDP |

### 10.2 Token Quick-Reference

```
COLORS
  Brand bg     #F7F5F2   .bg-brand-bg
  Surface-1    #FFFFFF   .bg-surface-1
  Surface-2    #F0EEEB   .bg-surface-2
  Text-1       #111111   .text-primary
  Text-2       #4A4A4A   .text-secondary
  CTA          #0E5E5A   .text-accent-cta / .bg-accent-cta
  Gold         #8C6A3C   .text-accent-gold
  Success      #2F7D4E   .text-status-success
  Error        #B91C1C   (hardcoded in PDP styles)

TYPOGRAPHY
  Headings     Source Serif 4, serif    .font-serif
  Body/UI      Inter, sans-serif       .font-sans (default)
  Weights      400 (.font-normal), 500 (.font-medium), 600 (.font-semibold)

SPACING
  Base unit    0.4rem (4px)
  Scale        4, 6, 8, 12, 16, 20, 24, 32, 48, 64, 96

RADIUS
  Brand        6px    .rounded-brand
  Pill         8px    variant_pills_radius
  Circle       9999px .rounded-full
  Sharp        0      cards, media

BREAKPOINTS
  sm   640px   md   768px   lg   1024px   xl   1280px   2xl  1440px

MOTION
  UI           150ms ease
  LUSENA       420ms cubic-bezier(0.2, 0, 0, 1) / 14px
  Dawn scroll  500ms ease-out-slow
  Hero entry   650–900ms ease-out-slow
```

### 10.3 Brand vs. Implementation Gap Analysis

#### Matches (brand → code alignment)

| Brandbook rule | Implementation status |
|---|---|
| Colors: porcelain bg, teal CTA, gold accent | ✅ Exact match |
| Fonts: Source Serif 4 + Inter | ✅ Exact match |
| CTA radius 6–8px | ✅ Buttons 6px, pills 8px |
| CTA height 44–48px | ✅ Default 48px, SM 44px |
| Focus: 2px outline | ✅ `box-shadow: 0 0 0 2px teal, 0 0 0 4px white` |
| Tap targets: min 44×44px | ✅ All buttons/icon-buttons meet this |
| Max 2 CTAs per screen | ✅ Primary + secondary on PDP |
| Calm motion, no bounce | ✅ Ease/ease-out curves only |
| Reduced motion support | ✅ All CSS + JS respect it |
| Image ratios (4:5 PLP, 1:1 PDP) | ✅ Product card uses `aspect-[4/5]` |
| Icon style: outline, 1.5px stroke, 24px | ✅ Consistent in `lusena-icon.liquid` |
| "Imperfect Silk" photography | ⚠️ Not technically enforced — content/art direction matter |

#### Mismatches / gaps

| Brandbook prescription | Current state | Risk |
|---|---|---|
| ~~i18n: `{{ 'key' | t }}` for all text~~ | All sections use hardcoded Polish strings | ✅ By design — PL-only market, no multi-language planned |
| Neutral scale N0–N900 (10 steps) | Only N400, N700 used as utility classes | Low — enough for current UI |
| Warning color `#B7791F` | Not used anywhere | Low — no warning states in validated surfaces |
| Overlay/scrim tokens `--scrim-60`, `--scrim-80` | Hero uses `rgba(0 0 0 / X%)`, lightbox uses `rgba(0,0,0,0.92)` | Low — works but doesn't use named tokens |
| Page margins: desktop 96px, tablet 64px, mobile 20–24px | Container padding: 96px (xl), 64px (lg), 32px (md), 20px (mobile) | ✅ Close match |
| Column grid: 12/8/4 col with gutters | Sections use ad-hoc Tailwind grids, not formal 12-col | Low — visual outcome is correct |

#### Ambiguities (brandbook doesn't specify, theme made a choice)

| Decision | What the theme chose |
|---|---|
| Sticky ATC bar behavior | Shows on scroll past main ATC, hides when main ATC visible. Max-width 1280px. |
| Quality evidence section layout | Expandable accordion cards rather than static content |
| Cross-sell placement | Below buybox panels, horizontal card grid |
| Shipping progress bar visual | Teal→green fill on 0.6rem track (white bg) |
| Mobile gallery navigation | Horizontal scroll with dot indicators, no arrows |
| Cart drawer width | `max-w-md` (448px) |
| Auto-hiding header behavior | Mobile scroll-down hides; 8px delta threshold |

### 10.4 Resolved Decisions

Items from the original open-questions list, resolved as of 2026-02-21:

| # | Topic | Decision | Rationale |
|---|---|---|---|
| 1 | Translation / i18n | **Not needed** | PL-only market. Hardcoded Polish text is intentional. No multi-language planned. |
| 2 | Collection page | **Already LUSENA-ized** | `templates/collection.json` maps to `lusena-main-collection.liquid` (breadcrumbs, product grid via `lusena-product-card`, pagination). Filter/sort button is non-functional — to be removed/hidden (no sort/filter needed now). |
| 3 | Breakpoints | **Tailwind for new code** | See section 10.5 for full analysis. 44 Tailwind vs 4 Dawn usages in `lusena-*` files. 768px is the primary flip. Keep the 4 Dawn sync-points as-is. |
| 4 | Dawn default sections | **Backlog** | Many inactive Dawn sections remain; not blocking. Can be cleaned up later. |
| 5 | `--content-grid` | **Ignore** | Referenced in AGENTS.md examples but never implemented. Not relevant. |
| 6 | Orphan snippets | **Backlog** | `lusena-pdp-accordions.liquid` — verify and clean up later. |
| 7 | Blog/article templates | **Backlog** | Dawn defaults in use. Adapt when blog content is prioritized. |
| 8 | Search page | **Backlog** | Dawn default. Adapt when needed. |
| 9 | Font loading | **Self-hosted variable fonts** | Completed. See section 10.6. Inter + Source Serif 4 variable `.woff2` files in `assets/`, Google Fonts `<link>` removed. GDPR-clean, all weights preserved. |
| 10 | Dark mode | **No dark mode** | LUSENA intentionally avoids dark sections for brand consistency. Color schemes 3 and 4 should not be used in LUSENA sections. |

### 10.5 Breakpoint System Decision (resolved)

**Decision: Use Tailwind breakpoints for all new LUSENA code.**

Analysis of all `lusena-*` files:

| System | Breakpoints | Occurrences in `lusena-*` files |
|---|---|---|
| **Tailwind** | 640 / 768 / 1024 / 1280 / 1440 px | **44** (768px alone = 35) |
| **Dawn** | 750 / 990 px | **4** |

The 4 Dawn-breakpoint usages are intentional sync points:
- `lusena-pdp-styles.liquid` (2×): Gallery show/hide and lightbox cursor must match Dawn's 750px media gallery flip.
- `lusena-comparison.liquid` (1×): Table padding aligning with `.page-width`.
- `lusena-science.liquid` (1×): 2-column layout matching Dawn layout.

**Rule for new sections:**

| Prefix | Breakpoint | When to use |
|---|---|---|
| _(none)_ | < 640px | Mobile-first base styles |
| `sm` | `min-width: 640px` | Rare, small-tablet tweaks |
| **`md`** | **`min-width: 768px`** | **Primary mobile → desktop flip** (most common) |
| `lg` | `min-width: 1024px` | Large desktop refinements |
| `xl` | `min-width: 1280px` | Extra-wide tweaks (rare) |
| `2xl` | `min-width: 1440px` | Container cap |

**Exception:** When directly overriding Dawn layout classes (`.page-width`, gallery, Dawn grid utilities), match Dawn's 750/990px to stay in sync. Never mix breakpoints within the same element's responsive chain.

Dawn's `base.css` uses 750/990 exclusively (25 and 15 occurrences respectively). This is fine — LUSENA sections don't inherit Dawn's responsive grid classes; they use `.container` and Tailwind grids.

### 10.6 Font Loading (resolved — self-hosted)

**Decision: Self-host both variable fonts from Shopify CDN. Google Fonts removed.**

Completed 2026-02-21. Fonts are now served from `assets/` via Shopify's CDN — zero external requests, GDPR-clean.

#### Font files in `assets/`

| File | Font | Style | Weights | Size |
|---|---|---|---|---|
| `InterVariable.woff2` | Inter | Normal | 100–900 | ~344 KB |
| `SourceSerif4Variable-Roman.woff2` | Source Serif 4 | Normal | 200–900 | ~419 KB |
| `SourceSerif4Variable-Italic.woff2` | Source Serif 4 | Italic | 200–900 | ~339 KB |

#### What was changed

**`layout/theme.liquid`:**
1. **Removed** the Google Fonts `<link>` block (preconnect + stylesheet, 9 lines).
2. **Added** 3 `@font-face` declarations inside the existing `{% style %}` block, using `{{ '…' | asset_url }}` for Shopify CDN delivery.
3. **Kept** the Shopify `font_face` filter lines — they still generate `@font-face` for Inter 400/700 and Source Serif 4 400 from `fonts.shopifycdn.com`. The self-hosted variable fonts take priority via CSS cascade (they appear later and cover a wider weight range).

#### Unicode range

All three `@font-face` rules use:
```
unicode-range: U+0000-024F, U+0259, U+1E00-1EFF, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
```
This covers Latin, Latin Extended-A (Polish characters: ą, ć, ę, ł, ń, ó, ś, ź, ż), Latin Extended-B, and common symbols/currency.

#### Weight coverage (before vs. after)

| Weight | Before (Google) | After (self-hosted) | Used in theme? |
|---|---|---|---|
| Inter 300 | ✅ | ✅ | Yes — `font-light` |
| Inter 400 | ✅ | ✅ | Yes — default body |
| Inter 500 | ✅ | ✅ | Yes — `font-medium` (most used) |
| Inter 600 | ✅ | ✅ | Yes — `font-semibold` |
| Inter 700 | ✅ | ✅ | Yes — bold |
| Source Serif 4 (all weights) | ✅ | ✅ | Yes — headings, logo |
| Source Serif 4 italic | ✅ | ✅ | Yes — hero, PDP eyebrow |

**Zero visual regression. All weights preserved.**

#### Verification (2026-02-21)

Self-hosted fonts verified via `sections/lusena-font-debug.liquid` debug panel:
- ✅ All Inter weights (300/400/500/600/700) render correctly with visible weight differentiation
- ✅ Source Serif 4 normal + italic render at all weights
- ✅ Polish characters (ąćęłńóśźż) display correctly
- ✅ `document.fonts` API confirms all font faces loaded from Shopify CDN
- ✅ Zero requests to `fonts.googleapis.com` or `fonts.gstatic.com`
- ✅ Debug section removed after successful verification

#### Caveat (unchanged)

`assets/lusena-shop.css` (Tailwind-compiled) hardcodes `font-family: Inter, sans-serif` and `font-family: "Source Serif 4", serif` by name rather than using Dawn CSS variables. This works because our `@font-face` rules use the same family names. If the brand ever changes fonts, both the `@font-face` rules **and** the Tailwind config would need updating.

### 10.7 Remaining Backlog

Low-priority items to address when relevant:

| Item | Priority | Notes |
|---|---|---|
| Remove filter/sort button from collection page | Low | Non-functional button in `lusena-main-collection.liquid`. Remove or hide until filtering is implemented. |
| Dawn default section cleanup | Low | Archive or label unused Dawn sections (`main-product.liquid`, `featured-collection.liquid`, etc.) |
| Orphan snippet audit | Low | Verify `lusena-pdp-accordions.liquid` and remove if unused |
| Blog/article LUSENA adaptation | Low | Adapt when blog content becomes a priority |
| Search page LUSENA adaptation | Low | Adapt when search UX becomes a priority |

---

*Last updated: 2026-02-21 (font self-hosting migration completed). Maintain this document alongside code changes. See `docs/THEME_CHANGES.md` for commit-linked changelog.*
