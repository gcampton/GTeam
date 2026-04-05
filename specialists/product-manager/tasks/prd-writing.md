### Product Requirements Document (PRD)

The PRD is not a spec document — it is a shared understanding document. Engineers, designers, and stakeholders should all be able to read it and know what they're building, why it matters, and how success will be measured.

**Full PRD template:**

```markdown
# PRD: [Feature / Initiative Name]
**Status:** Draft | In Review | Approved | In Development | Shipped
**Author:** [PM]  **Last Updated:** [Date]  **Version:** [X.X]
**Stakeholders:** [Eng Lead, Design Lead, Marketing, Legal if needed]

---

## 1. Problem Statement
What specific user pain or business opportunity are we solving?
Who experiences it, how often, and what is the cost of not solving it?

**Evidence:**
- User research: [interview findings, n=X]
- Behavioral data: [metric showing the problem]
- Support signal: [ticket volume / theme]
- Competitive signal: [what competitors do or don't do]

---

## 2. Goals & Success Metrics
| Goal | Primary Metric | Baseline | Target | Window |
|------|---------------|----------|--------|--------|
| [Goal] | [Metric] | [Current] | [Target] | [e.g. 60 days post-launch] |

**Guardrail metrics** (must not regress): [e.g. error rate, CSAT, load time]

---

## 3. Out of Scope
Explicitly state what this initiative will NOT address in this iteration:
- [Not X — reason and revisit condition]
- [Not Y — reason]

---

## 4. User Personas & Stories
**Primary Persona:** [Name] — [brief context]

**Story 1:** As a [persona], I want to [action] so that [measurable outcome].
**Acceptance Criteria:**
- [ ] Given [context], when [action], then [result]
- [ ] Given [edge case], when [action], then [fallback]

---

## 5. Technical Considerations
**Dependencies:**
- [System / team / API] — needed for [reason] — owner: [name] — risk: H/M/L

**Known Risks:**
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | M | H | [Action] |

**Open questions** (resolve before dev start):
- [ ] [Question] — Owner: [name] — Deadline: [date]

---

## 6. Launch Plan
| Phase | Date | Audience | Success Gate |
|-------|------|----------|-------------|
| Internal alpha | [date] | Team | No P0 bugs |
| Closed beta | [date] | [N] opted-in users | CSAT ≥ 4/5 |
| GA rollout | [date] | 20% → 100% over 2 weeks | Metrics on target at 20% |

**Rollback criteria:** If [metric] drops below [threshold] or error rate exceeds [X]%, revert flag.
```

**Getting sign-off:** Send the PRD for async review 48 hours before the sign-off meeting. In the meeting: walk through problem statement, success metrics, and out-of-scope only — the rest is pre-read. Collect written approval from Eng Lead, Design Lead, and the relevant business stakeholder. Do not begin development without it.
