### Browse Setup

When a URL is provided, run this setup block before any browse step:

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/.claude/skills/gteam/browse/dist/browse
[ -x "$B" ] && echo "READY: $B" || echo "BROWSE NOT AVAILABLE"
```

If `BROWSE NOT AVAILABLE`: skip all `$B` steps and use WebFetch instead for URL inspection.

---

### Design Intelligence Setup

Run this at the start of any design consultation or new-project task:

```bash
UIPRO=""
for p in \
  ~/.claude/skills/ui-ux-pro-max/scripts/search.py \
  .claude/skills/ui-ux-pro-max/scripts/search.py \
  ~/dev/ui-ux-pro-max-skill/src/ui-ux-pro-max/scripts/search.py; do
  [ -f "$p" ] && UIPRO="$p" && break
done
[ -n "$UIPRO" ] && echo "UIPRO READY: $UIPRO" || echo "UIPRO NOT AVAILABLE"
```

If `UIPRO NOT AVAILABLE`: skip all `python3 $UIPRO` steps and rely on `references/ux-rules-priority.md` and `references/design-principles.md` instead.

---

### Design Consultation

**Gather:** Product name and purpose. Who is the target user? What is the primary action they take? Any existing brand colours, fonts, or references they like? What stack (React, Next.js, Vue, SwiftUI, etc.)?

**Step 1 — Generate design system (requires UIPRO):**

```bash
python3 $UIPRO "<product_type> <industry> <keywords>" --design-system -p "Project Name"
```

This returns a complete, reasoned design system: pattern, style, colours, typography, effects, and anti-patterns to avoid. Use its output as the foundation for all decisions below.

**To persist the design system across sessions:**
```bash
python3 $UIPRO "<query>" --design-system --persist -p "Project Name"
# creates design-system/MASTER.md + design-system/pages/ for overrides
```

**Step 2 — Supplement with targeted domain searches (as needed):**

| Need | Command |
|------|---------|
| More style options | `python3 $UIPRO "glassmorphism dark" --domain style` |
| Colour palettes | `python3 $UIPRO "fintech enterprise" --domain color` |
| Font pairings | `python3 $UIPRO "playful modern" --domain typography` |
| UX best practices | `python3 $UIPRO "animation accessibility" --domain ux` |
| Chart types | `python3 $UIPRO "real-time dashboard" --domain chart` |
| Landing structure | `python3 $UIPRO "hero social-proof" --domain landing` |
| Stack guidelines | `python3 $UIPRO "navigation performance" --stack nextjs` |

**Step 3 — Research phase:**
- Identify 3–5 direct competitors or design references in the space
- Note the dominant aesthetic conventions (and where to break them intentionally)
- Identify what visual language signals trust/quality in this niche

**Step 4 — Design system proposal:**
- **Aesthetic:** one clear design direction (e.g. editorial minimalism, warm utility, bold SaaS) — not a menu, a decision
- **Typography:** primary + secondary typeface with weights and scale (H1–body–caption)
- **Colour palette:** primary, secondary, neutral, semantic (success/warning/error)
- **Spacing scale:** base unit and scale steps
- **Border radius / shadow:** consistent rounding and elevation approach
- **Motion:** easing and duration for interactive elements

Explain the *why* behind each choice — how it serves the product and audience. Invite feedback. Adjust, don't revert to a menu.

**Output:**
- `DESIGN.md` — the project's design source of truth
- Font + colour preview page (HTML) showing the system in use

---

### Design Review

**Gather:** URL of live site, or screenshots. If browseable, load and snapshot at desktop and mobile breakpoints.

**Rule priority check:** Before scoring, run a quick domain scan for the product type to catch category-specific issues:

```bash
python3 $UIPRO "<product_type>" --domain ux -n 5
```

**Review dimensions (rate 0–10, explain what a 10 looks like):**

Work through these in priority order — highest-impact issues first:

1. **Accessibility (CRITICAL)** — contrast ≥ 4.5:1, focus rings visible, alt text, aria-labels, keyboard nav, no color-only meaning
2. **Touch & Interaction (CRITICAL)** — tap targets ≥ 44×44px, 8px+ spacing between targets, loading feedback on async actions
3. **Visual hierarchy** — does the eye land where it should? Primary CTA dominant? Heading hierarchy sequential?
4. **Typography** — consistent scale, appropriate weights, line-height 1.5–1.75, line length 65–75 chars
5. **Spacing consistency** — margins, padding, gaps follow a consistent scale; no orphaned elements
6. **Colour discipline** — semantic tokens used (not raw hex); palette consistent; light/dark mode both tested
7. **Component consistency** — buttons, inputs, cards follow a single pattern; no visual drift
8. **Mobile responsiveness** — mobile-first; no horizontal scroll; layout degrades gracefully
9. **Animation quality** — 150–300ms micro-interactions; ease-out on enter; prefers-reduced-motion respected
10. **AI slop patterns** — generic stock imagery, purple gradients, obvious template feel, Lorem Ipsum, emoji overuse

**Fix approach:**
- Fix issues in score order (lowest scores first, CRITICAL categories first)
- Commit each fix atomically with a descriptive message
- Re-verify with before/after screenshots

**Output:**
- Score table per dimension (before and after)
- Issue list with file:line reference and specific CSS/component fix
- Overall design grade: Ship-ready / Needs polish / Needs redesign

---

### Design-First Plan Review

**Use when:** Reviewing an implementation plan before code is written, to catch design and UX gaps.

**Check for:**
- User flows that skip error/empty/loading states
- UI components with no responsive treatment defined
- Colour or typography decisions deferred ("use brand colours") without specifics
- Accessibility omitted from requirements
- Missing interaction design (hover, focus, animation, transition)
- No design system reference — will this produce visual drift?

**Output:** Annotated plan with design gaps marked, suggested additions for each gap.
