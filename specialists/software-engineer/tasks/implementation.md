## Implementation Support

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
