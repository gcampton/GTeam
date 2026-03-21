---
name: gteam-learn
version: 1.0.0
description: Analyse results/ logs across all specialists and propose updates to reference files — upgrading confidence levels and revising advice based on real outcomes.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Bash
---

> GTeam update check: `cd ~/.claude/skills/gteam && git pull && bun run build`
> Autonomy mode: execute fully automatically. Only pause for decisions with meaningful consequences to the user.

# GTeam Learn — Results-Based Reference Improvement

This job reads accumulated results/ entries across all specialists, compares them against current reference files, and proposes targeted edits — upgrading confidence markers and revising advice that doesn't hold up in practice.

**Only pause for user approval before writing changes to reference files.**

---

## Step 1: Discover specialists with results

Scan for result entries:

```bash
find ~/.claude/skills/gteam/specialists -path "*/results/*.md" ! -name "README.md" | sort
```

If no result files found: report "No results logged yet. Use the template in any `specialists/*/results/README.md` to log your first outcome." and stop.

---

## Step 2: For each specialist with results

For each specialist directory that has at least one result entry:

1. **Read all result files** in `specialists/{name}/results/` (skip README.md)
2. **Read all reference files** in `specialists/{name}/references/`
3. **Map results to references** — identify which section/recommendation each result entry applies to

---

## Step 3: Analyse each result

For each result entry, determine:

**A. Confidence upgrade** — does this result confirm a `[HYPOTHESIS]` recommendation without contradiction?
- If yes: propose changing `[HYPOTHESIS]` → `[TESTED: YYYY-MM-DD]` on that recommendation

**B. Revision needed** — does this result show the recommendation is wrong, incomplete, or context-dependent?
- If yes: propose a specific rewrite of the affected sentence/section
- If context-dependent: propose adding `[CONTEXT: ...]` to scope when the advice applies

**C. New insight** — does the result reveal something not covered in any reference file?
- If yes: propose a new entry in the appropriate reference file

**D. Conflict** — do multiple results contradict each other?
- Surface the conflict explicitly. Do not resolve contradictions automatically — flag for human judgement.

---

## Step 4: Build change proposal

Produce a structured change proposal before touching any files:

```
## Proposed Changes — [Specialist Name]

### Change 1: [reference file] — confidence upgrade
**Section:** [section name]
**Recommendation:** "[current text]"
**Result basis:** [result filename], outcome: [brief summary]
**Proposed change:** [HYPOTHESIS] → [TESTED: YYYY-MM-DD]

### Change 2: [reference file] — revision
**Section:** [section name]
**Current:** "[current text]"
**Result basis:** [result filename], outcome: [brief summary]
**Proposed:** "[revised text]"

### Change 3: [reference file] — new insight
**Add to section:** [section name]
**Proposed addition:** "[new text]"
```

---

## Step 5: User approval

Present the full change proposal. Ask:

> "Found [N] proposed changes across [M] specialists based on [K] result entries. Apply all, review one-by-one, or skip? (all / one-by-one / skip)"

- **all** — apply every proposed change
- **one-by-one** — show each change, wait for approve/skip before applying
- **skip** — exit without changes

---

## Step 6: Apply approved changes

For each approved change:
1. Use Edit to make the precise change to the reference file
2. Confirm: "Updated `[file]` — [description of change]"

After all changes applied:
- Report total: "[N] changes applied across [M] specialists"
- Remind: "Run `bun run gen:skill-docs` to regenerate SKILL.md files"

---

## Notes

- Never resolve conflicting results by picking one — surface conflicts for human judgement
- Never remove a recommendation based on a single negative result — add context or flag the exception
- `[TESTED]` means confirmed in at least one result; it does not mean universally true
- Preserve the original voice and structure of reference files — make surgical edits, not rewrites
