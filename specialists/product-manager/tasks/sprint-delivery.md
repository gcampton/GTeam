### Sprint & Delivery

The PM's job during delivery is not to manage the process — it's to protect the team's focus and eliminate blockers.

**Sprint goal writing:** One sentence, written in terms of user or business outcome, not tasks. Good: "Enable self-serve account deletion so users can comply with data deletion requests without contacting support." Bad: "Work on account settings and backend cleanup."

**Writing good user stories:** Apply the INVEST criteria — each story should be:
- **Independent:** Can be developed and deployed without depending on another in-progress story
- **Negotiable:** Not a fixed spec — conversation between PM and engineer about the best approach
- **Valuable:** Delivers value to a user or the business when complete
- **Estimable:** Small enough to be sized with reasonable confidence
- **Small:** Completable in one sprint (if it takes more than 3 days, split it)
- **Testable:** Acceptance criteria are clear enough to verify

Bad story: "Improve the dashboard." Good story: "As a team manager, I want to filter the dashboard by date range so that I can report on last month's activity without exporting to a spreadsheet."

**Definition of done (standard — adapt per team):**
- [ ] Acceptance criteria all pass
- [ ] Unit and integration tests written and passing
- [ ] No new lint errors introduced
- [ ] Code reviewed and approved
- [ ] Feature flag configured correctly
- [ ] Help documentation updated if user-facing
- [ ] PM has verified in staging environment

**Backlog grooming cadence:** Run a 45-minute grooming session mid-sprint (not the day before planning). Target: next sprint's candidate stories are all written, sized, and have clear acceptance criteria 48 hours before sprint planning. If stories arrive at planning unrefined, defer them — do not carry under-defined work into a sprint.

**Velocity tracking:** Track points committed vs. points delivered each sprint. After sprint 3, use a 3-sprint rolling average for capacity planning. Never use velocity as a team performance metric. Use it only to make more accurate commitments.

**Feature flag strategy for gradual rollouts:**
- Default: all new features ship behind a flag
- Internal rollout: flag on for team only (day 1–3 post-merge)
- Canary: 5–10% of users (watch error rate and core metrics for 48 hours)
- Staged rollout: 20% → 50% → 100% (move forward only when metrics are stable)
- Flag cleanup: remove flags within 2 sprints of full rollout — stale flags are technical debt
