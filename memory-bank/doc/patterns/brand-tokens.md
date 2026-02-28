# LUSENA Design Tokens (Actionable Reference)

> Compact extraction from `docs/theme-brandbook-uiux.md` and `docs/LUSENA_BrandBook_v2.md`.
> For full specifications, read those source documents.

## Colors

| Token | Value | CSS var/class | Usage |
|-------|-------|---------------|-------|
| Brand background | `#F7F5F2` | `--brand-bg`, `.bg-brand-bg` | Default page background |
| Primary text | `#111111` | `--primary`, `.text-primary` | Headings, dark text |
| Secondary text | `#4A4A4A` | `.text-secondary` | Body copy, captions |
| CTA accent | `#0E5E5A` | `--accent-cta`, `.text-accent-cta` | Buttons, links, active states |
| Gold accent | `#8C6A3C` | `--accent-gold`, `.text-accent-gold` | Badges, premium highlights |
| Surface 1 | `#FFFFFF` | `.bg-surface-1` | Card backgrounds |
| Surface 2 | `#F0EEEB` | `.bg-surface-2` | Alternating section backgrounds |
| Neutral 400 | `#B9B7B4` | `.text-neutral-400` | Disabled, placeholder |
| Neutral 700 | `#5A5855` | `.text-neutral-700` | Muted labels |
| Success | `#2F7D4E` | `.text-status-success` | In-stock indicators |
| Error | `#B91C1C` | — | Out-of-stock indicators |

### Color schemes (Shopify admin)

| Scheme | Background | Text | Usage |
|--------|------------|------|-------|
| scheme-1 | `#F7F5F2` | dark | Default sections |
| scheme-2 | `#F0EEEB` | dark | Alternating sections |
| scheme-3 | `#2E2D2B` | light | Dark accent sections |
| scheme-4 | `#111111` | light | Full dark sections |
| scheme-5 | `#8C6A3C` | light | Gold accent sections |

**Rule:** CTA color is always `#0E5E5A` — never changes between pages.

## Typography

| Role | Font | CSS |
|------|------|-----|
| Headings / brand | Source Serif 4, serif | `.font-serif` |
| Body / UI | Inter, sans-serif | `.font-sans` (default) |

**Weights:** 400 (regular), 500 (medium), 600 (semibold)

**Scale (Tailwind):**

| Class | Size | Line-height | Typical usage |
|-------|------|-------------|---------------|
| `text-xs` | 12px | 16px | Proof chips, badges, captions |
| `text-sm` | 14px | 20px | Trust bar, accordion body, prices |
| `text-base` | 16px | 24px | Body text, FAQ summary, buttons |
| `text-lg` | 18px | 28px | PDP eyebrow, footer headings |
| `text-xl` | 20px | 28px | Cart drawer title |
| `text-2xl` | 24px | 32px | PDP title (mobile), section headings |
| `text-3xl` | 30px | 36px | Section headings |
| `text-4xl` | 36px | 40px | Large section headings, PDP title (desktop) |
| `text-5xl` | 48px | 1 | Hero headline (mobile) |
| `text-7xl` | 72px | 1 | Hero headline (tablet) |
| `text-8xl` | 96px | 1 | Hero headline (desktop) |

**Rule:** Use Tailwind utility classes (`text-*`) for LUSENA sections, not Dawn heading scale.

## Spacing

### Token scale (mobile → desktop at 768px)

| Token | Mobile | Desktop |
|-------|--------|---------|
| `--lusena-space-xs` | 8px | 8px |
| `--lusena-space-sm` | 12px | 16px |
| `--lusena-space-md` | 20px | 24px |
| `--lusena-space-lg` | 32px | 48px |
| `--lusena-space-xl` | 40px | 64px |
| `--lusena-space-2xl` | 64px | 96px |
| `--lusena-space-3xl` | 80px | 128px |
| `--lusena-space-spacious` | 48px | 80px |

### Section padding tiers

| Tier class | Mobile | Desktop | Usage |
|------------|--------|---------|-------|
| `lusena-spacing--full-bleed` | 0 | 0 | Edge-to-edge media |
| `lusena-spacing--compact` | 32px | 48px | Trust bar, utility bars |
| `lusena-spacing--standard` | 40px | 64px | Most content sections |
| `lusena-spacing--spacious` | 48px | 80px | CTAs, trust-building |
| `lusena-spacing--hero` | 64px | 96px | Hero sections |

### Semantic gaps

| Class | Mobile | Desktop | Usage |
|-------|--------|---------|-------|
| `lusena-gap-kicker` | 12px | 12px | Kicker text bottom |
| `lusena-gap-heading` | 20px | 24px | Heading bottom |
| `lusena-gap-body` | 20px | 24px | Body text bottom |
| `lusena-gap-cta` | 28px | 36px | CTA button bottom |
| `lusena-gap-cta-top` | 28px | 36px | CTA button top |
| `lusena-gap-section-intro` | 32px | 48px | Section intro bottom |
| `lusena-gap-subsection` | 48px | 80px | Major content break |

## Breakpoints

| Name | Width | Role |
|------|-------|------|
| base | <640px | Mobile (default) |
| `sm` | 640px | Small tablets (rare) |
| **`md`** | **768px** | **Primary mobile↔desktop flip** |
| `lg` | 1024px | Laptops |
| `xl` | 1280px | Desktop |
| `2xl` | 1440px | Container cap |

**Rule:** Use Tailwind breakpoints (`md:`, `lg:`) for LUSENA. Dawn breakpoints (750/990px) only for existing Dawn layout classes.

## Border radii

| Token | Value | Usage |
|-------|-------|-------|
| `rounded-brand` | 6px | Buttons, inputs (**brand standard**) |
| `rounded-sm` | 2px | Payment badges, thumbnails |
| `rounded-full` | 9999px | Circles, icon buttons, cart badge |

## Shadows

| Name | Value | Usage |
|------|-------|-------|
| `shadow-sm` | `0 1px 2px 0 rgb(0 0 0 / .05)` | Proof chips, swatches |
| `shadow-2xl` | `0 25px 50px -12px rgb(0 0 0 / .25)` | Cart drawer |
| Focus ring | `0 0 0 2px #0E5E5A, 0 0 0 4px #fff` | `:focus-visible` |

**Rule:** Shadows used sparingly — most `shadow_opacity` settings are `0` in theme config.

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
**Border radius:** 6px (`rounded-brand`)

## Transitions

- **UI hover/focus:** 150ms ease
- **Button:** 150-200ms ease
- **Image hover scale:** 300ms ease-in-out
- **Scroll reveal:** 420ms `cubic-bezier(0.2, 0, 0, 1)`, translateY(14px)
