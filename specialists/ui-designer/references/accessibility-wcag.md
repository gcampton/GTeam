# Accessibility & WCAG 2.1 AA Reference

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Target: **WCAG 2.1 Level AA** — the legal baseline for most jurisdictions and the default expectation for professional web products.

---

## Contrast Ratios

| Text type | Minimum ratio (AA) | Notes |
|-----------|-------------------|-------|
| Body text (< 18pt normal, < 14pt bold) | 4.5:1 | Most UI text falls here |
| Large text (≥ 18pt normal OR ≥ 14pt bold) | 3:1 | ~24px regular, ~18.67px bold |
| UI components & graphical objects | 3:1 | Borders of inputs, icon strokes, chart lines |
| Disabled states | No requirement | But distinguish visually — low opacity works |
| Logo / decorative | No requirement | |

`[HYPOTHESIS]` The 3:1 rule for UI components is underenforced. Input borders at #ccc on white fail 3:1 — this is extremely common and technically non-compliant. Use #767676 minimum for borders, or rely on a thick enough stroke that size compensates.

### Checking Contrast

1. **Browser DevTools** — colour picker in Styles panel shows contrast ratio inline when you click a colour value. Fast for spot-checking.
2. **Colour Contrast Analyser** (TPGi, free) — eyedropper tool for checking any two pixels on screen. Use for screenshots or static designs.
3. **axe DevTools browser extension** — automated audit; catches the majority of contrast issues on a live page without manual checking.
4. **WebAIM Contrast Checker** — webaim.org/resources/contrastchecker — paste hex values.

Do not trust "accessible" colour systems blindly — always verify specific combinations at your actual font size and weight.

---

## Keyboard Navigation

- [ ] **Logical tab order** — Tab should move left-to-right, top-to-bottom, following visual reading order. Never use `tabindex` values > 0 to reorder; fix the DOM order instead.
- [ ] **Visible focus ring** — Every focusable element must have a visible focus indicator. Do not write `outline: none` without replacing it with a custom focus style. A 2px offset outline in the brand colour is sufficient.
- [ ] **Skip-to-content link** — The first focusable element on every page should be a "Skip to main content" link, visible on focus, that jumps to `<main>`. Keyboard and screen reader users need this to bypass repeated nav.
- [ ] **Focus trap in modals** — When a modal opens, trap focus inside it. When it closes, return focus to the trigger element.
- [ ] **No keyboard traps** — Users must be able to navigate away from any component using only the keyboard. Date pickers and custom dropdowns are common failure points.
- [ ] **Escape closes overlays** — Dialogs, drawers, tooltips, and dropdown menus should close on Escape.

`[HYPOTHESIS]` Focus ring visibility is the most commonly removed feature in production (designers hate the default browser ring). Use `:focus-visible` instead of `:focus` to show rings only for keyboard users, not mouse clicks — this resolves most designer objections while remaining accessible.

---

## Screen Reader Support

### Alt Text
- **Meaningful images:** Describe the content and function, not the appearance. "Bar chart showing Q3 revenue up 12% versus Q2" not "image of a bar chart."
- **Decorative images:** `alt=""` (empty, not missing). Missing alt is an error; empty alt tells the screen reader to skip it.
- **Functional images (icons as buttons):** The button needs an accessible name. Use `aria-label="Close dialog"` or a visually-hidden text span. Never leave a button with only an icon and no label.
- **Complex images (infographics, charts):** Provide a text equivalent nearby or in a linked description. Alt text alone is insufficient for complex data.

### ARIA

Use ARIA sparingly — native HTML elements already carry roles and semantics. Use ARIA to fill gaps, not to override.

| Pattern | Correct approach |
|---------|-----------------|
| Button that only has an icon | `<button aria-label="Delete item">` |
| Input without visible label | `<input aria-label="Search">` or `aria-labelledby` pointing to a heading |
| Custom dropdown | `role="combobox"` or `role="listbox"` with full keyboard support — or use a native `<select>` |
| Live status updates (cart count, notifications) | `aria-live="polite"` region that updates |
| Error message linked to field | `aria-describedby="error-id"` on the input |
| Disclosure widget (accordion) | `aria-expanded` on the trigger, `aria-controls` pointing to the panel |

`[HYPOTHESIS]` Building custom interactive components correctly (with full ARIA) takes significantly longer than using native HTML or a well-tested headless component library (Radix UI, Headless UI). Default to native or tested libraries; custom ARIA only when necessary.

---

## Tap Targets

- **Minimum:** 44×44px interactive area (WCAG 2.5.5 — AA requires 24×24px for SC 2.5.8, but 44×44px is the usability recommendation and WCAG 2.1 AA best practice)
- **Recommended:** 48×48px (Material Design standard, matches most user expectations on mobile)
- **Gap between targets:** 8px minimum so adjacent targets don't trigger accidentally

`[HYPOTHESIS]` The gap between targets matters as much as target size. A row of 44px icon buttons with 0px gap still produces mis-taps. Apply `gap: 8px` or `margin` between interactive elements in nav bars and toolbars.

Implementation: Use padding to expand hit area without changing visual size. A 24×24px icon in a `<button>` with `padding: 10px` becomes a 44×44px tap target.

---

## Forms

- [ ] **Label for every input** — `<label for="id">` linked explicitly, or `aria-label`, or `aria-labelledby`. Placeholder text alone is never a label — it disappears on focus and is not reliably read by screen readers.
- [ ] **Error messages linked to field** — Use `aria-describedby="field-error-id"` on the input. The error message must be programmatically associated, not just visually adjacent.
- [ ] **Required fields marked** — Use `aria-required="true"` or native `required` attribute. Indicate visually too (asterisk is convention; explain it once near the form).
- [ ] **Error messages describe the fix** — "Invalid email" is bad. "Enter a valid email address, e.g. name@example.com" is good.
- [ ] **Autocomplete attributes** — Use `autocomplete="email"`, `autocomplete="current-password"`, etc. on relevant fields. Required for WCAG 1.3.5 and genuinely useful.
- [ ] **Group related inputs** — Use `<fieldset>` + `<legend>` for radio groups, checkbox groups, and multi-part fields (date of birth: day/month/year).

---

## Colour-Only Information

Never use colour as the only way to convey information. Users who are colour blind, or on monochrome displays, will miss it.

| Bad | Good |
|-----|------|
| Red text = error, green text = success | Coloured text + error/check icon + "Error:" prefix |
| Red border on invalid field | Red border + error message below field |
| Coloured line on chart = different data series | Coloured line + labelled directly or different dash pattern |
| Highlighted row = selected | Highlighted row + checkmark or "Selected" label |

`[HYPOTHESIS]` The most common violation is form validation state communicated only by border colour (red border, no other indicator). Always add an icon or error text.

---

## Motion & Animation

- [ ] **prefers-reduced-motion** — Wrap non-essential animations in `@media (prefers-reduced-motion: reduce)` and disable or reduce them. This is mandatory for users with vestibular disorders.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

- [ ] **Auto-playing video** — Must have pause control. Must not auto-play with sound.
- [ ] **Flashing content** — Nothing should flash more than 3 times per second (seizure risk).

`[HYPOTHESIS]` Most UI animations (page transitions, skeleton fades, hover effects) are non-essential and should be disabled under prefers-reduced-motion. Treat animation as enhancement, not function.

---

## Common Failure Modes

| Failure | Why it fails WCAG | Fix |
|---------|------------------|-----|
| `outline: none` with no replacement focus style | 2.4.7 Focus Visible | Use `:focus-visible` with a 2px+ visible ring |
| Placeholder-only form label | 1.3.1 Info and Relationships, 3.3.2 Labels or Instructions | Add `<label>` element |
| Icon button with no text or aria-label | 4.1.2 Name, Role, Value | Add `aria-label` to the button |
| Error message not linked to input | 3.3.1 Error Identification | Add `aria-describedby` on input |
| Low-contrast text (< 4.5:1 body) | 1.4.3 Contrast Minimum | Use a darker text colour or lighter background |
| Keyboard trap in custom modal | 2.1.2 No Keyboard Trap | Implement focus trap with Escape to close |
| Colour-only validation state | 1.4.1 Use of Colour | Add icon + text to error state |
| Auto-playing video with sound | 1.4.2 Audio Control | Default to muted or add pause button |
| Missing skip nav link | 2.4.1 Bypass Blocks | Add visually-hidden skip link as first focusable element |
| Tap targets < 24×24px (AA new threshold) | 2.5.8 Target Size | Increase padding on small interactive elements |
| Image alt text missing | 1.1.1 Non-text Content | Add `alt` — empty string for decorative, descriptive for informative |
