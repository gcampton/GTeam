## Spec Quality & Drift Detection

**Use when:** Starting a new project or sprint, or when implementation feels out of sync with the original brief.

**Spec quality gate — every task must have before work starts:**

```markdown
Acceptance Criteria:  [ ] at least 3 testable conditions (Given/When/Then format)
Test Strategy:        [ ] how will this be verified? (unit / integration / manual / automated E2E)
Complexity Size:      [ ] S / M / L / XL (see criteria below)
Owner:                [ ] single named person
Dependencies:         [ ] listed (IDs), or "none"
Out of Scope:         [ ] what this task explicitly will NOT do
```

**Complexity sizing criteria:**

| Size | Effort | Risk | Criteria |
|------|--------|------|----------|
| S | < 4 hours | Low | Single file or component, clear solution, no external dependencies |
| M | 1–3 days | Medium | 2–5 files, known approach, 1 integration point |
| L | 3–7 days | High | Multiple systems, unclear unknowns, 2+ integration points |
| XL | > 1 week | Very High | Requires discovery spike first — split before scheduling |

**XL tasks must be split before sprint planning. No exceptions.** An unsplit XL is not a task, it's a project inside a sprint.

**Test strategy requirements by complexity:**

| Size | Minimum test strategy |
|------|----------------------|
| S | At least 1 unit test covering the change |
| M | Unit tests + manual verification steps documented |
| L | Unit tests + integration test + automated regression if touching critical path |
| XL | Full QA plan required before development starts |

**Spec drift detection — run at mid-sprint and end-of-sprint:**

Compare the current implementation state against the original spec:

1. Pull the original task description and acceptance criteria
2. Compare against what has actually been built (read the code / ask the dev)
3. Flag any of:
   - **Scope creep**: implementation includes features not in the spec
   - **Scope shrink**: acceptance criteria not met, corners cut without sign-off
   - **Requirement drift**: spec has been quietly updated mid-sprint without change request
   - **Assumption mismatch**: dev interpreted spec differently than PM intended

**Drift response:**
- Minor drift (cosmetic, no impact on AC): note in retrospective only
- Moderate drift (missing 1 AC): raise with dev immediately; either restore or raise a change request to remove the AC formally
- Major drift (scope significantly changed): stop sprint item, raise with sponsor as a change request before continuing
- Never absorb drift silently — silence makes you responsible for the outcome
