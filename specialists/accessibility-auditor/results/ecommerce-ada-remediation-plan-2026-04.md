# ADA Demand-Letter Remediation Plan
**Site:** E-commerce (homepage + checkout flow)**
**Date:** 2026-04-15
**Standard:** WCAG 2.2 Level A & AA (ADA Title III basis)
**Prepared by:** Accessibility Auditor — GTeam

---

## Executive Summary

Four violations have been identified from the demand letter. All four are WCAG Level A failures — the minimum threshold — making them high-exposure litigation targets. Two of them (mouse-only dropdowns, form errors as colour only) directly block users from completing a purchase and are the most common grounds for ADA e-commerce settlements. Remediation is straightforward; all four issues have well-established code patterns.

**Total estimated effort: 2–4 engineering days** for a competent frontend developer familiar with your stack.

---

## Violation Overview — Prioritised by Legal Risk and User Impact

| # | Issue | WCAG Criterion | Level | Legal Risk | User Impact |
|---|-------|---------------|-------|-----------|-------------|
| 1 | Mouse-only dropdown menus | 2.1.1 Keyboard / 4.1.2 Name, Role, Value | **A** | **Critical** | Blocks all keyboard-only, switch, and voice users from navigating the site |
| 2 | Form errors as red border only | 1.4.1 Use of Color / 3.3.1 Error Identification | **A** | **Critical** | Blocks users from completing checkout — highest-revenue path failure |
| 3 | Auto-playing background video | 1.4.2 Audio Control / 2.2.2 Pause, Stop, Hide | **A** | **High** | Disrupts screen reader users; triggers vestibular disorders |
| 4 | No skip navigation | 2.4.1 Bypass Blocks | **A** | **Medium** | Forces keyboard users to Tab through entire nav on every page load |

---

## Phased Remediation Plan

### Phase 1 — 0–72 Hours: Legal-Critical Blockers

These two violations directly block users from shopping or checking out. Fix these first.

---

#### Issue 1: Mouse-Only Dropdown Menus

**WCAG Violated:** 2.1.1 Keyboard (A), 4.1.2 Name, Role, Value (A)
**Why it's critical:** Keyboard-only, switch access, and voice control users cannot navigate the site at all. Courts have consistently ruled that keyboard inaccessibility constitutes an ADA violation for e-commerce.

**Root cause pattern:** Dropdown opens on CSS `:hover` only. No keyboard event handlers, no ARIA states, no focus management.

**Fix — Navigation dropdown (use `<nav>` + `<ul>`, not `role="menu"`):**

```html
<!-- BEFORE: hover-only, no ARIA, no keyboard support -->
<div class="nav-dropdown">
  <a href="/products">Products</a>
  <div class="dropdown-content">
    <a href="/products/shirts">Shirts</a>
    <a href="/products/pants">Pants</a>
  </div>
</div>

<!-- AFTER: keyboard accessible, ARIA states, focus management -->
<nav aria-label="Main navigation">
  <ul role="list">
    <li>
      <button
        aria-expanded="false"
        aria-controls="products-submenu"
        class="nav-trigger"
      >
        Products
        <svg aria-hidden="true" focusable="false"><!-- chevron icon --></svg>
      </button>
      <ul id="products-submenu" role="list" hidden>
        <li><a href="/products/shirts">Shirts</a></li>
        <li><a href="/products/pants">Pants</a></li>
      </ul>
    </li>
  </ul>
</nav>
```

```javascript
// Keyboard handler for nav triggers
document.querySelectorAll('.nav-trigger').forEach(trigger => {
  const menu = document.getElementById(trigger.getAttribute('aria-controls'));

  // Toggle on Enter/Space
  trigger.addEventListener('click', () => {
    const expanded = trigger.getAttribute('aria-expanded') === 'true';
    trigger.setAttribute('aria-expanded', String(!expanded));
    menu.hidden = expanded;
    if (!expanded) {
      // Move focus to first link in submenu
      menu.querySelector('a').focus();
    }
  });

  // Close on Escape; return focus to trigger
  trigger.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      trigger.setAttribute('aria-expanded', 'false');
      menu.hidden = true;
      trigger.focus();
    }
  });

  // Arrow key navigation within open submenu
  menu.addEventListener('keydown', (e) => {
    const items = [...menu.querySelectorAll('a')];
    const idx = items.indexOf(document.activeElement);
    if (e.key === 'ArrowDown') { e.preventDefault(); items[Math.min(idx + 1, items.length - 1)].focus(); }
    if (e.key === 'ArrowUp')   { e.preventDefault(); items[Math.max(idx - 1, 0)].focus(); }
    if (e.key === 'Escape')    { trigger.setAttribute('aria-expanded', 'false'); menu.hidden = true; trigger.focus(); }
    if (e.key === 'Tab' && !e.shiftKey && idx === items.length - 1) {
      // Last item — close menu naturally
      trigger.setAttribute('aria-expanded', 'false'); menu.hidden = true;
    }
  });
});

// Close on outside click
document.addEventListener('click', (e) => {
  document.querySelectorAll('.nav-trigger').forEach(trigger => {
    if (!trigger.parentElement.contains(e.target)) {
      trigger.setAttribute('aria-expanded', 'false');
      document.getElementById(trigger.getAttribute('aria-controls')).hidden = true;
    }
  });
});
```

```css
/* Keep hover behaviour for mouse users — add keyboard support on top */
.nav-trigger + ul[hidden] { display: none; }
.nav-trigger + ul:not([hidden]) { display: block; }

/* Hover still works */
li:hover > ul { display: block; }
li:hover > .nav-trigger { aria-expanded: true; } /* CSS can't set ARIA — JS must handle this */
```

**CSS hover note:** CSS `:hover` can remain for mouse users. JavaScript adds the parallel keyboard layer. Do NOT remove hover — just add keyboard parity.

**Effort:** 4–8 hours | **Owner:** Frontend developer

---

#### Issue 2: Checkout Form Errors as Red Border Only

**WCAG Violated:** 1.4.1 Use of Color (A), 3.3.1 Error Identification (A)
**Why it's critical:** Colour is the sole error indicator. Blind users, colour-blind users, and screen reader users receive no accessible error feedback on the highest-revenue page of the site. ADA lawsuits frequently cite checkout barriers.

**Root cause pattern:** Validation adds CSS class `border-red` only. No text message, no `aria-invalid`, no `role="alert"`.

**Fix:**

```html
<!-- BEFORE: red border only, no text, no ARIA -->
<input type="email" id="email" class="border-red">

<!-- AFTER: text error + ARIA association + live announcement -->
<div class="field-group">
  <label for="email">Email address <span aria-hidden="true">*</span></label>
  <input
    type="email"
    id="email"
    aria-required="true"
    aria-invalid="true"
    aria-describedby="email-error"
    class="input-error"
  >
  <span id="email-error" class="error-message" role="alert">
    <!-- Error icon is decorative; text carries the meaning -->
    <svg aria-hidden="true" focusable="false" class="error-icon"><!-- exclamation --></svg>
    Please enter a valid email address (e.g., name@example.com)
  </span>
</div>
```

```javascript
// Validation on submit (not on blur — reduces cognitive load)
function validateField(input) {
  const errorEl = document.getElementById(input.getAttribute('aria-describedby'));
  
  if (!input.validity.valid) {
    input.setAttribute('aria-invalid', 'true');
    errorEl.textContent = getErrorMessage(input); // your error message function
    errorEl.hidden = false;
  } else {
    input.setAttribute('aria-invalid', 'false');
    errorEl.textContent = '';
    errorEl.hidden = true;
  }
}

// On form submit: validate all, focus first error
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const fields = form.querySelectorAll('[aria-required="true"]');
  fields.forEach(validateField);
  
  const firstError = form.querySelector('[aria-invalid="true"]');
  if (firstError) {
    firstError.focus(); // moves screen reader cursor to the problem field
  }
});
```

```css
/* Error state: border + icon, not colour alone */
.input-error {
  border: 2px solid #d32f2f;  /* red border */
  /* Also add an icon or background pattern for colour-blind users */
}

.error-message {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #d32f2f;
  font-size: 0.875rem;
  margin-top: 4px;
}

.error-icon {
  flex-shrink: 0;
  width: 16px;
  height: 16px;
}
```

**Error message content requirements (3.3.3 AA):**
- State what is wrong: "Email address is required" not "Invalid input"
- State how to fix it: "Enter a valid email (e.g., name@example.com)"
- For required fields: "First name is required"

**Effort:** 4–6 hours | **Owner:** Frontend developer

---

### Phase 2 — 1–2 Weeks: High-Impact Compliance Gaps

---

#### Issue 3: Auto-Playing Background Video

**WCAG Violated:** 1.4.2 Audio Control (A), 2.2.2 Pause, Stop, Hide (A), 2.3.1 Three Flashes (A — if strobing)
**Bonus WCAG AA risk:** `prefers-reduced-motion` users experiencing vestibular symptoms (WCAG 2.3.3 AAA, but cited in COGA guidance and some complaints)

**Root cause pattern:** `<video autoplay>` or `<video autoplay muted>` with no user controls. Even muted video violates 2.2.2 if it plays automatically for more than 5 seconds with no stop mechanism.

**Fix Option A — Add a visible pause/play button (preferred):**

```html
<!-- Retain autoplay but add controls accessible to all users -->
<div class="hero-video-container">
  <video
    id="hero-video"
    autoplay
    muted
    loop
    playsinline
    aria-hidden="true"
  >
    <source src="hero.mp4" type="video/mp4">
  </video>

  <button
    id="video-toggle"
    class="video-pause-btn"
    aria-label="Pause background video"
    aria-pressed="false"
  >
    <svg aria-hidden="true" focusable="false" class="icon-pause"><!-- pause icon --></svg>
    <svg aria-hidden="true" focusable="false" class="icon-play" hidden><!-- play icon --></svg>
    <span class="sr-only">Pause background video</span>
  </button>
</div>
```

```javascript
const video = document.getElementById('hero-video');
const toggleBtn = document.getElementById('video-toggle');

// Respect prefers-reduced-motion immediately on load
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  video.pause();
  video.removeAttribute('autoplay');
  updateButtonState(true); // show play button
}

toggleBtn.addEventListener('click', () => {
  if (video.paused) {
    video.play();
    updateButtonState(false);
  } else {
    video.pause();
    updateButtonState(true);
  }
});

function updateButtonState(isPaused) {
  toggleBtn.setAttribute('aria-pressed', String(isPaused));
  toggleBtn.setAttribute('aria-label', isPaused ? 'Play background video' : 'Pause background video');
  toggleBtn.querySelector('.icon-pause').hidden = isPaused;
  toggleBtn.querySelector('.icon-play').hidden = !isPaused;
}
```

```css
.video-pause-btn {
  position: absolute;
  bottom: 16px;
  right: 16px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
  border: 2px solid #fff;  /* 3:1 contrast against dark overlay */
  border-radius: 4px;
  padding: 8px 12px;
  cursor: pointer;
  z-index: 10;
}

.video-pause-btn:focus {
  outline: 3px solid #005fcc;
  outline-offset: 2px;
}

/* sr-only utility */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}
```

**Fix Option B — Disable autoplay entirely (fastest to deploy):**

```html
<!-- Remove autoplay; video loads paused -->
<video id="hero-video" muted loop playsinline aria-hidden="true" poster="hero-poster.jpg">
  <source src="hero.mp4" type="video/mp4">
</video>
<!-- Add a play button if desired -->
```

> Option B is zero-risk and can be deployed in minutes. Option A preserves the visual design intent while achieving compliance.

**Additional check:** If the video contains audio at any point (e.g., audio starts after user interaction), captions are required (WCAG 1.2.2 AA).

**Effort:** 2–3 hours | **Owner:** Frontend developer

---

#### Issue 4: No Skip Navigation

**WCAG Violated:** 2.4.1 Bypass Blocks (A)
**Why it matters legally:** Every page load forces keyboard users to Tab through all navigation items before reaching content. In a large-nav e-commerce site this can be 30–60 Tab presses.

**Fix — Add as the first element in `<body>` on every page:**

```html
<!-- First element inside <body> -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<!-- If you have multiple skip targets -->
<nav aria-label="Skip links" class="skip-links">
  <a href="#main-content">Skip to main content</a>
  <a href="#main-nav">Skip to navigation</a>
  <a href="#search">Skip to search</a>
</nav>

<!-- Main content landmark (required target) -->
<main id="main-content" tabindex="-1">
  <!-- All page-specific content -->
</main>
```

```css
/* Hidden by default; visible on focus (Tab on page load) */
.skip-link,
.skip-links a {
  position: absolute;
  top: -40px;
  left: 0;
  padding: 10px 16px;
  background: #000;
  color: #fff;
  font-weight: 600;
  font-size: 1rem;
  text-decoration: none;
  border-radius: 0 0 4px 0;
  z-index: 9999;
  transition: top 0.15s ease;
}

.skip-link:focus,
.skip-links a:focus {
  top: 0;
  outline: 3px solid #005fcc;
  outline-offset: 2px;
}
```

> **tabindex="-1" on `<main>`:** Required so that clicking the skip link moves focus into the main landmark. Without it, the browser scrolls to the anchor but screen reader cursor stays at the top.

**If using a framework (React/Next.js):**

```jsx
// components/SkipNav.jsx
export function SkipNav() {
  return (
    <a
      href="#main-content"
      className="skip-link"
      // Ensure this renders before any nav in the DOM
    >
      Skip to main content
    </a>
  );
}

// In your layout:
export function Layout({ children }) {
  return (
    <>
      <SkipNav />
      <Header />
      <main id="main-content" tabIndex={-1}>
        {children}
      </main>
    </>
  );
}
```

**Effort:** 1–2 hours | **Owner:** Frontend developer or template author

---

### Phase 3 — 3–6 Weeks: Systemic Hardening

These steps close the loop for legal defensibility, not just individual fixes.

| Action | Purpose |
|--------|---------|
| Run axe-core or Deque axe DevTools full-site scan | Catch automated-detectable issues across all pages, not just the four cited ones |
| Manual keyboard-only walkthrough: homepage → PDP → cart → checkout → confirmation | Verify the full purchase path is completable without a mouse |
| Screen reader test with NVDA + Firefox (Windows) and VoiceOver + Safari (macOS) | Confirm fixes work in the most common AT pairings used in litigation |
| Establish automated CI scan | Integrate `axe-core` or `@axe-core/playwright` in your test suite to prevent regressions |
| Accessibility statement page | Publish a conformance statement with a contact method — demonstrates good faith, often reduces litigation exposure |
| Remediation log for legal counsel | Document: violation → fix applied → date → tester → pass/fail result |

---

## Verification Plan

Run the following after each phase:

**Phase 1 verification (before Phase 2 begins):**
1. **Keyboard-only:** Open site, Tab from address bar. Can you reach every nav item, open every dropdown, and complete a checkout? No mouse allowed.
2. **Screen reader:** NVDA + Firefox. Navigate to checkout. Do error messages get announced when you submit an invalid form?
3. **Automated:** Run `npx axe-core https://yoursite.com` or Chrome DevTools Lighthouse Accessibility audit. Target score ≥ 90.

**Phase 2 verification:**
4. **Reduced motion:** Enable `prefers-reduced-motion` in OS settings. Does homepage video stay paused?
5. **Skip link:** Tab on any page. Does "Skip to main content" appear? Does activating it move focus to `<main>`?

**Phase 3 verification:**
6. Full site axe scan: zero critical/serious violations
7. Keyboard purchase flow: completed end-to-end by a tester unfamiliar with the fixes
8. AT testing log: documented pass results for NVDA and VoiceOver

---

## Evidence Package for Legal Counsel

Prepare the following to demonstrate remediation good faith:

- [ ] **Before screenshots** — dropdown with hover-only state, form with red-border-only error, video without pause control, pages with no skip link
- [ ] **After screenshots** — each fix in place, with keyboard focus visually indicated
- [ ] **axe scan reports** — before and after JSON exports
- [ ] **Keyboard test log** — tester, date, browser, outcome per page
- [ ] **Screen reader test log** — NVDA/VoiceOver, date, form error announcement confirmed
- [ ] **Remediation tracker** — maps each cited violation to its WCAG criterion, fix, date closed, and test result

---

## WCAG Criterion Quick Reference for Legal Brief

| Violation | Criterion | Level | Published Standard |
|-----------|-----------|-------|-------------------|
| Mouse-only dropdowns | 2.1.1 Keyboard | **A** | WCAG 2.2 |
| No keyboard name/role for dropdowns | 4.1.2 Name, Role, Value | **A** | WCAG 2.2 |
| Errors in colour only | 1.4.1 Use of Color | **A** | WCAG 2.2 |
| No text error messages | 3.3.1 Error Identification | **A** | WCAG 2.2 |
| Auto-playing video (audio or movement) | 1.4.2 Audio Control | **A** | WCAG 2.2 |
| No pause/stop for moving content | 2.2.2 Pause, Stop, Hide | **A** | WCAG 2.2 |
| No skip navigation | 2.4.1 Bypass Blocks | **A** | WCAG 2.2 |

All violations are WCAG 2.2 Level A — the lowest compliance bar. Courts applying ADA Title III to websites frequently reference WCAG 2.1/2.2 AA as the operative standard (per DOJ March 2022 guidance and subsequent rule).

---

*Deliverable produced by GTeam Accessibility Auditor · 2026-04-15*
