# Product Manager Results Log

This directory stores real-world outcomes from applying GTeam product management recommendations.
Over time these results are used by the `gteam-learn` job to upgrade reference file
confidence levels and revise advice that doesn't hold up in practice.

---

## How to log a result

Copy the template below into a new file named `YYYY-MM-DD-brief-description.md`.
Be specific — vague entries ("users liked it") don't help future calibration.

```markdown
# [Strategy or Technique Name] — [Month YYYY]

**Reference file:** [which file in references/ this relates to]
**Section:** [which section/recommendation was tried]

## Context
- **Product type:** [SaaS / consumer app / marketplace / platform / other]
- **Company stage:** [pre-product-market fit / growth / scale / enterprise]
- **Team size:** [PM + eng + design headcount]

## What was tried
[Describe exactly what you did, following which recommendation]

## Result (after X weeks/months)
- **Time to first user:** [days from kickoff to first real user on the feature]
- **D30 retention:** [% of users who used the feature in launch week and returned in month 1]
- **Feature adoption rate:** [% of eligible users who activated the feature within 30 days]
- **NPS impact:** [before / after, or feature users vs. non-users]
- **Revenue impact:** [ARR lift, churn reduction, or upsell attributed — or "not measured"]

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
