### Architecture Discovery Phase

Before writing any documentation, perform discovery:

1. **Map the system:** Identify components, dependencies, data flows, external integrations
2. **Identify audiences:** Who reads this? (developers, operators, architects, end users)
3. **Assess existing docs:** What exists? What's outdated? What's missing?
4. **Prioritise gaps:** Broken docs (blocking users) → Missing docs (frequently asked) → Improvement (clarity/completeness)

Discovery artefacts:

- **Component inventory** — name, owner, repo, status for each component
- **Audience matrix** — audience → what they need → entry point document
- **Gap analysis table** — document → status (missing/outdated/adequate) → priority

Do not skip discovery. Writing without it produces docs that are technically correct but structurally useless — they answer questions nobody asked and miss the ones everyone has.

---

### Documentation Audit

Read existing docs before writing anything. Audit across four dimensions:

- **Accuracy** — does the doc match current behaviour? Run the steps yourself to check.
- **Completeness** — are there missing steps, parameters, or error scenarios?
- **Clarity** — can a target user follow it without guessing or asking for help?
- **Findability** — is content organised in the order a user needs it, not the order it was built?

Output a gap analysis that prioritises issues into three tiers: **broken** (wrong information that will cause failures), **missing** (gaps that leave users stranded), **needs improvement** (present but unclear or incomplete). Address broken first, then missing, then improvement.

---

### API Documentation

Document every endpoint with:

- **Method + path** at the top (`POST /v1/orders`)
- **Description** — what it does and when to use it, not how it's implemented
- **Request parameters table** — name / type / required / description / example value
- **Request body schema** — field-by-field with types, constraints, and examples
- **Response schema** — success and error shapes, with example responses
- **Error codes** — each code, what causes it, and how to fix it
- **Working code example** — curl plus at least one SDK language

Put authentication upfront in its own section before any endpoint docs. Document rate limits, pagination, and versioning at the top of the reference, not buried in individual endpoints.

The test: a developer who has never seen this API must be able to make a successful authenticated request within 10 minutes using only your docs.

---

### Developer Guides & Tutorials

**Getting started guide:** Get the user to their first successful API call or working feature use within 10 minutes. No theory before they've seen it work. Install → authenticate → one working call → what just happened.

**Tutorial structure:**
1. What you'll build (show the end result upfront)
2. Prerequisites (exact versions, accounts needed, with links to set them up)
3. Step-by-step — each step is atomic and ends in a verifiable state the user can check
4. What you learned — connect the mechanics to the concepts

**How-to guides:** Task-focused, not concept-focused. Scannable headers that complete the sentence "How to…". Code block for every command. Show expected output after commands that produce it. Call out failure modes at the step where they occur, not in a separate troubleshooting section.

Rule: never combine installation, configuration, and usage into one wall of text. Each is its own section with its own clear heading.

---

### README Files

Every README must answer three questions within the first screen: what is this, why should I care, how do I start.

Structure:
1. One-sentence description of what the project does and who it's for
2. Badges: CI status, license, package version
3. What it does — 2–3 sentences on the problem it solves, optionally with a screenshot or GIF
4. Installation — copy-pasteable, tested commands including all prerequisites
5. Quick start — 5 lines or fewer to a working result
6. Configuration reference — all options, types, defaults, and descriptions in a table
7. Contributing — how to run tests, how to submit changes
8. License

Test every install command in a clean environment (fresh container or VM) before publishing. If you can't copy-paste your own README and have it work, it's not ready.

---

### Release Notes & Changelogs

Write for users, not engineers. If the entry makes sense only to someone who worked on the code, rewrite it.

Format: **Added** / **Changed** / **Fixed** / **Deprecated** / **Removed**

Each entry must answer two questions: what changed, and why does it matter to the user? Implementation details go in commit messages and PRs, not release notes.

Breaking changes get a migration guide linked from the entry — not a vague "see the migration guide", a direct link to the specific guide for this version. Version number and release date are required on every entry, no exceptions.

Deprecated items include: what's deprecated, what replaces it, and which version it will be removed in.

---

### Visual Communication

**When diagrams are required:**

- System architecture (> 3 components)
- Data flow (> 2 transformation steps)
- Sequence diagrams (> 2 actors in an interaction)
- Decision trees (> 3 decision points)

**Diagram guidelines:**

- Use Mermaid syntax for version-controllable diagrams
- Label all arrows (what data/control flows)
- Include a legend if > 5 element types
- Keep diagrams to one screen width — split if wider
- Alt-text required for accessibility

**Diagram types and when to use each:**

| Type | Use When | Tool |
|---|---|---|
| Architecture | Showing system components and connections | Mermaid flowchart |
| Sequence | Showing request/response between services | Mermaid sequenceDiagram |
| Flowchart | Showing decision logic or process steps | Mermaid flowchart |
| ER diagram | Showing data model relationships | Mermaid erDiagram |
| State diagram | Showing lifecycle of an entity | Mermaid stateDiagram |

See `references/diagram-patterns.md` for Mermaid syntax quick reference and examples.

---

### Reading Paths for Multiple Audiences

Different audiences need different entry points into the same documentation:

| Audience | Needs | Entry Point | Depth |
|---|---|---|---|
| New developer | Get running locally | Quick-start guide | Step-by-step, copy-paste |
| Contributing developer | Understand architecture to make changes | Architecture overview → module docs | Conceptual + reference |
| Operator | Deploy, monitor, troubleshoot | Runbook / operations guide | Procedural |
| Architect | Evaluate design decisions and trade-offs | Architecture Decision Records (ADRs) | Rationale-focused |
| End user | Accomplish tasks with the product | User guide / tutorials | Task-oriented |

Design principle: **progressive disclosure** — start with the simplest useful information, link to deeper detail. Every page should be useful on its own without requiring the reader to have read everything else first.

---

### Long-Form Documentation Structure

For comprehensive technical manuals (10+ pages):

**Standard section order:**

1. Executive summary (1 page — what, why, for whom)
2. Architecture overview (diagrams + narrative)
3. Key design decisions (ADR format: context → decision → consequences)
4. Component deep-dives (one per major component)
5. Data model and flows
6. Security model (authn, authz, data classification)
7. Operations guide (deploy, monitor, troubleshoot, scale)
8. API reference (if applicable)
9. Glossary
10. Appendices (configuration reference, migration guides)

**Cross-document linking:**

- Every page should link to its parent and siblings
- Use consistent anchor naming: `#{section}-{subsection}`
- Include "Prerequisites" at top linking to required reading
- Include "Next steps" at bottom linking to logical next document

The test: can a reader enter at any section and orient themselves within 30 seconds? If not, add context links and a "where you are" breadcrumb.

---

### Final Documentation Delivery Gate

Before submitting any documentation output:

1. Run a completeness pass against the request prompt and verify every required element is present.
2. Ensure all code blocks are complete and executable (no truncated snippets, placeholders, or partial lines).
3. If writing getting-started docs, include:
   - an upfront 5-line quickstart
   - explicit prerequisites including credentials/API keys
   - progressive auth -> CRUD -> webhooks flow
   - troubleshooting for common setup failures
4. If producing audit/update plans, include:
   - explicit gap-analysis method
   - prioritisation by endpoint usage or business criticality
   - review + verification workflow proving docs match live behavior
5. End with a concise decision-ready summary: what changed, user impact, and recommended next action.
