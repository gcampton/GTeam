# WCAG 2.2 Quick Reference — Level A and AA

All criteria below are required for WCAG 2.2 Level AA conformance. [TESTED]

## 1. Perceivable

| Criterion | Name | Level | Plain English | Common Violation | Quick Fix |
|-----------|------|-------|--------------|-----------------|-----------|
| 1.1.1 | Non-text Content | A | Every image needs a text alternative | `<img>` without `alt` attribute | Add descriptive `alt`; use `alt=""` for decorative images |
| 1.2.1 | Audio-only and Video-only | A | Pre-recorded audio needs a transcript; pre-recorded video needs audio or text alternative | No transcript for podcast episodes | Provide a text transcript alongside the audio player |
| 1.2.2 | Captions (Prerecorded) | A | Pre-recorded video with audio needs captions | Auto-generated captions with errors | Review and correct auto-captions; include speaker ID and sound effects |
| 1.2.3 | Audio Description or Media Alternative | A | Pre-recorded video needs audio description or full text alternative | Training video with on-screen text not spoken | Add audio description track or provide transcript |
| 1.2.4 | Captions (Live) | AA | Live video with audio needs real-time captions | Live webinar without captions | Use live captioning service (CART) or auto-caption with correction |
| 1.2.5 | Audio Description (Prerecorded) | AA | Pre-recorded video needs audio description | Instructional video showing visual steps without narrating them | Add audio description track describing visual-only content |
| 1.3.1 | Info and Relationships | A | Visual structure must be in the code (headings, lists, tables, form groups) | Visual heading styled with CSS but using `<div>` | Use semantic HTML: `<h2>`, `<ul>`, `<table>`, `<fieldset>` |
| 1.3.2 | Meaningful Sequence | A | Reading order in code matches visual order | CSS grid reorders content visually but DOM order is wrong | Ensure DOM order matches visual reading order |
| 1.3.3 | Sensory Characteristics | A | Don't rely on shape, size, position, or sound alone to convey info | "Click the round button on the right" | Add text labels: "Click the Submit button" |
| 1.3.4 | Orientation | AA | Content works in both portrait and landscape | App locks to portrait mode | Allow both orientations unless essential (e.g., piano app) |
| 1.3.5 | Identify Input Purpose | AA | Input fields identify their purpose for autofill | Login form without `autocomplete` attributes | Add `autocomplete="email"`, `autocomplete="current-password"`, etc. |
| 1.4.1 | Use of Color | A | Colour is not the only way to convey information | Red text = error with no icon or label | Add icon, text label, or pattern in addition to colour |
| 1.4.2 | Audio Control | A | Audio playing for > 3 seconds can be paused/stopped or volume controlled | Background music auto-plays on homepage | Add pause/stop/volume controls; or don't auto-play |
| 1.4.3 | Contrast (Minimum) | AA | Normal text: 4.5:1; large text: 3:1 contrast ratio | Light grey text on white background | Darken text or lighten background to meet ratio |
| 1.4.4 | Resize Text | AA | Text can be resized to 200% without loss of content | Fixed `px` font sizes that don't scale | Use `rem` or `em` units for font sizes |
| 1.4.5 | Images of Text | AA | Use real text, not images of text | Logo uses image for tagline text | Replace image-text with styled HTML text |
| 1.4.10 | Reflow | AA | Content reflows at 320px width (400% zoom) with no horizontal scroll | Fixed-width layout breaks at small viewports | Use responsive CSS; avoid fixed widths |
| 1.4.11 | Non-text Contrast | AA | UI components and graphics: 3:1 contrast ratio | Light grey form input border on white | Darken border colour to meet 3:1 ratio |
| 1.4.12 | Text Spacing | AA | Content works when user overrides text spacing | Overflow hidden clips text when spacing increases | Don't use fixed heights on text containers |
| 1.4.13 | Content on Hover or Focus | AA | Tooltips/popovers: dismissible, hoverable, persistent | Tooltip disappears when moving mouse to it | Keep tooltip visible while hovering over it; Escape to dismiss |

## 2. Operable

| Criterion | Name | Level | Plain English | Common Violation | Quick Fix |
|-----------|------|-------|--------------|-----------------|-----------|
| 2.1.1 | Keyboard | A | All functionality available via keyboard | Dropdown menu only opens on mouse hover | Add keyboard event handlers; use `Enter`/`Space` to open |
| 2.1.2 | No Keyboard Trap | A | User can Tab out of every component | Date picker captures focus with no escape | Add `Escape` key handler; ensure Tab cycles out |
| 2.1.4 | Character Key Shortcuts | A | Single-key shortcuts can be turned off or remapped | App uses `S` key as shortcut conflicting with screen reader | Require modifier key (Ctrl+S) or allow remapping |
| 2.2.1 | Timing Adjustable | A | Time limits can be extended, adjusted, or turned off | Session timeout with no warning | Warn 20 seconds before timeout; allow extension |
| 2.2.2 | Pause, Stop, Hide | A | Moving/blinking/scrolling content can be paused | Auto-scrolling news ticker with no pause | Add pause/stop button |
| 2.3.1 | Three Flashes or Below | A | Nothing flashes more than 3 times per second | Hero video with strobe effects | Remove flashing content or keep below threshold |
| 2.4.1 | Bypass Blocks | A | Skip navigation link to bypass repeated content | No skip link, user must Tab through 50 nav items | Add "Skip to main content" link as first focusable element |
| 2.4.2 | Page Titled | A | Each page has a descriptive title | All pages titled "My App" | Use unique, descriptive titles: "Dashboard - My App" |
| 2.4.3 | Focus Order | A | Focus order follows logical reading sequence | Visual layout differs from DOM order | Match DOM order to visual reading order |
| 2.4.4 | Link Purpose (In Context) | A | Link text describes destination (in context) | Multiple "Read more" links | "Read more about accessibility auditing" or use `aria-label` |
| 2.4.5 | Multiple Ways | AA | More than one way to find pages (nav + search/sitemap) | Only way to reach pages is through navigation | Add search functionality or sitemap |
| 2.4.6 | Headings and Labels | AA | Headings and form labels are descriptive | Form label just says "Input 1" | Use descriptive labels: "Email address" |
| 2.4.7 | Focus Visible | AA | Visible focus indicator on all interactive elements | `outline: none` in CSS reset | Add visible focus styles: `outline: 2px solid #005fcc` |
| 2.4.11 | Focus Not Obscured (Minimum) | AA | Focused element is not entirely hidden behind other content | Sticky header covers focused element | Scroll-padding-top to account for sticky elements |
| 2.4.12 | Focus Not Obscured (Enhanced) | AAA | Focused element is fully visible (no partial obscuring) | — | — |
| 2.4.13 | Focus Appearance | AA | Focus indicator: >= 2px, 3:1 contrast | Thin 1px dotted outline barely visible | Use `outline: 2px solid` with sufficient contrast |
| 2.5.1 | Pointer Gestures | A | Multi-point gestures have single-pointer alternative | Pinch-to-zoom is the only way to zoom | Add +/- buttons as alternative |
| 2.5.2 | Pointer Cancellation | A | Actions fire on up-event, not down-event; can be aborted | Button fires on `mousedown` | Use `click` event (fires on `mouseup`) |
| 2.5.3 | Label in Name | A | Accessible name includes visible text | Button shows "Search" but `aria-label="Find items"` | Match `aria-label` to visible text: `aria-label="Search"` |
| 2.5.4 | Motion Actuation | A | Motion-triggered actions have conventional alternative | Shake phone to undo — no button | Add undo button as alternative |
| 2.5.7 | Dragging Movements | AA | Drag operations have single-pointer alternative | Sortable list only via drag-and-drop | Add move up/down buttons |
| 2.5.8 | Target Size (Minimum) | AA | Interactive targets >= 24x24 CSS px | Small 16x16 icon buttons | Increase size or add padding to meet 24x24 minimum |

## 3. Understandable

| Criterion | Name | Level | Plain English | Common Violation | Quick Fix |
|-----------|------|-------|--------------|-----------------|-----------|
| 3.1.1 | Language of Page | A | Page declares its language | Missing `lang` attribute on `<html>` | Add `<html lang="en">` |
| 3.1.2 | Language of Parts | AA | Language changes are marked in the code | French quote in English page not marked | Wrap in `<span lang="fr">` |
| 3.2.1 | On Focus | A | Moving focus doesn't trigger unexpected changes | Dropdown navigates on focus, not on selection | Trigger navigation on explicit `Enter` or button click |
| 3.2.2 | On Input | A | Changing a setting doesn't trigger unexpected changes | Selecting a radio button submits the form | Require explicit submit button |
| 3.2.3 | Consistent Navigation | AA | Navigation is in the same position across pages | Nav moves between header and sidebar on different pages | Keep navigation consistent across all pages |
| 3.2.4 | Consistent Identification | AA | Same function = same label everywhere | Search icon labelled "Search" on one page, "Find" on another | Use consistent labels site-wide |
| 3.3.1 | Error Identification | A | Errors described in text, not just colour | Red border on invalid field with no text message | Add text error message near the field |
| 3.3.2 | Labels or Instructions | A | Form inputs have visible labels; required fields identified | Placeholder-only labels that disappear on focus | Add persistent `<label>` elements |
| 3.3.3 | Error Suggestion | AA | Error messages suggest how to fix the problem | "Invalid input" with no guidance | "Enter a valid email (e.g., name@example.com)" |
| 3.3.4 | Error Prevention (Legal, Financial, Data) | AA | Legal/financial submissions: reversible, checked, or confirmed | One-click purchase with no confirmation | Add confirmation step before final submission |
| 3.3.7 | Redundant Entry | A | Don't ask for the same info twice in a process | Shipping address re-entered for billing | Auto-populate or "Same as shipping" checkbox |
| 3.3.8 | Accessible Authentication (Minimum) | AA | Login doesn't require cognitive function test | CAPTCHA with no accessible alternative | Provide audio CAPTCHA or alternative verification |

## 4. Robust

| Criterion | Name | Level | Plain English | Common Violation | Quick Fix |
|-----------|------|-------|--------------|-----------------|-----------|
| 4.1.2 | Name, Role, Value | A | Custom widgets expose name, role, and value to AT | Custom dropdown with no ARIA roles | Add `role="listbox"`, `role="option"`, `aria-selected` |
| 4.1.3 | Status Messages | AA | Status updates announced without receiving focus | "Item added to cart" toast not announced | Add `role="status"` or `aria-live="polite"` to the container |
