# PRD Template (standalone)

Clean copy-paste template. Guidance is in the methodology; this is the blank form.

---

```markdown
# PRD: [Feature / Initiative Name]
**Status:** Draft | In Review | Approved | In Development | Shipped
**Author:** [PM name]
**Last Updated:** [Date]
**Version:** 1.0
**Stakeholders:** [Eng Lead], [Design Lead], [Marketing], [Legal if needed]

---

## 1. Problem Statement

**Who:** [Persona / user segment]
**Pain:** [Specific pain — not "users want X"]
**Context:** [When / where / how often does this occur?]
**Cost of inaction:** [What happens if we don't solve this?]

**Evidence:**
- User research: [Key insight, n=X]
- Behavioral data: [Metric that shows the problem]
- Support signal: [Ticket volume / theme]
- Competitive signal: [What competitors do or don't do]

**JTBD link:** [Reference to JTBD canvas — which desired outcomes this addresses]

---

## 2. Goals & Success Metrics

| Goal | Primary Metric | Baseline | Target | Window |
|------|---------------|----------|--------|--------|
| [Goal] | [Metric] | [Current] | [Target] | [e.g. 60 days post-launch] |

**Guardrail metrics** (must not regress):
- [Metric]: must stay above [threshold]

---

## 3. Out of Scope

Explicitly excluded from this iteration:
- [Not X] — reason: [why deferred] — revisit condition: [when this would move up]
- [Not Y] — reason: [why]

---

## 4. Solution

**Chosen approach:** [Option name from brainstorming brief]
**Why this approach:** [2–3 sentences citing trade-offs]

### User Stories

**Story 1:** As a [persona], I want to [action] so that [measurable outcome].

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [result]
- [ ] Given [edge case], when [action], then [fallback]
- [ ] [Map to JTBD desired outcome: ...]

**Story 2:** ...

---

## 5. Technical Considerations

**Dependencies:**
| System / team | Needed for | Owner | Risk |
|--------------|-----------|-------|------|
| [API / service] | [Reason] | [Name] | H/M/L |

**Known Risks:**
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | M | H | [Specific action] |

**Open questions** (must resolve before dev start):
- [ ] [Question] — Owner: [Name] — Deadline: [Date]

---

## 6. Design & UX

**Figma link:** [URL or "TBD"]
**Key UX decisions:** [Any non-obvious design choices with rationale]
**Accessibility:** [Any specific A11y requirements]

---

## 7. Launch Plan

| Phase | Date | Audience | Success Gate |
|-------|------|----------|-------------|
| Internal alpha | [date] | Team only | No P0 bugs |
| Closed beta | [date] | [N] opted-in users | CSAT ≥ 4/5 |
| GA rollout | [date] | 20% → 100% | Primary metric on target at 20% |

**Feature flag name:** `[flag_name]`
**Rollback criteria:** If [metric] drops below [threshold] or error rate > [X]%, revert flag.

---

## 8. Sign-Off

| Stakeholder | Role | Approved | Date |
|-------------|------|---------|------|
| [Name] | Eng Lead | [ ] | |
| [Name] | Design Lead | [ ] | |
| [Name] | Business | [ ] | |

Do not begin development without written approval from all three.
```
