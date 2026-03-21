# Sales Results Log

This directory stores real-world outcomes from applying GTeam sales recommendations.
Over time these results are used by the `gteam-learn` job to upgrade reference file
confidence levels and revise advice that doesn't hold up in practice.

---

## How to log a result

Copy the template below into a new file named `YYYY-MM-DD-brief-description.md`.
Be specific — vague entries ("it worked") don't help future calibration.

```markdown
# [Strategy Name] — [Month YYYY]

**Reference file:** [which section of methodology.md this relates to]
**Section:** [Outbound Prospecting / Discovery Call / Deal Qualification / Proposal & RFP / Pipeline Management]

## Context
- **Sale type:** [outbound / inbound / channel / expansion]
- **ACV range:** [e.g. $10k–$25k / $25k–$100k / $100k+]
- **Industry / vertical:** [specific sector, not "B2B"]
- **Sales cycle length:** [e.g. 30 days / 60–90 days / 6+ months]
- **Team size:** [solo founder / small team (2–5) / dedicated sales team (6+)]

## What was tried
[Describe exactly what you did, following which recommendation — be specific enough
that someone else could replicate it]

## Result (after X days/weeks/deals)
- [Metric]: [before] → [after]
- [Metric]: [before] → [after]

## What worked
[Specific observations about what drove the positive result — be precise,
e.g. "signal-based subject lines outperformed role-based by 2.1x on reply rate"]

## What didn't work
[Specific observations about what failed or had no effect]

## Recommendation update
- [ ] Reference advice is correct as-is — mark as [TESTED]
- [ ] Reference advice needs revision — describe what should change
- [ ] Reference advice is wrong for this context — describe the exception
```

---

## Result metrics by workflow area

Log whichever metrics are relevant to the workflow being tested:

**Outbound Prospecting**
- Reply rate (overall and by signal tier)
- Positive reply rate
- Reply-to-meeting conversion rate
- Meeting booked rate (meetings booked per 100 contacts enrolled)
- Stage 1 → Stage 2 conversion rate

**Discovery Call**
- Discovery-to-qualification rate (% of discovery calls that advance to Stage 3)
- Average discovery call duration
- Number of MEDDPICC elements documented post-call (target: 5+/8)

**Deal Qualification (MEDDPICC)**
- Win rate on fully qualified deals (MEDDPICC ≥5/8 Green or Yellow) vs. underqualified
- Average deal size on qualified vs. unqualified pipeline
- Forecast accuracy (commit deals closed at what %)

**Proposal & RFP Response**
- Proposal-to-close rate
- Average time from proposal submission to decision
- Win rate when executive summary written first vs. written last
- Win rate with 3–5 win themes vs. no explicit themes

**Pipeline Management**
- Pipeline coverage ratio at quarter start vs. attainment
- Average sales cycle days (by stage and overall)
- Deal value ($) — average ACV closed
- Win rate (closed-won / total closed)
- At-risk deal recovery rate (% of flagged at-risk deals that closed)

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
