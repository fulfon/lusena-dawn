# LUSENA Design Tokens (Actionable Reference)

> Compact extraction from `assets/lusena-foundations.css` (single source of truth).
> For spacing system details, see `memory-bank/doc/patterns/spacing-system.md`.

## Colors

| Token | Value | CSS variable | Usage |
|-------|-------|-------------|-------|
| Brand background | `#F7F5F2` | `--lusena-brand-bg` | Default page background |
| Surface 1 | `#FFFFFF` | `--lusena-surface-1` | Card backgrounds |
| Surface 2 | `#F0EEEB` | `--lusena-surface-2` | Alternating section backgrounds |
| Primary text | `#111111` | `--lusena-text-1` | Headings, dark text |
| Secondary text | `#4A4A4A` | `--lusena-text-2` | Body copy, captions |
| CTA accent | `#0E5E5A` | `--lusena-accent-cta` | Buttons, links, active states |
| CTA hover | `#137A75` | `--lusena-accent-cta-hover` | Button hover |
| Gold accent | `#8C6A3C` | `--lusena-accent-2` | Badges, premium highlights |
| Success | `#2F7D4E` | `--lusena-status-success` | In-stock indicators |
| Error | `#B91C1C` | `--lusena-status-error` | Out-of-stock indicators |

Neutral scale: `--lusena-color-n0` (#FFFFFF) through `--lusena-color-n900` (#111111).

Utility classes: `.lusena-bg-brand`, `.lusena-bg-surface-1`, `.lusena-bg-surface-2`, `.lusena-section--inverted`.

**Rule:** CTA color is always `#0E5E5A` — never changes between pages.

### Color schemes (Shopify admin)

| Scheme | Background | Text | Usage |
|--------|------------|------|-------|
| scheme-1 | `#F7F5F2` | dark | Default sections |
| scheme-2 | `#F0EEEB` | dark | Alternating sections |
| scheme-3 | `#2E2D2B` | light | Dark accent sections |
| scheme-4 | `#111111` | light | Full dark sections |
| scheme-5 | `#8C6A3C` | light | Gold accent sections |

## Typography

| Role | Font | CSS variable |
|------|------|-------------|
| Headings / brand | Source Serif 4, serif | `--lusena-font-brand` |
| Body / UI | Inter, sans-serif | `--lusena-font-body` |

**Weights:** 400 (regular), 500 (medium), 600 (semibold)

**Semantic type classes (from `lusena-foundations.css`):**

| Class | Mobile (size / line) | Desktop (size / line) | Usage |
|-------|--------|---------|-------|
| `.lusena-type-hero` | 4.0rem / 4.8rem | 5.6rem / 6.4rem | Hero headlines |
| `.lusena-type-h1` | 3.2rem / 4.0rem | 4.0rem / 4.8rem | Page/section headings |
| `.lusena-type-h2` | 2.0rem / 2.4rem | 2.4rem / 3.2rem | Subheadings |
| `.lusena-type-body` | 1.6rem / 2.4rem | 1.6rem / 2.4rem | Body text |
| `.lusena-type-caption` | 1.2rem / 1.6rem | 1.2rem / 1.6rem | Captions, metadata |

**Rule:** Use `lusena-type-*` classes for all typography. All values follow the 8px baseline grid.

## Spacing

### Token scale (numeric, 8px grid)

| Token | Value |
|-------|-------|
| `--lusena-space-1` | 0.8rem (8px) |
| `--lusena-space-2` | 1.6rem (16px) |
| `--lusena-space-3` | 2.4rem (24px) |
| `--lusena-space-4` | 3.2rem (32px) |
| `--lusena-space-5` | 4rem (40px) |
| `--lusena-space-6` | 4.8rem (48px) |
| `--lusena-space-8` | 6.4rem (64px) |
| `--lusena-space-10` | 8rem (80px) |
| `--lusena-space-12` | 9.6rem (96px) |
| `--lusena-space-16` | 12.8rem (128px) |

Half-step: `--lusena-space-05` = 0.4rem (4px).

### Section padding tiers

| Tier class | Mobile | Desktop | Usage |
|------------|--------|---------|-------|
| `lusena-spacing--full-bleed` | 0 | 0 | Edge-to-edge media |
| `lusena-spacing--compact` | 32px | 48px | Trust bar, utility bars |
| `lusena-spacing--standard` | 48px | 64px | Most content sections |
| `lusena-spacing--spacious` | 64px | 96px | CTAs, trust-building |
| `lusena-spacing--hero` | 80px | 128px | Hero sections |

### Semantic gaps

| Class | Value | Usage |
|-------|-------|-------|
| `lusena-gap-kicker` | 1.2rem | Kicker text bottom |
| `lusena-gap-heading` | 2.4rem | Heading bottom |
| `lusena-gap-body` | 2.4rem | Body text bottom |
| `lusena-gap-cta` | 3.2rem | CTA button top margin |
| `lusena-gap-section-intro` | 4rem (mobile) / 4.8rem (desktop) | Section intro bottom |
| `lusena-gap-subsection` | 4.8rem (mobile) / 8rem (desktop) | Major content break |

## Breakpoints

| Width | Role |
|-------|------|
| 768px | **Primary mobile/desktop flip** (used in all `@media` queries) |
| 1024px | Large desktop (occasional grid adjustments) |
| 1280px | Max container width (`lusena-container`: `max-width: 120rem`) |

**Rule:** Use `@media (min-width: 768px)` in `{% stylesheet %}` blocks. No Tailwind breakpoint prefixes.

## Border radii

| Token | Value | Usage |
|-------|-------|-------|
| `--lusena-btn-radius` | 0.6rem (6px) | Buttons, inputs (**brand standard**) |
| Small radius | 0.2rem (2px) | Payment badges, thumbnails |
| Full radius | 9999px | Circles, icon buttons, cart badge |

## Shadows

Shadows are used sparingly — editorial rhythm favors hairline borders over shadows.

| Usage | Value |
|-------|-------|
| Proof chips, swatches | `0 1px 2px 0 rgb(0 0 0 / .05)` |
| Focus ring | `outline: 2px solid var(--lusena-accent-cta); outline-offset: 2px` |

## Buttons

| Variant | Background | Text |
|---------|------------|------|
| `lusena-btn--primary` | `rgb(14 94 90 / 0.9)` | White |
| `lusena-btn--outline` | `rgb(14 94 90 / 0.05)` border | Teal |
| `lusena-btn--ghost` | `#F0EEEB` | Dark |
| `lusena-btn--text` | Transparent | Teal |
| `lusena-btn--link` | Transparent + underline | Dark |

**Sizes:** default (48px height), small (44px height)
**Touch target:** 44x44px minimum (WCAG)
**Border radius:** 6px (`--lusena-btn-radius`)

## Transitions

| Token | Value | Usage |
|-------|-------|-------|
| `--lusena-transition-fast` | 150ms ease | UI hover/focus |
| `--lusena-transition-base` | 250ms ease | Accordion, drawer |
| Image hover scale | 300ms ease-in-out | Product cards |
| Scroll reveal | 420ms `cubic-bezier(0.2, 0, 0, 1)`, translateY(14px) | Dawn scroll-trigger |
