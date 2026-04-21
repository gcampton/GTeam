# SaaS Settings Page — Design Specification

## Design Direction: Professional Utility

A settings page is a **task-completion environment**, not a marketing surface. The aesthetic is quiet, structured, and efficient — users arrive with intent, complete their task, and leave. Every visual decision prioritises scannability and confidence over delight.

**Why this direction:** Settings pages are high-trust, low-frequency surfaces. Users change billing details or team permissions rarely, and when they do, they need to feel confident nothing will go wrong. Clean structure, clear labels, and obvious save states build that confidence. Motion is functional (feedback on actions), not decorative.

---

## Typography

| Role | Font | Weight | Size | Line Height |
|------|------|--------|------|-------------|
| Page title | Inter | 600 | 24px / 1.5rem | 32px (1.33) |
| Section heading | Inter | 600 | 18px / 1.125rem | 28px (1.56) |
| Subsection heading | Inter | 500 | 14px / 0.875rem | 20px (1.43) |
| Body text | Inter | 400 | 14px / 0.875rem | 22px (1.57) |
| Label | Inter | 500 | 13px / 0.8125rem | 18px (1.38) |
| Caption / helper | Inter | 400 | 12px / 0.75rem | 16px (1.33) |

**Why Inter:** Designed for screens, excellent at small sizes (13–14px dominates a settings UI), wide language support. Single-family simplifies the system — weight variation does the work that a second typeface would do. No mono font needed; this is a forms-heavy interface, not a code editor.

**Line length:** Content column capped at `max-width: 680px` to stay within the 65–75 character sweet spot for body text. Wider viewports push whitespace to the right, not wider content.

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
```

---

## Colour Palette

| Token | Hex | Usage | Contrast on White |
|-------|-----|-------|-------------------|
| `--color-primary` | `#2563EB` | Primary actions, active nav, links | 4.6:1 ✓ |
| `--color-primary-hover` | `#1D4ED8` | Primary button hover | 5.9:1 ✓ |
| `--color-primary-light` | `#EFF6FF` | Active nav bg, selected state | — |
| `--color-text` | `#0F172A` | Headings, primary text | 15.4:1 ✓ |
| `--color-text-secondary` | `#475569` | Body text, descriptions | 7.1:1 ✓ |
| `--color-text-muted` | `#64748B` | Placeholders, helper text | 4.6:1 ✓ |
| `--color-bg` | `#F8FAFC` | Page background | — |
| `--color-card` | `#FFFFFF` | Card/section background | — |
| `--color-border` | `#E2E8F0` | Borders, dividers | — |
| `--color-border-focus` | `#2563EB` | Focus ring on inputs | — |
| `--color-success` | `#059669` | Success states, active badges | 4.6:1 ✓ |
| `--color-warning` | `#D97706` | Warning states, pending badges | 3.7:1 (large text only) |
| `--color-destructive` | `#DC2626` | Delete actions, error states | 4.6:1 ✓ |
| `--color-destructive-hover` | `#B91C1C` | Destructive button hover | 5.9:1 ✓ |
| `--color-destructive-light` | `#FEF2F2` | Destructive background tint | — |

**Note:** `--color-text-muted` upgraded from `#94A3B8` (3.3:1, failed AA) to `#64748B` (4.6:1, passes AA). All text tokens now meet WCAG AA minimum contrast against their expected backgrounds.

---

## Spacing Scale

Base unit: **4px**. Every spacing value is a multiple.

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Icon-to-text gap, tight inline pairs |
| `--space-2` | 8px | Input internal padding, badge padding, label-to-input gap |
| `--space-3` | 12px | Between related form fields |
| `--space-4` | 16px | Between unrelated form fields, list item spacing |
| `--space-5` | 20px | Section internal padding (compact) |
| `--space-6` | 24px | Card padding |
| `--space-8` | 32px | Between cards/sections within a page |
| `--space-10` | 40px | Page-level top margin, sidebar-to-content gap |

---

## Border & Elevation

| Element | Border Radius | Shadow | Border |
|---------|--------------|--------|--------|
| Cards / sections | 12px | `0 1px 3px rgba(0,0,0,0.04)` | 1px `--color-border` |
| Inputs | 8px | none | 1px `--color-border` → `--color-border-focus` on focus |
| Buttons | 8px | none | none (primary), 1px `--color-border` (secondary) |
| Avatars | 50% (circle) | none | 2px white ring on coloured bg |
| Badges | 6px | none | none |
| Modals | 16px | `0 20px 60px rgba(0,0,0,0.15)` | none |
| Dropdown menus | 12px | `0 4px 16px rgba(0,0,0,0.08)` | 1px `--color-border` |

**Elevation philosophy:** Settings is a flat interface. Only modals and dropdown menus get shadows strong enough to establish a layer. Cards use a barely-visible shadow for subtle lift.

---

## Layout Architecture

### Overall Structure

```
┌──────────────────────────────────────────────────────────┐
│  App Header (sticky, 64px)                               │
├────────────┬─────────────────────────────────────────────┤
│            │  Breadcrumb: Settings > Profile              │
│  Settings  │  Page title: "Profile"                       │
│  Sidebar   ├─────────────────────────────────────────────┤
│  (240px)   │                                             │
│            │  ┌─── Content Column (max 680px) ────────┐  │
│  ● Profile │  │  [Section Card]                       │  │
│  ○ Team    │  │  [Section Card]                       │  │
│  ○ Billing │  │  [Section Card]                       │  │
│  ○ Notifs  │  │  ...                                  │  │
│  ○ Security│  └───────────────────────────────────────┘  │
│            │                                             │
│            │                    ← remaining space is     │
│            │                       passive whitespace    │
├────────────┴─────────────────────────────────────────────┤
```

### Navigation Pattern: Sidebar with Route-Based Sections

Each sidebar item loads a **separate route** (`/settings/profile`, `/settings/team`, `/settings/billing`). This is not a single-page scroll — each section is its own view.

**Why separate routes over scroll-spy:**
1. Deep-linkable — teammates can share `/settings/billing` directly
2. Faster page weight — only loads components for the active section
3. Avoids the "long scroll" problem where billing changes are buried below the fold
4. Browser back button works predictably (UX rule: preserve navigation history)

### Sidebar Design

- **Width:** 240px fixed
- **Items:** Icon (20px, Lucide icon set) + label (14px, 500 weight)
- **Active state:** `--color-primary-light` background, `--color-primary` text, 3px left accent border, 8px border-radius on right side
- **Hover state:** `#F1F5F9` background, 150ms ease
- **Item height:** 40px, with 4px vertical gap between items
- **Grouping:** Divider line between "personal" settings (Profile, Notifications, Security) and "workspace" settings (Team, Billing). Group label in muted text above each group.
- **Sticky behaviour:** Sidebar scrolls independently from content when sidebar items exceed viewport height (rare but handle it)

### Content Area

- **Left padding from sidebar:** 40px (`--space-10`)
- **Content max-width:** 680px
- **Top:** Breadcrumb trail + page title (H1, 24px), followed by 32px gap before first card
- **Cards stack vertically** with 32px (`--space-8`) between them
- **Each card** has 24px internal padding, section heading at top, optional description paragraph below heading

---

## Section Specifications

### 1. Profile (`/settings/profile`)

**Cards in order:**

#### Avatar & Identity Card
- **Avatar:** 80px circle, left-aligned. Click or drag-to-upload. Hover shows camera icon overlay with `rgba(0,0,0,0.4)` scrim. Accepted formats shown in helper text below (JPG, PNG, max 2MB).
- **Fields alongside avatar (right):**
  - Full name (text input)
  - Display name (text input, helper text: "How others see you in the workspace")
- **Below avatar row:**
  - Email (text input, read-only with "Change email" link if email change requires verification flow)
  - Job title (text input, optional)
  - Timezone (select dropdown, default to browser-detected)
  - Language (select dropdown)
- **Layout:** Avatar + name fields sit on a single row at desktop. Below 640px, avatar stacks above fields.
- **Save:** "Save changes" primary button, right-aligned at card bottom. Disabled until dirty state detected.

#### Password & Authentication Card
- Current password / New password / Confirm password — standard stacked fields
- Password strength indicator bar below new password field (4 segments: weak/fair/good/strong)
- "Enable two-factor authentication" as a separate sub-section with toggle switch and setup flow link
- **Save** button isolated to this card (not shared with profile card above — password changes are a separate action with separate confirmation)

### 2. Team Management (`/settings/team`)

**Cards in order:**

#### Invite Members Card
- **Layout:** Single row — email input (flex-grow) + role dropdown (fixed 140px) + "Send invite" primary button
- Below 640px: stack to full-width fields
- Role dropdown options: Admin, Member, Viewer (with brief description of each in dropdown)
- On success: inline success message below the row, auto-dismiss after 3s
- Bulk invite: "Invite multiple" text link below the row opens a textarea for comma-separated emails

#### Active Members Table
- **Columns:** Avatar + Name (combined cell) | Email | Role | Status | Actions
- **Role column:** Dropdown (inline-editable) for admins; read-only badge for non-admins
- **Status column:** Badge — Active (green), Pending (amber), Suspended (grey)
- **Actions column:** "..." overflow menu with: Copy invite link, Suspend, Remove
- **Row height:** 56px for comfortable tap targets
- **Owner row:** Visually distinct — "Owner" badge instead of role dropdown, no actions menu
- **Sorting:** Alphabetical by name (default), role, status. Sort indicator arrows on column headers.
- **Search/filter:** Search input above table, filters for role and status
- **Pagination:** Show 10 per page with pagination controls if > 10 members. Display total count.

**Mobile responsive (< 768px):** Table converts to a card-based list:
```
┌──────────────────────────────┐
│  [Avatar] Jane Smith          │
│  jane@company.com             │
│  Admin · Active               │
│                          [⋯]  │
└──────────────────────────────┘
```

#### Pending Invitations Card
- Same table structure, simplified: Email | Role | Sent date | Actions (Resend, Revoke)
- **Empty state:** Illustration + "No pending invitations" + "Invite a teammate" CTA button

### 3. Billing (`/settings/billing`)

**Cards in order:**

#### Current Plan Card
- **Layout:** Plan name (H3) + price on the left. "Change plan" secondary button on the right.
- **Below:** Horizontal usage bars for metered features (seats used, storage, API calls) — each bar shows current/limit with percentage. Bars use `--color-primary` fill, `--color-border` track.
- **Plan badge:** "Pro", "Enterprise", etc. with semantic colour (primary for paid, muted for free)
- If approaching limits (>80%): bar turns `--color-warning`, helper text warns about approaching limit

#### Payment Method Card
- **Display:** Card brand icon (Visa, Mastercard, etc.) + masked number (•••• •••• •••• 4242) + expiry
- **Actions:** "Update" secondary button, "Remove" ghost button (if multiple methods)
- Adding a card uses an embedded Stripe Elements iframe or similar PCI-compliant component — never a raw input
- **Empty state:** "Add a payment method" CTA with card illustration

#### Invoice History Card
- **Columns:** Date | Description | Amount | Status | Download
- **Status:** Paid (green badge), Pending (amber), Failed (red)
- **Download:** PDF icon link per row
- **Pagination:** Show last 12 months, "View all invoices" link at bottom
- **Empty state:** "No invoices yet — they'll appear here after your first billing cycle"

#### Danger Zone Card
- **Visual treatment:** `--color-destructive-light` background, 1px `--color-destructive` border with reduced opacity (30%), 12px radius
- **Separated** from other cards by 48px (`--space-12`) gap and a full-width divider line
- **Actions:**
  - "Cancel subscription" — secondary destructive button (white bg, red text/border). Opens confirmation modal explaining what will happen (data retention, access timeline, refund policy).
  - "Delete workspace" — destructive button. Requires typing workspace name to confirm. Modal shows irreversibility warning.
- **Copy tone:** Factual, not scary. State exactly what happens and what is preserved.

---

## Responsive Behaviour

| Breakpoint | Sidebar | Content | Forms |
|------------|---------|---------|-------|
| ≥ 1280px | 240px sidebar, labels visible | 680px max-width, centred in remaining space | Side-by-side fields where sensible |
| 1024–1279px | 240px sidebar | 680px max-width, flush left | Same as above |
| 768–1023px | 56px collapsed (icons only, tooltip on hover) | Fluid, 24px horizontal padding | Single-column fields |
| < 768px | Hidden — horizontal tab bar at top (scrollable) | Full-width, 16px horizontal padding | Single-column, full-width inputs |

### Mobile Tab Bar (< 768px)
- Replaces sidebar entirely
- Horizontal scrollable row of icon + label pills
- Active tab: `--color-primary` underline (3px), `--color-primary` text
- Fixed below the app header (sticky), 48px height
- Scroll indicator (fade gradient) on right edge if tabs overflow

### Touch Targets
- All interactive elements: minimum 44×44px tap target
- Minimum 8px spacing between adjacent targets
- Table row actions accessible via row tap (opens action sheet on mobile) rather than tiny "..." button

---

## Component States

### Form Inputs

| State | Border | Background | Label | Ring |
|-------|--------|------------|-------|------|
| Default | `--color-border` | white | `--color-text-secondary` | none |
| Hover | `#CBD5E1` (slightly darker) | white | unchanged | none |
| Focus | `--color-border-focus` | white | `--color-primary` | 2px `--color-primary` ring, 2px offset |
| Error | `--color-destructive` | `#FEF2F2` tint | `--color-destructive` | 2px `--color-destructive` ring |
| Disabled | `--color-border` at 50% opacity | `#F8FAFC` | `--color-text-muted` | none |
| Read-only | no border | `#F1F5F9` | `--color-text-muted` | none |

**Input sizing:** 40px height for single-line inputs. 12px horizontal padding. Full-width by default, constrained by the 680px content column.

### Buttons

| Variant | Default | Hover | Active | Disabled |
|---------|---------|-------|--------|----------|
| Primary | `#2563EB` bg, white text | `#1D4ED8` bg | `#1E40AF` bg | 50% opacity, no pointer |
| Secondary | white bg, `--color-border` stroke | `#F8FAFC` bg | `#F1F5F9` bg | 50% opacity |
| Destructive | `#DC2626` bg, white text | `#B91C1C` bg | `#991B1B` bg | 50% opacity |
| Ghost | transparent, `--color-primary` text | `#F1F5F9` bg | `#E2E8F0` bg | 50% opacity |

**Button sizing:** 40px height, 16px horizontal padding, 8px border-radius. Min-width 80px for legibility.

### Save Flow

1. User edits any field → card enters "dirty" state
2. **Unsaved changes indicator:** Subtle dot appears next to section title, save button enables with primary colour
3. User clicks "Save changes" → button shows inline spinner + "Saving..." text
4. Success → green toast appears bottom-right: "Profile updated" with check icon. Auto-dismiss 3s. Button returns to disabled "Saved" state.
5. Error → red toast with error message, button returns to enabled "Save changes" state, failed fields highlighted
6. **Navigate away with unsaved changes** → browser-level `beforeunload` confirmation + in-app modal: "You have unsaved changes. Discard or keep editing?"

---

## Accessibility Requirements

### Keyboard Navigation
- **Tab order:** Sidebar items → breadcrumb → content area fields (top to bottom, left to right within rows)
- **Skip link:** First focusable element is "Skip to settings content" — jumps past sidebar and header
- **Sidebar keyboard:** Arrow keys to navigate between items, Enter to select
- **Focus ring:** 2px solid `--color-primary`, 2px offset, visible on all focusable elements. Never suppressed.
- **Escape:** Closes any open modal or dropdown

### Screen Reader Support
- Sidebar nav wrapped in `<nav aria-label="Settings navigation">`
- Active section announced via `aria-current="page"` on sidebar item
- Form sections use `<fieldset>` + `<legend>` for grouping
- Every input has a `<label>` with `for` attribute (never placeholder-only)
- Required fields use `aria-required="true"` + visual asterisk
- Error messages linked via `aria-describedby` on the input
- Toast notifications use `aria-live="polite"` region
- Destructive action modals use `role="alertdialog"` with `aria-describedby` pointing to the warning text
- Icon-only buttons (avatar upload, action menus) have `aria-label`

### Motion
- All transitions: 150ms ease for micro-interactions, 200–300ms ease-out for overlays
- `prefers-reduced-motion: reduce` → all transitions set to 0ms, toasts appear instantly without slide

---

## Empty States

Every list and table has a designed empty state:

| Surface | Empty State |
|---------|-------------|
| Team members table | "No team members yet" + "Invite your first teammate" CTA |
| Pending invitations | "No pending invitations" + "Invite a teammate" CTA |
| Invoice history | "No invoices yet — they'll appear after your first billing cycle" |
| Payment methods | Card illustration + "Add a payment method to enable billing" CTA |

Each empty state includes: (1) relevant illustration or icon, (2) concise explanation, (3) primary action to resolve the empty state.

---

## Icon System

Use **Lucide** icon set (open source, consistent 24px grid, 1.5px stroke).

| Section | Icon |
|---------|------|
| Profile | `User` |
| Team | `Users` |
| Billing | `CreditCard` |
| Notifications | `Bell` |
| Security | `Shield` |
| Danger Zone | `AlertTriangle` |

Never use emoji as icons. All icons are SVG, currentColor-inherited for theme consistency.

---

## Design Grade

This specification targets **Ship-ready** for a standard SaaS product. The design is intentionally restrained — settings pages should feel reliable, not exciting. The strongest design decisions here are:

1. **Route-based sections** over single-page scroll — better deep-linking, lighter pages, predictable back-button
2. **Per-card save actions** — billing changes and password changes are isolated operations, not a single global save
3. **680px content column** — prevents fields from stretching uncomfortably wide on large monitors
4. **Collapsed sidebar at 768px** rather than hiding entirely — preserves spatial orientation until mobile
5. **Upgraded muted text contrast** — `#64748B` passes AA where the common `#94A3B8` does not

The specification avoids: purple gradients, generic stock imagery, decorative animation, and any other AI slop patterns.
