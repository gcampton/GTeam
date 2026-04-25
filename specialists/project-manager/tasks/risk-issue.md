## Risk & Issue Management

The difference between a risk and an issue: a risk hasn't happened yet; an issue has. Both require active management.

**Risk register:**

```markdown
| Risk | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation | Owner | Status |
|------|--------------------|----------------|------------|-------|--------|
| [Description of what could go wrong] | H | H | [Specific action to reduce likelihood or impact] | [Name] | Open |
```

**Issue log:**

```markdown
| Issue | Severity (1=Critical, 2=High, 3=Medium) | Resolution Plan | Due Date | Owner | Status |
|-------|----------------------------------------|-----------------|----------|-------|--------|
| [What has gone wrong] | 1 | [Specific steps to resolve] | [Date] | [Name] | Open |
```

**Weekly review:** Both the risk register and issue log are reviewed at the weekly status meeting — not quarterly, not when someone remembers. Risks that have materialised move to the issue log. Issues that are resolved are closed with a brief note on what resolved them (for future reference).

**Escalate vs. manage:**
- Manage internally: Medium risks with clear mitigation, low-severity issues that will resolve within one sprint
- Escalate to sponsor: High-impact risks where mitigation requires resources or decisions outside the PM's authority, any Severity-1 issue immediately, any Severity-2 issue unresolved after one week
- Document every escalation: what was escalated, to whom, on what date, and what response was received
