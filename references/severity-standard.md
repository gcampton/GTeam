# GTeam Severity Standard

Shared severity scale used across all specialists. Use this vocabulary consistently so issues can be compared and prioritised across specialist outputs in a job.

---

## Severity Levels

| Level | Label | Meaning | Action required |
|-------|-------|---------|-----------------|
| S1 | **CRITICAL** | Blocks operation, causes data loss, security breach, legal liability, or complete feature failure | Fix immediately before anything else. Do not ship. |
| S2 | **HIGH** | Significant functional problem, major UX failure, or material business/legal risk | Fix before next release. Flag to stakeholder. |
| S3 | **MEDIUM** | Degraded experience, sub-optimal output, minor compliance gap, or improvement opportunity | Fix in next sprint. Does not block release. |
| S4 | **LOW** | Cosmetic, stylistic, or nice-to-have improvement | Backlog. Address when convenient. |

---

## Domain Mappings

Different specialists use domain-specific terminology — all map to the above:

| Specialist | CRITICAL | HIGH | MEDIUM | LOW |
|-----------|---------|------|--------|-----|
| software-engineer | CRITICAL | HIGH | MEDIUM | LOW |
| seo | P1 | P2 | P3 | P4 |
| lawyer | HIGH risk | MEDIUM risk | LOW risk | OK |
| project-manager | Severity 1 | Severity 2 | Severity 3 | — |
| ui-designer | CRITICAL category | HIGH | MEDIUM | LOW |
| qa-testing | CRITICAL | HIGH | MEDIUM | LOW |

When a job runs multiple specialists, translate to the standard S1/S2/S3/S4 labels in the job summary so issues from different specialists can be ranked together.

---

## Ship-Readiness Rules

| Condition | Ship verdict |
|-----------|-------------|
| Any CRITICAL open | **Blocked** — do not ship |
| Any HIGH open | **At risk** — requires explicit sign-off to ship |
| Only MEDIUM/LOW open | **Ship with known issues** — document and track |
| All clear | **Ship** |

---

## Usage in Outputs

When producing issue tables, use this format:

```markdown
| File / Location | Severity | Description | Suggested fix |
|----------------|---------|-------------|---------------|
| auth/login.ts:42 | CRITICAL | SQL injection via unsanitised email param | Use parameterised query |
| checkout/form.tsx | HIGH | Missing keyboard trap in modal — focus escapes | Add focus lock on modal open |
```
