## WCAG 2.2 Audit

**Use when:** Auditing a page, component, or codebase for WCAG 2.2 compliance. This is the primary audit workflow.

**Gather:** URL or code to audit. Target conformance level (default: AA). Any known issues or compliance requirements (ADA, EAA, Section 508). User population details if available (helps prioritise).

---

### Step 1 — Automated Testing

Run automated tools first to catch the low-hanging fruit. Automated tools find ~30-40% of accessibility issues.

**axe-core (via CLI or browser extension):**
```bash
npx @axe-core/cli <url> --tags wcag2a,wcag2aa,wcag22aa
```

**Lighthouse accessibility audit:**
```bash
npx lighthouse <url> --only-categories=accessibility --output=json
```

**Limitations of automated testing:**
- Cannot detect missing alt text that is *wrong* (e.g., `alt="image"` passes automated checks)
- Cannot verify focus order makes logical sense
- Cannot assess whether content is actually understandable
- Cannot test screen reader announcement quality
- Cannot verify custom widget keyboard interaction patterns

After automated testing, proceed to manual testing for the issues automation misses.

---

### Step 2 — Manual Audit by POUR Category

Work through each POUR principle systematically.

#### Perceivable — Can users perceive the content?

| Check | WCAG Criterion | How to Test |
|-------|---------------|-------------|
| Images have meaningful alt text | 1.1.1 Non-text Content (A) | Inspect every `<img>`, `<svg>`, `<canvas>`. Decorative images need `alt=""` or `role="presentation"` |
| Video has captions | 1.2.2 Captions (A) | Play video — are captions accurate, synchronised, and complete? |
| Audio has transcript | 1.2.1 Audio-only (A) | Is a text transcript provided for audio-only content? |
| Video has audio description | 1.2.5 Audio Description (AA) | Is visual-only information described in an audio track? |
| Colour contrast meets minimums | 1.4.3 Contrast Minimum (AA) | Normal text: 4.5:1. Large text (>=18pt/>=14pt bold): 3:1. Use contrast checker tools |
| Information not conveyed by colour alone | 1.4.1 Use of Color (A) | Remove colour — is meaning still clear? (e.g., red/green for error/success needs icons too) |
| Text can be resized to 200% | 1.4.4 Resize Text (AA) | Zoom to 200% — does text reflow? Any clipping or overlap? |
| Content reflows at 320px width | 1.4.10 Reflow (AA) | Set viewport to 320px — no horizontal scrolling (except data tables, maps, diagrams) |
| Non-text contrast | 1.4.11 Non-text Contrast (AA) | UI components and graphical objects: 3:1 ratio against adjacent colours |
| Text spacing overridable | 1.4.12 Text Spacing (AA) | Apply 1.5x line height, 2x paragraph spacing, 0.12em letter spacing, 0.16em word spacing — no content loss |

#### Operable — Can users operate the interface?

| Check | WCAG Criterion | How to Test |
|-------|---------------|-------------|
| All functionality available via keyboard | 2.1.1 Keyboard (A) | Tab through entire page — can you reach and activate everything? |
| No keyboard traps | 2.1.2 No Keyboard Trap (A) | Can you Tab *out* of every component? Modals must return focus on close |
| Skip navigation link | 2.4.1 Bypass Blocks (A) | First Tab stop — is there a "Skip to main content" link? |
| Page has descriptive title | 2.4.2 Page Titled (A) | Check `<title>` — is it unique and descriptive? |
| Focus order is logical | 2.4.3 Focus Order (A) | Tab through — does focus follow visual reading order? |
| Link purpose clear from text | 2.4.4 Link Purpose (A) | No "click here" or "read more" without context. Links make sense out of context |
| Multiple ways to find pages | 2.4.5 Multiple Ways (AA) | Site has navigation + search or sitemap |
| Headings and labels descriptive | 2.4.6 Headings and Labels (AA) | Headings describe the section. Labels describe the input |
| Focus visible | 2.4.7 Focus Visible (AA) | Tab through — is there a visible focus indicator on every interactive element? |
| Focus appearance meets minimum | 2.4.11 Focus Appearance (AA) | Focus indicator: >= 2px outline, 3:1 contrast against unfocused state |
| Pointer target size | 2.5.8 Target Size Minimum (AA) | Interactive targets: >= 24x24 CSS pixels (44x44 recommended) |
| Dragging alternative | 2.5.7 Dragging Movements (AA) | Any drag operation has a single-pointer alternative |

#### Understandable — Can users understand the content?

| Check | WCAG Criterion | How to Test |
|-------|---------------|-------------|
| Page language declared | 3.1.1 Language of Page (A) | Check `<html lang="...">` — is it present and correct? |
| Language changes marked | 3.1.2 Language of Parts (AA) | Foreign-language phrases wrapped in `lang="..."` attribute |
| Consistent navigation | 3.2.3 Consistent Navigation (AA) | Is navigation in the same position across pages? |
| Consistent identification | 3.2.4 Consistent Identification (AA) | Same function = same label across pages (e.g., search is always "Search") |
| Error identification | 3.3.1 Error Identification (A) | Form errors described in text, not just colour. Error message near the field |
| Labels or instructions | 3.3.2 Labels or Instructions (A) | Every form input has a visible label. Required fields identified before submission |
| Error suggestion | 3.3.3 Error Suggestion (AA) | Error messages suggest how to fix (e.g., "Enter email as name@example.com") |
| Error prevention on legal/financial | 3.3.4 Error Prevention (AA) | Legal/financial submissions: reversible, checked, or confirmed before final |
| Redundant entry | 3.3.7 Redundant Entry (A) | Don't ask for the same information twice (or auto-populate if needed again) |

#### Robust — Can assistive technology parse the content?

| Check | WCAG Criterion | How to Test |
|-------|---------------|-------------|
| Valid HTML parsing | 4.1.1 Parsing (A) | Run HTML validator — no duplicate IDs, proper nesting, closed tags |
| Name, role, value for custom widgets | 4.1.2 Name, Role, Value (A) | Custom components have ARIA roles, states, and properties. Value changes announced |
| Status messages announced | 4.1.3 Status Messages (AA) | Toast notifications, form success messages use `role="status"` or `aria-live="polite"` |

---

### Step 3 — Common Violations by Frequency

These are the most common violations in the wild. Check these first for quick wins:

1. **Missing or inadequate alt text** — images without `alt`, or with `alt="image"`, `alt="photo"`
2. **Low colour contrast** — especially on placeholder text, disabled states, and links
3. **Missing form labels** — inputs without associated `<label>` elements
4. **Missing skip navigation** — no way to bypass repeated navigation blocks
5. **Inaccessible custom modals** — no focus trap, no Escape to close, no focus return
6. **Missing heading hierarchy** — skipping levels (H1 → H3), multiple H1s, no H1
7. **Non-descriptive links** — "click here", "read more", "learn more" without context
8. **Missing focus indicators** — `outline: none` with no replacement focus style
9. **Auto-playing media** — video or audio that plays without user initiation
10. **Touch targets too small** — buttons and links under 24x24px

---

### Step 4 — Deliver Audit Report

**Output format:**

| # | Violation | WCAG Criterion | Level | Severity | Element/Location | Remediation |
|---|-----------|---------------|-------|----------|-----------------|-------------|
| 1 | [Description] | [X.X.X Name] | A/AA | Critical/High/Medium/Low | [selector or location] | [Specific fix] |

**Severity definitions for accessibility:**
- **Critical** — Blocks access entirely for a group of users (keyboard trap, missing alt on only image conveying key info, form cannot be submitted)
- **High** — Significantly degrades experience for AT users (missing form labels, no skip nav, broken focus order)
- **Medium** — Causes confusion or extra effort (low contrast on secondary text, generic link text, missing language attribute)
- **Low** — Minor issue, still usable (decorative image with redundant alt text, minor heading skip)

**Summary section:**
- Total violations by severity
- Conformance status: Conformant / Partially conformant / Non-conformant
- Top 3 highest-impact fixes to prioritise
- Estimated remediation effort (quick wins vs sprint-level work)

After the report, proceed to `tasks/remediation.md` for fixes.
