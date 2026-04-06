# OWASP Top 10 (2021) Reference

Quick-reference for the OWASP Top 10 web application security risks. Use Grep to find specific categories — do not load this entire file.

---

## A01: Broken Access Control [TESTED]

**What:** Users can act outside their intended permissions — accessing other users' data, modifying access controls, or escalating privileges.

**Detect:** Search for missing authorization checks on endpoints, IDOR patterns (user-supplied IDs used directly in queries), missing function-level access control, CORS misconfiguration.

**Prevent:**
- Default deny — require explicit grants for every resource
- Server-side authorization checks on every request (never trust client-side)
- Use indirect object references (map user-facing IDs to internal IDs)
- Disable directory listing, remove metadata files from webroot
- Rate limit API access, log and alert on access control failures

**Severity:** CRITICAL when exploitable, HIGH when potential

---

## A02: Cryptographic Failures [TESTED]

**What:** Sensitive data exposed due to weak or missing cryptography — plaintext storage, weak hashing, missing TLS, insecure random number generation.

**Detect:** Search for MD5/SHA1 password hashing, hardcoded encryption keys, HTTP (not HTTPS) endpoints, `Math.random()` for security purposes, missing encryption at rest.

**Prevent:**
- Use bcrypt/argon2/scrypt for password hashing (never MD5/SHA1/SHA256)
- TLS 1.2+ for all data in transit, TLS 1.3 preferred
- AES-256-GCM or ChaCha20-Poly1305 for encryption at rest
- Use cryptographically secure random: `crypto.randomBytes()`, `secrets.token_hex()`, `OsRng`
- Key management via KMS — never store keys in code or config files

**Severity:** CRITICAL for plaintext credentials, HIGH for weak crypto

---

## A03: Injection [TESTED]

**What:** Untrusted data sent to an interpreter as part of a command or query — SQL, NoSQL, OS command, LDAP, XPath, template, or prompt injection.

**Detect:** String concatenation in queries, unsanitized user input in shell commands, template rendering of user content, user input passed to LLM prompts without sanitization.

**Prevent:**
- Parameterized queries / prepared statements for all database access
- Input validation: allowlist expected formats, reject unexpected
- Output encoding: HTML-encode for DOM, URL-encode for URLs, JS-encode for scripts
- Use ORM methods that auto-parameterize (but verify — some ORMs have raw query escape hatches)
- For command execution: avoid entirely if possible, use allowlists if unavoidable

**Severity:** CRITICAL — injection is almost always directly exploitable

---

## A04: Insecure Design [TESTED]

**What:** Missing or ineffective security controls at the design level — not implementation bugs, but architectural flaws.

**Detect:** No rate limiting on authentication, no abuse case analysis, missing business logic validation, no separation of duties for critical operations.

**Prevent:**
- Threat model during design (use STRIDE — see tasks/threat-modeling.md)
- Define abuse cases alongside use cases
- Implement rate limiting on all authentication and expensive operations
- Use secure design patterns: least privilege, defense in depth, fail securely

**Severity:** HIGH — design flaws require architectural changes to fix

---

## A05: Security Misconfiguration [TESTED]

**What:** Insecure default settings, incomplete configuration, open cloud storage, verbose error messages, unnecessary features enabled.

**Detect:** Default credentials, debug mode in production, directory listing enabled, stack traces in error responses, unnecessary HTTP methods enabled, missing security headers.

**Prevent:**
- Hardened baseline configuration for all environments
- Remove default accounts, change default passwords
- Disable debug/verbose error modes in production
- Security headers: CSP, X-Content-Type-Options, X-Frame-Options, HSTS
- Regular configuration audits, automated config scanning

**Severity:** HIGH for default credentials/debug mode, MEDIUM for missing headers

---

## A06: Vulnerable and Outdated Components [TESTED]

**What:** Using components (libraries, frameworks, OS) with known vulnerabilities.

**Detect:** Run `npm audit`, `pip-audit`, `cargo audit`, `govulncheck`. Check dependency lock files against CVE databases. Look for pinned versions that are significantly outdated.

**Prevent:**
- Automated dependency scanning in CI/CD pipeline
- Subscribe to security advisories for key dependencies
- Regular update cycle — don't let dependencies age
- Remove unused dependencies
- Prefer dependencies with active maintenance and security track records

**Severity:** Depends on the CVE — can be CRITICAL to LOW

---

## A07: Identification and Authentication Failures [TESTED]

**What:** Weaknesses in authentication mechanisms — credential stuffing, brute force, weak passwords, session management flaws.

**Detect:** Missing rate limiting on login, no account lockout, weak password requirements, session tokens in URLs, missing session invalidation on logout/password change.

**Prevent:**
- Multi-factor authentication (TOTP or WebAuthn preferred)
- Password policy: 12+ chars, check against breach databases (Have I Been Pwned API)
- Progressive rate limiting on failed auth attempts
- Secure session management: regenerate session ID on auth state change
- Credential stuffing protection: CAPTCHA after failed attempts, IP-based throttling

**Severity:** HIGH — auth failures enable account takeover

---

## A08: Software and Data Integrity Failures [TESTED]

**What:** Code and infrastructure that does not protect against integrity violations — insecure deserialization, unsigned updates, compromised CI/CD pipelines.

**Detect:** Deserialization of untrusted data, unsigned software updates, CI/CD pipelines without integrity verification, auto-update without signature checks.

**Prevent:**
- Digital signatures on all software updates and deployments
- Verify integrity of dependencies (lock files, checksums, SRI for CDN resources)
- Secure CI/CD pipeline: protected branches, required reviews, signed commits
- Avoid native deserialization of untrusted data — use safe formats (JSON) with schema validation

**Severity:** HIGH for insecure deserialization, CRITICAL for CI/CD compromise

---

## A09: Security Logging and Monitoring Failures [TESTED]

**What:** Insufficient logging, detection, monitoring, and active response — attackers rely on lack of monitoring to achieve their goals undetected.

**Detect:** Missing audit logs for auth events, no alerting on suspicious patterns, sensitive data in log files, logs not centralized or protected.

**Prevent:**
- Log all authentication events (success and failure), authorization failures, input validation failures
- Structured logging with correlation IDs for request tracing
- Never log sensitive data: passwords, tokens, PII, credit card numbers
- Centralize logs, set retention policies, protect log integrity
- Alert on: multiple failed logins, privilege escalation attempts, unusual access patterns

**Severity:** MEDIUM — enables other attacks to succeed undetected

---

## A10: Server-Side Request Forgery (SSRF) [TESTED]

**What:** Application fetches a remote resource based on user-supplied URL without validation — can be used to access internal services, cloud metadata, or other systems.

**Detect:** Any endpoint that accepts a URL parameter and fetches it server-side. Look for webhook handlers, URL preview features, file import from URL, PDF generators that fetch remote content.

**Prevent:**
- Allowlist permitted URL schemes (https only), domains, and IP ranges
- Block access to internal IP ranges (10.x, 172.16-31.x, 192.168.x, 169.254.x, localhost)
- Block access to cloud metadata endpoints (169.254.169.254)
- Validate and sanitize all URL input — resolve DNS and check the IP before connecting
- Use network-level controls: egress filtering, separate network for URL fetching

**Severity:** HIGH — can lead to internal network access and data exfiltration
