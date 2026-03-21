# Visual Design Principles Reference

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Use this reference to make concrete design decisions. Rules are specific enough to act on — if you need to guess, pick the option that matches the principle most closely and note it.

---

## Visual Hierarchy

### Scanning Patterns

**F-Pattern** — Dominant for text-heavy content (articles, search results, dashboards).
Users read the first line fully, scan a second shorter horizontal, then track down the left edge.
- Place the most important information in the first two lines
- Left-align primary labels and headings
- Never bury key actions in the right half of F-pattern layouts

**Z-Pattern** — Dominant for sparse content (landing pages, sign-in screens, cards).
Users scan top-left → top-right → diagonal → bottom-left → bottom-right.
- Logo/brand top-left, primary CTA top-right
- Value proposition in the diagonal path
- Final CTA bottom-right reinforces the journey

`[HYPOTHESIS]` Real users blend these patterns depending on content density. Validate with scroll/click heatmaps if it matters.

### Establishing Hierarchy (Dominant → Secondary → Tertiary)

Use a maximum of 3 visual weights per screen. More than 3 and nothing is dominant.

| Level | Technique | Example size/weight |
|-------|-----------|---------------------|
| Dominant | Largest size, highest contrast, most whitespace | 32–48px, bold, full-colour |
| Secondary | Smaller, medium contrast, some whitespace | 18–24px, medium, muted |
| Tertiary | Smallest, low contrast, dense | 14–16px, regular, grey |

Rules:
- Only ONE dominant element per screen (the thing you most want users to do/read)
- Secondary elements support the dominant; they never compete with it
- Use size before colour to establish weight — colour alone is fragile (colour blindness, dark mode)

---

## Typography Scale

### Modular Scales

| Scale | Ratio | Use when |
|-------|-------|----------|
| Major third | 1.25x | Compact UIs: dashboards, admin tools, dense forms — differences are subtle |
| Perfect fourth | 1.333x | General-purpose web: marketing sites, docs, blogs — clear steps without drama |
| Perfect fifth | 1.5x | Large-format or display-heavy: landing pages, editorial, hero-driven layouts |

**How to apply:** Pick a base (usually 16px for body), multiply up.

Perfect fourth from 16px: 16 → 21 → 28 → 37 → 49px
Perfect fifth from 16px: 16 → 24 → 36 → 54 → 81px

`[HYPOTHESIS]` Don't mix scales in a single product. Pick one and apply it consistently; the harmony matters more than the specific ratio.

### Type Rules

- **Line length:** 65–75 characters per line for body text. Shorter = choppy; longer = eye-tracking fatigue. On wide viewports, use `max-width: 70ch` or a constrained column.
- **Line height:** 1.4–1.6 for body text. Use 1.5 as default unless type is unusually large or small. Headlines should be tighter: 1.1–1.2.
- **Optical kerning:** Apply to headlines (≥24px). Use `font-kerning: normal` (browser default is usually fine) or `letter-spacing: -0.02em` for bold display type. Never apply negative letter-spacing to body text — it reduces legibility.
- **Font pairing:** One typeface for UI, one for editorial if needed. When in doubt, use a single typeface with weight variation — it's harder to break.
- **Weight range:** Body at 400, labels/UI at 500, headings at 600–700. Avoid 300 (thin) for anything functional — it fails contrast checks at smaller sizes.

---

## Colour Theory

### 60/30/10 Rule

| Role | Proportion | Typical use |
|------|-----------|-------------|
| Dominant (neutral) | 60% | Backgrounds, surface areas |
| Secondary (brand or accent) | 30% | Navs, sidebars, containers |
| Accent | 10% | CTAs, highlights, active states |

Violation: if your brand colour appears more than ~30% of a screen, it's fatiguing and the accent loses meaning.

### Warm vs Cool Neutrals

- **Warm neutrals** (slight yellow/red in grey): feel approachable, human, editorial. Pair with warm brand colours (amber, terracotta, coral).
- **Cool neutrals** (slight blue in grey): feel clinical, precise, technical. Pair with cool brand colours (blue, teal, indigo).

`[HYPOTHESIS]` Mixing warm and cool neutrals in the same palette creates subtle visual noise. Pick one temperature and stay consistent across surface colours.

To identify: desaturate your grey. If it leans towards green/blue, it's cool. Yellow/red = warm.

### Simultaneous Contrast

Adjacent colours affect each other's perceived hue and lightness. A grey on a blue background looks orange-tinted; the same grey on an orange background looks blue-tinted.

Practical rules:
- Check text/background combinations in context, not in isolation
- Don't pick accessible greys in a vacuum — test them on your actual background colour
- If a colour looks "off" but passes contrast ratio, it's probably simultaneous contrast — adjust the hue slightly

### Accessible Palettes

Generate colour palettes that pass WCAG AA before choosing them aesthetically. Start with the interaction of brand colour × white/dark backgrounds. See `accessibility-wcag.md` for contrast ratios.

Tools: Colour Contrast Analyser, Radix UI colour system, Tailwind colour palette (pre-checked at common pairings).

---

## Spacing

### Base Unit System

Use **4px** as the atomic unit. Every spacing value should be a multiple of 4.

**Common scale:**

| Token | Value | Use |
|-------|-------|-----|
| space-1 | 4px | Icon padding, tight inline gaps |
| space-2 | 8px | Between label and input, within component |
| space-3 | 12px | Internal component padding (compact) |
| space-4 | 16px | Standard component padding, between list items |
| space-6 | 24px | Between related groups of components |
| space-8 | 32px | Section separation, card margins |
| space-12 | 48px | Major section breaks |
| space-16 | 64px | Hero spacing, top-of-page breathing room |

### Rules

- Proximity implies relationship: elements closer together are perceived as related. Don't break this accidentally with inconsistent padding.
- More space = more important. Give dominant elements more breathing room than secondary ones.
- Group first, then separate: pad inside a group smaller than the gap between groups. If `gap-between-cards` is 24px, `padding-inside-card` should be ≥24px too — otherwise the card looks cramped relative to the layout.
- Never use odd pixel values (5px, 7px, 13px) except for border-radius.

---

## Gestalt Principles (Practical Application)

| Principle | What it means | Design use |
|-----------|--------------|------------|
| Proximity | Close elements are grouped | Put form labels directly above fields; keep action buttons near the content they affect |
| Similarity | Similar-looking elements are grouped | Use consistent button styling for same-type actions; don't vary colour/shape randomly |
| Closure | Users complete incomplete shapes | Use open card borders or partial lines — users fill in the boundary without a full stroke |
| Figure/Ground | Users separate foreground from background | Shadows, borders, and colour shifts create depth; avoid ambiguous z-depth (flat design anti-pattern) |
| Continuity | Elements in a line are perceived as related | Align form fields on a single left axis; misaligned columns break the flow |
| Common fate | Elements moving together are grouped | Animate related items together; independent animations read as separate objects |

`[HYPOTHESIS]` Gestalt violations are often the root cause of "something feels off" feedback. When a design feels cluttered but has few elements, check proximity and figure/ground first.

---

## Common AI Slop Patterns — and What to Do Instead

These patterns appear frequently in AI-generated designs and signal low effort or generic output. Avoid them.

| Slop pattern | Why it's a problem | Do this instead |
|---|---|---|
| Purple/violet gradient hero | Overused; signals template, not brand | Use a single brand colour at full opacity, or a photograph with colour overlay specific to the product |
| Decorative stock hero image (generic laptop/team/handshake) | Adds no information, looks interchangeable | Use product screenshots, user-generated content, or abstract geometric shapes anchored to the brand colour |
| Lorem Ipsum placeholder text | Forces reviewers to ignore the most important part of the design | Write real representative content, even if approximate; use real product names |
| Emoji as UI decoration (🚀 ✨ 💡 in headings) | Looks unprofessional in most product contexts; breaks visual hierarchy | Use icon components (Lucide, Heroicons) at consistent sizes, or no decoration at all |
| Generic sans-serif everything (Inter/Roboto system defaults, no variation) | Undifferentiated; every other product looks the same | Either use a distinctive typeface for headlines (even a weight shift to 800+ with tight tracking), or lean into the neutrality with very strong colour/spacing discipline |
| Rounded everything (radius >16px on all surfaces) | Creates a toy-like aesthetic for products that need to convey reliability | Vary radius by component function: small radius for inputs (4px), larger for cards (8–12px), pill only for badges and tags |
| Card grid for every layout | Not everything is a card; cards everywhere flatten information hierarchy | Use cards where content is scannable and reorderable; use lists for sequences; use full-bleed for featured content |
| Three-feature "Why us" section with icon + heading + two sentences | The most cloned marketing pattern online | Replace with a specific, concrete claim backed by numbers, a quote, or a before/after |

`[HYPOTHESIS]` Clients often can't name why AI-generated designs feel generic. Showing them a before/after with one of these patterns removed is more persuasive than explaining the principle.
