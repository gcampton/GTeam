# Data Analyst Results Log

This directory stores real-world outcomes from applying GTeam data analysis recommendations.
Over time these results are used by the `gteam-learn` job to upgrade reference file
confidence levels and revise advice that doesn't hold up in practice.

---

## How to log a result

Copy the template below into a new file named `YYYY-MM-DD-brief-description.md`.
Be specific — vague entries ("the analysis was useful") don't help future calibration.

```markdown
# [Analysis Type / Strategy] — [Month YYYY]

**Reference file:** [which file in references/ this relates to]
**Section:** [which section/recommendation was tried]

## Context
- **Data type:** [transactional / behavioural / marketing / operational / survey]
- **Business domain:** [e-commerce / SaaS / marketplace / fintech / other]
- **Team size:** [number of stakeholders consuming this analysis]
- **Tools used:** [SQL dialect, Python, spreadsheet tool, BI platform]

## What was tried
[Describe exactly what analysis was run or what dashboard was built, following which recommendation]

## Result (after X weeks)
- [Metric]: [before] → [after]
- [Metric]: [before] → [after]

## What worked
[Specific observations about what drove faster decisions or better outcomes]

## What didn't work
[Specific observations about what failed to land with stakeholders or produced unreliable results]

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

---

## Key metrics to track

- **Decision speed** — did the analysis reduce the time from question to decision for the stakeholder?
- **Analysis accuracy** — were the conclusions borne out by subsequent data or business outcomes?
- **Dashboard usage rate** — is the dashboard being used regularly, or was it built and abandoned?

The `gteam-learn` job reads this directory and proposes changes to reference files
based on accumulated results. Run it periodically to keep references current.
