## Systematic Debugging

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
