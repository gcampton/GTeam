---
name: gteam-legal-review
version: 1.0.0
description: Full legal review of a contract — risk assessment, redlined document, and recommended actions. Provide a contract file or paste the text.
allowed-tools:
  - Read
  - Write
  - WebSearch
---

> GTeam update check: `cd ~/.claude/skills/gteam && git pull && bun run build`
> Autonomy mode: execute fully automatically. Only pause for decisions with meaningful consequences to the user.

# Legal Review — GTeam Job

**Starting `legal-review` — running: Lawyer**

---

## Contract Review

### Legal Review

**Gather:** Ask for the document (file path or paste). Identify: contract type, parties, governing jurisdiction if visible.

**Review checklist — work through every clause:**
1. Liability & indemnification — who bears risk, any unlimited liability exposure?
2. IP ownership — who owns work product, licenses, background IP?
3. Termination — notice periods, termination for convenience vs cause, post-termination obligations
4. Governing law & jurisdiction — which courts, which law?
5. Payment terms — amounts, milestones, late payment, currency
6. Confidentiality — scope, duration, carve-outs
7. Warranties & representations — what's promised, what's disclaimed?
8. Dispute resolution — arbitration, mediation, litigation?
9. Force majeure — what events excuse performance?
10. Assignment — can either party assign without consent?

**Risk rating per clause:** HIGH / MEDIUM / LOW / OK

**Redline:** Produce a redlined version with suggested edits inline using `[SUGGESTED: ...]` markers.

**Surface to user only when:** a clause presents HIGH risk that could be deal-breaking, or when two equally valid interpretations exist and the choice has material consequences.

**Deliver:**
- Risk summary table (clause → risk level → one-line explanation)
- Redlined document with `[SUGGESTED: ...]` inline edits
- Recommended next steps (negotiate, accept, reject, seek specialist counsel)

