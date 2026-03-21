# UI Designer Results Log

This directory stores real-world outcomes from applying GTeam UI designer recommendations.
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
- **Product type:** [web app / mobile app / dashboard / marketing site / design system / other]
- **User base:** [e.g. B2B SaaS users, general consumers, internal tools, developers]
- **Design tool:** [e.g. Figma, Sketch, Adobe XD]
- **Starting position:** [e.g. usability score, task completion rate, bounce rate, design debt state]

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
