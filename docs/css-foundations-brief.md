# LUSENA CSS Foundations — Designer Brief

> **Date:** 2026-02-28
> **Your deliverable:** One CSS file (`lusena-foundations.css`) that defines the complete visual system for the LUSENA online store.

---

## 1. The brand

**LUSENA** is a premium Polish silk e-commerce store. We sell silk pillowcases, bonnets, scrunchies, eye masks, heatless curlers, and bundles — all focused on nighttime beauty routines.

**Positioning:** "The only complete nighttime beauty routine in 22 momme silk — pillowcases, hair protection and accessories from Suzhou, Silk Capital since the 15th century."

**Target customer:** Polish women aged 25–50. Four personas:
- "Seeks quality for years" (25–45) — premium, durable investment buyer
- "Perfect gift" (22–55) — wants an impressive, luxurious first impression
- "Hair/skin care enthusiast" (18–40) — wants visible results, reduced friction
- "Minimalist aesthete" (20–50) — refined, timeless design

**Key customer concerns:** "Is this real silk?", "Is the price worth it?", "Are the results real?" — the store must build trust before asking for the purchase.

**Brand personality:** Expert, empathetic, subtly luxurious, precise, calm. The archetype is Mentor/Caregiver with an Alchemist nuance (knowledge + transformation through material). Think high-end skincare brand, not fashion hype.

What that means for design:
- **Expert** — clean data presentation, structured layouts, clear hierarchy
- **Empathetic** — approachable spacing, readable text, nothing intimidating
- **Subtly luxurious** — generous whitespace, restrained accents, details in finishing touches (not in flashiness)
- **Precise** — tight alignment, consistent rhythm, nothing "approximately" placed
- **Calm** — quiet animations, no aggressive attention grabs, breathing room everywhere

**Taglines (Polish):**
- Primary (brand): "Urodę Tworzysz w Nocy." (Beauty Happens at Night) — used in heroes, key visuals
- Secondary (product): "22 momme. Gęstość, którą poczujesz." (22 momme. Density you can feel.) — used near products, comparisons
- Tertiary (action): "Obudź się piękniejsza." (Wake up more beautiful.) — used in CTAs, ads

**Tone rules:** No exclamation marks in headings. Sentence case everywhere. Proof-first messaging (evidence before emotion). Never more than 2 CTAs per viewport. All customer-facing content is in Polish; code/comments in English.

**Products (ordered by strategic importance):**

| Tier | Product | Role |
|------|---------|------|
| 1 (flagship) | Silk pillowcase 50x60 | Premium anchor, hero product |
| 1 (flagship) | Silk scrunchies | Conversion accelerator, entry price point |
| 2 (growth) | Silk bonnet | Hair care narrative, bundle partner |
| 2 (growth) | Heatless curler | Content hero, UGC driver |
| 3 (addon) | Silk eye mask | Bundle addon, never solo hero |
| — | Bundles (Night Routine, Starter Kit, Scrunchie Trio) | AOV boosters, gift positioning |

---

## 2. The goal

This CSS file will be the **single source of truth** for the visual identity across the entire store. Every page — current and future — draws from this one file.

**Your mission:** Design the CSS visual system that makes this store as appealing, trustworthy, and conversion-effective as possible for our target customer. A woman lands on our store, browses products, reads about quality, and decides whether to buy. Your CSS shapes every moment of that journey.

Think about what makes a premium e-commerce experience feel premium:
- How typography creates hierarchy and guides the eye toward purchase decisions
- How spacing creates breathing room that communicates quality
- How subtle interactions (hovers, focus states, transitions) feel polished and intentional
- How the responsive experience feels native on mobile, not just "shrunk desktop"
- How consistent visual rhythm across pages builds subconscious trust
- How section patterns (heroes, trust bars, editorial blocks, CTAs) work as a cohesive system

**You have full creative freedom** over the visual system. Design the best foundations you can — typography scale, spacing rhythm, layout patterns, shadows, borders, transitions, hover states, section patterns, card components, responsive behavior. All of it.

---

## 3. What's locked (do not change)

Only two things are fixed — the brand colors and the font families. These are core brand decisions.

### Colors

**Primary palette (Route A — Porcelain + Ink + Teal CTA):**
Character: modern, calm, high readability. Designed for e-commerce and print.

| Token | Hex | Usage |
|-------|-----|-------|
| `--lusena-brand-bg` | `#F7F5F2` | Default page background — warm porcelain |
| `--lusena-surface-1` | `#FFFFFF` | White card/section backgrounds |
| `--lusena-surface-2` | `#F0EEEB` | Alternating section backgrounds |
| `--lusena-text-1` | `#111111` | Headings, primary dark text |
| `--lusena-text-2` | `#4A4A4A` | Body copy, captions, muted text |
| `--lusena-accent-cta` | `#0E5E5A` | ALL call-to-action buttons, links, active states |
| `--lusena-accent-2` | `#8C6A3C` | Badges, premium highlights (used sparingly — warm gold-bronze) |

**Full neutral scale (N0–N900):**

| Token | Hex |
|-------|-----|
| N0 | `#FFFFFF` |
| N50 | `#FAFAF8` |
| N100 | `#F2F2F0` |
| N200 | `#E6E4E2` |
| N300 | `#D4D2CF` |
| N400 | `#B9B7B4` |
| N500 | `#9B9996` |
| N600 | `#7B7976` |
| N700 | `#5A5855` |
| N800 | `#2E2D2B` |
| N900 | `#111111` |

**Status colors:**

| Token | Hex | Usage |
|-------|-----|-------|
| Success | `#2F7D4E` | In-stock indicators, confirmations |
| Warning | `#B7791F` | Alerts, low-stock notices |
| Error | `#B91C1C` | Out-of-stock, form errors |

**Overlay/scrim values:**

| Token | Value |
|-------|-------|
| Scrim 60% | `#11111199` |
| Scrim 80% | `#111111CC` |

**Color usage rules:**
- CTA color `#0E5E5A` is constant across the entire store. It never changes.
- Gold accent `#8C6A3C` only as a subtle highlight — badges, premium indicators. Never at the same visual weight as CTA.
- On dark backgrounds (footer, inverted sections): use white text on N800/N900 backgrounds.
- Overlays on hero images: scrim-60 or scrim-80 for text legibility.

### Font families

| Role | Font |
|------|------|
| Headings / brand voice | **Source Serif 4**, serif |
| Body / UI | **Inter**, sans-serif |

Fonts are loaded via Google Fonts in the HTML `<head>` — you don't need to handle `@font-face`. Just reference the families in your CSS.

**Typography philosophy:**
- Source Serif 4 for headings — elegant, with good Polish diacritics support
- Inter for body/UI — high readability, tabular lining numerals for prices
- Maximum 5 semantic type classes for the design system (e.g., hero, h1, h2, body, caption — don't create more). Inside `.lusena-richtext`, you will also need to style bare `<h1>`–`<h6>` elements — you can map multiple heading levels to the same visual style where appropriate.
- Italic usage: for quotes and brand tagline emphasis, never for CTAs
- Line height: minimum 1.4x for text blocks longer than 3 lines
- Tracking: headings 0 to +0.02em; body 0
- Prices and parameters should use tabular lining numerals

Everything else — sizes, weights, line heights, spacing, radii, shadows, transitions, layout grids, hover behaviors — is yours to design.

---

## 4. Brand design direction

These are the brand's visual principles. They describe the *feeling* we want — how you achieve it in CSS is your creative decision.

### Photography & imagery direction
The store uses calm, soft photography with macro shots of silk texture, close-ups of stitching detail, and porcelain/cream backgrounds. Lighting is soft (key softbox at 45 degrees), warm (5200–5600K). The "Imperfect Silk" principle: for every 3 catalog shots (perfectly pressed), there's one showing natural soft creases or movement — because real silk flows and catches light on folds (proving it's not plastic). Your CSS should complement this photography style — the visual system should feel warm, calm, and textured, not cold and clinical.

### Iconography style
Icons follow a consistent style: 24px grid, 1.5px stroke weight, rounded corners (2-4px), monochrome (N700 on light, white on dark). No gradients, no shadows, no mixed stroke weights. Your icon container/sizing classes should respect this system.

### Motion & animation principles
- UI interactions (hover, focus): 150–200ms
- Modals, drawers, heroes: 250–400ms
- Easing: calm ease-in-out. No bouncy/spring animations.
- CTA hover: subtle lightening of accent color (~8-12% brighter) + text underline. No shadows on hover.
- Always respect `prefers-reduced-motion` — swap all animation to a simple 150ms fade.
- The brand personality is "calm" — animations should feel like silk unfolding, not like a notification demanding attention.

### Layout principles
- Generous whitespace is a brand signal — premium brands let content breathe
- Maximum 2 color accents per viewport
- Hero text should never exceed 60% of container width
- Vertical rhythm in 8px multiples
- CTA stacking: never 3+ CTAs side by side; maximum 2 (primary + secondary)
- Spacing between sections should be generous; spacing within sections should create clear visual groupings

### Accessibility requirements (WCAG 2.2 AA)
These contrast pairs have been verified and must be maintained:

| Element | Background | Foreground | Status |
|---------|------------|------------|--------|
| Body copy | Surface 1 | Text 1 | AA/AAA |
| Secondary copy | Surface 1 | Text 2 (min 14px) | AA |
| Primary CTA button | Accent CTA | White text | AA |
| Ghost CTA button | Surface 1 | Accent CTA text/border | AA |
| Gold badges | Surface 1 | Accent 2 text | AA |
| Inverted header/footer | N800/N900 | White text | AA/AAA |
| Overlay text | Scrim 80% | White text | AA |

---

## 5. What you're designing for

### 5.1 Current store pages

These pages exist today and your CSS must cover all of them:

**Homepage** — First impression. Hero banner (full-viewport image with text overlay), trust bar (icon + text strip), problem/solution section, bestseller product grid, brand heritage tiles, customer testimonials, bundles showcase, FAQ accordion, newsletter signup.

**Product page (PDP)** — The conversion page. Image gallery with thumbnails and zoom/lightbox, buy box (eyebrow + title + tagline + price with per-night framing + variant picker + add-to-cart + guarantee line + payment badges), proof badge chips, feature highlight icon cards, quality evidence expandable panels, comparison table (silk vs alternatives — responsive: table on desktop, stacked cards on mobile), FAQ accordion, cross-sell product grid, sticky add-to-cart bar on scroll.

**Collection page** — Product browsing. Product card grid with hover image swap, badges overlay.

**Quality page** (/nasza-jakosc) — Deep trust-building. Text hero with kicker, origin story (image + text 2-col), momme explanation (image + text 2-col), certificates logo grid, fire test video section, 6A quality section (image + feature list), QC process cards, comparison table, final CTA block.

**About page** (/o-nas) — Brand story. Hero (image + text 2-col), narrative section, values card grid.

**Returns page** (/zwroty) — Purchase anxiety removal. Hero with shield icon badge, editorial content (image + text 2-col with inline comparison rows), step-by-step process (numbered cards with connector line), FAQ accordion, reassurance CTA block (including a dark/inverted background variant).

**Cart drawer** — Slide-out right panel with dark overlay backdrop. Header bar, scrollable item list (thumbnail + title + variant + quantity stepper + price + remove), upsell product widget, free shipping progress bar, totals, checkout button. Appears globally.

**Announcement bar** — Thin strip above the header (e.g., "Free shipping over 200 PLN" or "60-day guarantee"). Single line of text, optional link. Always visible, not dismissible.

**Header** — Fixed top bar with backdrop blur, below the announcement bar. Logo, desktop navigation links, icon actions (search, account, cart with count badge). Mobile: hamburger menu with slide-down panel. Auto-hides on scroll down, reappears on scroll up.

**Footer** — Dark background (inverted colors — light text on dark). 4-column grid: brand description, shop links, help links, newsletter input (underline style). Copyright bar.

### 5.2 Future pages (not built yet, but your CSS must support them)

These pages will be built using the same visual system. Your foundations need to cover the patterns they'll use:

**Blog listing page** — Grid of article cards (image + title + date + excerpt), pagination.

**Blog article page** — Featured image, article title with date/author, **rich text content** (this is critical — the CMS generates bare HTML: `<h2>`, `<h3>`, `<p>`, `<ul>`, `<ol>`, `<blockquote>`, `<strong>`, `<em>`, `<a>`, `<img>`, `<table>`. You need a wrapper class like `.lusena-richtext` that styles all these bare elements beautifully within that scope). Share buttons, back-to-blog link.

**Search results page** — Search input, product results grid (same card pattern as collection), "no results" empty state.

**404 page** — Centered message with heading, body text, and "continue shopping" button.

**Contact page** — Contact form (text inputs, email input, textarea, submit button), page content.

**Cart page** (full page, not drawer) — Cart items table (responsive), discount code input, subtotal, checkout button, empty cart state.

**Collections list page** — Grid of collection cards (image + title), pagination.

**Customer account pages** — Login form, registration form, account dashboard with order history table, order detail page, addresses management with add/edit forms, password reset form.

**Gift card page** — Gift card display with balance, QR code, copy-to-clipboard code.

**Password page** — Shopify's store-offline page shown when the store is password-protected (during development/launch). Centered layout with logo, heading, password input, submit button, and optional "powered by Shopify" footer.

---

## 6. Complete visual pattern catalog

This is the full inventory of visual patterns your CSS needs to support. These are described as design patterns — how you implement them is your creative decision.

### 6.1 Layout patterns

- **Full-viewport hero** — Background image covering the viewport, gradient overlay, text + CTA centered on top
- **Text-only hero** — Full-width section with centered heading stack (kicker + heading + body + CTA), no background image
- **Two-column: image + text** — Responsive grid, image on one side, text content on the other. Must support both image-left and image-right variants. Stacks vertically on mobile.
- **Two-column: sticky sidebar** — One column stays pinned while the other scrolls (used for editorial layouts)
- **Three-column card grid** — Equal cards in responsive grid (1-col mobile, 3-col desktop)
- **Four-column card grid** — Cards in responsive grid (1, 2, 4 columns across breakpoints)
- **Product card grid** — 2-col mobile, 3-4-col desktop, with tighter horizontal gaps and generous vertical gaps
- **12-column asymmetric grid** — For PDP: media gallery (7 cols) + buy box (5 cols)
- **Horizontal strip / trust bar** — Single row of repeating icon+text items, 2x2 on mobile, 4-across on desktop
- **Centered CTA block** — Narrow centered container with heading + body + button(s)
- **Inverted CTA block** — Same as above but on a dark/accent background with inverted text colors
- **Multi-column footer** — Dark background, 3-4 column layout with different content types per column
- **Side-by-side comparison columns** — Two parallel columns with matching rows, positive/negative indicators
- **Problem/Solution split** — Two-column layout where one side shows "problem" items (negative indicators, e.g., red X icons) and the other shows "solution" items (positive indicators, e.g., green check icons). Each side has its own kicker + heading + item list. Used to contrast silk vs. cotton/polyester.

### 6.2 Component patterns

- **Product card** — Image container (specific aspect ratio for product photos) with optional badge overlay, hover effect to reveal secondary image, title below, price with optional strikethrough compare-at price
- **Content card** — Card with optional icon/image, heading, body text. Subtle hover lift/shadow effect.
- **Testimonial card** — Star rating, quote text, author attribution
- **Process step card** — Numbered indicator, icon, title, description. Connected by a visual line/connector between steps.
- **Icon in circle** — Circular container with centered icon, used as visual anchor for features/values
- **Proof chip / badge row** — Inline row of small items (icon + label), wrapped on mobile
- **Pill badge** — Rounded pill with icon + text, subtle border/backdrop
- **Image badge overlay** — Absolutely positioned label in corner of image container (e.g., "Bestseller")
- **Kicker label** — Small uppercase text with wide letter-spacing, placed above headings (the "eyebrow" pattern)
- **Section header with inline action** — Heading on left, "view all" link on right
- **Breadcrumb navigation** — Horizontal trail with separator icons, current page visually distinct
- **Specification / data table** — Key-value pairs with alternating row backgrounds
- **Responsive comparison table** — Full table on desktop, stacked card layout on mobile. Must support both two-column (LUSENA vs Others) and three-column (LUSENA vs cheap alternative vs premium import) variants.
- **Bullet list with custom markers** — List items with brand-styled markers (check icons, dots, custom icons)
- **Certificate/logo grid** — 2x2 grid of small image containers
- **Video container** — Aspect-ratio-constrained container for embedded video
- **Decorative background watermark** — Large semi-transparent icon behind content
- **Divider / separator** — Horizontal rule between content zones (subtle border style)
- **Blockquote / pull quote** — Styled quotation for testimonials and editorial content
- **Progress bar** — Track + fill bar (e.g., free shipping threshold), color change when complete
- **Counter badge** — Small circle overlaid on an icon (e.g., cart item count)
- **Price display** — Regular price, sale price with strikethrough original, "per night" secondary framing
- **Announcement bar** — Thin full-width strip with centered text and optional link

### 6.3 Interactive patterns

**Hover states:**
- Card hover: subtle lift (translateY) + shadow
- Product card image hover: secondary image crossfade
- Image hover: gentle zoom (scale) within overflow-hidden container
- Link hover: underline toggle (add or remove), color change
- Button hover: background opacity shift, background tint, or brightness change (varies by button variant)
- Destructive hover: color turns red on remove/delete actions

**Focus & keyboard navigation:**
- Visible focus ring on all interactive elements (`:focus-visible`)
- Skip-to-content link (accessibility)

**Disabled states:**
- Reduced opacity, no pointer events
- Faded background/border on form elements and buttons

**Loading states:**
- Button loading: content replaced by animated indicator (shimmer or dots)
- Cursor changes to `wait`
- Image loading placeholder: what an image container shows before the image loads (brand-bg color, subtle shimmer, or skeleton pulse). Important for product card grids with many images.

**Selected / active states:**
- Variant swatch: ring/border indicator around selected option
- Pill option: accent border + background tint for selected
- Unavailable option: reduced opacity, cursor not-allowed
- Out-of-stock product card: visual treatment for products shown in collection grid that cannot be purchased (e.g., muted/greyed image, "sold out" badge overlay, no hover effect)
- Gallery thumbnail: visual indicator for currently active image
- Pagination: current page highlighted
- Accordion: open/closed state with icon rotation

**Expand / collapse:**
- Accordion pattern: trigger with chevron, content panel animates height, chevron rotates
- Mobile menu: panel slides down from header
- Cart drawer: slides in from right with dark overlay backdrop

**Sticky elements:**
- Sticky header: fixed top, auto-hides on scroll down, reappears on scroll up, backdrop blur
- Sticky bottom bar: appears when user scrolls past a trigger point, hidden by default

**Scroll-triggered entry animations:**
- Fade-up on scroll into view
- Stagger effect for repeated items (each child appears with slight delay)
- Must respect `prefers-reduced-motion`

**Transitions:**
- All interactive state changes should transition smoothly (not snap)
- Consider: hover/focus (fast), accordion open/close (medium), drawer slide (medium), page-level animations (slow)

### 6.4 Form patterns

- **Text input** — Standard input with label, placeholder styling, focus state with accent highlight
- **Email input** — Same as text input
- **Password input** — Same as text input
- **Textarea** — Multi-line input, resizable
- **Search input** — Input with search icon, potentially with predictive results dropdown
- **Underline input** — Minimal style with only bottom border (for dark background contexts like footer)
- **Select dropdown** — Styled select with custom chevron
- **Newsletter signup** — Input + button side-by-side on desktop, stacked on mobile
- **Quantity stepper** — Minus button + number + plus button in an inline group, minus disabled at 1
- **Color swatch picker** — Round buttons showing colors, selected state with ring, disabled state with opacity
- **Pill option selector** — Rectangular buttons for sizes/options, selected state with accent styling, disabled state
- **Form validation: error** — Red-tinted message with error icon
- **Form validation: success** — Green-tinted message with check icon
- **Discount code input** — Input + apply button (cart context)

### 6.5 Page-level patterns

- **Rich text content** — This is critical. A wrapper class (e.g., `.lusena-richtext`) that styles bare HTML generated by the CMS: `<h1>`–`<h6>`, `<p>`, `<a>`, `<ul>`, `<ol>`, `<li>`, `<blockquote>`, `<strong>`, `<em>`, `<img>`, `<table>`, `<hr>`. Used in blog articles, product descriptions, and generic pages. Must look beautiful with proper spacing, typography, and link styling within this scope.
- **Empty state** — Centered message for "no results", "empty cart", etc. Heading + body + action button.
- **Pagination** — Previous/next + page numbers, current page indicator, disabled state for boundaries
- **Notification / alert** — Success, error, and info message bars with appropriate status colors
- **Overlay backdrop** — Dark semi-transparent backdrop for drawers, modals, lightboxes. Click-to-dismiss.
- **Text selection** — `::selection` styling with brand accent color on light backgrounds. On dark sections (footer, inverted CTA blocks), the `::selection` colors must be inverted (e.g., white background with dark text) so they remain visible.
- **Dark section variant** — Some sections use dark backgrounds (footer, accent sections). Need inverted text/link/border colors that work on dark.

### 6.6 Responsive behavior patterns

- **Show/hide at breakpoints** — Elements that appear only on mobile or only on desktop
- **Stack to side-by-side** — Vertical on mobile, horizontal on desktop (most 2-column layouts)
- **Text alignment shift** — Center-aligned on mobile, left-aligned on desktop
- **Font size scaling** — Type sizes that adjust between mobile and desktop
- **Grid column changes** — 1, 2, 3, 4 columns across breakpoints
- **Horizontal scroll to grid** — Some components scroll horizontally on mobile but display as grid on desktop
- **Full-width to contained** — Elements edge-to-edge on mobile, constrained on desktop

---

## 7. Technical constraints

### About the platform

This is a **Shopify** store built on the **Dawn** theme (v15.4.1). You don't need to know Shopify deeply, but these constraints affect your CSS:

1. **One file, no build tools.** Your deliverable is a single hand-written CSS file. No Tailwind, no Sass, no PostCSS, no npm. Just CSS. **This file replaces an existing compiled Tailwind CSS build** that currently provides utility classes. You are building the complete utility and component layer from scratch — the theme markup will be migrated to use your classes.

2. **No CSS reset needed.** The Dawn framework (`base.css`, loaded before your file) already handles the HTML reset — `box-sizing`, margin zeroing, form normalization, etc. Your file should NOT include a CSS reset.

3. **Don't restyle bare HTML elements globally.** Dawn already styles `h1`–`h6`, `a`, `p`, `button`, etc. with its own defaults. Your file should define classes (e.g., `.lusena-type-h1`) rather than overriding bare `h1` selectors globally. **Exception:** inside a scoped wrapper like `.lusena-richtext`, you SHOULD style bare elements — that's how CMS content works.

4. **Naming convention.** All custom CSS classes must use the `lusena-` prefix with **BEM methodology**: block (`lusena-card`), element (`lusena-card__title`), modifier (`lusena-card--featured`). All CSS custom properties must use `--lusena-*` (e.g., `--lusena-space-lg`, `--lusena-shadow-sm`). This prevents collisions with Dawn's own classes.

5. **Mobile-first responsive.** Base styles = mobile. Override with `@media (min-width: ...)` for larger screens. Primary breakpoint: **768px** (this is the mobile/desktop flip throughout the store). You may define additional breakpoints as needed.

6. **CSS custom properties for tokens.** Use `:root` CSS variables for all design tokens (colors, spacing, typography, shadows, etc.) so values can be referenced and overridden throughout the system.

7. **File size target:** Under 30KB unminified. This CSS is render-blocking — loaded on every page.

8. **Pure CSS only.** No Liquid template variables are available inside this file. It's a static `.css` asset.

9. **Rem note:** Dawn uses `font-size: 62.5%` on `<html>`, making `1rem = 10px`. Be aware of this if you use rem units. Using px is perfectly fine too.

10. **Accessibility requirements:**
    - Visible focus states (`:focus-visible`) on all interactive elements
    - Touch targets minimum 44x44px
    - `@media (prefers-reduced-motion: reduce)` for transitions/animations
    - All text/background color pairs must meet WCAG AA contrast (4.5:1 minimum)

11. **Z-index layering.** The theme has multiple stacking contexts that must layer correctly. Define a z-index token scale in `:root` covering at least these layers (from back to front): decorative watermarks → badge overlays → sticky header → search dropdown → overlay backdrop → drawer panel → lightbox/modal → sticky bottom bar. Without explicit tokens, z-index values will conflict.

12. **Section spacing tiers (Shopify-specific).** Each section in the Shopify theme editor selects its own spacing tier. Your spacing system must include tier-based section padding classes that the markup can apply (e.g., `lusena-spacing--compact`, `lusena-spacing--standard`, `lusena-spacing--spacious`, `lusena-spacing--hero`, `lusena-spacing--full-bleed`). Each tier defines its own `padding-top` and `padding-bottom`, responsive between mobile and desktop. Additionally:
    - When two adjacent sections share the same background color, the gap between them needs special handling. A JS snippet detects this and adds the class `lusena-section-gap-same` to the second section. Your CSS should ensure at least a minimum top padding when this class is present, without inflating already-generous tiers. When backgrounds differ, the class `lusena-section-gap-different` is added instead (normal tier padding applies).
    - Dawn's base CSS adds its own `margin-top` between `.section + .section` elements. Your file must neutralize this margin when LUSENA tier classes are present, for example: `.section:has(> [class*="lusena-spacing--"]) + .section, .section + .section:has(> [class*="lusena-spacing--"]) { margin-top: 0; }`

13. **Dark mode is out of scope.** Do not implement `prefers-color-scheme: dark`. The store has dark *sections* (footer, inverted CTA blocks) but no system-wide dark mode.

---

## 8. What to include in the file

At minimum, the file should provide CSS for everything described in Section 6. Organized however makes sense to you, but it should cover:

- **Design tokens** — CSS custom properties on `:root` for all reusable values (colors, spacing scale, typography scale, radii, shadows, transitions)
- **Typography system** — Semantic classes for every text role (hero, headings, body, kicker, caption, etc.) with responsive sizing
- **Spacing system** — Section-level padding tiers (see constraint 12), element-level semantic gap classes (e.g., gap below kickers, gap below headings, gap below body text, gap before CTAs, gap below section intros, major subsection break), and container-level vertical rhythm utilities (e.g., a parent class that adds uniform gaps between all direct children, with tight/standard/relaxed variants)
- **Layout system** — Container class with responsive horizontal margins + max-width, grid patterns (2/3/4-col, 12-col asymmetric, product grid), content width constraints
- **Color utility classes** — Background, text, and border classes for every brand color, including opacity variants (e.g., 50%, 80%) and dark-section inverted variants
- **Component classes** — Product card, content card, testimonial card, step card, proof chip, badge, breadcrumb, data table, comparison table, progress bar, divider, icon circle, kicker, price display, blockquote
- **Form styling** — Inputs, textareas, selects, validation states, quantity stepper, swatch/pill pickers, newsletter combo
- **Rich text wrapper** — Scoped styling for CMS-generated bare HTML content
- **Interactive states** — Hover, focus-visible, disabled, loading, selected/active, expand/collapse for all relevant components
- **Overlay/backdrop** — For drawers, modals, lightboxes
- **Pagination** — Page navigation controls
- **Empty states & notifications** — Error, success, info patterns
- **Utility classes** — Display, positioning, sizing, overflow, text alignment, aspect ratios (1:1, 3:4, 4:5, 16:9 at minimum), object-fit/object-position, cursor, pointer-events, opacity, transforms, line-clamp/text-truncation (single-line ellipsis and multi-line clamp for product titles and excerpts), visually-hidden/screen-reader-only class, transition timing token classes — whatever building blocks the markup will need
- **Responsive overrides** — Breakpoint-specific adjustments: show/hide, layout direction, font sizes, grid columns, spacing
- **Reduced motion** — `@media (prefers-reduced-motion: reduce)` fallbacks
- **Selection styling** — `::selection` with brand accent

---

## 9. What other files handle (don't include these)

| Concern | Handled elsewhere |
|---------|-------------------|
| HTML/CSS reset | Dawn's `base.css` |
| Button component variants (primary, outline, ghost, link, text, icon buttons, sizes, loading states) | Separate button system file |
| Product page-specific layout (gallery, buy box, accordion internals, sticky ATC bar) | Separate PDP styles file |
| Scroll-reveal animation JS logic | Separate JS file |
| Icon SVGs (rendering specific icons) | Separate Liquid snippet |

Your file is the foundation. The button system and PDP layout are built on top of it and will reference your tokens (colors, spacing, radii, transitions).

---

## 10. Deliverable

**One file: `lusena-foundations.css`**

- Hand-written, valid CSS
- Well-commented with clear section headers
- Mobile-first responsive
- Uses `--lusena-*` custom properties for all design tokens
- Uses `lusena-*` prefixed classes for all custom styles
- Under 30KB unminified
- No build dependencies

---

## 11. After delivery

After you deliver the file, we'll integrate it into the Shopify theme and go through it together on the live store with real content. We'll iterate from there. The first version doesn't need to be perfect — it needs to be a strong, comprehensive foundation we can refine.

Don't hold back. If you see opportunities to elevate the experience — go for it. The goal is to make this the most beautiful and conversion-effective silk store on the Polish internet.
