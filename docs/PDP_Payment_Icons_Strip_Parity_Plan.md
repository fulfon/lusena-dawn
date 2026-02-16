# PDP Payment Icons Strip Parity Plan (Draft shop -> Shopify theme)

Created: 2026-02-14  
Status: Planned  
Owner: Codex

## Goal

Port the PDP payment reassurance strip from the draft shop to the live LUSENA theme with visual parity:
- lock icon + payment logos + secure payment label
- desktop and mobile variants matching the draft arrangement and sizing
- logo assets copied as SVG files into theme `assets/`

## Scope

### In scope
- Match draft strip structure from `lusena-shop/src/pages/Product.tsx` (desktop + mobile variants).
- Copy SVG logos used by draft PDP: Visa, BLIK, PayPo, Przelewy24.
- Replace current text-only payment chips in `snippets/lusena-pdp-payment.liquid`.
- Update PDP payment strip styles in `snippets/lusena-pdp-styles.liquid`.
- Preserve section setting source for secure payment copy (`section.settings.secure_payment_label`).
- Preserve Dawn scroll reveal behavior where applicable.

### Out of scope
- Any other PDP fragments (gallery, proof chips, ATC, sticky ATC, accordions).
- Payment gateway/business logic changes.
- Rebuilding or replacing global utility CSS build.
- Changing section schema unless strictly required (not expected).

## Source of truth (Draft shop)

- `lusena-shop/src/pages/Product.tsx`
- `lusena-shop/src/lib/pdp-content.ts`
- `lusena-shop/src/assets/payment_icons/Visa.svg`
- `lusena-shop/src/assets/payment_icons/BLIK.svg`
- `lusena-shop/src/assets/payment_icons/logo_PayPo_Kolor.svg`
- `lusena-shop/src/assets/payment_icons/Przelewy24_logo.svg`

## Target in theme (Shopify)

- `templates/product.json` (active template section type check)
- `sections/lusena-main-product.liquid` (actual PDP render path)
- `snippets/lusena-pdp-payment.liquid` (fragment markup to replace)
- `snippets/lusena-pdp-styles.liquid` (fragment styling)
- `assets/` (new copied SVG files)

## Decisions (final) - 2026-02-14

1. Data source: keep payment label dynamic from existing section setting (`secure_payment_label`); payment method list stays static to match draft exact logos.
2. Interaction model: exact draft visual behavior (static strip, no new interactions), not Dawn default text chips.
3. Breakpoints: use draft split (`md` utility behavior in this theme, 768px) because this custom PDP already uses that utility system.
4. Motion: keep existing reveal-on-scroll compatibility with conditional `scroll-trigger` classes and `data-cascade`.
5. Missing-data fallback: if a logo asset is unavailable, render method name text fallback for that method (same resilience as draft logic).

## Open questions / unresolved assumptions

None.

## Data sources & content model

- `section.settings.secure_payment_label` remains source for user-facing secure payment text.
- Static payment methods (draft order): `Visa`, `BLIK`, `PayPo`, `Przelewy24`.
- Icon files will be referenced from theme `assets/` and rendered in the snippet.
- Fallback when icon mapping fails: display method text with subdued styling.
- Translation strategy: no new visible copy expected; existing setting value remains merchant-controlled.

## Target UX spec (Desktop + Mobile)

### Desktop (~1280px)
- Single row: lock icon, icon badges, secure label.
- Icon badge styles: thin border, rounded corners, compact horizontal padding.
- Icon heights: Visa 18px; all other logos 20px.
- Secure label: 11px, muted secondary tone, non-wrapping.

### Mobile (~390px)
- Single wrapped row: lock icon, secure label, icon badges.
- Tighter spacing than desktop.
- Icon heights: Visa 14px; all other logos 16px.
- Label uses 10px muted text and can remain inline before badges.

### Accessibility
- Decorative lock and logo images use meaningful `alt` for logos and semantic text fallback if image missing.
- No keyboard traps; component remains non-interactive static content.
- Keep semantics lightweight (container + text + images) without fake controls.

## Theme capability & conflict audit

| Capability / token | Draft source | Resolved draft value | Exists in theme? | Conflict detected? | Planned implementation path | Target file |
|---|---|---|---|---|---|---|
| Payment method set | `lusena-shop/src/lib/pdp-content.ts` | Visa, BLIK, PayPo, Przelewy24 | No (current theme has text chips incl. Mastercard) | Yes | Replace list with draft set and icon map | `snippets/lusena-pdp-payment.liquid` |
| Desktop/mobile split | `lusena-shop/src/pages/Product.tsx` | `hidden md:flex` + `md:hidden` | Yes | No | Reuse utility split directly in snippet | `snippets/lusena-pdp-payment.liquid` |
| Border/radius chip style | `lusena-shop/src/pages/Product.tsx` | `border-secondary/10`, `rounded-sm`, compact paddings | Yes (utilities exist) | No | Reuse utilities on badge wrappers | `snippets/lusena-pdp-payment.liquid` |
| Icon height token `h-[18px]` | `lusena-shop/src/pages/Product.tsx` | 18px for desktop Visa | No | No | Add scoped semantic class in snippet CSS instead of utility backfill | `snippets/lusena-pdp-styles.liquid` |
| Mobile Visa 14px + other 16px | `lusena-shop/src/pages/Product.tsx` | 14px/16px | Partially (`h-3.5`, `h-4` exist) | No | Prefer scoped icon classes for stable parity | `snippets/lusena-pdp-styles.liquid` |
| Secure text source | `templates/product.json` + section settings | merchant-configurable secure label | Yes | No | Keep `section.settings.secure_payment_label` | `snippets/lusena-pdp-payment.liquid` |
| Lock icon | current snippet + icon system | small muted lock icon | Yes (`lusena-icon` supports `lock`) | No | Reuse existing icon snippet | `snippets/lusena-pdp-payment.liquid` |
| Logo assets in theme | draft asset files | 4 SVG files | No | No | Copy SVG files into `assets/` with clear names | `assets/*` |

Audit notes:
- No conflicting utility stacks in draft payment strip.
- Missing `h-[18px]` utility will not be added globally; scoped fragment CSS is preferred.
- Existing `.lusena-pdp-payment-method` text-chip CSS conflicts with icon-badge parity and will be replaced/extended.

## Parity contract table

| Selector / element | Property | Draft value | Theme target value | State | Breakpoint | Tolerance |
|---|---|---|---|---|---|---|
| `.lusena-pdp-payment__desktop` | `display` | flex desktop only | flex desktop only | default | >=768px | exact |
| `.lusena-pdp-payment__mobile` | `display` | flex mobile only | flex mobile only | default | <768px | exact |
| `.lusena-pdp-payment-badge` | `border-color` | `rgba(74,74,74,0.1)` | same | default | all | exact |
| `.lusena-pdp-payment-badge` | `border-radius` | small (2px) | same | default | all | exact |
| `.lusena-pdp-payment-icon--visa-desktop` | `height` | 18px | 18px | default | >=768px | exact |
| `.lusena-pdp-payment-icon--other-desktop` | `height` | 20px | 20px | default | >=768px | exact |
| `.lusena-pdp-payment-icon--visa-mobile` | `height` | 14px | 14px | default | <768px | exact |
| `.lusena-pdp-payment-icon--other-mobile` | `height` | 16px | 16px | default | <768px | exact |
| `.lusena-pdp-payment-secure` | `font-size` | 11px desktop / 10px mobile | same | default | responsive | exact |
| `.lusena-pdp-payment-secure` | `color` | `rgba(74,74,74,0.6)` | same | default | all | exact |

## State fixture matrix

| State | Required fixture/data | Expected UI/UX |
|---|---|---|
| Empty | secure label blank + valid icons | row still renders with lock + icons; label can be empty without layout break |
| Populated | default PDP settings + icons present | full strip matches draft structure |
| Active/Selected | N/A | N/A (no interactive selection state) |
| Hover | pointer over badges | no special hover treatment required |
| Disabled | N/A | N/A |
| Loading | N/A | N/A (server-rendered static strip) |
| Error | one or more missing icon assets | fallback method text is shown for missing logo |
| Success | all assets load | all four logos render in order |
| Long content | long secure payment label | label remains readable; mobile wraps gracefully if needed |

## Implementation approach

1. Copy draft SVG files to `assets/` with stable naming compatible with Liquid asset references.
2. Replace snippet markup in `snippets/lusena-pdp-payment.liquid` to draft-equivalent desktop/mobile structure and icon mapping.
3. Update payment styles in `snippets/lusena-pdp-styles.liquid` with scoped classes for exact icon heights and spacing.
4. Remove or supersede legacy text-chip-only payment CSS to avoid style conflicts.

Implementation rules:
- Modify only the active custom PDP path (`lusena-main-product` and its snippets).
- Keep animation classes conditional per theme setting.
- Keep fallback text rendering for robustness.

## Milestones / deliverables

1. Plan approved by user.
2. SVG icons copied into theme assets.
3. Payment strip snippet + styles updated for parity.
4. Shopify `validate_theme` passes for touched files.
5. Visual verification requested from user at mobile and desktop widths.

## Verification checklist (developer pre-check)

### Computed-style checks

Breakpoints:
- Mobile: ~390px
- Desktop: ~1280px

Check:
- display toggling (`desktop` vs `mobile` containers)
- icon heights (18/20 desktop and 14/16 mobile)
- border color/radius/padding on badges
- secure label font size/color
- row spacing and wrapping

### Behavior checks

- Strip renders after PDP section load with no JS dependency.
- Missing icon mapping falls back to text without Liquid errors.
- Reveal-on-scroll classes remain valid when setting is enabled.

## Verification checklist (user visual confirmation)

1. Compare draft PDP payment strip and theme PDP at ~390px and ~1280px.
2. Confirm icon order and sizes (Visa, BLIK, PayPo, Przelewy24).
3. Confirm lock icon placement and secure payment label alignment.
4. Report any mismatch with screenshot + viewport.

## Risks / edge cases

- Some vendor SVGs include embedded styles/filters and may render differently if constrained incorrectly.
- Existing CSS selectors could still style new markup if not fully scoped.
- Merchant may set overly long secure label text causing mobile wrap differences.

Mitigations:
- Use explicit scoped icon classes for heights/contain behavior.
- Keep payment snippet class namespace isolated.
- Verify mobile and desktop in browser after implementation.

## Validation and wrap-up

- Shopify Dev MCP `validate_theme`: pending
- Files expected in implementation summary:
  - `snippets/lusena-pdp-payment.liquid`
  - `snippets/lusena-pdp-styles.liquid`
  - `assets/<payment-icons>.svg`
- Optional after approval:
  - Update `docs/THEME_CHANGES.md`
  - Create commit
