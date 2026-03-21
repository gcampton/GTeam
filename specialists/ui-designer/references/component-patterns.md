# UI Component Design Patterns Reference

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Patterns are described at the decision level — when to use what, what to avoid, and specific rules rather than general advice.

---

## Button Hierarchy

**Rule: one primary button per view.** If everything is primary, nothing is primary.

| Variant | Appearance | When to use |
|---------|-----------|-------------|
| Primary | Filled, brand colour, high contrast | The single most important action on the screen |
| Secondary | Outlined or lightly filled, lower visual weight | Important but not the default action; used alongside primary |
| Ghost | Text-only or very subtle hover, no border | Tertiary actions, inline actions, cancel/dismiss |
| Destructive | Red/danger colour fill or outline | Irreversible actions (delete, revoke, permanently remove) |
| Disabled | Low opacity (40–50%), no hover state | Action not currently available — only use if the reason is clear or a tooltip explains it |

**Rules:**
- Never place two primary buttons next to each other. If you have two equal-weight actions, one is secondary.
- Destructive buttons should not be the only button in a row. Always pair with a cancel/go-back option.
- Button label = verb + object. "Save changes" not "Submit". "Delete project" not "Delete".
- Loading state: disable button + show spinner inline. Keep button the same size. Never remove it.
- Size: default 36–40px height for desktop, 44px+ for mobile primary actions.

`[HYPOTHESIS]` Ghost buttons are frequently under-contrast — a ghost button with light grey text on white may fail 4.5:1 even with a border. Check contrast on all button states including default, hover, and disabled.

---

## Form Design

### Validation Timing
- **Validate on blur** (when user leaves the field), not on keydown/keyup. Live validation while typing creates anxiety and false errors.
- **Exception:** Password strength meters can update on keydown — they add information without blocking the user.
- **After first submit attempt:** switch to on-change validation so users get real-time feedback while fixing errors.

### Layout Rules
- Single-column form layout for most forms — multi-column causes scan-order confusion and reduces completion rates.
- `[HYPOTHESIS]` Exceptions: name fields (first/last side-by-side is culturally expected), city/state/zip on a single line where the grouping is meaningful.
- Field width should hint at expected input length: short fields for short inputs (phone, zip), full-width for open text.
- Group related fields under a visible section heading or `<fieldset>`. Don't make users guess what a block of fields is for.

### Multi-Step Forms
- Show a progress indicator (steps 1/3, or a progress bar) — users abandon when they don't know how long something is.
- Validate each step before advancing. Don't surface all errors at the end.
- Allow backward navigation without data loss.
- Label steps meaningfully ("Account details" not "Step 1").

### Error Handling
- Place error message directly below the relevant field, not at top of form only.
- Link error to field with `aria-describedby` (see `accessibility-wcag.md`).
- On form submit failure, focus the first error field.

---

## Cards

### Padding Consistency
- Use the same internal padding across all cards in a set. Mixing 16px and 24px padding on adjacent cards creates visual noise.
- Standard padding: 16–24px. Use 24px for content-heavy cards, 16px for compact list-style cards.

### Hover State
- Cards that are clickable should have a hover state. Minimum: subtle shadow increase or background tint shift.
- Do not use hover to reveal essential information — users on touch devices have no hover.
- Hover transform (`translateY(-2px)`) is common but use with `will-change: transform` and `prefers-reduced-motion` check.

### Link Target
- **Whole card is clickable:** Use for navigation cards where the card represents a single destination. Wrap in `<a>`, or use a stretched-link technique with `position: relative`.
- **Only title is clickable:** Use for mixed-action cards with multiple interactive elements (share, save, view). Prevents accidental navigation.
- Never have a clickable card that contains interactive elements where the hit areas conflict. Either the whole card navigates, or specific elements do — not both.

`[HYPOTHESIS]` Whole-card links break predictably when cards contain buttons — click on button triggers navigation instead. Audit card interactivity before choosing pattern.

---

## Navigation

### Breakpoints
- Hamburger menu at **≤768px** (standard tablet breakpoint). At 769px+, show horizontal or sidebar nav.
- Do not collapse nav at 1024px+ unless navigation has more than 8–10 items.

### Active State
- The current page/section must be visually distinct from other nav items. Use: filled background, left border accent, bold weight, or a combination.
- Active state must be distinguishable from hover state — they are different meanings.
- Never rely on colour alone for active state (see `accessibility-wcag.md`).

### Nested Nav Anti-Patterns
- Avoid more than 2 levels of nested navigation. Three levels deep requires users to hold too much mental context.
- Mega-menus: acceptable for e-commerce with many categories; avoid for apps and tools.
- Hover-triggered sub-menus are problematic on touch and for keyboard users — prefer click-triggered or always-expanded secondary nav.
- Breadcrumbs are not a substitute for nav. Add breadcrumbs for deep hierarchies but keep primary nav intact.

---

## Empty States

**Rule: every list, table, or content area must have a designed empty state.**

Empty state anatomy:
1. **Illustration or icon** — something that communicates the category of thing that's missing (not a generic empty box)
2. **Heading** — short, states the situation ("No projects yet")
3. **Supporting text** — one sentence explaining why or what to expect
4. **Primary action** — the single thing the user should do ("Create your first project")

`[HYPOTHESIS]` Empty states are the highest-return low-effort design improvement for new products. They reduce confusion, increase activation, and show product polish. Build them for every entity list.

Never show:
- An empty table with just column headers
- A blank content area with no explanation
- A generic "No results" with no action

---

## Loading States

### Skeleton Screens vs Spinners

| Pattern | When to use |
|---------|-------------|
| Skeleton screens | Content-heavy views where layout is predictable: feeds, lists, cards, dashboards |
| Spinner (inline) | Buttons during form submission, small inline async actions |
| Spinner (page-level) | Avoid — causes layout shift; prefer skeleton |
| Progress bar | Long operations where meaningful progress can be reported (uploads, imports) |

Skeleton rules:
- Match the shape of real content as closely as possible. A generic grey rectangle doesn't prepare users for the layout.
- Animate with a shimmer (left-to-right wave) rather than pulse — shimmer signals "loading content" more clearly.
- Don't show skeletons for < 300ms loads — it creates unnecessary visual noise.

### Button Loading State
1. Disable the button (prevent double-submit)
2. Replace label text with spinner icon, or add spinner inline before the text ("Saving...")
3. Keep button the same visual size — don't collapse or expand
4. On completion: either restore button label or redirect

---

## Error States

| Error type | Pattern | When to use |
|-----------|---------|-------------|
| Inline (field-level) | Text below input, red accent, icon | Form validation errors, field-specific issues |
| Toast / snackbar | Timed overlay, non-blocking, usually bottom of screen | Operation feedback that doesn't require user action ("Saved", "Failed to connect") |
| Inline banner | Persistent message in page flow, dismissible | Page-level warnings that don't block but need acknowledgement ("Email not verified") |
| Modal / dialog | Blocking overlay, requires user decision | Critical errors or decisions the user must resolve before continuing |
| Full-page error | Replaces main content | 404, 500, empty permissions state |

Rules:
- Toast errors should not auto-dismiss — errors need to be read and understood. Success messages can auto-dismiss (3–5s).
- Never show a modal for a non-critical error. Modals interrupt flow; reserve for destructive confirms and blocking states.
- Every error message should state: what happened + what to do. "Something went wrong" alone is not useful.

---

## Tables

- [ ] **Sticky header** — for tables longer than ~10 rows, the column headers must stay visible when scrolling. Use `position: sticky; top: 0`.
- [ ] **Sortable columns** — indicate sortability with an icon (↑↓ or chevrons). Show current sort column and direction clearly. Default sort should be the most useful order (recent first for time-series, alphabetical for entity lists).
- [ ] **Row actions** — place at the end (right) of each row, right-aligned. Show on row hover or always visible for primary action. Use a `…` overflow menu for 3+ row actions.
- [ ] **No horizontal scroll on mobile** — instead: stack columns, hide less-important columns, or switch to a card-based list view at ≤768px. Horizontal scroll tables are never acceptable as the primary mobile experience.
- [ ] **Row selection** — checkboxes in first column for bulk actions. Bulk action toolbar appears above table when rows are selected.
- [ ] **Empty state** — see Empty States section above.
- [ ] **Pagination vs infinite scroll** — pagination for datasets where users need to navigate to a specific page or position; infinite scroll for feeds where position doesn't matter.

`[HYPOTHESIS]` Table design is where most admin UI falls apart. Invest time in the responsive strategy early — retrofitting a wide desktop table for mobile is significantly more work than designing mobile-first.

### Column Alignment

| Content type | Alignment |
|---|---|
| Text (names, labels) | Left |
| Numbers (currency, counts) | Right (decimal-aligned) |
| Dates | Left or right (be consistent) |
| Status badges | Left or center |
| Actions | Right, end of row |
