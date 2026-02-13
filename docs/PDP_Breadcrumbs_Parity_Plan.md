# Product + Collection Breadcrumbs — Draftshop Parity Plan

Date: 2026-02-09

## Goal

Port the draft shop PDP breadcrumbs fragment (Home → Category → Product title) into the Shopify theme so it matches **exactly** on mobile and desktop (layout, spacing, typography, colors, truncation, hover state, and icon), and reuse the same fragment on the collection page.

## Scope

- Show breadcrumbs on:
  - Product page (PDP)
  - Collection page
- Match draft markup semantics: `<nav aria-label="Breadcrumb">`, `<ol>`, `<li>`, links, current item as plain text.
- Match visual + interaction parity (same class list as draft):
  - Padding and spacing (`py-4`, `gap-1.5`)
  - Typography (`text-xs`, current item `font-semibold`)
  - Colors (`text-neutral-700`, chevron `text-neutral-400`, current item `text-primary`)
  - Hover state on links (`hover:text-primary` + `transition-colors duration-150`)
  - Current item truncation (`truncate` + `max-w-[200px]`)
  - Chevron-right icon sizing (`w-3 h-3`)

## Non-goals

- Adding breadcrumbs to every page type (homepage/pages/blog/article/cart/search/etc.).
- Adding structured data (BreadcrumbList) in this iteration.
- Changing Dawn’s global typography scale or layout system.

## Source of Truth (Draft Shop)

- Component: `lusena-shop/src/components/product/Breadcrumbs.tsx`
- Usage on PDP: `lusena-shop/src/pages/Product.tsx`
- Data shape used by the component: `lusena-shop/src/lib/products.ts` (`categoryPath` + `title`)

## Target in Theme

- Product section: `sections/lusena-main-product.liquid`
- Collection section: `sections/lusena-main-collection.liquid`
- New snippet: `snippets/lusena-breadcrumbs.liquid` (LiquidDoc header required)
- Icon source: `snippets/lusena-icon.liquid` (add `chevron-right` icon to match Lucide ChevronRight)
- Tailwind utility patching (if missing in `assets/lusena-shop.css` build): `snippets/lusena-missing-utilities.liquid`

## Decisions (final)

- Pages that show breadcrumbs: product + collection only.
- Text labels are hardcoded (no locales):
  - Home label: `Strona główna`
  - Product category label (PDP middle crumb): `Jedwab` (hardcoded, draft parity)
- Product page category link behavior:
  - If a collection context exists (product opened from a collection page): use `collection.url`.
  - If no collection context:
    - If `collections['jedwab']` exists, link to that collection’s URL.
    - Otherwise fall back to `/collections/all`.
- Current item:
  - On product page: `product.title` (not a link)
  - On collection page: `collection.title` (not a link)
- Breakpoints follow the existing LUSENA Tailwind utilities already used on the PDP (`md:` at 768px).
- Parity standard:
  - Visual + interaction parity matches the draft breadcrumbs fragment.
  - Category link is intentionally dynamic in Shopify (depending on collection context) while keeping the exact same visual treatment.

## Open Questions / Unresolved Assumptions

- None.

## Data Sources & Content Model

- Product page:
  - `routes.root_url` for Home
  - `collection` (optional) for category URL
  - `product.title` for current item
- Collection page:
  - `routes.root_url` for Home
  - `collection.title` for current item

## Target UX Spec

- Container: inside the standard `.container` used by LUSENA sections.
- Vertical rhythm: `py-4` (top + bottom).
- Inline list:
  - `ol` is a single row with chevrons between crumbs.
  - Chevrons use Lucide-like SVG (from `lusena-icon`).
  - Current item truncates to `200px` and never wraps.
- Accessibility:
  - `nav` has `aria-label="Breadcrumb"`.
  - Current item is plain text; links remain real `<a>` elements.

## Implementation Approach

1. Create `snippets/lusena-breadcrumbs.liquid` that renders the fragment with the same class list as the draft.
2. Render the snippet at the top of `sections/lusena-main-product.liquid` (inside the section’s `.container`, above the grid).
3. Render the snippet at the top of `sections/lusena-main-collection.liquid` (inside the section’s `.container`, above the collection content).
4. Extend `snippets/lusena-icon.liquid` with a `chevron-right` case matching Lucide ChevronRight.
5. If any Tailwind utility classes used by the fragment are missing from `assets/lusena-shop.css`, add minimal definitions to `snippets/lusena-missing-utilities.liquid` (keep scope tight to only what’s needed for parity).

## Milestones / Deliverables

- Breadcrumbs visible on PDP and matching the draft fragment for:
  - Mobile (~390px)
  - Desktop (~1280px)
- Breadcrumbs visible on collection page using the same visual style.

## Verification Checklist

Manual:
- Verify crumb order, labels, and URLs.
- Verify hover state on the first two crumbs.
- Verify chevron alignment and sizing.
- Verify current item truncation at `200px` and that it does not wrap.

Shopify validation:
- Run Shopify Dev MCP `validate_theme` for all changed files (conversationId: `b33ed46a-24d7-4e3e-8d00-b7389b2b9b38`).

Playwright:
- Confirm `http://127.0.0.1:9292/` is running (start via `shopify theme dev` if needed).
- Capture screenshots on PDP and collection page at mobile and desktop widths.
- Compare PDP screenshots to the draft shop PDP breadcrumbs fragment (visual parity).

## Risks / Edge Cases

- Very long titles: ensure truncation matches draft (`truncate` + `max-w-[200px]`).
- Product opened directly (no `collection` context): fallback behavior must still render a working category link.
- Tailwind utility gaps: if `assets/lusena-shop.css` doesn’t include the required utility classes, add them to `snippets/lusena-missing-utilities.liquid`.

