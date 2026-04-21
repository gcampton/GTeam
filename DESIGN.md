# B2B SaaS Design System Specification

> Source of truth for all visual and interaction design decisions.
> Generated 2026-04-06 by GTeam UI Designer.

---

## 1. Design Direction

**Aesthetic:** Professional Clarity — clean, structured, trust-forward. Swiss modernist roots with warm approachability. Not cold corporate, not startup-playful. The product should feel like a reliable tool built by people who respect your time.

**Why this direction:** B2B buyers evaluate software for professionalism, clarity, and perceived reliability before they evaluate features. A trust-first aesthetic with strong information hierarchy reduces cognitive load in data-dense workflows and signals enterprise readiness without feeling sterile.

**Anti-patterns to avoid:**
- AI slop: purple/pink gradients, generic stock imagery, emoji as icons, Lorem Ipsum
- Visual clutter: decorative elements that don't serve hierarchy or wayfinding
- Undifferentiated neutrality: all-grey, no personality, "could be any product"

---

## 2. Typography

### Typeface Selection

| Role | Typeface | Why |
|------|----------|-----|
| **Headings** | **Plus Jakarta Sans** (600, 700, 800) | Geometric, modern, distinctive without being loud. Strong at display sizes. Designed for screens with excellent hinting. |
| **Body** | **Plus Jakarta Sans** (400, 500) | Single-family system reduces cognitive switching. Jakarta has unusually good legibility at body sizes for a geometric sans — wide apertures, generous x-height. |
| **Monospace** | **JetBrains Mono** (400, 500) | For code blocks, data tables with numeric alignment, and technical content. Designed for extended reading, not just terminal use. |

**Fallback stack:** `'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`

### Type Scale

Base size: **16px** (1rem). Scale ratio: **1.25** (Major Third).

| Token | Size | Weight | Line Height | Letter Spacing | Usage |
|-------|------|--------|-------------|----------------|-------|
| `display-xl` | 48px / 3rem | 800 | 1.1 | -0.02em | Hero headlines, marketing pages |
| `display-lg` | 36px / 2.25rem | 700 | 1.15 | -0.015em | Page titles, section heroes |
| `heading-1` | 30px / 1.875rem | 700 | 1.2 | -0.01em | Primary page headings |
| `heading-2` | 24px / 1.5rem | 600 | 1.25 | -0.005em | Section headings, card titles |
| `heading-3` | 20px / 1.25rem | 600 | 1.3 | 0 | Subsection headings |
| `heading-4` | 16px / 1rem | 600 | 1.4 | 0.01em | Label headings, sidebar sections |
| `body-lg` | 18px / 1.125rem | 400 | 1.6 | 0 | Lead paragraphs, feature descriptions |
| `body` | 16px / 1rem | 400 | 1.6 | 0 | Default body text |
| `body-sm` | 14px / 0.875rem | 400 | 1.5 | 0.005em | Secondary text, table cells, metadata |
| `caption` | 12px / 0.75rem | 500 | 1.4 | 0.02em | Labels, timestamps, helper text |
| `overline` | 11px / 0.6875rem | 600 | 1.3 | 0.08em | Category tags, uppercase labels |

### Typography Rules

- **Maximum line length:** 65-75 characters for body text. Use `max-width: 65ch` on text containers.
- **Heading hierarchy must be sequential.** Never skip from h1 to h3. Screen readers navigate by heading level.
- **Optical kerning** on headings at display-xl and display-lg sizes: `letter-spacing: -0.02em` to -0.015em.
- **Never apply negative letter-spacing to body text.** It reduces legibility at small sizes.
- **Minimum text size:** 12px for any visible text. 11px overline is the absolute floor.

---

## 3. Colour System

### Palette

Built on semantic tokens, not raw hex values. Every colour has a named role.

#### Core Palette

| Token | Value | On-colour | Usage |
|-------|-------|-----------|-------|
| `primary` | `#0F172A` | `#FFFFFF` | Navigation, primary text, strong emphasis |
| `primary-hover` | `#1E293B` | `#FFFFFF` | Hover state for primary elements |
| `secondary` | `#334155` | `#FFFFFF` | Secondary actions, icons, supporting text |
| `accent` | `#2563EB` | `#FFFFFF` | Interactive elements, links, selected states |
| `accent-hover` | `#1D4ED8` | `#FFFFFF` | Hover on interactive elements |
| `accent-light` | `#DBEAFE` | `#1E40AF` | Accent backgrounds, selected row highlights |

#### Surface Palette

| Token | Value | Usage |
|-------|-------|-------|
| `background` | `#F8FAFC` | Page background, app shell |
| `surface` | `#FFFFFF` | Cards, panels, modals, dropdowns |
| `surface-raised` | `#FFFFFF` | Elevated surfaces (with shadow) |
| `surface-sunken` | `#F1F5F9` | Inset areas, code blocks, input backgrounds |
| `surface-overlay` | `rgba(15, 23, 42, 0.5)` | Modal/dialog backdrop |

#### Text Palette

| Token | Value | Contrast on surface | Usage |
|-------|-------|---------------------|-------|
| `text-primary` | `#0F172A` | 16.75:1 | Headings, primary content |
| `text-secondary` | `#475569` | 7.09:1 | Supporting text, descriptions |
| `text-muted` | `#64748B` | 4.62:1 | Timestamps, helper text, placeholders |
| `text-disabled` | `#94A3B8` | 2.84:1 | Disabled labels (paired with disabled controls) |
| `text-inverse` | `#FFFFFF` | — | Text on dark/coloured backgrounds |

#### Semantic Palette

| Token | Value | On-colour | Light BG | Usage |
|-------|-------|-----------|----------|-------|
| `success` | `#059669` | `#FFFFFF` | `#ECFDF5` | Completed, saved, active, healthy |
| `warning` | `#D97706` | `#FFFFFF` | `#FFFBEB` | Attention needed, approaching limit |
| `error` | `#DC2626` | `#FFFFFF` | `#FEF2F2` | Errors, destructive actions, failed |
| `info` | `#2563EB` | `#FFFFFF` | `#EFF6FF` | Informational notices, tips |

#### Border Palette

| Token | Value | Usage |
|-------|-------|-------|
| `border-default` | `#E2E8F0` | Card borders, dividers, input borders |
| `border-strong` | `#CBD5E1` | Emphasized separators |
| `border-focus` | `#2563EB` | Focus ring colour (2px solid + 2px offset) |
| `border-error` | `#DC2626` | Error state input borders |

### Colour Rules

- **All body text must meet WCAG AA:** 4.5:1 minimum contrast ratio against its background. `text-muted` at 4.62:1 is the floor — never go lighter.
- **Large text (24px+ or 18.67px+ bold):** 3:1 minimum.
- **Semantic colours are not decoration.** Green means success. Red means error or destructive. Don't repurpose them for branding.
- **Never use colour as the only indicator.** Always pair with an icon, label, or pattern change.
- **CTA colour:** Use `accent` (#2563EB) for primary CTAs. One primary CTA per view — everything else is secondary or ghost.

---

## 4. Spacing System

### Base Unit

**4px** atomic unit. Every spacing value is a multiple of 4.

### Scale

| Token | Value | Usage |
|-------|-------|-------|
| `space-0` | 0px | Reset, no spacing |
| `space-0.5` | 2px | Hairline gaps (icon-to-text micro-adjust) |
| `space-1` | 4px | Tight internal padding, inline gaps |
| `space-2` | 8px | Compact element spacing, button icon gap |
| `space-3` | 12px | Input padding, small card padding |
| `space-4` | 16px | Standard card padding, element gaps |
| `space-5` | 20px | Section padding in compact views |
| `space-6` | 24px | Content-heavy card padding, form gaps |
| `space-8` | 32px | Section spacing within a page |
| `space-10` | 40px | Major section breaks |
| `space-12` | 48px | Page-level section spacing |
| `space-16` | 64px | Hero spacing, top-of-page breathing room |
| `space-20` | 80px | Page section dividers, major landmarks |
| `space-24` | 96px | Hero vertical padding, landing sections |

### Spacing Rules

- **Consistent internal padding:** All cards in a set use the same padding. Standard: 24px for content-rich cards, 16px for compact/list cards.
- **Related elements are closer together** (Gestalt proximity). Label 4px above input. Help text 4px below input. Groups of fields separated by 24px.
- **Vertical rhythm:** Body text at 16px with 1.6 line-height = 25.6px. Spacing between paragraphs should be a multiple of this rhythm (24px or 32px).
- **Never mix scales.** Pick one and apply consistently. Harmony matters more than any specific ratio.

---

## 5. Layout

### Grid

| Breakpoint | Columns | Gutter | Margin | Token |
|------------|---------|--------|--------|-------|
| `xs` 0–639px | 4 | 16px | 16px | Mobile |
| `sm` 640–767px | 6 | 16px | 24px | Large mobile |
| `md` 768–1023px | 8 | 24px | 32px | Tablet |
| `lg` 1024–1279px | 12 | 24px | 32px | Desktop |
| `xl` 1280–1535px | 12 | 32px | 48px | Large desktop |
| `2xl` 1536px+ | 12 | 32px | auto (max-width: 1440px, centered) | Wide |

### Layout Principles

- **Max content width:** 1440px. Beyond this, center content with auto margins.
- **Sidebar navigation:** 240px collapsed to icon-only 64px. Sidebar is persistent on lg+, toggleable on md, hidden (hamburger) on sm and below.
- **Sticky header:** Fixed navigation must compensate with equal `padding-top` on the body. Never allow nav to overlap content.
- **Breadcrumbs** for any interface with 3+ levels of navigation depth.
- **Active nav state** must be visually distinct: bold weight + accent colour + left border or underline.

---

## 6. Elevation & Depth

### Shadow Scale

| Token | Value | Usage |
|-------|-------|-------|
| `shadow-none` | none | Flat elements, inline content |
| `shadow-xs` | `0 1px 2px rgba(15, 23, 42, 0.05)` | Subtle lift: inputs, chips |
| `shadow-sm` | `0 1px 3px rgba(15, 23, 42, 0.08), 0 1px 2px rgba(15, 23, 42, 0.04)` | Cards at rest |
| `shadow-md` | `0 4px 6px rgba(15, 23, 42, 0.08), 0 2px 4px rgba(15, 23, 42, 0.04)` | Cards on hover, dropdowns |
| `shadow-lg` | `0 10px 15px rgba(15, 23, 42, 0.08), 0 4px 6px rgba(15, 23, 42, 0.04)` | Modals, popovers, floating panels |
| `shadow-xl` | `0 20px 25px rgba(15, 23, 42, 0.1), 0 8px 10px rgba(15, 23, 42, 0.04)` | Dialogs, command palettes |

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `radius-none` | 0px | Hard-edge elements (full-width dividers) |
| `radius-sm` | 4px | Chips, tags, small badges |
| `radius-md` | 6px | Inputs, buttons, small cards |
| `radius-lg` | 8px | Cards, panels, modals |
| `radius-xl` | 12px | Feature cards, hero elements |
| `radius-full` | 9999px | Avatars, pills, toggle tracks |

### Depth Rules

- **Elevation correlates with interactivity.** Static content is flat. Interactive surfaces lift on hover. Overlays use the highest elevation.
- **Shadows use the primary colour tinted** (slate-900 at low opacity), not pure black. This integrates shadows with the palette.
- **Consistent radius within component families.** All cards use `radius-lg`. All inputs use `radius-md`. Don't mix.

---

## 7. Component Tokens

### Buttons

| Variant | Background | Text | Border | Hover BG | Active BG |
|---------|-----------|------|--------|----------|-----------|
| **Primary** | `accent` | `text-inverse` | none | `accent-hover` | `#1E40AF` |
| **Secondary** | `surface` | `text-primary` | `border-default` | `surface-sunken` | `#E2E8F0` |
| **Ghost** | transparent | `accent` | none | `accent-light` | `#BFDBFE` |
| **Destructive** | `error` | `text-inverse` | none | `#B91C1C` | `#991B1B` |
| **Disabled** | `#E2E8F0` | `text-disabled` | none | — | — |

| Size | Height | Padding (h) | Font | Radius |
|------|--------|-------------|------|--------|
| `sm` | 32px | 12px | `body-sm` (14px), weight 600 | `radius-md` |
| `md` | 40px | 16px | `body` (16px), weight 600 | `radius-md` |
| `lg` | 48px | 24px | `body-lg` (18px), weight 600 | `radius-md` |

**Button rules:**
- One primary button per view. If two actions compete, one is secondary.
- Destructive buttons always paired with a cancel option. Never standalone.
- Loading state: disable + inline spinner. Button keeps its size. Never remove or collapse.
- Minimum touch target: 44x44px (even if visual button is smaller, the hit area must meet this).

### Inputs

| State | Border | Background | Label | Helper Text |
|-------|--------|-----------|-------|-------------|
| **Default** | `border-default` | `surface-sunken` | `text-secondary` | `text-muted` |
| **Hover** | `border-strong` | `surface-sunken` | `text-secondary` | `text-muted` |
| **Focus** | `border-focus` (2px) + ring | `surface` | `text-primary` | `text-muted` |
| **Error** | `border-error` | `surface` | `error` | `error` |
| **Disabled** | `border-default` | `#F1F5F9` | `text-disabled` | `text-disabled` |

| Property | Value |
|----------|-------|
| Height | 40px (md), 32px (sm), 48px (lg) |
| Padding | 12px horizontal, centered vertical |
| Border radius | `radius-md` (6px) |
| Label position | Above input, 4px gap |
| Helper/error text | Below input, 4px gap |

**Input rules:**
- Field width hints at expected input length. Short fields for phone/zip. Full-width for open text.
- Focus ring must be visible: 2px solid `accent` with 2px offset. This is a WCAG requirement.
- Error messages appear inline below the field, not in a toast. Use red icon + text, not colour alone.

### Cards

| Property | Value |
|----------|-------|
| Background | `surface` |
| Border | 1px solid `border-default` |
| Border radius | `radius-lg` (8px) |
| Padding | 24px (content-rich) or 16px (compact/list) |
| Shadow | `shadow-sm` at rest, `shadow-md` on hover (if interactive) |

**Card rules:**
- All cards in a set use identical padding. Mixing 16px and 24px on adjacent cards creates visual noise.
- **Clickable card:** Entire card is the tap target. Use for navigation cards with a single destination.
- **Action card:** Contains multiple interactive elements (buttons, links). Only specific elements are clickable — not the whole card.
- Never combine whole-card click with internal buttons. The hit areas conflict.

### Tables

| Property | Value |
|----------|-------|
| Header background | `surface-sunken` |
| Header text | `text-secondary`, `caption` size, weight 600, uppercase |
| Row height | 48px minimum |
| Row border | 1px solid `border-default` (bottom only) |
| Row hover | `surface-sunken` background |
| Cell padding | 12px horizontal, centered vertical |
| Selected row | `accent-light` background |

**Table rules:**
- Sticky header for tables longer than ~10 rows. Column headers must remain visible when scrolling.
- Sortable columns show direction icon (chevron). Current sort column and direction clearly indicated.
- Mobile: switch to card-based layout at breakpoint `sm` and below. Horizontal-scroll tables are not acceptable as the primary mobile experience. Use `overflow-x: auto` as a fallback, not the strategy.
- Row selection via checkbox in first column. Bulk action toolbar appears above table when rows are selected.

### Badges & Tags

| Variant | Background | Text | Border |
|---------|-----------|------|--------|
| Default | `#F1F5F9` | `text-secondary` | none |
| Success | `success-light` | `#065F46` | none |
| Warning | `warning-light` | `#92400E` | none |
| Error | `error-light` | `#991B1B` | none |
| Info | `info-light` | `#1E40AF` | none |

Size: 24px height, `caption` font, `radius-sm` (4px), 8px horizontal padding.

### Navigation

| Element | Specification |
|---------|--------------|
| Sidebar width | 240px expanded, 64px collapsed (icon-only) |
| Sidebar background | `primary` (#0F172A) |
| Sidebar text | `#94A3B8` default, `#FFFFFF` active |
| Active indicator | 3px left border `accent`, background `rgba(37, 99, 235, 0.1)` |
| Nav item height | 40px |
| Nav item padding | 12px horizontal |
| Top bar height | 56px |
| Top bar background | `surface` with 1px bottom border |

### Modals & Dialogs

| Property | Value |
|----------|-------|
| Overlay | `surface-overlay` |
| Panel background | `surface` |
| Border radius | `radius-xl` (12px) |
| Shadow | `shadow-xl` |
| Width | 480px (sm), 640px (md), 800px (lg) |
| Padding | 24px body, 16px-24px header/footer |
| Close button | Top-right, 44x44px hit area minimum |

---

## 8. Interaction & Motion

### Timing

| Token | Duration | Easing | Usage |
|-------|----------|--------|-------|
| `duration-instant` | 0ms | — | Opacity toggles, immediate state changes |
| `duration-fast` | 100ms | `ease-out` | Hover colour changes, focus rings |
| `duration-normal` | 200ms | `ease-out` | Button transitions, dropdown open, tooltip show |
| `duration-slow` | 300ms | `ease-in-out` | Modal enter/exit, sidebar expand/collapse |
| `duration-slower` | 500ms | `ease-in-out` | Page transitions, skeleton → content reveal |

### Motion Rules

- **Enter:** `ease-out` (fast start, gentle stop). Elements arrive with confidence.
- **Exit:** `ease-in` (gentle start, fast finish). Elements leave quickly.
- **Micro-interactions (hover, focus, toggle):** 150-200ms. Snappy but not instant.
- **Layout shifts (expand, collapse, reorder):** 200-300ms. Smooth but not sluggish.
- **`prefers-reduced-motion: reduce`** must be respected. Reduce all animations to opacity-only transitions or disable entirely. This is non-negotiable.
- **No auto-playing animations** that loop indefinitely. Loading spinners are the exception.

### Interactive States

Every interactive element must have all five states defined:

| State | Visual Treatment |
|-------|-----------------|
| **Default** | Base appearance |
| **Hover** | Subtle background shift or shadow lift. 150ms transition. |
| **Focus** | 2px solid `accent` ring with 2px offset. Always visible — never remove the default outline without replacing it. |
| **Active/Pressed** | Slight darken or scale(0.98). Immediate feedback. |
| **Disabled** | 40% opacity or muted colours. `cursor: not-allowed`. Remove from tab order or mark `aria-disabled`. |

---

## 9. Accessibility Requirements

These are not optional. They are the floor, not the ceiling.

| Requirement | Specification |
|-------------|--------------|
| **Text contrast** | 4.5:1 minimum (body), 3:1 minimum (large text 24px+) |
| **Interactive contrast** | 3:1 minimum for UI components and graphical objects |
| **Focus indicators** | Visible on all interactive elements. 2px solid ring, contrasting colour. |
| **Keyboard navigation** | All functionality operable via keyboard. Tab order matches visual order. No keyboard traps. |
| **Skip link** | "Skip to main content" link as first focusable element on every page. |
| **Touch targets** | 44x44px minimum. 8px minimum gap between adjacent targets. |
| **Alt text** | All meaningful images. Decorative images use `alt=""`. |
| **ARIA labels** | All icon-only buttons have `aria-label`. All form inputs have associated labels. |
| **Heading hierarchy** | Sequential h1-h6. One h1 per page. No skipped levels. |
| **Colour independence** | Never use colour as the sole indicator. Pair with icons, labels, or patterns. |
| **Reduced motion** | Respect `prefers-reduced-motion`. Provide static alternatives. |
| **Error identification** | Errors described in text, not just by colour. Associated with the relevant field via `aria-describedby`. |

---

## 10. Iconography

| Property | Specification |
|----------|--------------|
| **Library** | Lucide Icons (preferred) or Heroicons. SVG only — never emoji as UI icons. |
| **Default size** | 20x20px (matches body text). 16px for compact/inline. 24px for navigation. |
| **Stroke width** | 1.5px (consistent with both Lucide and Heroicons defaults) |
| **Colour** | Inherits from `currentColor`. Icons follow text colour of their context. |
| **Touch target** | Icon buttons are minimum 44x44px hit area regardless of visual icon size. |

---

## 11. Empty, Loading, and Error States

Every view must have all three designed. These are not afterthoughts.

### Empty States

- Illustration (optional) + headline + description + primary action
- Never show an empty table with just column headers
- Tone: helpful, not apologetic. Tell the user what to do next.

### Loading States

| Context | Pattern |
|---------|---------|
| Initial page load | Skeleton screens matching the final layout shape |
| Data refresh | Subtle shimmer on existing content, no layout shift |
| Form submission | Button disabled + inline spinner, same button size |
| Background operation | Toast notification with progress, non-blocking |

### Error States

| Context | Pattern |
|---------|---------|
| Form validation | Inline below field, red icon + text, `aria-describedby` linked |
| API/network error | Banner at top of content area, retry action available |
| 404/missing page | Full-page with navigation back, search, or home link |
| Permission denied | Explanation of what's needed, who to contact |

---

## 12. Dark Mode Considerations

This spec defines the light theme as primary. When implementing dark mode:

- Invert surface hierarchy: darkest surface is the background, lighter surfaces are elevated.
- Do not simply invert all colours. Reduce text brightness to ~87% white (`#DEE2E6`) to avoid eye strain.
- Semantic colours need dark-mode variants with adjusted saturation (desaturate slightly, increase lightness).
- Re-verify all contrast ratios — dark mode often introduces contrast failures.
- Shadows become less effective on dark backgrounds. Use subtle borders or luminance shifts instead.

---

## Appendix: Design Token Summary

All tokens in one reference table for engineering handoff.

```
// Typography
--font-heading:     'Plus Jakarta Sans', sans-serif
--font-body:        'Plus Jakarta Sans', sans-serif
--font-mono:        'JetBrains Mono', monospace

// Colours — Core
--color-primary:       #0F172A
--color-secondary:     #334155
--color-accent:        #2563EB
--color-accent-hover:  #1D4ED8
--color-accent-light:  #DBEAFE

// Colours — Surface
--color-bg:            #F8FAFC
--color-surface:       #FFFFFF
--color-surface-sunken:#F1F5F9

// Colours — Text
--color-text:          #0F172A
--color-text-secondary:#475569
--color-text-muted:    #64748B

// Colours — Semantic
--color-success:       #059669
--color-warning:       #D97706
--color-error:         #DC2626
--color-info:          #2563EB

// Colours — Border
--color-border:        #E2E8F0
--color-border-focus:  #2563EB
--color-border-error:  #DC2626

// Spacing (4px base)
--space-1:  4px    --space-2:  8px    --space-3: 12px
--space-4: 16px    --space-5: 20px    --space-6: 24px
--space-8: 32px    --space-10: 40px   --space-12: 48px
--space-16: 64px   --space-20: 80px   --space-24: 96px

// Radius
--radius-sm:   4px    --radius-md:   6px
--radius-lg:   8px    --radius-xl:  12px
--radius-full: 9999px

// Shadows
--shadow-xs:  0 1px 2px rgba(15,23,42,0.05)
--shadow-sm:  0 1px 3px rgba(15,23,42,0.08), 0 1px 2px rgba(15,23,42,0.04)
--shadow-md:  0 4px 6px rgba(15,23,42,0.08), 0 2px 4px rgba(15,23,42,0.04)
--shadow-lg:  0 10px 15px rgba(15,23,42,0.08), 0 4px 6px rgba(15,23,42,0.04)
--shadow-xl:  0 20px 25px rgba(15,23,42,0.1), 0 8px 10px rgba(15,23,42,0.04)

// Motion
--duration-fast:   100ms    --duration-normal: 200ms
--duration-slow:   300ms    --duration-slower: 500ms
--ease-out:   cubic-bezier(0, 0, 0.2, 1)
--ease-in:    cubic-bezier(0.4, 0, 1, 1)
--ease-in-out:cubic-bezier(0.4, 0, 0.2, 1)
```

---

*This design system is a living document. Update it as decisions are tested and refined in production. Every rule here has a reason — if you need to break one, document why.*
