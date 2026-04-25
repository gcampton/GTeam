## Task Breakdown

A plan that exists only at the milestone level is not a plan. Break work down until every leaf task is executable by one person in one day or less.

**Work Breakdown Structure (WBS):** Decompose the project top-down: Project → Phases → Deliverables → Work Packages → Tasks. Stop decomposing when a task meets all of: single owner, ≤1 day effort, clear acceptance criterion. Tasks that can't be estimated are tasks that aren't understood — spike them.

**Task template:**

```markdown
**ID:** [T-001]
**Title:** [Action verb + object, e.g. "Implement user login API endpoint"]
**Description:** [What needs to be done and why]
**Owner:** [Single person — not a team]
**Estimate:** [Hours or days]
**Dependencies:** [Task IDs that must complete first]
**Acceptance Criteria:**
- [ ] [Specific, testable condition]
- [ ] [Specific, testable condition]
```

**Critical path identification:** Map task dependencies visually or in a table. The critical path is the longest chain of dependent tasks — it determines the earliest possible completion date. Any delay on the critical path delays the project. Prioritise unblocking critical path tasks above all else.

### User Story Templates

Use the appropriate template for the type of work. Every story must have a persona, an action, and an outcome.

**Feature Story:**
"As a [persona], I want to [action] so that [outcome]."

**Improvement Story:**
"As a [persona], I want [existing feature] to [improvement] so that [outcome]."

**Bug Story:**
"As a [persona], when I [action], I expect [expected behaviour] but instead [actual behaviour]."

**Enabler Story (technical):**
"In order to [technical goal], we need to [technical action] so that [downstream benefit]."

**Integration Story:**
"As a [persona], I want [System A] to [interaction] with [System B] so that [outcome]."

### Story Antipatterns

| Antipattern | Example | Fix |
|---|---|---|
| Solution story | "As a dev, I want to add a Redis cache" | Reframe: "As a user, I want pages to load in < 2s" |
| Compound story | "...I want to create, edit, and delete items" | Split into 3 stories |
| Missing persona | "As a user..." (too generic) | Use specific persona: "As a hiring manager..." |
| Vague AC | "System handles errors gracefully" | Specify: "Given invalid email, then show 'Enter a valid email' below the field" |
| Gold-plated | Story includes nice-to-haves mixed with essentials | Split into MVP story + enhancement story |
| No outcome | "As a user, I want a dashboard" (no "so that") | Add outcome: "...so that I can monitor daily sales at a glance" |

**Milestone definition:** Define no more than 5 milestones per project phase. Each milestone must be a concrete, verifiable state of the project — not a date. Example: "All API endpoints implemented and passing integration tests" is a milestone. "Week 4 complete" is not.
