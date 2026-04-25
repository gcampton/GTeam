## Release & Documentation

**Post-ship documentation update — run after a PR merges:**

1. Read current `README.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md`, `CLAUDE.md` (if present)
2. `git diff origin/<base>` — identify everything that shipped
3. Update each doc:
   - **README.md** — update feature list, screenshots, quickstart commands if changed
   - **ARCHITECTURE.md** — update diagrams, data flow, component descriptions for structural changes
   - **CONTRIBUTING.md** — update setup steps, test commands, any new conventions
   - **CLAUDE.md** — update commands, project structure, any new patterns Claude needs to know
4. **CHANGELOG.md** — polish the voice of the new entry; remove jargon; make it readable by a non-technical user
5. Clean up `TODOS.md` — mark shipped items done, remove stale items
6. Commit all doc updates as a single commit: `git commit -m "docs: update for vX.Y.Z"`
