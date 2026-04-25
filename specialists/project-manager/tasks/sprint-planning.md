## Sprint Planning

Sprint planning translates the task list into time-boxed commitments a team can actually deliver.

**Sprint goal definition:** Every sprint has one sentence that describes what the team will achieve and why it matters. "Complete user authentication and onboarding flow so we can begin beta testing" is a sprint goal. "Work on various tasks" is not.

**Capacity planning:**
1. Count available working hours for the sprint period
2. Subtract known overhead: team meetings (estimate actual hours, not calendar blocks), 1:1s, code review time, interruptions (reserve 20% for stable teams, 30% for new teams)
3. The remainder is your available capacity for sprint work — be honest, not optimistic

**Sizing:** Use t-shirt sizes (S/M/L/XL) for initial roadmap estimation, story points or hours for sprint-level commitment. Calibrate against a reference task the team agrees on. Never let a single story exceed 40% of sprint capacity — split it.

### Estimation with Fibonacci Scale

| Points | Complexity | Uncertainty | Example |
|---|---|---|---|
| 1 | Trivial change, single file | None — done it before | Fix typo, update config value |
| 2 | Small change, clear scope | Minimal | Add validation rule, update copy |
| 3 | Moderate, 1–2 components | Low | New API endpoint (known pattern) |
| 5 | Multi-component, some unknowns | Medium | New feature with UI + API + DB |
| 8 | Complex, cross-cutting | High | New integration with external system |
| 13 | Very complex, significant unknowns | Very high | Architecture change, new subsystem |
| 21+ | Epic — must be split | Too high to estimate | Split into smaller stories first |

**Estimation rules:**
- Use planning poker or async estimation (each team member estimates independently first)
- If estimates diverge > 2 levels, discuss — the spread reveals hidden assumptions
- Velocity = rolling average of last 3 sprints (don't use until sprint 2+)
- Never convert points to hours — they measure complexity, not time

### Acceptance Criteria Standards

Minimum AC count by story size:

| Story Points | Minimum ACs | Format |
|---|---|---|
| 1–2 | 3–4 | Given/When/Then |
| 3–5 | 4–6 | Given/When/Then |
| 8 | 5–8 | Given/When/Then + edge cases |
| 13+ | Split the story first | — |

**Given/When/Then template:**
```
Given [precondition/context]
When [action/trigger]
Then [expected outcome]
```

**AC quality checklist:**
- [ ] Each AC is independently testable
- [ ] No implementation details (describes what, not how)
- [ ] Covers happy path + at least one error/edge case
- [ ] Uses concrete values, not vague terms ("displays error message" not "handles errors")

**Backlog prioritisation (MoSCoW):**
- **Must:** Non-negotiable for this sprint's goal — without it, the sprint fails
- **Should:** High value, expected, but can survive one sprint delay without catastrophe
- **Could:** Nice to have — pull in only after Must and Should are committed and capacity remains
- **Won't:** Explicitly deferred — document why, to prevent it re-surfacing mid-sprint

**Velocity tracking:** Do not use velocity for forecasting until sprint 2 is complete. After sprint 2, use a 3-sprint rolling average. Velocity is a planning tool, not a performance metric — never use it to compare individuals or teams.
