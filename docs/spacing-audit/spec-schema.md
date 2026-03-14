# Spacing Audit Spec Schema

## File structure

Each spec file is a JSON file in `docs/spacing-audit/specs/` named `{page}-{viewport}.json`.

Examples: `homepage-desktop.json`, `pdp-mobile.json`, `quality-desktop.json`

## Top-level fields

| Field | Type | Description |
|-------|------|-------------|
| `page` | string | Page identifier (homepage, pdp, quality, etc.) |
| `url` | string | URL path to test (e.g., `/`, `/products/...`) |
| `viewport` | `{width, height}` | Target viewport size in pixels |
| `tolerancePx` | number | Default tolerance for all gap checks (default: 4) |
| `notes` | string | Optional description |
| `sectionGaps` | array | Expected gaps between adjacent sections |
| `sections` | object | Per-section spacing expectations |

## Section gaps

```json
{
  "between": ["hero", "trust"],
  "expectedGapPx": 0
}
```

Matches sections by their short ID (the part after `shopify-section-template--{id}__`).

## Section definitions

```json
{
  "matchClass": "lusena-heritage",
  "expectedPaddingTop": 96,
  "expectedPaddingBottom": 96,
  "containers": { ... }
}
```

- `matchClass`: A CSS class on the inner `<section>` element (must be unique within the page)
- `expectedPaddingTop` / `expectedPaddingBottom`: In pixels
- `containers`: Keyed by container selector (`.lusena-container`, `.lusena-container--narrow`)

## Container children

Each container has an ordered array of child rules:

```json
{
  "matchClass": "lusena-text-center",
  "expectedGapToNext": 32,
  "tolerancePx": 4,
  "note": "explanation",
  "children": [ ... ]
}
```

- `matchClass`: First CSS class on the element (matched in DOM order)
- `expectedGapToNext`: Expected pixel gap to the next sibling (transform-compensated)
- `tolerancePx`: Override tolerance for this specific check
- `repeat`: If `true`, this rule matches multiple consecutive siblings with the same class
- `children`: Nested child rules (for depth > 1)

## How matching works

1. Sections are matched by finding an inner `<section>` whose class list contains `matchClass`
2. Container children are matched in DOM order — first child rule matches first visible child with that class, then removed from candidates
3. If a child has `repeat: true`, it matches all consecutive siblings with that class
4. Gaps are only checked when `expectedGapToNext` is present — omitted means "don't check"

## Tolerance

- Default: `tolerancePx` at top level (recommended: 4px)
- Per-rule override: `tolerancePx` on any child rule
- A check passes if `|measured - expected| <= tolerance`
