## Design Review

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
