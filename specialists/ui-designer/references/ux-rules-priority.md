# UX Rules by Priority

Source: ui-ux-pro-max-skill (BM25-searchable database with 99 UX guidelines, 50+ styles, 161 colour palettes, 57 font pairings).

Use the search tool for real-time queries: `python3 $UIPRO "<keyword>" --domain ux`

## Priority Order

| Priority | Category | Impact | Key Threshold |
|----------|----------|--------|---------------|
| 1 | Accessibility | CRITICAL | Contrast 4.5:1, keyboard nav, aria-labels |
| 2 | Touch & Interaction | CRITICAL | Min 44×44px, 8px spacing, loading feedback |
| 3 | Performance | HIGH | WebP/AVIF, lazy load, CLS < 0.1 |
| 4 | Style Selection | HIGH | Match product type, SVG icons, consistency |
| 5 | Layout & Responsive | HIGH | Mobile-first, no horizontal scroll, 4pt/8dp spacing |
| 6 | Typography & Color | MEDIUM | 16px min body, line-height 1.5, semantic tokens |
| 7 | Animation | MEDIUM | 150–300ms, ease-out enter, prefers-reduced-motion |
| 8 | Forms & Feedback | MEDIUM | Visible labels, error below field, submit feedback |
| 9 | Navigation Patterns | HIGH | Predictable back, bottom nav ≤5, deep links |
| 10 | Charts & Data | LOW | Legend, tooltip, accessible colour pairs |

---

## 1. Accessibility (CRITICAL)

- **color-contrast** — 4.5:1 minimum for normal text; 3:1 for large text (18pt+)
- **focus-states** — Visible focus rings on all interactive elements (2–4px offset)
- **alt-text** — Descriptive alt text for meaningful images; `alt=""` for decorative
- **aria-labels** — `aria-label` for icon-only buttons; `accessibilityLabel` in native
- **keyboard-nav** — Tab order matches visual order; full keyboard support
- **form-labels** — `<label for="...">` on every input; never placeholder-only
- **skip-links** — "Skip to main content" link for keyboard users
- **heading-hierarchy** — Sequential h1→h2→h3; never skip levels
- **color-not-only** — Don't convey information by colour alone (add icon or text)
- **dynamic-type** — Support system text scaling; no truncation as text grows
- **reduced-motion** — Respect `prefers-reduced-motion`; disable/reduce animations
- **escape-routes** — Provide cancel/back in all modals and multi-step flows

## 2. Touch & Interaction (CRITICAL)

- **touch-target-size** — Min 44×44pt (Apple) / 48×48dp (Material); extend hit area if needed
- **touch-spacing** — 8px/8dp minimum gap between adjacent touch targets
- **hover-vs-tap** — Primary interactions use click/tap; never rely on hover alone
- **loading-buttons** — Disable button during async; show spinner or progress
- **error-feedback** — Clear error message near the problem; not only at top
- **cursor-pointer** — Add `cursor: pointer` to all clickable elements on web
- **tap-delay** — Use `touch-action: manipulation` to eliminate 300ms delay
- **press-feedback** — Visual feedback on press (ripple/highlight)
- **safe-area-awareness** — Keep targets away from notch, Dynamic Island, gesture bar

## 3. Performance (HIGH)

- **image-optimization** — WebP/AVIF, responsive `srcset/sizes`, lazy load off-screen
- **image-dimension** — Declare `width`/`height` or `aspect-ratio` to prevent CLS
- **font-loading** — `font-display: swap`; preload only critical fonts
- **bundle-splitting** — Split by route/feature; React Suspense / Next.js dynamic imports
- **content-jumping** — Reserve space for async content; CLS < 0.1
- **virtualize-lists** — Virtualise lists with 50+ items
- **progressive-loading** — Skeleton/shimmer for operations > 1 second
- **debounce-throttle** — Debounce scroll, resize, and input handlers

## 4. Style Selection (HIGH)

- **style-match** — Match style to product type (`python3 $UIPRO "<product>" --design-system`)
- **consistency** — Same style family across all pages; no mixing flat + skeuomorphic
- **no-emoji-icons** — Use SVG icon sets (Heroicons, Lucide, Phosphor); never emojis as icons
- **color-palette-from-product** — Choose palette from industry conventions (`--domain color`)
- **dark-mode-pairing** — Design light/dark variants together; desaturated not inverted
- **icon-style-consistent** — One icon set throughout; consistent stroke width and corner radius
- **primary-action** — One primary CTA per screen; all secondary actions visually subordinate
- **elevation-consistent** — Consistent shadow scale (4 levels max); no random shadow values

## 5. Layout & Responsive (HIGH)

- **viewport-meta** — `width=device-width, initial-scale=1`; never disable zoom
- **mobile-first** — Design mobile first, then scale up to tablet and desktop
- **breakpoints** — Systematic: 375 / 768 / 1024 / 1440
- **readable-font-size** — Min 16px body on mobile (prevents iOS auto-zoom)
- **line-length** — 35–60 chars mobile; 60–75 chars desktop
- **horizontal-scroll** — Zero horizontal scroll on mobile
- **spacing-scale** — 4pt/8dp incremental system throughout
- **container-width** — Consistent max-width on desktop (`max-w-6xl` / `max-w-7xl`)
- **fixed-element-offset** — Fixed navbar/bottom bar reserves safe padding below it
- **viewport-units** — Use `min-h-dvh` not `100vh` on mobile

## 6. Typography & Color (MEDIUM)

- **line-height** — 1.5–1.75 for body text
- **font-pairing** — Match heading/body personalities (`python3 $UIPRO "<style>" --domain typography`)
- **font-scale** — Consistent type scale: 12 14 16 18 24 32 48
- **weight-hierarchy** — Bold headings (600–700), Regular body (400), Medium labels (500)
- **color-semantic** — Semantic tokens (primary, error, surface) — no raw hex in components
- **color-dark-mode** — Dark mode: desaturated/lighter tonal variants; test contrast separately
- **color-accessible-pairs** — Foreground/background ≥ 4.5:1 (AA) or 7:1 (AAA)
- **whitespace-balance** — Use whitespace to group related items; avoid visual clutter

## 7. Animation (MEDIUM)

- **duration-timing** — 150–300ms micro-interactions; complex ≤ 400ms; never > 500ms
- **transform-performance** — Animate only `transform` and `opacity`; never `width/height/top/left`
- **loading-states** — Skeleton or progress indicator when loading > 300ms
- **easing** — ease-out for entering; ease-in for exiting; never linear for UI transitions
- **motion-meaning** — Every animation expresses cause-effect; zero decorative-only animations
- **interruptible** — Animations must be interruptible on user input immediately
- **stagger-sequence** — 30–50ms stagger per list/grid item entrance

## 8. Forms & Feedback (MEDIUM)

- **input-labels** — Visible label on every input; placeholder is supplementary, not a label
- **error-placement** — Error message directly below the related field
- **submit-feedback** — Loading → success/error state on every form submit
- **required-indicators** — Mark required fields with asterisk and legend
- **empty-states** — Helpful message + action when no content exists
- **toast-dismiss** — Auto-dismiss toasts in 3–5 seconds; position non-blocking
- **confirmation-dialogs** — Confirm before destructive or irreversible actions
- **inline-validation** — Validate on blur (not on keystroke); show errors after user finishes input
- **error-recovery** — Every error message includes a clear recovery path (retry/edit/help link)
- **form-autosave** — Long forms auto-save drafts to prevent data loss

## 9. Navigation Patterns (HIGH)

- **bottom-nav-limit** — Bottom nav max 5 items; always icon + label
- **back-behavior** — Back navigation predictable and consistent; preserve scroll/state
- **deep-linking** — All key screens reachable via deep link / URL
- **nav-state-active** — Current location visually highlighted (colour, weight, indicator)
- **modal-escape** — Every modal/sheet has a clear close affordance; swipe-down on mobile
- **state-preservation** — Back navigation restores scroll position, filters, and input
- **adaptive-navigation** — ≥ 1024px: sidebar; < 1024px: bottom/top nav
- **no-mixed-patterns** — Don't mix Tab + Sidebar + Bottom Nav at the same hierarchy level

## 10. Charts & Data (LOW)

- **chart-type** — Match chart to data: trend → line; comparison → bar; proportion → donut
- **color-guidance** — Accessible palettes; never red/green only (colourblind users)
- **legend-visible** — Always show legend positioned near the chart
- **tooltip-on-interact** — Hover (web) / tap (mobile) tooltip showing exact values
- **axis-labels** — Label axes with units; readable scale; no rotated labels on mobile
- **responsive-chart** — Reflow or simplify on small screens
- **empty-data-state** — "No data yet" message + guidance; never a blank chart frame
- **no-pie-overuse** — Pie/donut only for ≤ 5 categories; switch to bar for more

---

## Domain Search Quick Reference

```bash
# Full design system (always start here for new projects)
python3 $UIPRO "<product> <industry> <keywords>" --design-system -p "Project Name"

# Specific domain
python3 $UIPRO "<keyword>" --domain ux          # UX best practices
python3 $UIPRO "<keyword>" --domain style       # UI styles (glassmorphism, brutalism, etc.)
python3 $UIPRO "<keyword>" --domain color       # Colour palettes by product type
python3 $UIPRO "<keyword>" --domain typography  # Font pairings + Google Fonts imports
python3 $UIPRO "<keyword>" --domain chart       # Chart types and library recommendations
python3 $UIPRO "<keyword>" --domain landing     # Landing page structure + CTA strategies

# Stack-specific guidelines
python3 $UIPRO "<keyword>" --stack nextjs
python3 $UIPRO "<keyword>" --stack react
python3 $UIPRO "<keyword>" --stack vue
python3 $UIPRO "<keyword>" --stack svelte
python3 $UIPRO "<keyword>" --stack react-native
python3 $UIPRO "<keyword>" --stack flutter
```
