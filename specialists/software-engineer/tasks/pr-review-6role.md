## 6-Role PR Review

**Use when:** A PR is ready for final review before merge. Run after standard Code Review for significant changes.

**Six reviewer lenses — work through all six:**

**1. Security reviewer:**
- Injection attacks (SQL, command, LDAP, template, prompt)
- Authentication and authorisation checks on every new endpoint/action
- Secrets management: no hardcoded credentials, tokens, or keys
- Input validation at all trust boundaries
- Verdict: PASS / FAIL (security failures block merge without exception)

**2. Performance reviewer:**
- Database queries: N+1 patterns, missing indexes, full table scans in hot paths
- Unbounded loops or recursion on user-supplied data
- Caching opportunities missed or over-invalidated
- Memory allocations in tight loops
- Verdict: PASS / WARN / FAIL

**3. Correctness reviewer:**
- Does the code actually do what the PR description says?
- Edge cases: empty collections, null/undefined, zero values, max values, concurrent calls
- Error paths: are all error cases handled? Do they return meaningful messages?
- Idempotency: can this be safely retried?
- Verdict: PASS / FAIL

**4. Maintainability reviewer:**
- Can a new engineer understand this code in 10 minutes?
- Functions doing more than one thing (split them)
- Magic numbers or strings (extract to named constants)
- Dead code introduced or existing dead code not cleaned up
- Test coverage: new logic has tests; tests are readable as documentation
- Verdict: PASS / WARN / FAIL

**5. UX reviewer (for UI changes):**
- Does the change work correctly on mobile viewports?
- Accessible: keyboard navigable, screen reader compatible, colour contrast ≥ 4.5:1
- Loading states, error states, and empty states handled
- Consistent with existing design patterns in the app
- Verdict: PASS / WARN / FAIL / N/A

**6. Business logic reviewer:**
- Does this match the PRD / ticket acceptance criteria exactly?
- Are there edge cases the ticket didn't mention that could cause business impact?
- Feature flags or gradual rollout needed?
- Any downstream systems or integrations that need updates?
- Verdict: PASS / WARN / FAIL

**Final verdict:**
- Any FAIL → blocked, must fix before merge
- 3+ WARNs in the same category → treat as FAIL
- All PASS → approve with confidence

**Output:**
- Per-lens verdict table with specific findings
- Blocking issues (FAIL) listed first with required changes
- Non-blocking suggestions (WARN) listed separately
- Merge recommendation: Approve / Approve with minor changes / Request changes / Block
