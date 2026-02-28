# System Patterns

## CSS Architecture

### Layer stack (loading order in layout/theme.liquid)
1. **Inline font-faces & root CSS** — Custom fonts (Inter, Source Serif 4), CSS custom properties, base styles
2. **Dawn base:** `assets/base.css` (3,641 lines) — Foundation styles
3. **Tailwind compiled:** `assets/lusena-shop.css` (26KB) — Brand utilities, Tailwind classes
4. **Spacing system:** `assets/lusena-spacing.css` (266 lines) — LUSENA spacing tokens (source of truth)
5. **Global snippets:** `lusena-missing-utilities`, `lusena-button-system`, `lusena-spacing-system`
6. **Component styles:** `{% stylesheet %}` blocks in sections/snippets → compiled into `compiled_assets/styles.css`

### Key constraint
`{% stylesheet %}` blocks have ~73KB cumulative limit (`compiled_assets/styles.css` truncation). Spacing CSS MUST go in `assets/lusena-spacing.css`, NOT in `{% stylesheet %}` blocks.

> Full CSS architecture details: `memory-bank/doc/patterns/css-architecture.md`

## Naming conventions

- All LUSENA files: `lusena-*` prefix
- Sections: `sections/lusena-{component}.liquid`
- Snippets: `snippets/lusena-{component}.liquid`
- Assets: `assets/lusena-{name}.{css|js}`
- CSS classes: `lusena-spacing--*`, `lusena-content-flow*`, `lusena-gap-*`, `lusena-btn*`
- CSS variables: `--lusena-space-*`, `--lusena-section-*`, `--lusena-tier-*`

## Spacing system (LUSENA is source of truth, NOT Dawn)

### Section padding: tier classes
| Tier | Mobile | Desktop | Usage |
|------|--------|---------|-------|
| `lusena-spacing--full-bleed` | 0 | 0 | Edge-to-edge media |
| `lusena-spacing--compact` | 32px | 48px | Utility sections (trust bar) |
| `lusena-spacing--standard` | 40px | 64px | Informational content |
| `lusena-spacing--spacious` | 48px | 80px | Trust-building, CTAs |
| `lusena-spacing--hero` | 64px | 96px | Hero sections |

### Container rhythm: content-flow utilities
- `lusena-content-flow` — 20/24px (standard)
- `lusena-content-flow--tight` — 12/16px (kicker + heading pairs)
- `lusena-content-flow--relaxed` — 28/32px (hero/editorial)

### Element gaps: semantic classes
`lusena-gap-kicker`, `lusena-gap-heading`, `lusena-gap-body`, `lusena-gap-cta`, `lusena-gap-cta-top`, `lusena-gap-section-intro`, `lusena-gap-subsection`

### Key spacing rules
1. Always use LUSENA classes, never hardcode Tailwind spacing
2. When in doubt, go one tier up
3. Prefer content-flow on parent over gap classes on children
4. Kicker+heading = wrap in `<div class="lusena-content-flow--tight lusena-gap-section-intro">`
5. Same-bg section gap is a floor (`max` formula), not additive

> Full specification: `memory-bank/doc/patterns/spacing-system.md`
> CSS source: `assets/lusena-spacing.css`
> Skill: `.claude/skills/lusena-spacing/SKILL.md`

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
