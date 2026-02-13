# PDP Value Props Parity Plan (Draft shop → Shopify theme)

Date: 2026-02-09

## Goal

Port the PDP fragment containing:

1) The 6 “feature highlight” cards:
- “Mniej zmarszczek, więcej blasku…”
- “22 momme — o 30% gęstszy niż standard…”
- “OEKO-TEX® Standard 100…”
- “Gotowe na prezent…”
- “Proste pranie w pralce…”
- “Włosy bez puszenia i łamania…”

2) The “Dlaczego LUSENA?” expandable stack (4 items):
- “OEKO-TEX® Standard 100…”
- “Jedwab z Suzhou — 600 lat tradycji…”
- “22 momme — optymalny standard…”
- “Kontrola jakości w Polsce + wysyłka 24h…”

…from `lusena-shop/` into the Shopify theme product page (PDP) with 1:1 visual parity on mobile and desktop.

## Scope

- Match layout, spacing, typography sizes/weights, colors, border radius, and interactions (open/close behavior + chevron rotation + animation timing/feel).
- Match breakpoints used by the draft fragment (Tailwind `sm/md/lg`), not Dawn defaults.
- Keep content in Polish exactly as in the draft fragment (including punctuation and dash characters).

## Non-goals

- Rebuilding unrelated PDP areas (gallery, buy box, reviews, cross-sell).
- Introducing new content models beyond what’s required for this fragment.
- Changing global theme typography/colors outside what’s needed for parity.

## Source of truth (draft shop)

Feature highlights (content + icon mapping):
- `lusena-shop/src/lib/products.ts` (PILLOWCASE `features[]`)
- `lusena-shop/src/components/product/FeatureHighlights.tsx` (markup + Tailwind classes)

Quality evidence (content + interaction model):
- `lusena-shop/src/lib/pdp-content.ts` (`QUALITY_EVIDENCE`)
- `lusena-shop/src/components/product/QualityEvidenceStack.tsx` (markup + JS state + Tailwind classes)

Design tokens / breakpoints:
- `lusena-shop/tailwind.config.js` (colors, container padding, breakpoints)

## Target in theme (Shopify)

Where it must appear:
- PDP template: `templates/product.json`
- Existing main PDP section: `sections/lusena-main-product.liquid`

Planned landing:
- Add two new PDP sections referenced by `templates/product.json` directly after `main`:
  - `sections/lusena-pdp-feature-highlights.liquid`
  - `sections/lusena-pdp-quality-evidence.liquid`

Rationale: keeps the fragment isolated and allows strict parity without touching `lusena-main-product` internals.

## Decisions (final)

- Breakpoints: match the draft (Tailwind): `sm=640px`, `md=768px`, `lg=1024px`, `xl=1280px`.
- Container: use the same “container” behavior as the theme’s Tailwind utilities (already present in `assets/lusena-shop.css`).
- Content model:
  - Feature Highlights: always 6 cards, but per-product title/body/icon can differ.
  - Implement Feature Highlights as section blocks with draft defaults, with optional per-product overrides via product metafields (so one shared template still supports per-product copy).
  - “Dlaczego LUSENA?”: same across products using `templates/product.json`.
- Accordion behavior: single-open stack (at most 1 expanded), default state = all collapsed.
- Animations: follow Dawn/LUSENA convention but only when enabled:
  - Feature cards + evidence rows get `{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}`.
  - Containers get `data-cascade` only when the setting is enabled.
- “Dlaczego LUSENA?” CTAs are links:
  - “Sprawdź certyfikat →” opens the same PDF as “Pobierz Certyfikat (PDF)” on `/pages/nasza-jakosc` (use `shop.metafields.lusena.oeko_tex_certificate` when present; otherwise fall back to `/pages/nasza-jakosc`).
  - “Więcej o pochodzeniu →” → `/pages/o-nas`
  - “Porównaj momme →” → `/pages/nasza-jakosc`
  - “Więcej o nas →” → `/pages/nasza-jakosc`

## Data sources & content model

### Feature highlights section

- Section blocks: 6× “feature” blocks.
- Block settings:
  - `icon` (select): `sparkles`, `wind`, `shield-check`, `gift`, `droplets`, `heart` (plus any already supported by `snippets/lusena-icon.liquid`; unknown keys fall back to `sparkles`)
  - `title` (text)
  - `description` (textarea)

Per-product overrides (recommended implementation detail):
- Use product metafields as overrides (namespace `lusena`, keys below). If present, they take precedence over block settings; otherwise block settings render the draft default copy.
- Rationale: for a fixed-size (always 6) per-product set, product metafields are the fastest to configure in Shopify and require the least ongoing maintenance. Metaobjects become worth it when you need variable-length lists, reuse across many products, or richer validation/workflows.
- Metafield keys (all optional; type recommendation in parentheses):
  - `lusena.pdp_feature_1_icon` (single line text, e.g. `sparkles`)
  - `lusena.pdp_feature_1_title` (single line text)
  - `lusena.pdp_feature_1_description` (multi-line text)
  - …
  - `lusena.pdp_feature_6_icon`
  - `lusena.pdp_feature_6_title`
  - `lusena.pdp_feature_6_description`

### Quality evidence section

- Section setting:
  - `heading` default: `Dlaczego LUSENA?`
- Section blocks: 4× “evidence” blocks.
- Block settings:
  - `icon` (select): `shield-check`, `map-pin`, `layers`, `package`
  - `title` (text)
  - `summary` (textarea)
  - `detail` (textarea)
  - `cta_label` (text)

## Target UX spec (must match draft)

### Feature highlights (grid)

Markup / classes (draft reference: `FeatureHighlights.tsx`):
- Section padding: `py-16 md:py-24` (64px / 96px)
- Grid: `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`
- Gaps: `gap-8 lg:gap-12` (32px / 48px)
- Card spacing: `space-y-3`
- Icon bubble: `w-10 h-10 rounded-full bg-surface-2` with inner icon `w-5 h-5 text-accent-cta` and `strokeWidth=1.5`
- Title: `font-serif text-[20px] leading-[28px] text-primary`
- Body: `text-sm text-secondary leading-relaxed`

### Quality evidence (expandable stack)

Markup / classes (draft reference: `QualityEvidenceStack.tsx`):
- Section: `py-16 md:py-24 bg-brand-bg`
- Heading: centered, `text-[24px] md:text-[28px] md:leading-[36px] font-serif text-primary mb-12`
- Stack container: `max-w-3xl mx-auto space-y-4`
- Item wrapper: `bg-surface-2 rounded-sm overflow-hidden`
- Toggle button row:
  - `w-full flex items-start gap-4 p-5 md:p-6 text-left`
  - hover: `hover:bg-surface-2/80` + `transition-colors duration-150`
  - icon bubble: `w-10 h-10 rounded-full bg-brand-bg ... shrink-0 mt-0.5`
  - chevron: `w-5 h-5 text-secondary/50 ... transition-transform duration-200` rotates 180° when open
- Expand area animation:
  - wrapper: `overflow-hidden transition-all duration-300`
  - open: `max-h-[500px] opacity-100`
  - closed: `max-h-0 opacity-0`
- Expand content: `px-5 md:px-6 pb-5 md:pb-6 pl-[4.5rem]`
- CTA: `text-xs text-accent-cta font-medium hover:underline`

## Implementation approach

Planned files to add/change:
- Add `sections/lusena-pdp-feature-highlights.liquid`
- Add `sections/lusena-pdp-quality-evidence.liquid`
- Update `templates/product.json` to include the new sections in order after `main`
- Update `snippets/lusena-icon.liquid` to include missing icons used by the fragment:
  - `sparkles`, `wind`, `droplets`, `heart`, `map-pin`, `package`

JS strategy for accordion:
- Use a small section-scoped script to handle:
  - toggle click
  - single-open behavior
  - applying/removing the open/closed classes matching the draft
  - setting `aria-expanded`
  - rotating the chevron via class toggle (exact class parity)

CSS strategy:
- Prefer reusing existing utility classes from `assets/lusena-shop.css` (already present in theme).
- Only add minimal bespoke CSS if a draft behavior can’t be expressed via existing utilities.

## Milestones / deliverables

1) Theme sections render with correct content defaults (no missing icons).
2) Interactions match (open/close + transitions + keyboard focus).
3) Template updated so the fragment appears in the same PDP location as draft.
4) Theme validates cleanly with Shopify Dev MCP `validate_theme`.

## Verification checklist

Manual (must check both):
- Mobile ~390px wide:
  - feature grid is 1 column, gaps/padding match
  - accordion stack spacing + open/close animation matches
- Desktop ~1280px wide:
  - feature grid is 3 columns
  - typography sizes match (H2 28px, cards 20px titles)
  - brand background + surface colors match
- Interaction:
  - only one evidence row open at a time
  - chevron rotates and transitions
  - `aria-expanded` reflects state

Optional (when needed):
- Playwright parity pass against `http://127.0.0.1:9292/` once the theme is running.

## Risks / edge cases

- Icon set mismatch: if `snippets/lusena-icon.liquid` lacks an icon, parity breaks; handle by extending the snippet.
- Theme setting `animations_reveal_on_scroll`: verify it doesn’t materially change parity when enabled; keep it strictly gated.
