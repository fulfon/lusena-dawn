# Zwroty Page Parity Plan (Draft shop -> Shopify theme)

Created: 2026-02-13  
Status: Planned  
Owner: Codex

## Goal

Copy the full `/zwroty` page from the draft shop into the Shopify theme with near 1:1 visual and interaction parity at mobile and desktop breakpoints.

Parity means matching:
- Section structure and order from draft (`hero -> steps -> editorial compare -> faq -> final cta`).
- Typography scale, spacing rhythm, iconography, and color treatment.
- Interaction behavior (accordion, hover states, and scroll-reveal motion policy in theme).

## Scope

### In scope
- Upgrade existing `page.zwroty` composition to include all draft sections.
- Match draft hero proof chips, badge treatment, and decorative background shield.
- Match 3-step cards (labels, icons, hover uplift, connector line on desktop).
- Add editorial comparison section ("why 60 days") with side-by-side rows.
- Match FAQ heading/kicker, accordion behavior, and contact action.
- Add final CTA section with two actions and supporting copy.
- Keep all user-facing content editable via section settings and blocks with draft defaults.

### Out of scope
- PDP "returns fragment" behavior (`product` page) already handled by a separate parity plan.
- Global navigation/footer changes unrelated to `/zwroty`.
- Replacing existing reusable icon system outside this page.

## Source of truth (Draft shop)

- `lusena-shop/src/pages/Returns.tsx`
- `lusena-shop/src/components/ui/Accordion.tsx`
- `lusena-shop/tailwind.config.js`
- `lusena-shop/src/index.css`

## Target in theme (Shopify)

- `templates/page.zwroty.json` (live page wiring)
- `sections/lusena-returns-hero.liquid`
- `sections/lusena-returns-steps.liquid`
- `sections/lusena-returns-faq.liquid`
- `sections/lusena-returns-editorial.liquid` (new)
- `sections/lusena-returns-final-cta.liquid` (new)
- `snippets/lusena-missing-utilities.liquid` (minimal utility backfills only where justified)
- `snippets/lusena-icon.liquid` (reuse existing icons; extend only if needed)

## Decisions (final) - 2026-02-13

1. Page architecture: keep modular section model and add missing sections to `page.zwroty` (`A`).
2. Motion model: use Dawn `scroll-trigger` reveal system only (`A`), no GSAP.
3. Content model: keep copy/settings editable in section schema with draft defaults (`A`).
4. Breakpoints: use theme/draft `md` strategy at `768px` (`A`).
5. FAQ interaction parity: implement single-open accordion behavior within section scope (draft-equivalent behavior) while keeping semantic `<details>` structure.

## Open questions / unresolved assumptions

None.

## Data sources & content model

- Content source is section settings + blocks in `templates/page.zwroty.json`.
- Hero proof chips: block-based or list settings in `lusena-returns-hero`.
- Steps: block-based with icon selector mapped to `lusena-icon` names (`shopping-bag`, `mail`, `banknote`/equivalent), plus label/title/text.
- Editorial compare rows: block-based with `standard` and `lusena` strings.
- FAQ: block-based question/answer richtext plus optional contact CTA link.
- Final CTA: heading/body/buttons from settings.
- Fallback behavior:
  - If optional link is blank, corresponding button is hidden.
  - If no blocks in repeatable sections, section still renders heading and avoids broken layout.
- Translation strategy:
  - Keep page copy editable in settings (consistent with current LUSENA page sections).
  - No new locale keys required for this migration.

## Target UX spec (Desktop + Mobile)

### Desktop (~1280px)
- Hero:
  - `py-24 md:py-32`, centered content (`max-w-4xl`), decorative shield watermark behind content.
  - Kicker, 2-line heading with italic second line, body copy, proof chips row, rounded badge.
- Steps:
  - 3 columns, card surface style with subtle hover lift.
  - Dashed connector line at card icon row height.
  - Each step has `Krok N` label, icon circle, title, description.
- Editorial compare:
  - 2-column layout (`lg:grid-cols-2`), narrative text left, comparison rows right.
  - Header labels "Standard rynkowy" vs "LUSENA", row styling with neutral vs accent surfaces.
- FAQ:
  - Kicker + heading, white card container, single-open accordion feel.
  - Contact prompt and outline button.
- Final CTA:
  - Full-width accent background, centered heading/body, primary and secondary actions.

### Mobile (~390px)
- Same section order as desktop.
- Hero remains centered; proof chips wrap.
- Steps collapse to one column with no connector line.
- Editorial becomes one column with narrative above comparison rows.
- FAQ and CTA keep spacing hierarchy and tap targets >= 44px.

### Accessibility

- Interactive controls use semantic elements (`summary`, `a`, `button` when appropriate).
- Icons are decorative (`aria-hidden`) unless explicitly labeled.
- Visible focus styles preserved (`focus-visible` ring classes/patterns).
- Accordion supports keyboard via native details/summary semantics.
- Reduced motion respected by theme baseline and avoiding custom heavy motion.

## Theme capability & conflict audit

| Capability / token | Draft source | Resolved draft value | Exists in theme? | Conflict detected? | Planned implementation path | Target file |
|---|---|---|---|---|---|---|
| `text-4xl` | `Returns.tsx` hero title | `3.6rem / 4rem` | Yes | No | Reuse utility | `sections/lusena-returns-hero.liquid` |
| `md:text-6xl` | `Returns.tsx` hero title | `6rem / 1` | No | No | Minimal utility backfill | `snippets/lusena-missing-utilities.liquid` |
| `py-24 md:py-32` | all major sections | `9.6rem / 12.8rem` | Yes | No | Reuse existing classes | `sections/lusena-returns-*.liquid` |
| `rounded-brand-lg` | step cards | `8px` | No | No | Minimal utility backfill | `snippets/lusena-missing-utilities.liquid` |
| `max-w-6xl` | editorial container | `72rem` | No | No | Minimal utility backfill | `snippets/lusena-missing-utilities.liquid` |
| `bg-accent-cta/10` | compare row icon dot | `rgba(14,94,90,0.1)` | No | No | Minimal utility backfill | `snippets/lusena-missing-utilities.liquid` |
| `bg-accent-cta/5` | compare row background | `rgba(14,94,90,0.05)` | No | No | Minimal utility backfill | `snippets/lusena-missing-utilities.liquid` |
| `border-accent-cta/10` | compare row border | `rgba(14,94,90,0.1)` | No | No | Minimal utility backfill | `snippets/lusena-missing-utilities.liquid` |
| `text-white/80` | final cta body/button text | `rgba(255,255,255,0.8)` | No | No | Minimal utility backfill | `snippets/lusena-missing-utilities.liquid` |
| `bg-white/10` | final cta icon circle | `rgba(255,255,255,0.1)` | No | No | Minimal utility backfill | `snippets/lusena-missing-utilities.liquid` |
| `w-7 h-7` | step icons | `1.75rem` | No | No | Minimal utility backfill | `snippets/lusena-missing-utilities.liquid` |
| `backdrop-blur-md` | hero badge | `blur(12px)` | No | No | Scoped semantic CSS class | `sections/lusena-returns-hero.liquid` |
| `w-[28rem] h-[28rem]` | hero background shield | `28rem` | No | No | Scoped semantic CSS class | `sections/lusena-returns-hero.liquid` |
| `opacity-[0.03]` | hero background shield | `0.03` | No | No | Scoped semantic CSS class | `sections/lusena-returns-hero.liquid` |
| `left-[20%] right-[20%] top-16 border-dashed` | steps connector line | `20% offsets, 4rem top, dashed line` | No | No | Scoped semantic CSS class | `sections/lusena-returns-steps.liquid` |
| `lg:grid-cols-2` | editorial layout | 2 columns at `>=1024px` | No | No | Scoped semantic CSS grid rule | `sections/lusena-returns-editorial.liquid` |
| Icon set (`ShieldCheck`, `ShoppingBag`, `Mail`, `RotateCcw`, `Clock`, `ArrowRight`) | `Returns.tsx` | Lucide-like strokes | Partial | Yes (emoji fallback mismatch) | Reuse/extend `lusena-icon`; remove emoji dependency for parity | `snippets/lusena-icon.liquid` + returns sections |
| Accordion behavior (`single`, `collapsible`) | `Accordion.tsx` | one-open-at-a-time | Partial | Yes (current multi-open `<details>`) | Add section-scoped JS to close siblings on open | `sections/lusena-returns-faq.liquid` |

Audit rules applied:
- Resolved source utility values before planning Liquid port.
- No conflicting utility composition carried over.
- Scoped CSS preferred for one-off arbitrary values; utility backfill limited to reusable tokens.

## Parity contract table

| Selector / element | Property | Draft value | Theme target value | State | Breakpoint | Tolerance |
|---|---|---|---|---|---|---|
| `.lusena-returns-hero__title` | `font-size` | `3.6rem` / `6rem` | `3.6rem` / `6rem` | default | mobile/desktop | exact |
| `.lusena-returns-hero__badge` | `backdrop-filter` | `blur(12px)` | `blur(12px)` | default | all | exact |
| `.lusena-returns-hero__proof-chip` | `gap` | `0.5rem` | `0.5rem` | default | all | exact |
| `.lusena-returns-steps__card` | `border-radius` | `8px` | `8px` | default | all | exact |
| `.lusena-returns-steps__card` | `transform` | `translateY(-0.4rem)` on hover | same | hover | desktop | exact |
| `.lusena-returns-steps__connector` | `border-style` | `dashed` | `dashed` | default | desktop | exact |
| `.lusena-returns-editorial__grid` | `grid-template-columns` | `1fr 1fr` | `1fr 1fr` | default | desktop | exact |
| `.lusena-returns-compare__lusena` | `background-color` | `accent-cta/5` | `accent-cta/5` | default | all | exact |
| `.lusena-returns-faq__item[open]` | open policy | single item open | single item open | interaction | all | exact |
| `.lusena-returns-final-cta` | `background-color` | `accent-cta` | `accent-cta` | default | all | exact |
| `.lusena-returns-final-cta__body` | `color` | `white/80` | `white/80` | default | all | exact |
| `.lusena-returns-final-cta__primary` | bg/fg | white / accent-cta | white / accent-cta | hover/default | all | exact |

## State fixture matrix

| State | Required fixture/data | Expected UI/UX |
|---|---|---|
| Empty | No blocks in steps/editorial/faq | Section headings remain; no broken layout; optional block areas collapse cleanly |
| Populated | Default draft-like content | Full visual parity for all sections |
| Active/Selected | Open one FAQ item | Open item content visible, chevron rotated, other items closed |
| Hover | Desktop pointer over step cards/buttons | Card lift, button hover colors match draft |
| Disabled | Missing optional links | Related button/link hidden, no dead targets |
| Loading | Not applicable (static page) | No loading spinners required |
| Error | Invalid/missing richtext in block | Section renders safely without Liquid errors |
| Success | Valid full content | Page matches draft and interactions pass |
| Long content | Very long FAQ answer/title | Text wraps without overlap; spacing remains readable |

## Implementation approach

1. Extend `templates/page.zwroty.json` section order to include new `returns_editorial` and `returns_final_cta`.
2. Upgrade `sections/lusena-returns-hero.liquid`:
   - add decorative shield, proof chip row, icon-based badge, and scoped classes for one-off values.
3. Upgrade `sections/lusena-returns-steps.liquid`:
   - add step label, icon rendering via `lusena-icon`, card styling parity, and dashed connector line.
4. Add `sections/lusena-returns-editorial.liquid` (new):
   - narrative column + comparison matrix with block-driven rows and quality-page style CTA link.
5. Upgrade `sections/lusena-returns-faq.liquid`:
   - add kicker, include 5th FAQ default item, and add scoped JS for single-open behavior.
6. Add `sections/lusena-returns-final-cta.liquid` (new):
   - accent background hero-cta with primary/secondary actions.
7. Add only required reusable missing utilities in `snippets/lusena-missing-utilities.liquid`; keep one-off arbitrary values in scoped section CSS.

Implementation rules:
- Modify only the code path used by `templates/page.zwroty.json`.
- Keep JS hooks stable (`data-*` selectors) and scoped to returns page sections.
- Preserve semantic HTML and keyboard behavior.
- Keep all user-facing content editable in schema defaults aligned to draft.

## Milestones / deliverables

1. Plan approved by user.
2. Returns page section architecture updated (`hero`, `steps`, `editorial`, `faq`, `final cta`).
3. Visual/token parity applied with scoped CSS and minimal utility backfills.
4. Shopify `validate_theme` passes for all touched files.
5. User visual parity confirmation at mobile and desktop.

## Verification checklist (developer pre-check)

### Computed-style checks

Breakpoints:
- Mobile: ~390px
- Desktop: ~1280px

Check for critical selectors:
- font-size
- line-height
- spacing (margin/padding/gap)
- dimensions (width/height/min/max)
- alignment (text-align, align-items, justify-content)
- visibility/display in each state

### Behavior checks

- FAQ opens one item and closes others.
- Steps card hover lift only on pointer devices.
- CTA buttons route correctly (`/collections/all`, contact email/page).
- No overlap or clipping in long text variants.

## Verification checklist (user visual confirmation)

1. Compare draft vs theme `/zwroty` at ~390px and ~1280px.
2. Confirm spacing/typography/colors and icon styles match.
3. Confirm interactions (FAQ open/close, links, button hovers) match.
4. Report mismatches with screenshot + viewport.

## Risks / edge cases

- `templates/page.zwroty.json` is auto-generated and can be overwritten in Theme Editor.
- Missing utility tokens can silently regress styling if not backfilled or scoped correctly.
- Existing `sections/lusena-page-returns.liquid` is legacy and unused; avoid accidental edits to non-live path.
- Richtext answers may include markup that changes line-height rhythm; test with long content.

## Validation and wrap-up

- Shopify Dev MCP `validate_theme`: pending
- Files to include in summary:
  - `templates/page.zwroty.json`
  - `sections/lusena-returns-hero.liquid`
  - `sections/lusena-returns-steps.liquid`
  - `sections/lusena-returns-editorial.liquid`
  - `sections/lusena-returns-faq.liquid`
  - `sections/lusena-returns-final-cta.liquid`
  - `snippets/lusena-missing-utilities.liquid`
- Optional after approval:
  - Update `docs/THEME_CHANGES.md`
  - Create commit
