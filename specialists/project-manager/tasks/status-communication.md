## Status & Communication

Stakeholders who don't receive information will invent it. Your job is to make sure they're working with facts.

**Weekly status report format:**

```markdown
# Status Report: [Project Name] — Week of [Date]

## Overall Status: [Green / Amber / Red]

| Workstream | Status | Notes |
|------------|--------|-------|
| [Area 1]   | Green  | On track for milestone X |
| [Area 2]   | Amber  | Risk: dependency delay, mitigation in progress |
| [Area 3]   | Red    | Blocked — decision needed (see below) |

## Decisions Needed from Stakeholders
- **[Decision]** — context, options, recommendation, needed by [date]

## Blockers
| Blocker | Owner | Due Date |
|---------|-------|----------|
| [Description] | [Name] | [Date] |

## Commitments for Next Week
- [Specific deliverable] — Owner: [Name]
- [Specific deliverable] — Owner: [Name]

## Completed This Week
- [What shipped or was completed]
```

**RAG escalation rules:**
- **Green:** On track. No stakeholder action needed.
- **Amber:** At risk. A specific threat exists with a mitigation in progress. Stakeholders are informed but no decision is needed yet. If mitigation doesn't resolve within one sprint cycle, escalate to Red.
- **Red:** Blocked or off track. A decision or resource is needed from a stakeholder by a specific date. Do not stay Red for more than one report without escalating to the project sponsor directly — phone call, not email.

**Change request process:** Any request to add scope, extend timeline, or change a deliverable is a change request. No exceptions. Log it immediately:
1. Document what's being requested and by whom
2. Estimate the impact on timeline, budget, and other deliverables
3. Present options (absorb vs. defer vs. descope something else)
4. Get written sign-off before absorbing into the plan

Never absorb a change silently. Silent absorption makes the PM accountable for scope the team never agreed to.
