# Growth Hacker Results Log

This directory stores real-world outcomes from applying GTeam growth hacker recommendations.
Over time these results are used by the `gteam-learn` job to upgrade reference file
confidence levels and revise advice that doesn't hold up in practice.

---

## How to log a result

Copy the template below into a new file named `YYYY-MM-DD-brief-description.md`.
Be specific — vague entries ("it worked") don't help future calibration.

```markdown
# [Strategy Name] — [Month YYYY]

**Reference file:** [which section of methodology.md this relates to]
**Section:** [Growth Audit / Experiment Design / Acquisition Channels / Activation & Onboarding / Retention & Referral]

## Context
- **Product type:** [SaaS / e-commerce / marketplace / consumer app / B2B tool / other]
- **Stage:** [pre-PMF / post-PMF / scaling]
- **Channel tested:** [paid search / paid social / SEO / referral / product-led / other]
- **Audience:** [ICP description — e.g. "SMB finance teams, 10-50 employees"]

## What was tried
[Describe exactly what you did, following which recommendation]

## Result (after X weeks)
- **CAC:** [before] → [after]
- **LTV:** [before] → [after]
- **D30 retention:** [before] → [after]
- **Activation rate:** [before] → [after]
- **Referral k-factor:** [before] → [after]
- [Other relevant metric]: [before] → [after]

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
