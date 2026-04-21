# Security Audit Report: Node.js Express Payment Processing API

**Date:** 2026-04-06
**Scope:** Full application security audit — payment processing, Stripe integration, transaction storage, admin refund endpoints
**Stack:** Node.js, Express, Stripe SDK, database (assumed relational), admin panel
**Audit type:** Architecture and design-level review (no codebase provided — findings based on described system)

---

## Executive Summary

A payment processing API is a **high-value target** — it handles credit card numbers, communicates with a financial API (Stripe), stores transaction records containing PII, and exposes privileged admin endpoints for refunds. The attack surface is wide: card data in transit, at rest, and in logs; the admin refund flow as a fraud vector; and the Stripe integration as a trust boundary. This audit identifies **28 findings** across all OWASP Top 10 categories, with **5 CRITICAL**, **8 HIGH**, **9 MEDIUM**, and **6 LOW** severity issues. The two most urgent concerns are: (1) whether raw card numbers touch the server at all (they should not — use Stripe Elements/Checkout), and (2) whether admin refund endpoints have sufficient authorization and audit controls.

---

## Findings

### CRITICAL Findings (Block Deployment)

| # | Category | Severity | Finding | Remediation |
|---|---|---|---|---|
| C1 | Cryptographic Failures | **CRITICAL** | **Raw credit card numbers reaching the server.** If the API accepts card numbers in request bodies (`POST /charge` with `card_number` field), the server is in PCI DSS scope. Any logging, error serialization, or database write of raw PANs is a compliance violation and breach risk. | **Never accept raw card numbers server-side.** Use Stripe Elements, Stripe Checkout, or Stripe.js to tokenize cards client-side. The server should only ever receive a Stripe `tok_*` or `pm_*` token. This removes the server from PCI DSS scope (SAQ A or SAQ A-EP). |
| C2 | Injection | **CRITICAL** | **SQL/NoSQL injection in transaction queries.** If transaction records are queried using string concatenation (e.g., `WHERE transaction_id = '${req.params.id}'`), an attacker can extract the entire transaction database including PII. | Use parameterized queries exclusively. For Knex: `.where('id', req.params.id)`. For Prisma/Sequelize: use the ORM's built-in parameterization. For raw queries: use `$1` placeholders. **Grep the codebase for string interpolation inside any SQL string.** |
| C3 | Broken Access Control | **CRITICAL** | **Admin refund endpoint without role verification.** If `/admin/refund` checks only that a user is authenticated (has a valid JWT/session) but not that they have the `admin` role, any authenticated user can issue refunds — a direct financial loss vector. | Implement RBAC middleware: `requireRole('admin')` on all `/admin/*` routes. Verify role claims server-side against the database, not from the JWT payload alone (JWTs can be forged if the signing key leaks). |
| C4 | Broken Access Control | **CRITICAL** | **IDOR on transaction lookup.** If `GET /transactions/:id` returns any transaction by ID without verifying the requesting user owns it, attackers can enumerate transaction records (sequential IDs make this trivial). | Verify ownership: `WHERE id = ? AND user_id = ?`. Use UUIDs (v4) instead of sequential integers for transaction IDs to prevent enumeration. |
| C5 | Cryptographic Failures | **CRITICAL** | **Stripe secret key exposure.** If `STRIPE_SECRET_KEY` is hardcoded in source code, committed to git, or logged in error output, an attacker gains full Stripe API access — can issue charges, refunds, and read all customer data. | Store in a secrets manager (AWS Secrets Manager, Vault, etc.). Never commit to git. Add `sk_live_*` and `sk_test_*` patterns to `.gitignore` and run `git log --all -p | grep sk_live` to check history. Rotate the key immediately if it has ever been committed. |

### HIGH Findings (Fix Before Next Release)

| # | Category | Severity | Finding | Remediation |
|---|---|---|---|---|
| H1 | Authentication Failures | **HIGH** | **Missing rate limiting on authentication endpoints.** Without rate limiting on `/login` and `/admin/login`, credential stuffing and brute-force attacks are trivial. Payment APIs are high-value targets for automated attacks. | Implement progressive rate limiting: max 5 failed attempts per account per 15 minutes, max 20 per IP per 15 minutes. Use `express-rate-limit` with a Redis-backed store (not in-memory, which resets on restart). Return `429 Too Many Requests` with `Retry-After` header. |
| H2 | Insecure Design | **HIGH** | **No idempotency on charge endpoints.** If `POST /charge` is not idempotent, network retries or double-clicks can result in duplicate charges — a financial and legal liability. | Require an `Idempotency-Key` header on all payment endpoints. Pass this to Stripe via `stripe.charges.create({...}, { idempotencyKey })`. Store processed keys in Redis with a 24h TTL to reject duplicates at the application level. |
| H3 | Insecure Design | **HIGH** | **No refund amount validation.** If the admin refund endpoint accepts an arbitrary amount without checking it against the original charge, an admin (or attacker with admin access) can issue refunds exceeding the original charge amount. | Validate: `refund_amount <= original_charge_amount - already_refunded_amount`. Pull the original charge from Stripe (`stripe.charges.retrieve()`) and compare server-side. Never trust the client-supplied amount alone. |
| H4 | Logging Failures | **HIGH** | **Sensitive data in logs.** Express request loggers (Morgan, Winston) will log full request bodies by default. If card numbers, CVVs, or Stripe tokens appear in logs, this is a PCI violation and data breach waiting to happen. | Implement a log sanitizer middleware that redacts: card numbers (mask all but last 4), CVVs (never log), Stripe keys, auth tokens, and PII fields. Example: `body.card_number = '****' + body.card_number.slice(-4)` before logging. Better yet — don't accept card numbers at all (see C1). |
| H5 | Security Misconfiguration | **HIGH** | **Verbose error responses in production.** Express's default error handler returns stack traces including file paths, dependency versions, and database connection strings. | Set `NODE_ENV=production`. Use a custom error handler that returns generic messages to clients: `{ error: "Internal server error", reference: "<uuid>" }`. Log the full error server-side with the reference UUID for debugging. Never expose `err.stack`, `err.message`, or SQL errors to clients. |
| H6 | Broken Access Control | **HIGH** | **Missing CSRF protection on refund endpoints.** If admin endpoints are accessed via a web dashboard (cookie-based auth), any site the admin visits can forge a refund request via the admin's browser session. | For cookie-based auth: implement CSRF tokens (use `csurf` middleware or the double-submit cookie pattern). For API-only (JWT in Authorization header): CSRF is not applicable, but verify the token is in the header, not a cookie. |
| H7 | Data Integrity Failures | **HIGH** | **Stripe webhook signature not verified.** If the `/webhooks/stripe` endpoint processes webhook events without verifying the `stripe-signature` header, an attacker can forge payment confirmations, trigger false refunds, or manipulate transaction state. | Always verify: `stripe.webhooks.constructEvent(body, sig, endpointSecret)`. Use the raw request body (not parsed JSON) for signature verification. Reject any event that fails verification with `400`. |
| H8 | Insecure Design | **HIGH** | **No separation of duties for high-value refunds.** A single admin issuing a $50,000 refund should require approval from a second admin. Without this, a compromised admin account enables unlimited financial fraud. | Implement approval thresholds: refunds above a configurable amount (e.g., $1,000) require a second admin's approval. Log the requesting admin, approving admin, and timestamps. |

### MEDIUM Findings (Schedule in Backlog)

| # | Category | Severity | Finding | Remediation |
|---|---|---|---|---|
| M1 | Security Misconfiguration | **MEDIUM** | **Missing security headers.** Without `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`, `Content-Security-Policy`, and `Referrer-Policy`, the API is vulnerable to downgrade attacks, clickjacking, and content sniffing. | Add `helmet` middleware: `app.use(helmet())`. Configure HSTS with `max-age=31536000; includeSubDomains; preload`. Set CSP to `default-src 'none'` for APIs. |
| M2 | Security Misconfiguration | **MEDIUM** | **CORS misconfiguration.** If `Access-Control-Allow-Origin: *` is set, any website can make authenticated requests to the API. For a payment API, this is an exploitation vector. | Whitelist specific origins: `cors({ origin: ['https://yourapp.com'] })`. Never use `*` with `credentials: true`. Audit the CORS config for `Access-Control-Allow-Credentials` set alongside a wildcard origin. |
| M3 | Vulnerable Components | **MEDIUM** | **Outdated dependencies with known CVEs.** Express, Stripe SDK, and database drivers all have historical CVEs. A payment API must be on the latest patch versions. | Run `npm audit` weekly. Pin exact versions in `package.json`. Set up Dependabot or Renovate for automated PRs. Prioritize: Stripe SDK (financial), Express (HTTP parsing), and any database driver. |
| M4 | Authentication Failures | **MEDIUM** | **JWT misconfiguration risks.** If using JWTs: accepting `alg: none`, using symmetric signing with a weak secret, not validating `exp`/`iss`/`aud`, or storing tokens in `localStorage` (XSS-accessible). | Use asymmetric signing (RS256 or EdDSA). Explicitly set `algorithms: ['RS256']` in verification to prevent `alg: none` attacks. Validate `exp`, `iss`, `aud` on every request. Store tokens in httpOnly, secure, sameSite cookies — not localStorage. Short-lived access tokens (15 min) with refresh token rotation. |
| M5 | Logging Failures | **MEDIUM** | **Insufficient audit trail for financial operations.** Every charge, refund, and admin action must be logged with: who, what, when, from where (IP), and the outcome. Without this, fraud investigation and compliance audits are impossible. | Create an immutable audit log table: `{ actor_id, action, resource_type, resource_id, ip_address, user_agent, request_id, old_value, new_value, timestamp }`. Write to this on every state-changing operation. Append-only — no UPDATE or DELETE on this table. Ship logs to a centralized, tamper-evident system (e.g., CloudWatch, Datadog, Splunk). |
| M6 | SSRF | **MEDIUM** | **Webhook URL configuration.** If the system allows configuring callback URLs (e.g., for payment notifications), an attacker could set a callback to `http://169.254.169.254/latest/meta-data/` to steal cloud instance credentials. | Validate and sanitize all webhook/callback URLs: resolve DNS, reject private IP ranges (10.x, 172.16-31.x, 192.168.x, 169.254.x, localhost, ::1). Use an allowlist of schemes (https only). |
| M7 | Insecure Design | **MEDIUM** | **No request size limits.** Without `express.json({ limit: '100kb' })`, an attacker can send multi-GB request bodies to exhaust memory and crash the server (DoS). | Set `app.use(express.json({ limit: '100kb' }))`. For file upload endpoints, use streaming with size limits. Apply at the reverse proxy level as well (nginx `client_max_body_size`). |
| M8 | Insecure Design | **MEDIUM** | **Missing timeout on Stripe API calls.** If a Stripe call hangs (network issue, Stripe outage), the Express request handler holds the connection indefinitely, exhausting the server's connection pool. | Set timeouts on the Stripe client: `new Stripe(key, { timeout: 30000 })`. Implement circuit breakers for Stripe calls. Return `503 Service Unavailable` if Stripe is down, with a `Retry-After` header. |
| M9 | Broken Access Control | **MEDIUM** | **Transaction listing without pagination limits.** If `GET /transactions` returns all transactions without server-enforced pagination, an attacker can dump the entire transaction table in one request. | Enforce server-side pagination: `max_per_page = 100`, default `per_page = 25`. Never allow the client to request unlimited results. Add cursor-based pagination for large datasets. |

### LOW Findings (Address When Convenient)

| # | Category | Severity | Finding | Remediation |
|---|---|---|---|---|
| L1 | Security Misconfiguration | **LOW** | **Express version fingerprinting.** The `X-Powered-By: Express` header reveals the framework, aiding targeted attacks. | `app.disable('x-powered-by')` or use `helmet()` which removes it automatically. |
| L2 | Security Misconfiguration | **LOW** | **Missing `__proto__` pollution protection.** Express's JSON parser can be vulnerable to prototype pollution via crafted payloads like `{"__proto__": {"isAdmin": true}}`. | Use a JSON parser that strips `__proto__` and `constructor.prototype` keys. Alternatively: `app.use(express.json({ reviver: (key, val) => key === '__proto__' ? undefined : val }))`. |
| L3 | Logging Failures | **LOW** | **No request correlation IDs.** Without a unique ID per request, tracing a single transaction across logs, Stripe calls, and database queries requires timestamp correlation — error-prone in high-throughput systems. | Generate a UUID per request in middleware: `req.id = crypto.randomUUID()`. Pass to Stripe as metadata, include in all log lines, and return in error responses as a reference. |
| L4 | Insecure Design | **LOW** | **No graceful shutdown handling.** If the server receives SIGTERM during an in-flight Stripe charge, the charge may succeed on Stripe's side but the local transaction record may not be written — leading to an orphaned charge. | Implement graceful shutdown: stop accepting new connections, wait for in-flight requests to complete (with a timeout), then exit. Use `server.close()` + drain timeout. |
| L5 | Security Misconfiguration | **LOW** | **Missing `Permissions-Policy` header.** Without it, embedded iframes could access camera, microphone, or geolocation — not relevant for an API, but matters if the admin dashboard is served from the same origin. | `app.use((req, res, next) => { res.setHeader('Permissions-Policy', 'camera=(), microphone=(), geolocation=()'); next(); })`. |
| L6 | Data Integrity Failures | **LOW** | **No integrity checks on npm packages.** If `package-lock.json` is not committed or `npm ci` is not used in CI, dependency resolution may differ between environments, potentially introducing untested or compromised packages. | Always commit `package-lock.json`. Use `npm ci` (not `npm install`) in CI/CD. Consider enabling npm's `--ignore-scripts` flag for untrusted packages and auditing post-install scripts. |

---

## Dependency Vulnerability Scan

**Action required:** Run the following against the actual codebase:

```bash
# Check for known CVEs in dependencies
npm audit --json

# Check for outdated packages
npm outdated

# Stripe SDK specifically — ensure v14+ for latest security fixes
npm ls stripe
```

**Key dependencies to verify:**
| Package | Concern | Minimum safe version |
|---|---|---|
| `express` | HTTP parsing vulnerabilities, prototype pollution | 4.21+ |
| `stripe` | Payment security, webhook verification | 14.0+ |
| `jsonwebtoken` | Algorithm confusion attacks | 9.0+ (uses `jose` internally) |
| `helmet` | Security header defaults | 7.0+ |
| `express-rate-limit` | Rate limiting bypass via proxy headers | 7.0+ |

---

## Secrets Scan Checklist

**Run against the actual codebase:**

```bash
# Stripe keys in source
grep -rn "sk_live_\|sk_test_\|rk_live_\|rk_test_\|whsec_" --include="*.{ts,js,json,env,yml}" .

# Generic secrets
grep -rn "password\s*=\|secret\s*=\|api_key\s*=" --include="*.{ts,js,json,yml}" .

# .env files committed
git ls-files | grep -i "\.env"

# Private keys
find . -name "*.pem" -o -name "*.key" | grep -v node_modules
```

**Verify `.gitignore` includes:**
```
.env
.env.*
*.pem
*.key
```

---

## PCI DSS Compliance Summary

This system handles payment card data and is therefore subject to PCI DSS. The compliance level depends on architecture decisions:

| Architecture | PCI Scope | Compliance Level |
|---|---|---|
| Raw card numbers hit the server | **Full PCI DSS** — 300+ controls, annual audit | SAQ D |
| Stripe.js tokenizes client-side, tokens hit server | **Reduced scope** — ~140 controls | SAQ A-EP |
| Stripe Checkout (hosted payment page) | **Minimal scope** — ~20 controls | SAQ A |

**Recommendation:** Use Stripe Checkout or Stripe Elements with client-side tokenization. This is the single highest-impact architectural decision for reducing security risk and compliance burden.

---

## Recommended Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Browser    │────▸│ Stripe.js /  │────▸│   Stripe    │
│  (Customer)  │     │  Elements    │     │   Servers   │
└─────────────┘     └──────┬───────┘     └──────┬──────┘
                           │ tok_xxx             │
                           ▼                     │
                    ┌──────────────┐              │
                    │  Your API    │◂─────────────┘
                    │  (Express)   │    webhook events
                    │              │    (signature verified)
                    │ • Receives   │
                    │   tokens     │
                    │   ONLY       │
                    │ • Never sees │
                    │   raw card # │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  Database    │
                    │ • tx records │
                    │ • NO card #s │
                    │ • Stripe IDs │
                    │   only       │
                    └──────────────┘
```

---

## Recommendations (Prioritised)

### 1. CRITICAL — Do Immediately
1. **Eliminate raw card numbers from the server** (C1). Use Stripe Elements/Checkout for client-side tokenization. This single change removes 60% of the risk surface.
2. **Verify Stripe webhook signatures** (H7). Without this, attackers can forge payment events.
3. **Parameterize all database queries** (C2). Grep for string interpolation in SQL.
4. **Implement RBAC on admin endpoints** (C3). Verify roles server-side, not from JWT claims alone.
5. **Rotate Stripe keys** (C5) if they have ever been in source code or logs.

### 2. HIGH — Fix Before Next Release
6. **Rate limit authentication endpoints** (H1) — 5 attempts / 15 min / account.
7. **Add idempotency keys to charge endpoints** (H2) to prevent duplicate charges.
8. **Validate refund amounts** (H3) against original charge.
9. **Sanitize all log output** (H4) — redact card numbers, tokens, PII.
10. **Suppress verbose errors in production** (H5) — generic messages to clients, full logs server-side.
11. **Add CSRF protection** (H6) if using cookie-based admin auth.
12. **Require dual approval for high-value refunds** (H8).

### 3. MEDIUM — Schedule in Sprint Backlog
13. Add security headers via `helmet` (M1).
14. Restrict CORS to specific origins (M2).
15. Run `npm audit` and update vulnerable dependencies (M3).
16. Harden JWT configuration (M4).
17. Build an immutable financial audit log (M5).
18. Validate webhook callback URLs against SSRF (M6).
19. Set request body size limits (M7).
20. Add Stripe API call timeouts and circuit breakers (M8).
21. Enforce server-side pagination (M9).

### 4. LOW — Address When Convenient
22. Remove `X-Powered-By` header (L1).
23. Add prototype pollution protection (L2).
24. Implement request correlation IDs (L3).
25. Add graceful shutdown (L4).
26. Set `Permissions-Policy` header (L5).
27. Commit lockfiles, use `npm ci` in CI (L6).

---

## Security Posture Score

**Score: 35 / 100** (estimated, pending codebase verification)

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| PCI Compliance | 25% | 2/10 | Assumed raw cards hit server — if using Stripe Elements, score jumps to 7/10 |
| Access Control | 20% | 3/10 | Admin endpoints described without RBAC or IDOR protection |
| Input Validation | 15% | 4/10 | No evidence of parameterized queries or validation |
| Cryptography | 15% | 5/10 | Stripe handles card encryption, but key management unknown |
| Logging & Monitoring | 10% | 3/10 | No audit trail described for financial operations |
| Configuration | 10% | 4/10 | Security headers, CORS, error handling undetermined |
| Dependency Security | 5% | 5/10 | Unknown — requires `npm audit` |

**Justification:** A payment processing API without confirmed PCI-compliant card handling, RBAC on admin endpoints, and webhook signature verification scores in the "needs significant work" range. The score can realistically reach 75-85/100 by addressing all CRITICAL and HIGH findings.

---

*Report generated by GTeam Security Engineer. Findings are based on the system as described — verify against the actual codebase and adjust severity ratings based on what the code review reveals.*
