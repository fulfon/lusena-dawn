Use:
1. Core Framework: React 19 (TypeScript)
2. Language: TypeScript
3. Styling: Tailwind CSS
4. Icons: Lucide React
5. Typography: Google Fonts
6. Architecture: Single Page Application (SPA)
7. Data: Static/Mock Data

<UI/UX instructions>
---

# LUSENA Shopify UI/UX Design Rules

**Scope:** Homepage (Landing), Collection page (PLP), Product page (PDP)
**Goal:** Maximum conversion with premium aesthetic + flawless UX + brand consistency.

---

## 0) Non-Negotiables (must pass)

1. **Premium calm aesthetic**: editorial, minimal, soft contrast, no aggressive sales UI.
2. **One primary action per viewport** (especially above the fold).
3. **No “accidental whitespace”**: every gap is intentional, from the spacing system.
4. **Mobile-first** (design for 360–430px first, then scale up).
5. **Performance-safe**: animations are progressive enhancement; UX works perfectly without JS.

---

## 1) Brand Consistency Rules

### 1.1 Color

* Use **Route A palette tokens** consistently across all templates.
* **CTA color is fixed globally** (same color, same hover state across Home/PLP/PDP).
* Accent usage: **max 1–2 accent colors per screen**.
* Text must meet **AA contrast** for body and UI labels.

### 1.2 Typography (“no common fonts” requirement)

Choose **one** approved premium pair:

* Option A: **Canela / Portrait** (headings) + **GT America / Neue Haas Grotesk** (body/UI)
* Option B (fallback only if licensing blocks): keep current system but apply premium typographic treatment (see below).

**Typography behavior rules:**

* Prices and measurements use **tabular lining numerals**.
* Headlines: editorial, restrained, no all-caps headlines.
* Line-length: body text target **55–75 characters** on desktop.

### 1.3 Imagery rules (luxury consistency)

* PLP product cards: **4:5** ratio always.
* PDP primary media: **1:1** packshot first.
* Home hero: **16:9 desktop**, **4:5 mobile**.
* Include at least one “**real silk**” lifestyle visual (natural flow/crease) per key page.

---

## 2) Grid, Spacing, Vertical Rhythm, “No Whitespace”

### 2.1 Grid

* Desktop: **12-column** grid.
* Tablet: **8-column** grid.
* Mobile: **4-column** grid.
* Gutters and margins must be consistent across templates (no one-off exceptions).

### 2.2 Spacing system (hard rule)

* Only use spacing values from the system: **4/8-based scale** (e.g., 8, 12, 16, 24, 32, 48, 64, 96).
* Section spacing: minimum **24–32px** between major sections on mobile; increases proportionally on desktop.
* No “random” paddings like 27px, 41px etc.

### 2.3 “No whitespace” meaning (interpretation)

* Not “cramped”. It means:

  * No dead zones, no unstructured empty areas.
  * Every space is part of rhythm and hierarchy.
  * Use deliberate breathing room where premium clarity requires it.

---

## 3) Visual Hierarchy Rules

1. Each page has exactly **one H1**.
2. No skipping heading levels (H2 → H4 not allowed).
3. The user’s eye path must be:
   **Primary benefit → proof → price/value → CTA → reassurance**
4. **Primary CTA** must be visually dominant and consistent:

   * Same placement logic, same styling, same interaction states everywhere.
5. Secondary actions must never compete (lower contrast or smaller button style).

---

## 4) Gestalt Rules (must be applied intentionally)

### 4.1 Proximity

* Group “decision elements” tightly: price + “per night” anchor + pay-later info.
* Separate informational blocks (story, care, FAQ) clearly.

### 4.2 Common Region

* Guarantees / risk reversal must appear inside a **boxed region** (subtle border or background), directly below primary CTA on PDP.

### 4.3 Similarity

* All trust icons: same size, stroke weight, alignment.
* All product cards: identical structure and spacing.

### 4.4 Figure–Ground

* Text on imagery must always be legible via scrim/overlay; no harsh blocks.

---

## 5) Motion rules (required)

**Motion style:** gentle, premium, slow; never bouncy; never “playful”.

### 5.1 Where motion is allowed

* Home hero: subtle float or parallax micro-shift (low amplitude).
* Section reveals: fade/slide-in on scroll (very subtle).
* Add-to-cart confirmation: small fade/slide.

### 5.2 Where motion is NOT allowed

* Core shopping controls: variant selection, quantity, price, cart interactions must remain stable.
* No motion that causes layout shift (CLS).

### 5.3 Timing rules

* Hover/focus: **150–200ms**
* Transitions/modals/hero: **250–400ms**
* Ease: calm ease-in-out (no elastic/spring).
* Must respect **prefers-reduced-motion**:

  * If reduced motion is enabled: remove movement, keep simple fades or none.

---

# PAGE SPECS

## 6) Homepage (Landing) — Required Sections & Order

Design must follow this order. You may refine layout but not remove key decision drivers.

### 6.1 Above the fold (First screen)

**Hero block**

* H1: brand tagline + benefit line.
* Subtext: 1 sentence explaining the “night beauty” promise (short).
* **One primary CTA** (e.g., “Shop Pillowcases”).
* Optional supporting link: “Why silk?” (text link, not a button).

**Trust strip (directly under hero)**

* 3–4 items max, compact:

  * Rating/reviews
  * OEKO-TEX / compliance proof
  * Fast Poland shipping
  * 60-day test / guarantee

**Design constraints:**

* Hero text must not exceed ~60% width on desktop.
* No busy collage; keep one strong hero image.

### 6.2 Mid page (Education → Products)

**Problem → Solution**

* 2-column editorial layout:

  * Left: problem (hair frizz, skin creases)
  * Right: solution (22 momme mulberry silk)
* Use icons sparingly.

**Bestsellers mini-grid**

* 2–3 products only (do not flood).
* Each card: image 4:5, name, price, one badge max.

**Heritage / Material proof**

* Short story block: Suzhou heritage + quality proof + OEKO-TEX, 22 momme.
* Must feel editorial, not corporate.

### 6.3 Lower page (Objection handling → conversion reinforcement)

**UGC / Reviews preview**

* 3–4 tiles with rating + short quote.
* Link to full reviews.

**Bundles / Gift section**

* Present bundles as “gift-ready, premium packaging” value.
* Show savings clearly but elegantly.

**FAQ (short)**

* Only the highest-friction objections:

  * Authenticity
  * Care/wash
  * Shipping & returns
  * Guarantee / trial period

**Newsletter / Circle**

* Minimal, calm, value-led (“early access”, “care guide”), no spam vibe.

---

## 7) Collection Page (PLP) — Rules for “money page”

### 7.1 Product card spec

* Ratio: 4:5.
* Title max 2 lines.
* Price + compare-at (if used) must align perfectly across grid.
* One badge max (e.g., “Bestseller”).
* Hover: swap to second image (no layout jump).

### 7.2 Filters & sorting

* Default sort: **Bestselling**.
* Mobile: sticky “Filters” entry; filters open in a drawer.
* All interactive elements must be **44×44px** minimum tap target.

### 7.3 Trust strip

* Add a thin trust line above grid or under header:

  * shipping, returns, guarantee (3 items max)
* Must be subtle (not banner ads).

### 7.4 Pagination

* Prefer “Load more” over infinite scroll.

---

## 8) Product Page (PDP) — Conversion Architecture

### 8.1 Above the fold (must include)

1. **Emotional headline** (one-line, benefit-led)
2. **Gallery**

   * Slide 1: packshot 1:1
   * Slide 2: short video 10–15s (muted)
3. **Trust bar** (rating + shipping + OEKO-TEX)
4. Product title + short benefit descriptor
5. Variant selector (always above CTA)
6. Price + “per night” value anchor + pay-later info
7. 3 bullet benefits (ultra scannable)
8. Primary CTA (dominant)
9. **Risk reversal box directly under CTA** (common region)

   * Guarantee / trial period
   * Returns simplicity
   * Customer support promise

### 8.2 Below the fold (structured)

* What’s included / specs (accordion)
* Care instructions (simple steps, icon + 3 lines)
* Shipping & returns (plain language)
* Reviews (verified cues, sorting)
* Cross-sell: “Pairs well with” (max 3 items)

### 8.3 Sticky ATC on mobile

* Sticky bar appears after user scrolls past CTA:

  * Variant + price + Add to cart
* Must be minimal and not cover content.

---

# 9) UX Microcopy Rules (tone)

* Short, calm, confident; avoid hype.
* Explain value using sensory/quality language (“22 momme”, “mulberry silk”, “OEKO-TEX”, “gift-ready”).
* Always reduce anxiety near purchase actions (shipping, returns, guarantee).

---

# 10) Designer Deliverables (what you must hand off)

1. **Figma** with:

   * Homepage (desktop + mobile)
   * PLP (desktop + mobile)
   * PDP (desktop + mobile)
2. **Design tokens** page:

   * Colors (Route A tokens)
   * Type scale (H1–H5, body, caption)
   * Spacing scale
   * Button styles (primary/secondary/text)
3. **Component library**:

   * Product card
   * Trust strip
   * Badge
   * Accordion
   * Variant selector
   * Review tile
   * Sticky ATC bar
4. **Motion spec**:

   * List of scroll-reveal + micro-interactions
   * Timing + easing
   * Reduced-motion behavior
5. **Redline notes** (handoff):

   * Grid rules, padding/margins, breakpoints, tap sizes

---

# 11) Acceptance Checklist (final QA)

A design is accepted only if:

* Typography and spacing are 100% consistent (no random values).
* Home/PLP/PDP share a unified visual language (buttons, cards, trust UI).
* Primary CTA is unmissable and consistent.
* Trust + risk reversal appear before user hesitates (above fold / near CTA).
* Motion is premium, subtle, and removable via prefers-reduced-motion.
* Mobile experience is as elegant as desktop.

---
</UI/UX instructions>
