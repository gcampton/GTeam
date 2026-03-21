# Design Review Rubric

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Use this rubric to score any UI design submission. Score each dimension 0–10, sum for a total out of 80, then apply grade thresholds. Issue the top 5 issues from lowest-scoring dimensions first.

---

## How to Use

1. Score each dimension independently before reading other scores — avoid anchoring.
2. Note one specific, actionable observation per dimension as evidence for the score.
3. Sum scores → apply grade → list issues by score order (lowest first, max 5 issues).
4. Do not mix evaluation with solution-giving in the score step. Score first, recommend after.

---

## Dimension Scoring

### 1. Visual Hierarchy (0–10)

Does the design make immediately clear what matters most? Can you identify dominant → secondary → tertiary in under 5 seconds?

| Score | Description |
|-------|-------------|
| 0–2 | No discernible hierarchy. Everything is the same visual weight. Multiple elements compete equally. No clear dominant element. User has no anchor to start reading from. |
| 3–4 | Some differentiation but inconsistent or accidental. Hierarchy exists in parts of the screen but breaks down elsewhere. Two or more elements are competing for dominance. |
| 5–6 | Hierarchy is present and mostly legible. One clearly dominant element. Secondary elements are distinct. Tertiary items may be unclear or slightly competing with secondary. |
| 7–8 | Clear, consistent hierarchy throughout. One dominant per screen, supporting elements clearly subordinate. Reading path is intuitive and matches F or Z pattern appropriately. |
| 9–10 | Hierarchy is precise and purposeful. Visual weight is used to guide attention exactly where intended. Nothing is accidental — every element's size/contrast/space has a clear rationale. |

---

### 2. Typography (0–10)

Is the type system consistent, readable, and appropriate to the product?

| Score | Description |
|-------|-------------|
| 0–2 | No coherent type system. Random font sizes not on a scale. Body text unreadable (too small, too tight, too wide). Multiple typefaces used inconsistently. |
| 3–4 | Some typographic decisions but inconsistent application. Scale partially followed. Line height or line length outside acceptable range. Weight variation unclear. |
| 5–6 | Readable and broadly consistent. Modular scale mostly followed. Body text within readable parameters (65–75 chars, 1.4–1.6 line-height). Minor inconsistencies (rogue size or weight). |
| 7–8 | Strong type system applied consistently. Scale is clear and correct for the product type. Headlines, subheadings, body, labels, and captions are all visually distinct and appropriate. |
| 9–10 | Type system is fully considered and exemplary. Scale choice matches the product's density requirements. Optical kerning applied to headlines. Every text element is purposeful. |

---

### 3. Spacing Consistency (0–10)

Does the spacing follow a system? Does it communicate grouping and hierarchy through proximity?

| Score | Description |
|-------|-------------|
| 0–2 | Arbitrary spacing throughout. No detectable unit system. Elements are crammed together or randomly spaced. Proximity bears no relationship to content grouping. |
| 3–4 | Some spacing patterns but broken in many places. 4px or 8px grid partially applied. Related elements are occasionally grouped correctly but exceptions are frequent. |
| 5–6 | Mostly on-grid spacing. A few off-value exceptions. Proximity generally communicates grouping correctly. Spacing between sections is distinct from spacing within components. |
| 7–8 | Consistent 4px or 8px grid throughout. Space communicates hierarchy — dominant elements have more breathing room. Internal vs external component spacing is clearly differentiated. |
| 9–10 | Spatial system is precise and contributes directly to hierarchy. Every spacing decision is deliberate and on-grid. The layout breathes correctly — not over-spaced or cramped anywhere. |

---

### 4. Colour Discipline (0–10)

Is colour used purposefully with appropriate restraint and accessibility?

| Score | Description |
|-------|-------------|
| 0–2 | Colour is arbitrary or overused. Multiple saturated colours compete. Contrast failures across the design. No visible 60/30/10 structure. Colour communicates nothing about hierarchy or interaction. |
| 3–4 | Some colour system but inconsistent. Brand colour applied inconsistently. Neutral palette mixes warm and cool. Some contrast failures. Accent colour diluted by overuse. |
| 5–6 | Broadly appropriate colour use. Roughly 60/30/10 structure. Palette is coherent. Most text passes contrast (spot-check passes). Accent is distinct but may appear slightly too often. |
| 7–8 | Disciplined colour system. 60/30/10 clearly applied. All text/background combinations pass WCAG AA. Neutral temperature is consistent. Interactive elements are clearly signalled by colour + other cue. |
| 9–10 | Colour is precise and meaningful. Every application serves a purpose. Palette is internally consistent (warm/cool coherent, values follow a system). No colour conveys information without a non-colour backup. |

---

### 5. Component Consistency (0–10)

Are the same UI patterns used consistently across the design?

| Score | Description |
|-------|-------------|
| 0–2 | Completely inconsistent. Buttons in multiple styles with no apparent logic. Form fields vary randomly. Spacing, radius, and shadow are different per component. Looks like a collage of different designs. |
| 3–4 | Some consistent elements but major inconsistencies. Primary button is consistent but secondary/ghost vary. Cards have two or three different padding values. Icons from different sets mixed. |
| 5–6 | Core components are consistent (primary button, main nav, main form fields). Secondary components (badges, tags, tooltips) may vary. Some components are one-offs without systematic justification. |
| 7–8 | Strong component system. Buttons, forms, cards, and navigation are all applied consistently. One-off components are justified exceptions. Border radius and shadow follow a scale. |
| 9–10 | Design system is evident and fully applied. Every component follows a clear pattern. Naming, sizing, states (hover, active, disabled) are all consistent and complete across all components. |

---

### 6. Mobile Responsiveness (0–10)

Does the design work at mobile viewport widths (≤375px)?

| Score | Description |
|-------|-------------|
| 0–2 | No mobile consideration. Desktop layout at full width on mobile. Content overflows. Text unreadable without zooming. Tap targets are tiny. |
| 3–4 | Some responsive breakpoints but significant problems remain. Nav collapses but content is still cramped. Tables overflow horizontally. Tap targets inconsistent. |
| 5–6 | Functional at mobile widths. Navigation handled (hamburger or simplified). Text is readable. Main flows work. Tables or complex components may have issues. |
| 7–8 | Well-considered mobile experience. All main flows are usable on touch. Tap targets ≥44px. No horizontal scroll. Typography and spacing adjusted for small screen. |
| 9–10 | Mobile experience is excellent and considered as a first-class design target. Touch interactions are optimised. Progressive disclosure used appropriately. Performance and hierarchy optimised for small screens. |

---

### 7. AI Slop Detection (0–10)

Does the design look original and specific, or generic and template-like?

| Score | Description |
|-------|-------------|
| 0–2 | Design is a direct template instantiation. Purple gradient hero, stock imagery, Lorem Ipsum, generic icons, rounded-everything aesthetic, emoji in headings. Interchangeable with a thousand other products. |
| 3–4 | Several slop patterns present. Generic sans-serif with no visual identity. Three-feature icon grid. Stock photography. Little to distinguish this product from any competitor. |
| 5–6 | Some differentiation present but generic patterns still visible. Brand colour applied but personality hasn't carried through. Content is real but layouts are stock. |
| 7–8 | Design shows clear product identity. Generic patterns have been replaced with specific, intentional choices. Content is real and representative. Visual identity is coherent and distinctive. |
| 9–10 | Design is unmistakably specific to this product. Every element is intentional. Visual language would be difficult to copy wholesale. Product screenshots or real content used throughout. No generic filler visible. |

See `design-principles.md` — Common AI Slop Patterns for the specific list.

---

### 8. Interaction Feedback (0–10)

Do interactive elements communicate their state clearly? Does the user always know what's happening?

| Score | Description |
|-------|-------------|
| 0–2 | No interactive feedback. Buttons have no hover/active state. Loading actions show no progress. Errors appear without visual indication on the triggering element. Forms submit silently. |
| 3–4 | Some states designed but inconsistent. Hover works on primary button but not secondary. No loading states. Error states exist for some fields but not all. |
| 5–6 | Core interactive feedback present. Primary button has hover, active, and loading state. Form errors are visible. Some states may be missing (disabled, empty). |
| 7–8 | All interactive elements have full state coverage: default, hover, active/pressed, disabled, loading, error, success. Feedback is immediate (< 100ms) and visually clear. |
| 9–10 | Interaction feedback is exceptional. State changes are obvious but not jarring. Transitions are smooth and meaningful. Feedback is informative (specific error messages, meaningful loading copy). Every action has a result the user can see. |

---

## Grade Thresholds

| Total score | Grade | Recommendation |
|-------------|-------|----------------|
| 72–80 | Excellent | Ship-ready. Minor polish optional but not blocking. |
| 64–71 | Good | Ship-ready with fixes. Address any dimension scoring ≤ 6. |
| 48–63 | Needs polish | Do not ship. Fix top 3 issues before re-review. |
| 32–47 | Needs rework | Significant design problems. Multiple dimensions need redesign. |
| < 32 | Needs redesign | Fundamental issues. Start from principles rather than patching. |

Boundary is inclusive (a 64 is "Good", a 63 is "Needs polish").

---

## Issue Prioritisation

After scoring, generate an issue list ordered by priority:

1. **Order by score** — lowest-scoring dimension first. A score of 2 is more urgent than a score of 6.
2. **Max 5 issues per review session** — more than 5 and the designer is overwhelmed. Re-review after fixes.
3. **Each issue must include:**
   - Dimension name and score
   - One specific observation (what you actually saw, not a general statement)
   - One actionable recommendation (specific enough to act on today)
4. **Do not list issues from dimensions scoring 8+** — they don't need attention this round.

### Issue Template

```
[Dimension] Score: X/10
Observation: [Specific thing observed — what element, what location, what the problem is]
Fix: [Specific action to take]
```

### Example Issue List (ordered correctly)

```
[Colour Discipline] Score: 3/10
Observation: Brand blue appears in 7 different elements including background fills, borders, text, and the CTA button — no hierarchy between them.
Fix: Reserve the brand blue for one role only (CTA button). Use tints (10% opacity) for background fills, and a darker navy for headings.

[Mobile Responsiveness] Score: 4/10
Observation: The pricing comparison table has 5 columns and overflows horizontally at 375px viewport with no alternative mobile treatment.
Fix: At ≤768px, collapse the table to a stacked card view or a horizontally swipeable card per pricing tier.

[Interaction Feedback] Score: 5/10
Observation: The "Save" button has no loading or success state — after clicking, nothing visible happens until the page reloads.
Fix: Add inline loading state (disable button, show spinner) and a success state (green checkmark + "Saved" label that fades after 2s).
```

---

## Re-Review Protocol

After a "Needs polish" or below result:

1. Designer addresses the top 5 issues only
2. Re-review scores only the fixed dimensions (other scores carried forward)
3. New total = carried scores + re-review scores
4. A dimension cannot score higher than 8 on re-review without significant redesign — minor patches rarely achieve 9–10

`[HYPOTHESIS]` Scoring the same design twice with the same rubric produces results within ±1 point per dimension for objective dimensions (spacing, contrast) and ±2 for subjective dimensions (hierarchy, slop detection). If scores diverge more than that between reviewers, the rubric criterion needs a clearer example.
