# JTBD Canvas Template

Copy this template when starting a new feature or product area. Fill every field before opening a PRD.

---

```markdown
# JTBD Canvas: [Job Name / Feature Area]
**Date:** [Date]  **PM:** [Name]  **Research basis:** [N interviews / data source]

---

## Job Statement
When [situation — the trigger context],
I want to [motivation — what they're trying to accomplish],
So I can [expected outcome — the end state they're aiming for].

---

## Job Dimensions

**Functional job** (what they're practically trying to do):
[One sentence]

**Emotional job** (how they want to feel during or after):
[One sentence]

**Social job** (how they want to be perceived by others):
[One sentence]

---

## Job Executor
**Who:** [Role or persona]
**When triggered:** [What situation causes this job to arise?]
**How often:** [Daily / Weekly / Monthly / Ad-hoc]
**Urgency:** [Planned vs. urgent; time pressure context]

---

## Current Solutions (the "hired" alternatives)

| Current solution | Why it's inadequate | Our opportunity |
|-----------------|--------------------|----|
| [Workaround 1] | [Specific gap or pain] | [How we solve it better] |
| [Competitor] | [Specific gap] | [Differentiation] |
| [Manual process] | [Cost in time/quality] | [What we automate or improve] |

---

## Desired Outcomes

Rate each 1–10:
- **Importance:** How critical is this outcome to successfully completing the job?
- **Satisfaction:** How satisfied are users with current solutions' ability to deliver this?
- **Opportunity score:** Importance + max(Importance − Satisfaction, 0)
  → Score ≥ 10: underserved, high priority
  → Score 6–9: worth addressing
  → Score < 6: satisfied, lower priority

| # | Desired outcome (direction + metric + object + context) | Importance | Satisfaction | Opportunity |
|---|--------------------------------------------------------|------------|--------------|-------------|
| 1 | Minimise the time to [action] when [context] | /10 | /10 | |
| 2 | Increase the likelihood of [outcome] when [context] | /10 | /10 | |
| 3 | Reduce the effort required to [action] | /10 | /10 | |
| 4 | Increase the accuracy of [output] | /10 | /10 | |
| 5 | Minimise the risk of [negative outcome] | /10 | /10 | |
[Add rows as needed — aim for 10–15 outcomes]

**Top 3 by opportunity score:**
1. [Outcome] — score: [X]
2. [Outcome] — score: [X]
3. [Outcome] — score: [X]

---

## Solution Hypothesis (link to PRD)

For each top-3 outcome, one sentence on the feature hypothesis:
1. "If we build [X], users will be able to [outcome] faster/better because [mechanism]."
2. ...
3. ...
```

---

## How to use this canvas

1. **Fill before the PRD.** The canvas reveals what to build; the PRD specifies how.
2. **Outcome statements use the formula:** `[direction] [metric] [object] [context]`
   - Good: "Minimise the time it takes to find a customer record when triaging a support ticket"
   - Bad: "Make search faster" (no direction, no context)
3. **Rate outcomes with users, not in a meeting room.** Survey or interview 10+ users per segment.
4. **Revisit after 6 months.** Importance and satisfaction scores shift as the market and product mature.
