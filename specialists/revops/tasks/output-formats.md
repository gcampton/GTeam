## Output Formats

**RevOps Audit Report:**

```markdown
# RevOps Audit: [Company]
Date: [YYYY-MM-DD]

## Current State
[Funnel conversion rates at each stage with benchmark comparison]

## Critical Issues
| Issue | Impact | Fix | Owner | Timeline |
|-------|--------|-----|-------|----------|
| [e.g. No MQL definition] | [Leads falling through] | [Define and implement] | [RevOps] | [2 weeks] |

## Recommended Stage Definitions
[Lifecycle stages table with entry/exit criteria]

## Lead Scoring Model
[Fit dimensions + points table] [Engagement actions + points table] [MQL threshold recommendation]

## Routing Rules
[Decision tree for lead assignment]

## Automation Backlog (prioritised)
1. [Automation name] — [trigger] → [action] — [expected impact]
2. ...

## Dashboard Spec
[Tier 1/2/3 metrics with targets]

## 30/60/90-Day Implementation Plan
- Week 1–2: [Quick wins — stage definitions, MQL criteria]
- Week 3–6: [Scoring + routing setup]
- Week 7–12: [Automation builds + dashboard]
```

Save output to `~/dev/1_myprojects/gteam/specialists/revops/results/[company]-revops-[date].md`
