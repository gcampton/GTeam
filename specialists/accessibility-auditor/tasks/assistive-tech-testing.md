## Assistive Technology Testing

**Use when:** Testing a page or component with assistive technologies to verify real-world usability beyond WCAG checklist compliance.

**Gather:** URL or component to test. Target platforms (macOS, Windows, iOS, Android). Any specific AT concerns raised by users.

---

### Screen Reader Testing

Test with at least one screen reader. Coverage priority by market share:

| Screen Reader | Platform | Browser Pairing | Market Share |
|--------------|----------|----------------|-------------|
| NVDA | Windows | Chrome or Firefox | ~40% |
| JAWS | Windows | Chrome | ~30% |
| VoiceOver | macOS/iOS | Safari | ~25% |
| TalkBack | Android | Chrome | ~5% |

**Key commands for testing:**

**VoiceOver (macOS):**
- `Cmd+F5` — toggle VoiceOver on/off
- `VO+Right/Left` (VO = Ctrl+Option) — navigate by element
- `VO+Space` — activate element
- `VO+U` — rotor (headings, links, landmarks, form controls)
- `VO+Cmd+H` — next heading

**NVDA (Windows):**
- `Insert+Space` — toggle browse/focus mode
- `H/Shift+H` — next/previous heading
- `Tab/Shift+Tab` — next/previous focusable element
- `Enter/Space` — activate element
- `D/Shift+D` — next/previous landmark

**What to check with screen readers:**

1. **Page structure** — Does the screen reader announce landmarks (banner, navigation, main, contentinfo)? Can the user jump between them?
2. **Heading hierarchy** — Navigate by headings. Do they form a logical outline? Can the user understand page structure from headings alone?
3. **Images** — Are images announced with meaningful descriptions? Are decorative images silent?
4. **Forms** — Are labels announced when focusing inputs? Are required fields indicated? Are error messages announced?
5. **Links and buttons** — Is the purpose clear from the announcement? Do buttons announce their state (expanded/collapsed, pressed)?
6. **Dynamic content** — Are toast notifications, loading states, and content updates announced via live regions?
7. **Tables** — Are data tables announced with headers? Can the user navigate by row and column?
8. **Custom widgets** — Do tabs, accordions, menus announce their role and state correctly?

---

### Keyboard-Only Navigation Testing

Unplug the mouse. Navigate the entire page using only the keyboard.

**Test sequence:**

1. **Tab order** — Press Tab repeatedly. Does focus move in a logical reading order (top-to-bottom, left-to-right for LTR)? No unexpected jumps?
2. **Focus visibility** — Is there a visible focus indicator on every element that receives focus? Is it high-contrast enough to see?
3. **Interactive elements** — Can you activate every button (Enter/Space), link (Enter), checkbox (Space), radio (Arrow keys), select (Arrow keys)?
4. **Modals and dialogs** — When a modal opens: does focus move into it? Is focus trapped inside? Does Escape close it? Does focus return to the trigger?
5. **Menus and dropdowns** — Can you open with Enter/Space, navigate with Arrow keys, close with Escape?
6. **Skip link** — First Tab press: is there a "Skip to main content" link? Does it work?
7. **No keyboard traps** — Can you Tab out of every component? Watch for: rich text editors, embedded maps, video players, date pickers, CAPTCHA
8. **Custom widgets** — Do tabs, accordions, carousels follow expected keyboard patterns? (Arrow keys for tabs, Enter to expand accordion)

**Common keyboard failures:**
- `onClick` without `onKeyDown` — element only works with mouse
- `div` or `span` used as button without `role="button"` and `tabindex="0"`
- `tabindex` values > 0 creating chaotic focus order
- Focus moves to hidden or off-screen elements
- Modal doesn't trap focus — user can Tab behind the overlay

---

### Voice Control Testing

Test with voice control (macOS Voice Control, Dragon NaturallySpeaking).

**What to check:**
1. Can the user say "Click [button text]" to activate any button? (Requires visible labels matching accessible names)
2. Can the user say "Show numbers" to see and select interactive elements?
3. Are there interactive elements with no visible text label? (These are invisible to voice control users)
4. Do `aria-label` values match visible text? (Mismatch breaks voice commands — WCAG 2.5.3 Label in Name)

---

### Zoom and Magnification Testing

**200% browser zoom test:**
1. Set browser zoom to 200%
2. All content still readable? No text clipped or overlapping?
3. All functionality still usable? No horizontal scrolling needed?
4. Images and icons still meaningful at 2x size?

**400% browser zoom test (WCAG 1.4.10 Reflow):**
1. Set browser zoom to 400% (equivalent to 320px viewport)
2. Content reflows into single column? No two-dimensional scrolling?
3. All information and functionality still available?
4. Exceptions allowed: data tables, toolbars, maps, diagrams

**Text-only zoom test:**
1. Increase font size only (not page zoom) — Firefox: `View > Zoom > Zoom Text Only`
2. Does text resize? Or is it locked with `px` units?
3. Any overflow, clipping, or overlap when text grows?

---

### Colour Blindness Simulation

Simulate the three main types of colour vision deficiency:

| Type | Affects | Prevalence | What Breaks |
|------|---------|-----------|-------------|
| Protanopia | Red-blind | ~1% of males | Red/green distinctions, red text on dark backgrounds |
| Deuteranopia | Green-blind | ~5% of males | Red/green distinctions (most common) |
| Tritanopia | Blue-blind | ~0.003% | Blue/yellow distinctions |

**Testing tools:** Chrome DevTools > Rendering > Emulate vision deficiencies

**Check:**
1. Can you distinguish all UI states without relying on colour? (error/success, active/inactive, selected/unselected)
2. Do charts and graphs use patterns, labels, or shapes in addition to colour?
3. Are links distinguishable from body text by more than just colour? (underline, weight, or 3:1 contrast with surrounding text)
4. Are required form fields indicated by more than a red asterisk?

---

### Motion Sensitivity Testing

**Check `prefers-reduced-motion` support:**
```css
/* This media query should be implemented */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

**Test:** Enable "Reduce motion" in OS settings. Then:
1. Do animations stop or simplify?
2. Does parallax scrolling stop?
3. Do auto-playing carousels/sliders stop?
4. Are there any flashing elements (> 3 flashes per second = seizure risk, WCAG 2.3.1)?

**Auto-playing media:**
- Video/audio must not auto-play, or must have controls to stop within 3 seconds
- Carousels must have pause/stop controls
- Moving or blinking content must be pausable (WCAG 2.2.2)

---

### Deliver AT Testing Report

**Output format:**

| AT Test | Pass/Fail | Issue | Impact | Fix |
|---------|-----------|-------|--------|-----|
| Screen reader: landmarks | Pass/Fail | [Description] | [Who is affected] | [Specific fix] |
| Keyboard: tab order | Pass/Fail | [Description] | [Who is affected] | [Specific fix] |
| Zoom: 200% | Pass/Fail | [Description] | [Who is affected] | [Specific fix] |
| Colour: deuteranopia | Pass/Fail | [Description] | [Who is affected] | [Specific fix] |
| Motion: reduced-motion | Pass/Fail | [Description] | [Who is affected] | [Specific fix] |

**Summary:** Overall AT compatibility rating: Good / Needs Work / Inaccessible
