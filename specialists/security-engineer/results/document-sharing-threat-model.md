# Threat Model: Document Sharing Web Application

**Date:** 2026-04-15
**Modeled by:** Security Engineer (GTeam)
**Version:** 1.0

---

## Scope

**In scope:**
- Document upload, storage, and download flows
- JWT-based authentication and session management
- Share-link generation and access
- S3 file storage and access controls
- PostgreSQL schema and query patterns
- API surface and transport layer

**Out of scope:**
- Infrastructure provisioning / AWS account security posture
- CI/CD pipeline security
- Third-party identity providers (SSO/OAuth) unless integrated with the JWT flow
- Client-side application code (assumed to be a standard browser-based SPA)

---

## Assets

| # | Asset | Sensitivity | Notes |
|---|---|---|---|
| A1 | User document contents | RESTRICTED | Could contain PII, trade secrets, legal docs |
| A2 | User credentials (passwords, sessions) | RESTRICTED | Account takeover vector |
| A3 | JWT signing secret | RESTRICTED | Compromise allows forging any user identity |
| A4 | AWS IAM credentials / S3 access keys | RESTRICTED | Full S3 read/write/delete if leaked |
| A5 | PostgreSQL connection string | RESTRICTED | Full database read/write access |
| A6 | File metadata (names, sizes, owners) | CONFIDENTIAL | Reveals user activity patterns |
| A7 | Share link tokens | CONFIDENTIAL | Grants document access without authentication |
| A8 | Audit / access logs | INTERNAL | Required for incident response |
| A9 | Application source code | INTERNAL | Exposes logic and potential vulnerabilities |

---

## Trust Boundaries

```
┌─────────────────────────────────────────────────────────────────┐
│  PUBLIC INTERNET                                                │
│                                                                 │
│   [Browser / API Client]   [Share Link Consumer (anonymous)]   │
└────────────────┬──────────────────────┬────────────────────────┘
                 │  HTTPS (TLS)         │  HTTPS (TLS)
    ═════════════╪══════════════════════╪══════════ BOUNDARY 1 (Client ↔ API)
                 │                      │
┌────────────────▼──────────────────────▼────────────────────────┐
│  APPLICATION TIER                                               │
│                                                                 │
│   [API Server]  ── JWT validation ── [Auth Middleware]          │
│       │                    │                                    │
└───────┼────────────────────┼────────────────────────────────────┘
        │                    │
   ═════╪════════════════════╪══════════ BOUNDARY 2 (API ↔ Storage)
        │                    │
   ┌────▼────┐          ┌────▼──────┐
   │   S3    │          │ PostgreSQL │
   │ Bucket  │          │ Database  │
   └─────────┘          └───────────┘
        │
   ═════╪═════════════════════════════ BOUNDARY 3 (S3 ↔ Internet — only if bucket misconfigured)
        │
   [Direct S3 URL consumer]
```

**Boundary 1 — Client ↔ API:** All user-initiated requests. JWT is the trust token. Highest-risk boundary — all unauthenticated and externally controllable input enters here, including share-link consumers who present no credentials.

**Boundary 2 — API ↔ Storage:** IAM role (S3) and connection string (PostgreSQL) are the trust tokens. Compromise of the application tier grants full access to both storage backends.

**Boundary 3 — S3 ↔ Internet:** Only exists if the bucket has a public ACL or misconfigured bucket policy. Every file should be reachable only through the API or short-lived pre-signed URLs — never via a permanent public object URL.

**Internal boundary — Authenticated user ↔ Other users' data:** S3 and PostgreSQL store all users' data in a shared namespace; the only separation is the application-layer authorization check. This is the most commonly exploited internal boundary (IDOR).

---

## Threat Analysis

| ID | Component | STRIDE | Threat | Likelihood | Impact | Severity | Mitigation | Owner |
|---|---|---|---|---|---|---|---|---|
| T01 | JWT Auth | Spoofing | **Algorithm confusion attack** — attacker sends JWT with `alg: none` or downgrades RS256 to HS256 using the public key as HMAC secret, forging any user identity | High | High | **CRITICAL** | Pin accepted algorithm in JWT validation config (e.g., `algorithms: ['RS256']`). Never allow `none`. Use a well-maintained JWT library with strict algorithm enforcement. Test by sending a `none`-signed token — must return `401`. | Backend team |
| T02 | JWT Auth | Spoofing | **JWT secret brute force** — weak or default signing secret cracked offline after an attacker intercepts a valid token | Medium | High | **HIGH** | Enforce minimum 256-bit random secret via CSPRNG. Store in secrets manager (AWS Secrets Manager / Vault). Rotate quarterly. | Backend team |
| T03 | JWT Auth | Tampering | **JWT claims manipulation** — attacker modifies `userId`, `role`, or `email` claims if signature validation is missing or bypassed in any code path | Medium | High | **HIGH** | Validate signature on every request before trusting any claim. Re-fetch user role from DB on privilege-sensitive operations — do not rely solely on the JWT `role` claim. | Backend team |
| T04 | JWT Auth | Information Disclosure | **JWT leaked in server logs or browser history** — token passed as a URL query parameter (`?token=...`) instead of the `Authorization` header | High | Medium | **HIGH** | Always transmit JWT in `Authorization: Bearer` header. Scrub tokens from access logs. Set `Cache-Control: no-store` on auth responses. | Backend team |
| T05 | JWT Auth | Denial of Service | **No JWT revocation mechanism** — stolen token remains valid until natural expiry; no way to invalidate a compromised session | Medium | Medium | **MEDIUM** | Implement token blocklist (Redis) for logout and forced revocation. Keep access token expiry short (15–60 min) with refresh token rotation. On password change or account lock, purge all active tokens. | Backend team |
| T06 | JWT Auth | Elevation of Privilege | **JWT `role` claim escalation** — user crafts a token claiming admin role if the role is embedded in the JWT and not re-verified against the DB | Medium | High | **HIGH** | Never grant elevated access based solely on a JWT claim. Verify role against the database on every privileged operation. | Backend team |
| T07 | File Upload | Tampering | **Path traversal via filename** — attacker uploads a file named `../../etc/passwd` or `../app/config.js`, overwriting server or S3 objects at an attacker-chosen path | High | High | **CRITICAL** | Sanitize filenames server-side: strip all path components, normalize unicode, reject filenames containing `/`, `\`, `..`, or null bytes. Generate a random UUID as the S3 object key; store the original filename only in the database as display metadata. | Backend team |
| T08 | File Upload | Tampering | **Malicious file upload (web shell, malware, weaponized Office doc)** — attacker uploads a `.php` or `.exe` file; if served directly it may execute server-side or in the browser | High | High | **CRITICAL** | (1) Validate file type by magic bytes, not extension or `Content-Type` header. (2) Allowlist permitted MIME types (PDF, DOCX, XLSX, PNG, JPG, etc.). (3) Serve all downloads through the API with `Content-Disposition: attachment` to prevent browser execution. (4) Integrate async malware scanning (ClamAV or cloud AV service) before marking upload as available. Never serve unscanned files. | Backend team + DevOps |
| T09 | File Upload | Information Disclosure | **XXE injection via uploaded XML/SVG/DOCX** — if the application parses uploaded document content server-side, an XXE payload can read local files (`/etc/passwd`) or trigger SSRF | Medium | High | **HIGH** | Disable external entity processing in all XML parsers (`FEATURE_SECURE_PROCESSING`, `resolve_entities=False`). Do not parse document contents server-side unless required. If parsing is required, use a sandboxed, network-isolated environment. | Backend team |
| T10 | File Upload | Tampering | **Polyglot / MIME confusion — SVG XSS** — SVG file with embedded `<script>` served inline causes stored XSS in the browser | Medium | Medium | **MEDIUM** | Never serve files with `Content-Disposition: inline` for SVG, HTML, or XML types. Force `attachment` on all downloads. Set `X-Content-Type-Options: nosniff`. | Backend team |
| T11 | File Upload | Denial of Service | **Missing upload size limit — storage exhaustion** — attacker uploads arbitrarily large files, exhausting S3 storage or blocking API worker threads | High | High | **CRITICAL** | Enforce upload size limit at the web server layer (e.g., Nginx `client_max_body_size`) and validate again at the API layer before writing to S3. Impose per-user storage quota enforced in the DB. | Backend team + DevOps |
| T12 | File Upload | Denial of Service | **Zip bomb / decompression bomb** — small compressed file expands to gigabytes in memory if the app extracts archives without safeguards | Medium | High | **HIGH** | Do not extract archives without size limits. Set a maximum decompressed-size threshold and abort extraction if exceeded. Prefer streaming over full in-memory decompression. | Backend team |
| T13 | Share Links | Elevation of Privilege | **IDOR on file access — no authorization check** — authenticated user accesses another user's file by substituting the file ID in a request (`GET /files/42` → `GET /files/43`) | High | High | **CRITICAL** | Every file access must verify the requesting user either owns the file or holds a valid share grant. Required query pattern: `WHERE id = $1 AND (owner_id = $2 OR EXISTS (valid share grant for token))`. Write a failing integration test — user A must receive `403` on user B's file ID — before merging. | Backend team |
| T14 | Share Links | Information Disclosure | **Share token enumeration** — predictable or sequential share tokens allow an attacker to enumerate all shared documents | Medium | High | **HIGH** | Generate share tokens with `crypto.randomBytes(32)` (256 bits of entropy). Store only the SHA-256 hash of the token in the DB; compare hash on access. Tokens must never be sequential, time-based, or derived from file IDs. | Backend team |
| T15 | Share Links | Information Disclosure | **Share link with excessive or unlimited expiry** — link shared for a meeting remains valid indefinitely, enabling future unauthorized access after the intended use | High | Medium | **HIGH** | Set a default maximum expiry (7 days). Allow users to set shorter expiry but not longer. Provide a "revoke link" action. Run a scheduled job to purge expired tokens. | Backend team |
| T16 | Share Links | Repudiation | **No audit trail for share link access** — impossible to determine who accessed a document via share link after a data breach | High | Low | **MEDIUM** | Log every share link access: token ID (not raw token), timestamp, IP, User-Agent, file ID, result (success/denied). Retain logs for 90+ days in a tamper-resistant sink. | Backend team |
| T17 | S3 Storage | Information Disclosure | **Misconfigured S3 bucket — public-read ACL** — all uploaded documents accessible to the internet without authentication by guessing or enumerating S3 object keys | Medium | High | **CRITICAL** | Set bucket ACL to `private`. Enable S3 Block Public Access at the account level. Verify automatically in CI: `aws s3api get-bucket-acl --bucket <name>` must return no public grants. Never use permanent public object URLs for user documents. | DevOps |
| T18 | S3 Storage | Information Disclosure | **Pre-signed URL with excessive lifetime** — S3 pre-signed URL generated for a download is valid for hours or days; forwarding it grants anyone access | High | Medium | **HIGH** | Set pre-signed URL expiry to the minimum required (5–15 minutes). Do not store or log pre-signed URLs. Regenerate on each authenticated download request. | Backend team |
| T19 | S3 Storage | Information Disclosure | **Pre-signed URL leakage in server access logs** — ALB, CloudFront, or application middleware logs the full pre-signed URL including `X-Amz-Signature` query parameters | Medium | High | **HIGH** | Configure log scrubbing to redact query string parameters on S3 requests. For high-sensitivity documents, proxy the download through the API (stream from S3) rather than redirecting the client to a pre-signed URL. | DevOps |
| T20 | S3 Storage | Elevation of Privilege | **Overly permissive IAM role** — application IAM role grants `s3:*` or includes `s3:DeleteBucket` / `s3:PutBucketPolicy`; exploiting the app grants full S3 control | Medium | High | **HIGH** | Apply least-privilege IAM policy: allow only `s3:GetObject` and `s3:PutObject` on the specific bucket and key prefix. Deny `s3:DeleteBucket`, `s3:PutBucketPolicy`, `s3:PutBucketAcl`. Use separate roles for application vs. admin operations. | DevOps |
| T21 | S3 Storage | Tampering | **Missing S3 server-side encryption at rest** — unencrypted objects expose data if the AWS account or underlying storage is compromised | Low | High | **MEDIUM** | Enable S3 SSE-KMS with a customer-managed CMK. Enforce via bucket policy (`Deny PutObject` without `x-amz-server-side-encryption` header). Enable S3 versioning to recover from accidental or malicious deletion. | DevOps |
| T22 | PostgreSQL | Tampering | **SQL injection in file search or filter parameters** — unparameterized queries in file listing or search endpoints allow DB manipulation or cross-user data exfiltration | Medium | High | **HIGH** | Use parameterized queries or an ORM with strict escaping on every query. Never interpolate user input into SQL strings. Enable query logging in dev/staging to catch raw string concatenation during code review. | Backend team |
| T23 | PostgreSQL | Elevation of Privilege | **Horizontal privilege escalation via DB queries** — `SELECT * FROM files WHERE id = $input` without `AND owner_id = $currentUser` leaks records belonging to other users | High | High | **CRITICAL** | Always scope queries to the authenticated user: include `owner_id = $currentUserId` predicate on every user-scoped query. Add automated integration test: user A cannot read user B's records even with a valid file ID. | Backend team |
| T24 | PostgreSQL | Information Disclosure | **Database error messages exposed to client** — unhandled DB exceptions return raw PostgreSQL error strings that reveal table names, column names, or query fragments | High | Medium | **HIGH** | Catch all DB exceptions at the service layer. Return a generic error message and a correlation ID to the client. Log the full error server-side only. | Backend team |
| T25 | PostgreSQL | Denial of Service | **Unindexed or unbounded queries** — expensive full-table scans triggered via unindexed search fields degrade availability under normal load or targeted abuse | Medium | Medium | **MEDIUM** | Add indexes on `owner_id`, `share_token_hash`, and any searchable fields. Set `statement_timeout` in PostgreSQL. Paginate all list endpoints (cursor-based preferred). | Backend team |
| T26 | API / Transport | Tampering | **Missing TLS enforcement** — API accessible over plain HTTP; credentials and document content transmitted in cleartext, interceptable by a passive network attacker | Medium | High | **HIGH** | Enforce HTTPS: redirect all HTTP to HTTPS. Set `Strict-Transport-Security: max-age=31536000; includeSubDomains`. Configure TLS 1.2 minimum (TLS 1.3 preferred). Disable weak cipher suites. | DevOps |
| T27 | API / Transport | Denial of Service | **No rate limiting on upload/download endpoints** — automated requests exhaust bandwidth, S3 API budget, or trigger excessive DB writes | High | High | **CRITICAL** | Apply per-user rate limits: upload (e.g., 10 req/min), download (e.g., 50 req/min). Apply IP-based limits on unauthenticated share-link access endpoints. Use sliding window algorithm. Return `429 Too Many Requests` with `Retry-After` header. | Backend team + DevOps |
| T28 | API / Transport | Repudiation | **Insufficient audit logging** — no record of who uploaded, downloaded, shared, or deleted which document; post-breach investigation is impossible | High | Medium | **HIGH** | Log all security-relevant events: upload, download, share link create/access/revoke, delete, login success/failure, auth failure. Include: timestamp, user ID, resource ID, action, IP, User-Agent. Store in a tamper-resistant log sink with 90-day minimum retention. | Backend team + DevOps |
| T29 | API / Transport | Information Disclosure | **Verbose error responses with stack traces** — unhandled exceptions return full stack traces revealing framework version, file paths, and internal logic | High | Medium | **HIGH** | Configure a production error handler that returns only a generic message and a correlation ID. Map all exceptions to appropriate HTTP status codes. Never serialize exception objects directly to API responses. | Backend team |
| T30 | API / Transport | Spoofing | **CSRF on file management actions** — if the API accepts cookies for auth (rather than `Authorization` header), forged cross-site requests can trigger delete or share actions | Low | Medium | **LOW** | If using cookie-based auth: set `SameSite=Lax` (or `Strict`) and enforce CSRF tokens. If using `Authorization: Bearer` header only, CSRF is not applicable — browsers will not auto-send the header cross-origin. Prefer header-based auth to eliminate this attack surface entirely. | Backend team |

---

## Accepted Risks

| ID | Risk | Justification | Review Date |
|---|---|---|---|
| T21 | S3 SSE-KMS not yet enabled | Defense-in-depth control; primary data protection is private bucket ACL + IAM. Low standalone likelihood. Scheduled for infrastructure sprint. | 2026-07-15 |
| T25 | Unindexed DB queries | Operational/performance risk rather than a direct security breach in isolation. Scheduled for DB hardening sprint with load testing. | 2026-07-15 |
| T30 | CSRF | Only applicable if cookie auth is used. If JWT in `Authorization` header is confirmed as the sole auth mechanism, this threat is neutralized by browser same-origin policy. | 2026-07-15 |

---

## Recommendations

### Deployment blockers — CRITICAL (must fix before launch)

1. **T01** — Pin JWT algorithm; test with `alg: none` token — must return `401`.
2. **T07** — Sanitize filenames; use UUID as S3 key. Original filename is DB metadata only.
3. **T08** — Validate file type by magic bytes; async malware scan before serving any file.
4. **T11** — Upload size limits at web server + API layer; per-user quota in DB.
5. **T13** — Authorization check on every file access. Failing integration test (user A → user B file = `403`) required before merge.
6. **T17** — S3 bucket private; Block Public Access enabled. Verified in CI.
7. **T23** — Scope all DB queries with `owner_id = $currentUserId`. Code review every `SELECT`/`UPDATE`/`DELETE` on user-owned resources.
8. **T27** — Rate limiting on upload/download and share-link endpoints deployed before go-live.

### High priority (first sprint post-launch)

9. **T02** — Rotate JWT secret; enforce 256-bit CSPRNG minimum; store in secrets manager.
10. **T03 / T06** — Re-fetch role from DB on every privileged operation.
11. **T04** — Confirm JWT is never sent as URL param; audit access log format to scrub tokens.
12. **T09** — Disable XML external entities in all document parsers.
13. **T14** — 256-bit random share tokens; store SHA-256 hash in DB only.
14. **T15** — Share link expiry enforced; "revoke" action available; expiry cleanup job scheduled.
15. **T18** — Pre-signed URL expiry ≤ 15 minutes; regenerated per authenticated request.
16. **T19** — Pre-signed URLs scrubbed from logs; proxy streaming for high-sensitivity documents.
17. **T20** — IAM policy audited; wildcards removed; least-privilege enforced.
18. **T22** — All queries parameterized; ORM audit complete.
19. **T24** — Generic error messages with correlation IDs returned to client; full errors logged server-side.
20. **T26** — HTTPS enforced; HSTS header deployed.
21. **T28** — Structured audit log shipped to tamper-resistant sink.
22. **T29** — Production error handler configured; stack traces never serialized to API responses.

### Medium priority (security hardening sprint)

23. **T05** — JWT blocklist (Redis) for logout and forced session revocation.
24. **T10** — `Content-Disposition: attachment` enforced on all file downloads.
25. **T12** — Decompressed-size safeguard if archive extraction is supported.
26. **T16** — Share link access events logged (token ID, not raw token value).
27. **T21** — S3 SSE-KMS enabled; bucket policy enforces encryption header.
28. **T25** — DB indexes on `owner_id`, `share_token_hash`; `statement_timeout` set; lists paginated.
