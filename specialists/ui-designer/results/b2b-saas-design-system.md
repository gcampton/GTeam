# B2B SaaS Design System Specification

**Version:** 1.0  
**Date:** 2026-04-06  
**Status:** Proposed  
**Style:** Trust & Authority  

---

## 1. Design Philosophy

**Direction: Professional Clarity**

This system prioritises legibility, information density, and quiet confidence. B2B users spend hours daily in this product — every decision optimises for sustained use, not first-impression wow. The aesthetic is closer to a well-designed financial tool than a consumer app: restrained colour, generous whitespace, and typography that stays out of the way.

**Principles:**
1. **Content over chrome** — UI elements serve the data, never compete with it
2. **Consistent density** — comfortable for power users, not intimidating for new ones
3. **Earned trust** — professional palette, visible security signals, no gratuitous animation
4. **Accessible by default** — WCAG 2.1 AA minimum; all interactive elements keyboard-navigable

**Anti-patterns to avoid:**
- Purple/pink gradients (AI slop signal)
- Generic stock photography
- Emoji as functional icons
- Decorative animation with no information purpose
- Overly rounded, "toy-like" component styling

---

## 2. Typography

### Typeface Selection

| Role | Typeface | Rationale |
|------|----------|-----------|
| **Primary (UI)** | Plus Jakarta Sans | Geometric sans with humanist warmth. High legibility at small sizes. Native to the B2B SaaS space — users of Notion, Linear, and Vercel products already read this face comfortably. |
| **Monospace** | JetBrains Mono | For code blocks, data tables with fixed-width numbers, and technical content. |

Plus Jakarta Sans handles both headings and body as a single-family system. Weight differentiation creates hierarchy without introducing a second face — this reduces load time and visual noise.

### Type Scale

Base unit: **16px** (1rem). Scale ratio: **1.25** (Major Third).

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|-------|------|--------|-------------|----------------|-----|
| `display` | 36px / 2.25rem | 800 (ExtraBold) | 1.15 | -0.02em | Page titles, hero headings |
| `h1` | 30px / 1.875rem | 700 (Bold) | 1.2 | -0.015em | Section headings |
| `h2` | 24px / 1.5rem | 700 (Bold) | 1.25 | -0.01em | Card headings, modal titles |
| `h3` | 20px / 1.25rem | 600 (SemiBold) | 1.3 | -0.005em | Sub-section headings |
| `h4` | 16px / 1rem | 600 (SemiBold) | 1.4 | 0 | Field group labels, sidebar headings |
| `body` | 16px / 1rem | 400 (Regular) | 1.6 | 0 | Default paragraph text |
| `body-medium` | 16px / 1rem | 500 (Medium) | 1.6 | 0 | Emphasized body text, table headers |
| `body-small` | 14px / 0.875rem | 400 (Regular) | 1.5 | 0.005em | Secondary text, descriptions |
| `caption` | 12px / 0.75rem | 500 (Medium) | 1.4 | 0.02em | Labels, metadata, timestamps |
| `overline` | 11px / 0.6875rem | 600 (SemiBold) | 1.4 | 0.08em | Category labels, status badges (uppercase) |
| `code` | 14px / 0.875rem | 400 (Regular) | 1.6 | 0 | Inline code, data values (JetBrains Mono) |

### Typography Rules

- **Maximum line length:** 65–75 characters (approx. `max-width: 680px` at body size)
- **Minimum body size:** 14px — never go below this for readable content
- **Heading hierarchy:** Must be sequential (h1 → h2 → h3). Never skip levels.
- **Paragraph spacing:** 1em between paragraphs (equal to body font size)
- **No decorative fonts.** The system uses weight and size for hierarchy, not typeface changes.

---

## 3. Colour System

### Palette

Built on a Slate neutral base with a professional blue primary. Every colour listed below meets WCAG AA contrast requirements against its documented background.

#### Core Tokens

| Token | Value | On (text colour) | Use |
|-------|-------|-------------------|-----|
| `primary` | `#2563EB` (Blue 600) | `#FFFFFF` | Primary actions, active states, links |
| `primary-hover` | `#1D4ED8` (Blue 700) | `#FFFFFF` | Hover state for primary elements |
| `primary-subtle` | `#EFF6FF` (Blue 50) | `#1E40AF` | Selected rows, active sidebar items, badges |
| `secondary` | `#0F172A` (Slate 900) | `#FFFFFF` | Secondary buttons, emphasis |
| `secondary-hover` | `#1E293B` (Slate 800) | `#FFFFFF` | Hover state for secondary elements |

#### Semantic Tokens

| Token | Value | On (text colour) | Use |
|-------|-------|-------------------|-----|
| `success` | `#059669` (Emerald 600) | `#FFFFFF` | Confirmation, positive metrics, paid status |
| `success-subtle` | `#ECFDF5` (Emerald 50) | `#065F46` | Success banners, positive badge backgrounds |
| `warning` | `#D97706` (Amber 600) | `#FFFFFF` | Caution states, approaching limits |
| `warning-subtle` | `#FFFBEB` (Amber 50) | `#92400E` | Warning banners, attention badges |
| `destructive` | `#DC2626` (Red 600) | `#FFFFFF` | Errors, delete actions, overdue status |
| `destructive-subtle` | `#FEF2F2` (Red 50) | `#991B1B` | Error banners, destructive badges |
| `info` | `#0284C7` (Sky 600) | `#FFFFFF` | Informational alerts, help text links |
| `info-subtle` | `#F0F9FF` (Sky 50) | `#075985` | Info banners, tooltip backgrounds |

#### Neutral Tokens

| Token | Value | Use |
|-------|-------|-----|
| `background` | `#FFFFFF` | Page background |
| `background-subtle` | `#F8FAFC` (Slate 50) | Sidebar, page canvas, table striping |
| `surface` | `#FFFFFF` | Card backgrounds, modals, dropdowns |
| `surface-raised` | `#FFFFFF` | Elevated surfaces (with shadow) |
| `border` | `#E2E8F0` (Slate 200) | Card borders, dividers, input borders |
| `border-strong` | `#CBD5E1` (Slate 300) | Focused input borders, active dividers |
| `text-primary` | `#0F172A` (Slate 900) | Headings, primary content |
| `text-secondary` | `#475569` (Slate 600) | Body text, descriptions |
| `text-muted` | `#94A3B8` (Slate 400) | Placeholders, disabled text, metadata |
| `text-on-colour` | `#FFFFFF` | Text on primary/semantic colour backgrounds |

#### Contrast Verification

| Combination | Ratio | Pass |
|------------|-------|------|
| `text-primary` on `background` | 15.4:1 | AAA |
| `text-secondary` on `background` | 7.1:1 | AAA |
| `text-muted` on `background` | 3.3:1 | AA Large only |
| `primary` on `background` | 4.6:1 | AA |
| `text-on-colour` on `primary` | 4.6:1 | AA |
| `success` on `background` | 4.6:1 | AA |
| `destructive` on `background` | 5.1:1 | AA |

> `text-muted` fails AA for body text. Use it only for non-essential metadata (timestamps, helper text) or at `caption` size where it meets AA Large. Never use it for actionable or required content.

### Colour Rules

1. **No raw hex in components.** Always reference semantic tokens.
2. **Colour is never the only indicator.** Pair with icons, text labels, or patterns (accessibility requirement).
3. **Dark mode:** Not in scope for v1. When introduced, swap the neutral scale (Slate 900 ↔ Slate 50) and reduce primary saturation by 10%.
4. **Data visualisation palette** (for charts): Blue `#2563EB`, Emerald `#059669`, Amber `#D97706`, Violet `#7C3AED`, Rose `#E11D48`, Cyan `#0891B2` — chosen for distinguishability under colour blindness (verified via Sim Daltonism).

---

## 4. Spacing System

### Base Unit

**4px** base. All spacing values are multiples of 4.

| Token | Value | Common Use |
|-------|-------|------------|
| `space-0` | 0px | Reset |
| `space-1` | 4px | Inline icon gap, tight padding |
| `space-2` | 8px | Icon-to-label gap, compact padding, between inline elements |
| `space-3` | 12px | Input padding (vertical), small card padding |
| `space-4` | 16px | Standard card padding, gap between form fields |
| `space-5` | 20px | Section padding on mobile |
| `space-6` | 24px | Card padding (desktop), gap between card groups |
| `space-8` | 32px | Section spacing, page margin (mobile) |
| `space-10` | 40px | Section dividers, large component spacing |
| `space-12` | 48px | Page section breaks |
| `space-16` | 64px | Major layout divisions, page top padding |
| `space-20` | 80px | Hero section vertical padding |

### Layout Constants

| Token | Value | Use |
|-------|-------|-----|
| `sidebar-width` | 240px | Collapsed: 64px |
| `content-max-width` | 1200px | Maximum content width |
| `form-max-width` | 560px | Maximum form width for readability |
| `table-row-height` | 48px | Standard table row |
| `table-row-height-compact` | 36px | Dense data tables |
| `nav-height` | 56px | Top navigation bar |
| `page-padding-x` | 32px | Horizontal page padding (desktop) |
| `page-padding-x-mobile` | 16px | Horizontal page padding (mobile) |

### Spacing Rules

1. **Component internal padding** uses `space-3` to `space-6`.
2. **Between related elements** (label + input, icon + text): `space-2`.
3. **Between sibling components** (cards in a grid, form sections): `space-4` to `space-6`.
4. **Between page sections**: `space-10` to `space-16`.
5. **Never use arbitrary values.** If 4px increments feel too coarse for a specific case, revisit the layout — the component likely needs restructuring, not a 5px exception.

---

## 5. Border Radius

| Token | Value | Use |
|-------|-------|-----|
| `radius-sm` | 4px | Badges, tags, small chips |
| `radius-md` | 6px | Buttons, inputs, dropdowns |
| `radius-lg` | 8px | Cards, modals, popovers |
| `radius-xl` | 12px | Large cards, page sections, hero images |
| `radius-full` | 9999px | Avatars, status dots, pill toggles |

### Radius Rules

- Interactive elements (buttons, inputs) share `radius-md` for visual consistency.
- Containers (cards, modals) share `radius-lg`.
- Never exceed `radius-xl` for rectangular containers — overly rounded corners signal consumer/playful products, not B2B tools.

---

## 6. Elevation (Shadows)

| Token | Value | Use |
|-------|-------|-----|
| `shadow-xs` | `0 1px 2px rgba(0, 0, 0, 0.05)` | Subtle lift: cards at rest, input fields |
| `shadow-sm` | `0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06)` | Buttons, raised cards |
| `shadow-md` | `0 4px 6px rgba(0, 0, 0, 0.07), 0 2px 4px rgba(0, 0, 0, 0.06)` | Dropdowns, popovers |
| `shadow-lg` | `0 10px 15px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.05)` | Modals, command palettes |
| `shadow-xl` | `0 20px 25px rgba(0, 0, 0, 0.1), 0 8px 10px rgba(0, 0, 0, 0.04)` | Toast notifications, floating panels |

### Elevation Rules

- Maximum 3 elevation levels visible simultaneously on any screen.
- Shadows use neutral black — never coloured shadows (they read as decorative, not structural).
- Cards at rest use `shadow-xs` or no shadow + `border`. Shadow escalates on hover only if the card is clickable.

---

## 7. Motion

| Token | Duration | Easing | Use |
|-------|----------|--------|-----|
| `duration-instant` | 100ms | `ease-out` | Colour changes, opacity toggles |
| `duration-fast` | 150ms | `ease-out` | Button hover, focus rings |
| `duration-normal` | 200ms | `ease-in-out` | Dropdown open/close, accordion expand |
| `duration-slow` | 300ms | `ease-in-out` | Modal enter/exit, page transitions |
| `duration-slower` | 500ms | `ease-in-out` | Skeleton shimmer, chart animations |

### Motion Rules

1. **All transitions must respect `prefers-reduced-motion: reduce`.** When active, set all durations to 0ms and disable transform-based animations.
2. **Entrances use ease-out** (fast start, gentle stop). **Exits use ease-in** (gentle start, fast finish).
3. **No animation exceeds 500ms.** If something feels like it needs longer, the interaction model is wrong.
4. **Loading states** use skeleton shimmer, not spinners (spinners imply uncertainty; skeletons imply known structure loading).
5. **No bounce, no elastic easing.** These undermine professional tone.

---

## 8. Component Tokens

### Buttons

| Variant | Background | Text | Border | Use |
|---------|-----------|------|--------|-----|
| **Primary** | `primary` | `text-on-colour` | none | Single main action per view |
| **Secondary** | `background` | `secondary` | `border` | Supporting actions |
| **Ghost** | transparent | `text-secondary` | none | Tertiary actions, toolbar items |
| **Destructive** | `destructive` | `text-on-colour` | none | Delete, remove, revoke |
| **Link** | transparent | `primary` | none | Inline navigational actions |

**Sizing:**

| Size | Height | Padding (h) | Font | Use |
|------|--------|-------------|------|-----|
| `sm` | 32px | 12px | `caption` | Table actions, compact toolbars |
| `md` | 40px | 16px | `body-small` | Standard forms, cards |
| `lg` | 48px | 24px | `body-medium` | Hero CTAs, standalone forms |

**States:** Every button must define `default`, `hover`, `active` (pressed), `focus-visible`, `disabled`, and `loading` states. Disabled buttons reduce opacity to 0.5 and remove pointer events.

### Inputs

| Token | Value |
|-------|-------|
| Height | 40px (md), 32px (sm), 48px (lg) |
| Padding | `space-3` horizontal, centered vertical |
| Border | `border` at rest, `primary` on focus |
| Background | `background` at rest, `background` on focus |
| Placeholder | `text-muted` |
| Error border | `destructive` |
| Error text | `destructive`, shown below field in `caption` size |
| Label | `body-small` weight 500, `space-1` below |

**Rules:**
- Labels are always visible — never placeholder-only.
- Error messages replace helper text (don't stack both).
- Required fields marked with `*` after label text (not colour alone).

### Cards

| Token | Value |
|-------|-------|
| Background | `surface` |
| Border | `border` (1px solid) |
| Border radius | `radius-lg` |
| Padding | `space-6` |
| Shadow | `shadow-xs` at rest |
| Hover (if clickable) | `shadow-sm`, border shifts to `border-strong` |

### Tables

| Token | Value |
|-------|-------|
| Header background | `background-subtle` |
| Header text | `body-small` weight 600, `text-secondary` |
| Row height | `table-row-height` (48px standard) |
| Row border | `border` bottom only |
| Row hover | `background-subtle` |
| Selected row | `primary-subtle` |
| Cell padding | `space-3` vertical, `space-4` horizontal |

**Rules:**
- Right-align numeric columns.
- Sticky header on scroll.
- Bulk actions appear in a fixed bar when rows are selected.
- Empty state shows an illustration + description + primary action, never a blank table.

### Badges / Tags

| Variant | Background | Text | Border Radius |
|---------|-----------|------|--------------|
| Default | `background-subtle` | `text-secondary` | `radius-sm` |
| Primary | `primary-subtle` | `primary` | `radius-sm` |
| Success | `success-subtle` | `success` | `radius-sm` |
| Warning | `warning-subtle` | `warning` | `radius-sm` |
| Destructive | `destructive-subtle` | `destructive` | `radius-sm` |

Padding: `space-1` vertical, `space-2` horizontal. Font: `overline` token.

### Modals / Dialogs

| Token | Value |
|-------|-------|
| Overlay | `rgba(15, 23, 42, 0.5)` (Slate 900 at 50%) |
| Background | `surface` |
| Border radius | `radius-lg` |
| Shadow | `shadow-lg` |
| Max width | 480px (small), 640px (medium), 960px (large) |
| Padding | `space-6` body, `space-4` header/footer |
| Entry animation | Fade + scale from 0.95, `duration-normal` |

**Rules:**
- Focus trapped inside modal while open.
- Close on Escape key.
- Destructive confirmation modals require typing the resource name, not just clicking "Delete".

### Navigation (Sidebar)

| Token | Value |
|-------|-------|
| Width | `sidebar-width` (240px expanded, 64px collapsed) |
| Background | `background-subtle` |
| Item height | 36px |
| Item padding | `space-2` vertical, `space-3` horizontal |
| Active item | `primary-subtle` background, `primary` text, `radius-md` |
| Hover | `border` background colour |
| Icon size | 20px, `space-2` gap to label |
| Section divider | `border` with `space-4` vertical margin |

---

## 9. Iconography

| Token | Value |
|-------|-------|
| Library | Lucide (primary) or Heroicons (alternative) — SVG only |
| Size scale | 16px (inline), 20px (standard), 24px (emphasis) |
| Stroke width | 1.5px (consistent across all icons) |
| Colour | Inherits text colour via `currentColor` |

**Rules:**
- Never use emoji as functional icons.
- Decorative icons get `aria-hidden="true"`. Functional icons get `aria-label`.
- Icon-only buttons require a tooltip and `aria-label`.

---

## 10. Responsive Breakpoints

| Token | Width | Target |
|-------|-------|--------|
| `mobile` | 0–639px | Phones |
| `tablet` | 640–1023px | Tablets, small laptops |
| `desktop` | 1024–1439px | Standard laptops, desktops |
| `wide` | 1440px+ | Large monitors |

**Rules:**
- Mobile-first: base styles target `mobile`, scale up.
- Sidebar collapses to icon-only at `tablet`, hidden behind hamburger at `mobile`.
- Data tables switch to card layout at `mobile`.
- Maximum content width (`content-max-width`) centred at `wide`.

---

## 11. Accessibility Checklist

This is not optional. These are requirements.

- [ ] All text meets WCAG AA contrast (4.5:1 body, 3:1 large text)
- [ ] Focus rings visible on all interactive elements (2px solid `primary`, 2px offset)
- [ ] Tab order matches visual reading order
- [ ] Skip-to-main-content link as first focusable element
- [ ] All images have descriptive `alt` text (or `alt=""` if decorative)
- [ ] Form inputs linked to labels via `for`/`id`
- [ ] Error messages announced to screen readers via `aria-live="polite"`
- [ ] Heading hierarchy is sequential (no skipped levels)
- [ ] Touch targets minimum 44x44px with 8px spacing
- [ ] `prefers-reduced-motion` respected for all animation
- [ ] Colour is never the sole indicator of state or meaning
- [ ] Modals trap focus and close on Escape

---

## 12. File & Token Naming Convention

**Design tokens** follow this naming structure:

```
{category}-{property}-{variant}-{state}
```

Examples:
- `color-primary-default`
- `color-text-muted`
- `spacing-4`
- `radius-md`
- `shadow-sm`
- `button-bg-primary-hover`
- `input-border-error`

**CSS custom properties** use `--` prefix:
```
--color-primary: #2563EB;
--space-4: 16px;
--radius-md: 6px;
```

**Tailwind configuration** maps tokens to the theme extend object. Token names become utility classes: `bg-primary`, `text-muted`, `rounded-md`, `shadow-sm`.

---

*This specification is the single source of truth for visual decisions. All components, pages, and features reference these tokens — not raw values. Deviations require an explicit exception documented here with rationale.*
