## Ship Workflow

**Gather:** Confirm the target base branch. Check `git status` — working tree must be clean before shipping.

**Pre-ship checklist:**
1. Merge latest base branch (`git fetch origin && git merge origin/<base>`) — resolve conflicts if any
2. Run the full test suite — do not ship on a red build
3. Run `git diff origin/<base> --stat` — review what's going out
4. Bump `VERSION` file (semver: patch for fixes, minor for features, major for breaking changes)
5. Update `CHANGELOG.md` — add entry under `## Unreleased` with today's date, describe changes in user-facing terms (not commit messages)
6. Commit version bump + changelog together: `git commit -m "chore: release vX.Y.Z"`
7. Push branch, create PR via `gh pr create`

**PR description template:**
- What changed (user-facing summary, not a commit list)
- Why (motivation or ticket reference)
- How to test (specific steps to verify the change)
- Screenshots for UI changes
