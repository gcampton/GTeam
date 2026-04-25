## Funnel Analysis

**Use when:** Identifying where users drop off in a multi-step conversion journey (checkout, onboarding, sign-up flow, sales funnel).

**Gather:** Funnel steps (list each page/screen in order), current conversion rate at each step (or ask user to provide from GA4/Mixpanel/Amplitude), total traffic volume entering the funnel.

**Funnel analysis process:**

**Step 1 — Map the funnel with drop-off rates:**

```
Step 1: [Page/action]     — 100% (baseline)
Step 2: [Page/action]     — X% (drop-off: Y%)
Step 3: [Page/action]     — X% (drop-off: Y%)
...
Step N: Conversion        — X% (overall conversion rate)
```

**Step 2 — Identify the biggest leak:**
- The step with the highest absolute drop-off is the priority (even if the % drop is similar to others, more volume lost = more revenue at stake)
- Quantify the value: "Improving step 3 from 40% → 50% would recover [N] conversions/month worth £[X]"

**Step 3 — Diagnose the drop-off cause:**

For each major drop-off point, form a hypothesis:

| Drop-off cause | Diagnostic check |
|---------------|-----------------|
| Page loads too slowly | PageSpeed Insights score |
| Confusing UI / can't find what to do | Session recording + heatmap |
| Price shock | Survey: "What stopped you from completing?" |
| Form too long | Count fields; compare to friction benchmark |
| Technical error | Check browser console, error tracking |
| Wrong audience arriving | Check traffic source breakdown |
| Distrust at payment step | Is trust signal present here? |

**Step 4 — Prioritise fixes using PIE framework:**

Score each proposed fix 1–10 on:
- **P**otential: how much lift is possible if this works?
- **I**mportance: how much traffic goes through this step?
- **E**ase: how hard is this to implement?

PIE score = (P + I + E) ÷ 3. Run the highest PIE score test first.

**Deliver:**
- Funnel visualisation (step → rate → drop-off)
- Revenue impact of fixing the biggest leak (specific calculation)
- Ranked fix list by PIE score
- Session recording / heatmap brief: what to look for at each major drop-off point
