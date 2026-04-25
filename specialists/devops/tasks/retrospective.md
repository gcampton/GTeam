## Engineering Retrospective

**Gather:** Time period (default: last 7 days). Detect team members from commit history.

**Data collection:**
```bash
git log --since="7 days ago" --oneline --stat
git log --since="7 days ago" --format="%an" | sort | uniq -c | sort -rn
```

**Analysis per contributor:**
- Commit count and lines changed
- Types of work: features, fixes, refactors, docs, tests
- Specific praise: one concrete thing they did well (reference actual commit)
- Growth area: one specific pattern to improve (constructive, not critical)

**Team-level analysis:**
- Test coverage trend: did tests increase, decrease, or stay flat?
- Technical debt: new TODOs added vs resolved
- Velocity: was the week high/low output? Why?
- Blockers: any commits with "fix", "revert", "hotfix" — what caused them?

**Output:**
- Per-person summary (praise + growth area)
- Team health metrics table
- Top 3 wins for the period
- Top 3 focus areas for next period
