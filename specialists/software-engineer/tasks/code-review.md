## Code Review

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
