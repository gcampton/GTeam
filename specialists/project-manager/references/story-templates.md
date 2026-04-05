# Story Templates & Estimation Quick Reference

## Story Type Templates

### Feature Story
"As a [persona], I want to [action] so that [outcome]."

- "As a hiring manager, I want to filter candidates by skills so that I can shortlist qualified applicants faster."
- "As a subscriber, I want to receive a weekly digest email so that I stay informed without checking the app daily."

### Improvement Story
"As a [persona], I want [existing feature] to [improvement] so that [outcome]."

- "As a sales rep, I want the search bar to support fuzzy matching so that I can find contacts even with partial names."
- "As an admin, I want the export function to include date filters so that I can pull reports for specific periods."

### Bug Story
"As a [persona], when I [action], I expect [expected behaviour] but instead [actual behaviour]."

- "As a customer, when I apply a discount code, I expect the total to update immediately but instead the page shows the original price until refresh."
- "As a team lead, when I reassign a task, I expect the new assignee to be notified but instead no notification is sent."

### Enabler Story (technical)
"In order to [technical goal], we need to [technical action] so that [downstream benefit]."

- "In order to support 10x current traffic, we need to add connection pooling to the database layer so that response times stay under 200ms at peak load."
- "In order to deploy multiple times per day, we need to add automated integration tests to the CI pipeline so that regressions are caught before merge."

### Integration Story
"As a [persona], I want [System A] to [interaction] with [System B] so that [outcome]."

- "As an accountant, I want the invoicing system to sync paid invoices with Xero so that reconciliation happens automatically."
- "As a support agent, I want the CRM to pull order history from the e-commerce platform so that I can resolve queries without switching tools."

---

## Given/When/Then Template

```
Given [precondition/context]
When [action/trigger]
Then [expected outcome]
```

**Example:**
```
Given a logged-in user with items in their cart
When they click "Checkout"
Then they are redirected to the payment page with the correct total displayed
```

---

## AC Quality Checklist

- [ ] Each AC is independently testable
- [ ] No implementation details (describes what, not how)
- [ ] Covers happy path + at least one error/edge case
- [ ] Uses concrete values, not vague terms ("displays error message" not "handles errors")

### Minimum AC Count by Story Size

| Story Points | Minimum ACs | Format |
|---|---|---|
| 1-2 | 3-4 | Given/When/Then |
| 3-5 | 4-6 | Given/When/Then |
| 8 | 5-8 | Given/When/Then + edge cases |
| 13+ | Split the story first | - |

---

## Antipatterns Quick Reference

| Antipattern | Example | Fix |
|---|---|---|
| Solution story | "As a dev, I want to add a Redis cache" | Reframe: "As a user, I want pages to load in < 2s" |
| Compound story | "...I want to create, edit, and delete items" | Split into 3 stories |
| Missing persona | "As a user..." (too generic) | Use specific persona: "As a hiring manager..." |
| Vague AC | "System handles errors gracefully" | Specify: "Given invalid email, then show 'Enter a valid email' below the field" |
| Gold-plated | Nice-to-haves mixed with essentials | Split into MVP story + enhancement story |
| No outcome | "As a user, I want a dashboard" (no "so that") | Add outcome: "...so that I can monitor daily sales at a glance" |

---

## Fibonacci Estimation Scale

| Points | Complexity | Uncertainty | Example |
|---|---|---|---|
| 1 | Trivial change, single file | None - done it before | Fix typo, update config value |
| 2 | Small change, clear scope | Minimal | Add validation rule, update copy |
| 3 | Moderate, 1-2 components | Low | New API endpoint (known pattern) |
| 5 | Multi-component, some unknowns | Medium | New feature with UI + API + DB |
| 8 | Complex, cross-cutting | High | New integration with external system |
| 13 | Very complex, significant unknowns | Very high | Architecture change, new subsystem |
| 21+ | Epic - must be split | Too high to estimate | Split into smaller stories first |

**Estimation rules:**
- Use planning poker or async estimation (each team member estimates independently first)
- If estimates diverge > 2 levels, discuss - the spread reveals hidden assumptions
- Velocity = rolling average of last 3 sprints (don't use until sprint 2+)
- Never convert points to hours - they measure complexity, not time
