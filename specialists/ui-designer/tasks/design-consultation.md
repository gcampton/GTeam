## Design Intelligence Setup

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

## Design Consultation

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
