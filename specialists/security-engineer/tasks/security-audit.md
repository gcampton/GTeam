### Security Audit

**Use when:** Reviewing an existing application, codebase, or API for security vulnerabilities. Covers OWASP Top 10, dependency vulnerabilities, secrets detection, and API security.

**Gather:**
- Codebase path or repository URL
- Technology stack (language, framework, database, deployment)
- Scope: full audit, specific area (auth, API, data handling), or quick scan
- Previous audit findings if available

---

**Step 1 — OWASP Top 10 review:**

Grep `references/owasp-top-10.md` for specific categories relevant to the codebase. Check each applicable category:

1. **Broken Access Control** — IDOR, missing auth checks, privilege escalation paths
2. **Cryptographic Failures** — weak hashing, plaintext secrets, missing TLS, insecure random
3. **Injection** — SQL, NoSQL, command, LDAP, template, prompt injection
4. **Insecure Design** — missing rate limits, no abuse case handling, trust boundary violations
5. **Security Misconfiguration** — default credentials, verbose errors, unnecessary features enabled
6. **Vulnerable Components** — outdated dependencies with known CVEs
7. **Authentication Failures** — weak passwords allowed, missing MFA, session fixation
8. **Data Integrity Failures** — unsigned updates, insecure deserialization, unverified CI/CD pipelines
9. **Logging Failures** — missing audit trails, sensitive data in logs, no alerting
10. **SSRF** — unvalidated URLs, internal service access from user input

**Step 2 — Dependency vulnerability scan:**

Run the appropriate scanner for the stack:
```bash
# JavaScript/TypeScript
npm audit --json 2>/dev/null || npx audit-ci --config /dev/null 2>/dev/null
# Or check package-lock.json / bun.lockb manually

# Python
pip-audit 2>/dev/null || safety check 2>/dev/null

# Rust
cargo audit 2>/dev/null

# Go
govulncheck ./... 2>/dev/null
```

If scanners are not installed, manually check key dependencies against known CVE databases using Grep on lock files.

**Step 3 — Secrets detection:**

Search the codebase for hardcoded secrets:
```bash
# API keys, tokens, passwords
grep -rn "(?i)(api[_-]?key|secret|password|token|credential|auth)" --include="*.{ts,js,py,go,rs,java,env,yml,yaml,json}" .

# .env files committed to repo
find . -name ".env*" -not -path "*/node_modules/*" -not -path "*/.git/*"

# Private keys
find . -name "*.pem" -o -name "*.key" -not -path "*/node_modules/*"
```

Check `.gitignore` for proper exclusion of sensitive files.

**Step 4 — API security review:**

For each API endpoint discovered:
- **Authentication:** Is the endpoint protected? What auth mechanism? Can it be bypassed?
- **Authorization:** Does it check the caller has permission for the specific resource?
- **Input validation:** Are all parameters validated for type, length, format, and range?
- **Rate limiting:** Is there protection against abuse and brute-force?
- **Output filtering:** Does the response include only necessary fields? No data leakage?
- **Error handling:** Do errors reveal internal details (stack traces, SQL errors, file paths)?

**Step 5 — Compile findings:**

Rate each finding using the severity standard:
- **CRITICAL** — Actively exploitable, data breach risk, requires immediate fix
- **HIGH** — Exploitable with moderate effort, significant impact, fix before next release
- **MEDIUM** — Requires specific conditions to exploit, fix in normal development cycle
- **LOW** — Minimal risk, best practice improvement, fix when convenient

**Output — Security Audit Report:**

```markdown
# Security Audit Report: [Project Name]

**Date:** [date]
**Scope:** [what was audited]
**Stack:** [technologies]

## Executive Summary
[2-3 sentences: overall security posture, critical findings count, recommendation]

## Findings

| # | Category | Severity | Description | File/Location | Remediation |
|---|---|---|---|---|---|
| 1 | [OWASP category] | CRITICAL | [description] | [file:line] | [specific fix] |

## Dependency Vulnerabilities
[Scanner output summary, CVEs found, upgrade recommendations]

## Secrets Scan Results
[Any hardcoded secrets found, recommended rotation and remediation]

## Recommendations (Prioritised)
1. [CRITICAL fixes — do immediately]
2. [HIGH fixes — do before next release]
3. [MEDIUM improvements — schedule in backlog]
4. [LOW improvements — address when convenient]

## Security Posture Score
[0-100 rating with justification]
```
