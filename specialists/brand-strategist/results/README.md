# Brand Strategist Results Log

This directory stores real-world outcomes from applying GTeam brand strategy recommendations.
Over time these results are used by the `gteam-learn` job to upgrade reference file
confidence levels and revise advice that doesn't hold up in practice.

---

## How to log a result

Copy the template below into a new file named `YYYY-MM-DD-brief-description.md`.
Be specific — vague entries ("it worked") don't help future calibration.

```markdown
# [Strategy Name] — [Month YYYY]

**Reference file:** [which file in references/ this relates to]
**Section:** [which section/recommendation was tried]

## Context
- **Brand maturity:** [new brand / early-stage / established / rebrand]
- **Company stage:** [pre-revenue / seed / growth / enterprise]
- **Industry:** [SaaS / e-commerce / professional services / consumer / other]
- **Starting position:** [e.g. no brand guidelines, inconsistent identity, repositioning, brand audit]

## What was tried
[Describe exactly what you did, following which recommendation]

## Result (after X weeks)
- [Metric]: [before] → [after]
- [Metric]: [before] → [after]

## What worked
[Specific observations about what drove the positive result]

## What didn't work
[Specific observations about what failed or had no effect]

## Recommendation update
- [ ] Reference advice is correct as-is — mark as [TESTED]
- [ ] Reference advice needs revision — describe what should change
- [ ] Reference advice is wrong for this context — describe the exception
```

---

## Key metrics to track in result entries

- **Brand recognition:** percentage of target customers who correctly identify the brand from positioning statement alone (tested via customer survey).
- **Consistency score:** average brand audit score across all touchpoints (1–4 scale, target 3.5+).
- **Message clarity:** percentage of target customers who can accurately paraphrase the brand's core value proposition after first exposure.
- **Competitive distinctiveness:** percentage of target customers who can differentiate this brand from the nearest competitor without prompting.

---

## Confidence level system

Reference files use these markers on recommendations:

| Marker | Meaning |
|--------|---------|
| `[HYPOTHESIS]` | Best-practice advice, no real-world results yet |
| `[TESTED: YYYY-MM-DD]` | Confirmed by at least one result entry |
| `[REVISED: YYYY-MM-DD]` | Originally hypothesis, updated based on results |
| `[CONTEXT: ...]` | Applies only in specific conditions |

The `gteam-learn` job reads this directory and proposes changes to reference files
based on accumulated results. Run it periodically to keep references current.
