# Zwroty Final CTA Parity Plan (Draft shop -> Shopify theme)

Created: 2026-02-14  
Status: Planned  
Owner: Codex

## Goal

Adjust only the `/zwroty` section segment with the heading "Wypróbuj Przez 60 Nocy" so it matches the draft shop fragment at mobile and desktop breakpoints.

Parity for this fragment means matching:
- Typography scale and hierarchy (icon -> heading -> body -> actions).
- CTA layout and spacing rhythm.
- Button/link visual treatment and interactive states.
- Accent background treatment and white opacity text treatment.

## Scope

### In scope
- Update `sections/lusena-returns-final-cta.liquid` markup/CSS to draft-equivalent values.
- Keep all copy editable via section settings.
- Keep current Dawn reveal-on-scroll behavior for this section.
- Preserve existing link-based fallback behavior (hide action when link is blank).

### Out of scope
- Other `/zwroty` sections (`hero`, `steps`, `editorial`, `faq`).
- Global button system refactors outside this section.
- Template composition changes in `templates/page.zwroty.json`.

## Source of truth (Draft shop)

- `lusena-shop/src/pages/Returns.tsx` (final CTA block, lines 314-347).
- `lusena-shop/src/components/ui/button.tsx` (button variant + size classes used by CTA actions).
- `lusena-shop/src/index.css` and resolved utility tokens in theme equivalents.

## Target in theme (Shopify)

- `sections/lusena-returns-final-cta.liquid`
- `templates/page.zwroty.json` (confirms this section is in live page path)

## Decisions (final) - 2026-02-14

1. Match draft visual behavior exactly for this fragment, while keeping existing section setting fields unchanged.
2. Keep theme breakpoint strategy (`md` at `768px`) and reveal-on-scroll gate via `settings.animations_reveal_on_scroll`.
3. Prefer section-scoped semantic CSS for exact values; do not add new global utility backfills unless strictly required.

## Open questions / unresolved assumptions

None.

## Data sources & content model

- Copy is sourced from section settings:
  - `heading_line_1`, `heading_line_2`, `body`, `primary_button_label`, `secondary_button_label`.
- Links are sourced from:
  - `primary_button_link`, `secondary_button_link`.
- Fallback behavior:
  - Hide a CTA action if either label or link is blank.
- Translation strategy:
  - Keep current editable section settings model (no locale-key migration in this task).

## Target UX spec (Desktop + Mobile)

### Desktop (~1280px)
- Accent CTA band with centered content in `max-w-3xl`.
- 48x48 icon circle (`white/10`) above heading.
- Heading with first line regular + second line italic, larger desktop type scale.
- Body in `white/80`, readable width (`max-w-xl`), relaxed line-height.
- Two actions in one row: primary white-filled button + muted text link.

### Mobile (~390px)
- Same visual hierarchy with stacked actions.
- Heading wraps cleanly across lines and keeps strong emphasis.
- Tap targets remain at least 44px for primary action.

### Accessibility
- Keep semantic links for actions.
- Preserve visible focus styles for keyboard users.
- Preserve sufficient contrast on accent background.

## Theme capability & conflict audit

| Capability / token | Draft source | Resolved draft value | Exists in theme? | Conflict detected? | Planned implementation path | Target file |
|---|---|---|---|---|---|---|
| Accent section background | Returns CTA block | `bg-accent-cta` | Yes | No | Reuse existing class | `sections/lusena-returns-final-cta.liquid` |
| Icon circle | Returns CTA block | `48px`, `white/10`, fully rounded | Yes (via scoped css) | No | Keep scoped CSS | `sections/lusena-returns-final-cta.liquid` |
| Heading scale | `Returns.tsx` | mobile `3rem` (`text-3xl`), desktop `4.8rem` (`md:text-5xl`) | Yes | No | Reuse existing utility classes | `sections/lusena-returns-final-cta.liquid` |
| Body tone | Returns CTA block | `white/80` | No utility (`text-white/80`) | No | Keep scoped CSS color | `sections/lusena-returns-final-cta.liquid` |
| Primary CTA look | `Returns.tsx` + `button.tsx` | `h-12 px-8 py-3`, rounded-brand, focus ring, white bg/accent text, hover white/90 | Partial | No | Match full button class stack from draft equivalent | `sections/lusena-returns-final-cta.liquid` |
| Secondary CTA look | `Returns.tsx` + `button.tsx` | text-variant button base + `text-white/80 hover:text-white` | Partial | No | Keep semantic link with button base states and scoped color class | `sections/lusena-returns-final-cta.liquid` |
| CTA spacing rhythm | Returns CTA block | heading/body/actions cadence with larger desktop emphasis | Partial | No | Adjust section-local spacing classes/CSS | `sections/lusena-returns-final-cta.liquid` |

Audit rules:
- No conflicting typography classes on heading.
- Keep section-local styling for non-reusable values.
- Reuse existing button/focus classes where available.

## Parity contract table

| Selector / element | Property | Draft value | Theme target value | State | Breakpoint | Tolerance |
|---|---|---|---|---|---|---|
| `.lusena-returns-final-cta` | `background-color` | `rgb(14 94 90)` | `rgb(14 94 90)` | default | all | exact |
| `.lusena-returns-final-cta__icon-wrap` | `width/height` | `48px / 48px` | `48px / 48px` | default | all | exact |
| `.lusena-returns-final-cta__heading` | `font-size` | `3rem` mobile, `4.8rem` desktop | same | default | mobile/desktop | exact |
| `.lusena-returns-final-cta__body` | `color` | `rgba(255,255,255,0.8)` | same | default | all | exact |
| `.lusena-returns-final-cta__primary` | `size + radius + colors` | `h-12 px-8 py-3`, rounded-brand, white / accent | same | default | all | exact |
| `.lusena-returns-final-cta__primary` | `background-color` | `white/90` | `white/90` | hover | all | exact |
| `.lusena-returns-final-cta__secondary-link` | `color` | white/80 -> white | white/80 -> white | hover | all | exact |

## State fixture matrix

| State | Required fixture/data | Expected UI/UX |
|---|---|---|
| Empty | primary or secondary link blank | Missing action is hidden; layout remains balanced |
| Populated | default content present | Full CTA hierarchy and both actions visible |
| Active/Selected | keyboard focus on actions | Focus ring visible and non-clipped |
| Hover | desktop pointer on actions | Primary darkens to white/90; secondary text becomes white |
| Disabled | not applicable (links) | no disabled state required |
| Loading | not applicable | no loading state required |
| Error | malformed copy in settings | safe text render, no layout break |
| Success | valid links/copy | navigation works and visual parity holds |
| Long content | long body copy | wraps within max width, no overlap |

## Implementation approach

1. Update section markup with semantic hook classes for heading and primary CTA.
2. Adjust scoped CSS for exact heading scale and spacing rhythm parity.
3. Align both CTA class stacks with draft-equivalent button base (`button.tsx`) while preserving current links/settings.

Implementation rules:
- Modify only `sections/lusena-returns-final-cta.liquid`.
- Keep current schema fields unchanged.
- Keep reveal-on-scroll conditional classes.

## Milestones / deliverables

1. Plan approved by user.
2. Section implementation completed.
3. Shopify `validate_theme` passes for touched file(s).
4. User confirms visual parity at mobile and desktop.

## Verification checklist (developer pre-check)

### Computed-style checks

Breakpoints:
- Mobile: ~390px
- Desktop: ~1280px

Check:
- heading font-size/line-height
- spacing between icon, heading, body, actions
- primary and secondary CTA colors
- icon circle dimension and opacity

### Behavior checks

- Primary and secondary links navigate correctly.
- Hover and focus states match the parity contract.
- Section remains centered and readable with long body text.

## Verification checklist (user visual confirmation)

1. Compare the "Wypróbuj Przez 60 Nocy" segment against draft on ~390px and ~1280px.
2. Confirm heading scale, CTA spacing, and button/link styles.
3. Confirm hover/focus behavior on both actions.
4. Report any mismatch with screenshot + viewport width.

## Risks / edge cases

- Existing in-repo `/zwroty` worktree edits may impact this fragment's final appearance.
- Existing page-level CSS could influence spacing in edge contexts.
- Theme editor overrides may alter section settings and affect visual parity.

## Validation and wrap-up

- Shopify Dev MCP `validate_theme`: pending
- Files to include in summary:
  - `sections/lusena-returns-final-cta.liquid`
  - `docs/Page_Zwroty_Final_CTA_Parity_Plan.md`
- Optional after approval:
  - Update `docs/THEME_CHANGES.md`
  - Create commit
