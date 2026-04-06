# Security Review Checklist

Quick-reference checklist for reviewing any PR, system, or architecture for security issues. Check each item — mark PASS, FAIL, or N/A.

---

## Authentication & Authorization
- [ ] All endpoints require authentication (unless explicitly public)
- [ ] Authorization checked server-side on every request
- [ ] No IDOR — user-supplied IDs validated against caller's permissions
- [ ] Password hashing uses bcrypt/argon2/scrypt (not MD5/SHA1/SHA256)
- [ ] Session tokens regenerated on auth state change
- [ ] Rate limiting on login and password reset endpoints

## Input & Output
- [ ] All user input validated (type, length, range, format)
- [ ] Parameterized queries for all database access (no string concatenation)
- [ ] Output encoded for the correct context (HTML, JS, URL, CSS)
- [ ] File uploads validated by content type, size limited, stored outside webroot
- [ ] No user input passed to shell commands, eval, or template engines unsanitized

## Data Protection
- [ ] Sensitive data encrypted at rest (credentials, PII, financial data)
- [ ] TLS 1.2+ for all data in transit
- [ ] No secrets hardcoded in source code or config files
- [ ] PII minimized — only collecting what is needed
- [ ] Sensitive data not logged (passwords, tokens, credit cards)

## Security Headers & Configuration
- [ ] HTTPS enforced, HSTS enabled
- [ ] CSP headers configured
- [ ] CORS restricted to known origins
- [ ] X-Content-Type-Options: nosniff
- [ ] Debug/verbose errors disabled in production
- [ ] Default credentials changed or removed

## Dependencies & Supply Chain
- [ ] No known CVEs in dependencies (npm audit / pip-audit / cargo audit)
- [ ] Dependencies pinned to specific versions
- [ ] Lock files committed and reviewed
- [ ] Unused dependencies removed

## Logging & Monitoring
- [ ] Auth events logged (success and failure)
- [ ] Authorization failures logged
- [ ] No sensitive data in logs
- [ ] Alerting configured for suspicious patterns
