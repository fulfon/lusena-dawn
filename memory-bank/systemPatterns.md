# System Patterns

## CSS Architecture

### Migration in progress

We are replacing the old fragmented CSS with a single `assets/lusena-foundations.css`. During transition, both old and new files coexist. See `memory-bank/progress.md` for phase status.

**Target stack (after migration):**
1. **Inline font-faces & root CSS** — Custom fonts (Inter, Source Serif 4), CSS custom properties
2. **Dawn base:** `assets/base.css` — Foundation styles
3. **LUSENA foundations:** `assets/lusena-foundations.css` — Single source of truth (tokens, spacing, typography, components, utilities)
4. **Button system:** `snippets/lusena-button-system.liquid`
5. **Component styles:** `{% stylesheet %}` blocks in sections/snippets

**Old stack (being phased out):**
- `assets/lusena-shop.css` (26KB Tailwind) → replaced by foundations
- `assets/lusena-spacing.css` (266 lines) → absorbed into foundations
- `snippets/lusena-missing-utilities.liquid` (351 lines) → absorbed into foundations

### Key constraint
`{% stylesheet %}` blocks have ~73KB cumulative limit (`compiled_assets/styles.css` truncation). Large CSS MUST go in standalone asset files, NOT in `{% stylesheet %}` blocks.

> Full CSS architecture details: `memory-bank/doc/patterns/css-architecture.md`

## Naming conventions

- All LUSENA files: `lusena-*` prefix
- Sections: `sections/lusena-{component}.liquid`
- Snippets: `snippets/lusena-{component}.liquid`
- Assets: `assets/lusena-{name}.{css|js}`
- CSS classes: `lusena-spacing--*`, `lusena-content-flow*`, `lusena-gap-*`, `lusena-btn*`
- CSS variables: `--lusena-space-*`, `--lusena-section-*`, `--lusena-tier-*`

## Spacing system (LUSENA foundations is source of truth)

### Section padding: tier classes (values from `lusena-foundations.css`)
| Tier | Mobile | Desktop | Usage |
|------|--------|---------|-------|
| `lusena-spacing--full-bleed` | 0 | 0 | Edge-to-edge media |
| `lusena-spacing--compact` | 32px | 48px | Utility sections (trust bar) |
| `lusena-spacing--standard` | 48px | 64px | Informational content |
| `lusena-spacing--spacious` | 64px | 96px | Trust-building, CTAs |
| `lusena-spacing--hero` | 80px | 128px | Hero sections |

Modifier: `lusena-spacing--snug-top` — reduces top to 32/48px for heroes sharing bg with header.

### Container rhythm: content-flow utilities
- `lusena-content-flow` — 24px (standard)
- `lusena-content-flow--tight` — 16px (kicker + heading pairs)
- `lusena-content-flow--relaxed` — 32px (hero/editorial)

### Element gaps: semantic classes
`lusena-gap-kicker`, `lusena-gap-heading`, `lusena-gap-body`, `lusena-gap-cta`, `lusena-gap-cta-top`, `lusena-gap-section-intro`, `lusena-gap-subsection`

### Key spacing rules
1. Always use LUSENA classes, never hardcode spacing
2. When in doubt, go one tier up — premium feel means generous spacing
3. Prefer content-flow on parent over gap classes on children
4. Kicker+heading = wrap in `<div class="lusena-content-flow--tight lusena-gap-section-intro">`
5. Same-bg section gap is a floor (`max` formula), not additive — detector handles automatically
6. Snug-top modifier: use when hero has same bg as header

> Full specification: `memory-bank/doc/patterns/spacing-system.md`
> CSS source: `assets/lusena-foundations.css`

## Color scheme architecture

5 color schemes configured in Shopify admin:
| Scheme | Background | Usage |
|--------|------------|-------|
| scheme-1 | #F7F5F2 (brand-bg) | Default sections |
| scheme-2 | #F0EEEB (surface-2) | Alternating sections |
| scheme-3 | #2E2D2B | Dark accent sections |
| scheme-4 | #111111 | Full dark sections |
| scheme-5 | #8C6A3C (gold) | Gold accent sections |

## Animation conventions

- Scroll-reveal: Dawn's `scroll-trigger` system gated by `settings.animations_reveal_on_scroll`
- Pattern: `scroll-trigger animate--slide-in` (conditionally applied)
- Repeated items: `data-cascade` on container for stagger effect
- If element needs `transform` for layout, put scroll-trigger on a wrapper

## Component systems

- **Buttons:** `snippets/lusena-button-system.liquid` — primary, outline, ghost, text, link variants
- **Icons:** `snippets/lusena-icon.liquid` — centralized SVG rendering
- **Product cards:** `snippets/lusena-product-card.liquid`
- **Breadcrumbs:** `snippets/lusena-breadcrumbs.liquid`

> Full design tokens: `memory-bank/doc/patterns/brand-tokens.md`
