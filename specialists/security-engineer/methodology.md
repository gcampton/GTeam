### Task Router

Identify the security task type and load the appropriate task file. Do NOT load all task files — only the one matching the request.

| Request pattern | Task file |
|---|---|
| Threat model, attack surface, trust boundaries, STRIDE | `tasks/threat-modeling.md` |
| Security audit, vulnerability scan, OWASP review, dependency audit, secrets detection | `tasks/security-audit.md` |
| Auth design, encryption, zero trust, security architecture | `tasks/secure-architecture.md` |
| Incident response, breach analysis, post-mortem, root cause (security) | `tasks/incident-analysis.md` |

**Routing rules:**
1. Read the user's request and match to exactly one task file
2. Load that file with Read: `{{GTEAM_DIR}}/specialists/security-engineer/tasks/<file>.md`
3. Follow the loaded task's workflow end-to-end
4. If the request spans multiple tasks, run them sequentially — complete one before starting the next

**Reference loading:**
- Do NOT pre-load reference files. Use Grep to search `{{GTEAM_DIR}}/specialists/security-engineer/references/` only when you need specific guidance during a task.
- Check `{{GTEAM_DIR}}/specialists/security-engineer/checklists/` for quick verification gates.
