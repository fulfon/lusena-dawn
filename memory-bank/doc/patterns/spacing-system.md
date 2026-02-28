# LUSENA Spacing System (Quick Reference)

> CSS source of truth: `assets/lusena-foundations.css`
> Values below are from the foundations file (8px baseline grid, all values in px for readability).

## Tier selection cheat-sheet

| Section role | Recommended tier | Mobile | Desktop |
|-------------|-----------------|--------|---------|
| Full-width media | `lusena-spacing--full-bleed` | 0 | 0 |
| Trust bar / utility bar | `lusena-spacing--compact` | 32px | 48px |
| Content / info sections | `lusena-spacing--standard` | 48px | 64px |
| CTA / conversion sections | `lusena-spacing--spacious` | 64px | 96px |
| Hero / banner | `lusena-spacing--hero` | 80px | 128px |

Modifier: `lusena-spacing--snug-top` — reduces top to 32/48px for heroes sharing bg with header.

## Content-flow selection

| Class | Gap | When to use |
|-------|-----|-------------|
| `lusena-content-flow--tight` | 16px | Kicker + heading pairs, section intros |
| `lusena-content-flow` | 24px | Standard containers, body text flow |
| `lusena-content-flow--relaxed` | 32px | Hero text columns, editorial blocks |

Note: `lusena-content-flow` is spacing-only (no flex). Use `lusena-stack` for flex-col + spacing.

## Gap classes

| Class | Gap | Usage |
|-------|-----|-------|
| `lusena-gap-kicker` | 8px | Below kicker text (includes `display: block`) |
| `lusena-gap-heading` | 24px | Below headings |
| `lusena-gap-body` | 24px | Below body text |
| `lusena-gap-cta` | 32px | Below CTA buttons |
| `lusena-gap-cta-top` | 32px | Above CTA buttons |
| `lusena-gap-section-intro` | 32px | Below section intro block |
| `lusena-gap-subsection` | 64px | Between major content breaks |

## Key rules (abbreviated)

1. **Always use LUSENA classes** — never hardcode spacing
2. **When in doubt, go one tier up** — premium feel means generous spacing
3. **Prefer content-flow on parent** over individual gap classes on children
4. **Kicker+heading pattern:** always wrap in `<div class="lusena-content-flow--tight lusena-gap-section-intro">`
5. **Same-bg section gap** is a floor (max formula), not additive — detector handles automatically
6. **Snug-top modifier** (`lusena-spacing--snug-top`): use when hero has same bg as header
7. **CTA visibility:** use `lusena-gap-cta-top` for conditionally visible CTA elements
