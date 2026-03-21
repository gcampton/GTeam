# Customer Success Results Log

This directory stores real-world outcomes from applying GTeam customer success recommendations.
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
- **Customer segment:** [enterprise / mid-market / SMB / self-serve]
- **Product type:** [SaaS / services / marketplace / other]
- **Contract value (approx):** [ARR range or "not applicable"]
- **Starting position:** [e.g. onboarding, at-risk, expansion, churn recovery]

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

- **NRR (Net Revenue Retention):** total revenue from existing customers (including expansion, minus churn and contraction) / starting revenue × 100. Benchmark: >100% for healthy SaaS.
- **Gross churn rate:** ARR lost from cancellations in period / starting ARR. Benchmark: <5% annually for SMB, <2% for enterprise.
- **Time-to-value:** days from contract sign to first "aha moment" milestone. Track by customer tier.
- **QBR attendance rate:** percentage of scheduled QBRs where exec sponsor attended. Benchmark: >70%.
- **NPS score:** net promoter score from most recent survey cohort. Track trend, not just absolute.

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
