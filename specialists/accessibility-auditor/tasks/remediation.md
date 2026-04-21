## Accessibility Remediation

**Use when:** Fixing specific accessibility violations identified during an audit or AT testing. Provides code examples and implementation guidance.

**Gather:** List of violations to fix (from audit report), codebase access, framework in use (React, Vue, vanilla HTML, etc.).

---

### Missing Alt Text

**Decorative images** — images that add no information (backgrounds, spacers, icons next to text that already conveys the meaning):
```html
<!-- Before: screen reader announces "bullet dot icon" -->
<img src="bullet.svg">

<!-- After: silent to screen readers -->
<img src="bullet.svg" alt="" role="presentation">
```

**Informative images** — images that convey meaning:
```html
<!-- Before: no description -->
<img src="revenue-chart.png">

<!-- After: describes what the image shows -->
<img src="revenue-chart.png" alt="Revenue growth chart showing 40% increase from Q1 to Q4 2025">
```

**Functional images** — images used as buttons or links:
```html
<!-- Before: no accessible name -->
<button><img src="search-icon.svg"></button>

<!-- After: describes the action -->
<button><img src="search-icon.svg" alt="Search"></button>
<!-- Or better: -->
<button aria-label="Search"><img src="search-icon.svg" alt=""></button>
```

---

### Colour Contrast Fixes

**Requirements:**
- Normal text (< 18pt / < 14pt bold): **4.5:1** contrast ratio
- Large text (>= 18pt / >= 14pt bold): **3:1** contrast ratio
- UI components and graphical objects: **3:1** contrast ratio

**Common failures and fixes:**

```css
/* FAIL: light grey on white — 2.5:1 ratio */
.placeholder { color: #aaaaaa; }

/* PASS: darker grey on white — 4.6:1 ratio */
.placeholder { color: #767676; }

/* FAIL: disabled button with no contrast */
.btn-disabled { color: #cccccc; background: #eeeeee; }

/* PASS: disabled but still readable — 3:1 minimum */
.btn-disabled { color: #767676; background: #eeeeee; }
```

**Tools:** Use `WebSearch "contrast ratio checker"` or Chrome DevTools colour picker (shows ratio in real time).

---

### Form Labels and Error Messages

**Every input needs a programmatic label:**

```html
<!-- FAIL: no label association -->
<input type="email" placeholder="Email">

<!-- PASS: explicit label -->
<label for="email">Email address</label>
<input type="email" id="email" placeholder="name@example.com">

<!-- PASS: implicit label (wrapping) -->
<label>
  Email address
  <input type="email" placeholder="name@example.com">
</label>
```

**Error messages must be programmatically associated:**

```html
<!-- FAIL: error shown visually but not announced -->
<input type="email" id="email">
<span class="error">Please enter a valid email</span>

<!-- PASS: error linked via aria-describedby -->
<input type="email" id="email" aria-invalid="true" aria-describedby="email-error">
<span id="email-error" class="error" role="alert">Please enter a valid email address (e.g., name@example.com)</span>
```

**Required fields:**
```html
<!-- PASS: programmatically and visually indicated -->
<label for="name">Full name <span aria-hidden="true">*</span></label>
<input type="text" id="name" required aria-required="true">
```

---

### Focus Management for Modals and SPAs

**Modal dialog pattern:**

```html
<div role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <h2 id="modal-title">Confirm deletion</h2>
  <p>Are you sure you want to delete this item?</p>
  <button>Cancel</button>
  <button>Delete</button>
</div>
```

```javascript
// Opening a modal:
// 1. Store the trigger element
const trigger = document.activeElement;
// 2. Move focus to the first focusable element inside the modal
modal.querySelector('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])').focus();
// 3. Trap focus inside (Tab and Shift+Tab cycle within modal)
// 4. On close: return focus to trigger
modal.addEventListener('close', () => trigger.focus());
// 5. Escape key closes the modal
modal.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});
```

**SPA route changes:**
```javascript
// After client-side navigation, announce the new page:
// Option 1: Move focus to the main heading
document.querySelector('h1').focus();

// Option 2: Use a live region to announce
const announcer = document.getElementById('route-announcer');
announcer.textContent = `Navigated to ${pageTitle}`;
```

```html
<!-- Route announcer (hidden, but announced by screen readers) -->
<div id="route-announcer" role="status" aria-live="polite" aria-atomic="true" class="sr-only"></div>
```

---

### Skip Navigation Links

```html
<!-- First element in <body> -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<!-- Target -->
<main id="main-content" tabindex="-1">
  <!-- page content -->
</main>
```

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  padding: 8px 16px;
  background: #000;
  color: #fff;
  z-index: 100;
  transition: top 0.2s;
}
.skip-link:focus {
  top: 0;
}
```

---

### ARIA Roles, States, and Properties

**The First Rule of ARIA: don't use ARIA if a native HTML element will do the job.**

| Need | Don't Use | Use Instead |
|------|-----------|-------------|
| Button | `<div role="button" tabindex="0">` | `<button>` |
| Link | `<span role="link" tabindex="0">` | `<a href="...">` |
| Checkbox | `<div role="checkbox">` | `<input type="checkbox">` |
| Navigation | `<div role="navigation">` | `<nav>` |
| Heading | `<div role="heading" aria-level="2">` | `<h2>` |

**When ARIA is needed (custom widgets):**
- Tabs — `role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`, `aria-controls`
- Accordion — `aria-expanded` on triggers, `aria-controls` linking to panels
- Combobox — `role="combobox"`, `aria-expanded`, `aria-autocomplete`, `aria-activedescendant`
- Live regions — `aria-live="polite"` for updates, `aria-live="assertive"` for urgent alerts

See `references/aria-patterns.md` for full patterns with keyboard interaction.

---

### Responsive Text Sizing

```css
/* FAIL: fixed pixel sizes don't scale with user preferences */
body { font-size: 16px; }
h1 { font-size: 32px; }

/* PASS: rem units respect user's base font size */
body { font-size: 1rem; }      /* 16px default, scales with user setting */
h1 { font-size: 2rem; }        /* 32px default, scales proportionally */

/* PASS: clamp for responsive sizing */
h1 { font-size: clamp(1.5rem, 4vw, 2.5rem); }
```

**Line heights and spacing:**
```css
p {
  line-height: 1.5;          /* WCAG 1.4.12: at least 1.5x font size */
  letter-spacing: 0.12em;    /* must be overridable to this value */
  word-spacing: 0.16em;      /* must be overridable to this value */
}
```

---

### Video Captions and Audio Descriptions

**Captions (for deaf/hard-of-hearing users):**
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions-en.vtt" srclang="en" label="English" default>
</video>
```

**Caption requirements:**
- Synchronised with audio (within 100ms)
- Include speaker identification when multiple speakers
- Include relevant sound effects: `[door slams]`, `[phone rings]`
- 99% accuracy minimum

**Audio descriptions (for blind/low-vision users):**
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions-en.vtt" srclang="en" label="English" default>
  <track kind="descriptions" src="descriptions-en.vtt" srclang="en" label="Audio Descriptions">
</video>
```

---

### ADA Demand-Letter Response Blueprint

When the request is legal-risk driven (demand letter, compliance notice, formal complaint), always provide:

1. **Phased plan** with deadlines:
   - Phase 1 (0-72 hours): blockers and legal-risk-critical fixes
   - Phase 2 (1-2 weeks): high-impact usability/compliance gaps
   - Phase 3 (3-6 weeks): systemic hardening and verification cadence
2. **Per-issue remediation rows** including:
   - affected pattern
   - WCAG criterion
   - concrete implementation fix
   - effort estimate
   - owner role
3. **Coverage guarantee** for common litigation triggers:
   - keyboard-inaccessible navigation/dropdowns
   - form validation errors without text or programmatic association
   - autoplay media without controls/pause
   - missing skip navigation landmarks
4. **Evidence package** recommendation:
   - before/after screenshots
   - test log (axe + keyboard + screen reader)
   - remediation tracker for counsel/compliance review

If output length is constrained, prioritise full coverage of all cited violations before adding optional extra detail.

---

### Remediation Priority

Fix by **user impact**, not by ease of implementation:

1. **Critical — blocks access:** keyboard traps, missing form labels on required fields, auto-playing audio with no stop control
2. **High — significantly degrades experience:** missing alt text on informative images, broken focus management in modals, no skip navigation
3. **Medium — causes extra effort:** low contrast on secondary text, generic link text, missing language attributes
4. **Low — minor inconvenience:** decorative images with redundant alt text, minor heading hierarchy skips

### Remediation Delivery Gate (required)

Before finalising remediation output:

1. Confirm every cited violation has a concrete code fix (no unresolved placeholders or cut-off snippets).
2. If the request asks for a plan, provide phased remediation with effort estimates per phase.
3. If the input includes media, navigation, or form failures, explicitly cover:
   - autoplay/video controls and reduced-motion handling
   - skip-navigation implementation
   - programmatic form error messaging and association
4. Include a verification plan: keyboard-only pass, screen reader pass, automated scan pass.

After fixing, re-run the WCAG audit to verify the fix and check for regressions.
