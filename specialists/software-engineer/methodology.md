### Browse Setup

When a URL is provided, run this setup block before any browse step:

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/.claude/skills/gteam/browse/dist/browse
[ -x "$B" ] && echo "READY: $B" || echo "BROWSE NOT AVAILABLE"
```

If `BROWSE NOT AVAILABLE`: skip all `$B` steps and use WebFetch instead for URL inspection.

---

### Code Review

**Gather:** Confirm the base branch (detect with `git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'`, fallback to `main`). Run `git diff origin/<base>` for the full diff. If on the base branch with no diff, say so and stop.

**Two-pass review:**

Pass 1 — Correctness & safety:
- SQL injection, XSS, command injection, path traversal, open redirects
- LLM trust boundary violations (user input passed to prompts without sanitisation)
- Conditional side effects (mutations inside conditionals without rollback)
- Race conditions and missing locks on shared state
- Auth/permission checks missing or bypassable
- Secrets or credentials in code or test fixtures

Pass 2 — Structure & maintainability:
- Functions doing more than one thing
- Duplicated logic that should be extracted
- Missing error handling at system boundaries
- Dead code or unused imports
- Tests absent for new logic; tests that only test the happy path
- Unclear variable/function names where intent is non-obvious

**Output:**
- Issue table: file:line → severity (CRITICAL / HIGH / MEDIUM / LOW) → description → suggested fix
- Inline fix suggestions for CRITICAL and HIGH issues (copy-ready, not just descriptions)
- Summary: ship-ready / needs fixes before merge / blocked

---

### QA Testing

**Gather:** URL of running application, or path to codebase. Clarify: Quick (critical/high bugs only), Standard (+ medium), or Exhaustive (+ cosmetic). Default: Standard. If a URL is provided, use `$B` to load and test the live app.

**Testing sequence:**
1. Load and verify the app starts: `$B goto <url> && $B console && $B snapshot`
2. Test primary user flows end-to-end (registration, login, core feature, logout)
3. Test edge cases: empty inputs, very long inputs, special characters, concurrent actions
4. Test error states: invalid credentials, network failure, missing required fields
5. Test responsive layout: desktop, tablet, mobile breakpoints
6. Check accessibility basics: focusable elements, alt text on images, colour contrast
7. Verify no sensitive data exposed in network responses or localStorage

**For each bug found:**
- Severity: CRITICAL (data loss/security) / HIGH (feature broken) / MEDIUM (degraded UX) / LOW (cosmetic)
- Repro steps (numbered, copy-pasteable)
- Expected vs actual behaviour
- Screenshot or console output as evidence

**Fix loop:** Fix bugs in severity order, commit each fix atomically, re-verify before moving to next.

**Output:**
- Health score before and after (0–100)
- Bug table: component → severity → description → status (fixed/open)
- Ship-readiness verdict

---

### Implementation Support

**Gather:** Description of the task — new feature, bug fix, or refactor. Read relevant existing files before proposing changes.

**Approach:**
1. Understand the existing code structure before touching anything
2. Write failing tests first (TDD) where the codebase has tests
3. Implement the minimal change that satisfies the requirement — no gold-plating
4. Run existing tests after every change; fix regressions immediately
5. Commit in logical, atomic chunks with clear messages

**Code standards:**
- Match the style, naming, and patterns already in the codebase
- No new dependencies without justification
- No abstractions for one-off operations
- Error handling only at system boundaries (user input, external APIs)
- Security: validate all user input, parameterise all queries, never trust client-supplied IDs

**Verification gate (mandatory before declaring any task complete):**
1. Run the test suite — show the output, do not summarise it
2. If tests fail, fix immediately before moving on
3. If no tests exist, manually verify the changed behaviour end-to-end
4. Do NOT say "should work" or "looks correct" — demonstrate it works with evidence

---

### Systematic Debugging

**Use when:** A bug exists, a test is failing, or behaviour is unexpected. Never guess — diagnose.

**Process:**

**Step 1 — Reproduce first:**
- Confirm the bug is reliably reproducible before touching any code
- Write down the exact steps, inputs, and environment needed to trigger it
- If you can't reproduce it, you can't fix it — ask for more information

**Step 2 — Form a hypothesis:**
- State what you think is happening and why (one sentence)
- Identify the smallest possible piece of code that could cause this
- Do not look at more code than necessary — scope creep in debugging wastes time

**Step 3 — Isolate the failure:**
- Add logging or a debugger breakpoint at the hypothesis point — do not scan unrelated code
- Check: does the symptom match the hypothesis? If no, revise the hypothesis
- Bisect if needed: binary-search through code changes or data to find the turning point

**Step 4 — Check `references/debugging-patterns.md`:**
- Look up the failure pattern — many bugs are instances of known patterns
- Common categories: off-by-one, race condition, wrong async/await, type coercion, scope leak, stale closure, N+1 query, missing null check

**Step 5 — Fix minimally:**
- Make the smallest change that fixes the root cause
- Do NOT refactor surrounding code while fixing a bug — that is a separate commit
- Write a test that would have caught this bug (regression test)

**Step 6 — Verify end-to-end:**
- Run the full test suite — not just the affected test
- Manually verify the original repro steps no longer produce the bug
- Check that the fix doesn't break adjacent behaviour

**Output:**
- Root cause (one sentence: "The bug was X because Y")
- Fix applied (file:line, what changed)
- Regression test added (or explanation why one isn't possible)

---

### 6-Role PR Review

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
