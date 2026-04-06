# Secure Coding Patterns

Common security patterns for application development. Use Grep to find specific patterns — do not load this entire file.

---

## Input Validation [TESTED]

- Validate on the server, never trust client-side validation alone
- Use allowlists (accept known-good) over denylists (reject known-bad)
- Validate type, length, range, and format for every user-supplied value
- Reject unexpected input early — fail fast at the boundary
- Canonicalize before validation (decode URL encoding, normalize Unicode)

---

## Output Encoding [TESTED]

- HTML context: encode `<>&"'` to HTML entities before rendering in DOM
- JavaScript context: use `JSON.stringify()` or JS-specific encoding
- URL context: use `encodeURIComponent()` for query parameters
- CSS context: escape with CSS-specific encoding (avoid user input in CSS entirely if possible)
- Never mix contexts — encoding for HTML does not protect in JavaScript context

---

## Parameterized Queries [TESTED]

- Always use parameterized queries or prepared statements for database access
- Never concatenate user input into SQL strings, even with "escaping"
- ORM methods are generally safe, but watch for raw query escape hatches (`$queryRaw`, `execute()`)
- For dynamic column/table names: use allowlists, never interpolate user input
- Same principle applies to NoSQL: use query builders, not string concatenation

---

## CSRF Protection [TESTED]

- Use synchronizer token pattern: server generates token, client sends it with every state-changing request
- Double-submit cookie: token in both cookie and request body/header
- SameSite cookie attribute: set to `Lax` (default in modern browsers) or `Strict`
- Check `Origin` and `Referer` headers as defense-in-depth
- CSRF protection is required for any state-changing operation (POST, PUT, DELETE, PATCH)

---

## Content Security Policy (CSP) [TESTED]

Recommended starter policy:
```
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
```

- Avoid `unsafe-eval` — it enables XSS via `eval()`, `Function()`, `setTimeout(string)`
- Avoid `unsafe-inline` for scripts — use nonces or hashes instead
- `frame-ancestors 'none'` prevents clickjacking (replaces X-Frame-Options)
- Use `report-uri` or `report-to` to collect violation reports before enforcing

---

## CORS Configuration [TESTED]

- Never use `Access-Control-Allow-Origin: *` in production with credentials
- Allowlist specific origins — validate against a list, do not reflect the `Origin` header
- Set `Access-Control-Allow-Credentials: true` only when necessary
- Restrict `Access-Control-Allow-Methods` to required HTTP methods only
- Set `Access-Control-Max-Age` to cache preflight results (reduce OPTIONS requests)

---

## Rate Limiting [TESTED]

- Apply to authentication endpoints: 5-10 attempts per minute per IP/account
- Apply to expensive operations: API calls, file uploads, search, report generation
- Use sliding window or token bucket algorithm (not fixed window — avoids burst at boundary)
- Return `429 Too Many Requests` with `Retry-After` header
- Rate limit by multiple dimensions: IP, user account, API key (defense against distributed attacks)

---

## Secure Session Management [TESTED]

- Generate session IDs with cryptographic randomness (minimum 128 bits of entropy)
- Set cookie flags: `HttpOnly` (no JavaScript access), `Secure` (HTTPS only), `SameSite=Lax`
- Regenerate session ID on authentication state change (login, privilege escalation, password change)
- Set reasonable session timeouts: idle timeout (15-30 min for sensitive apps) and absolute timeout (8-24 hours)
- Invalidate sessions server-side on logout — don't just delete the cookie
- Store minimal data in sessions — prefer server-side session storage over large cookies

---

## Secure File Upload [TESTED]

- Validate file type by content (magic bytes), not just extension or MIME type
- Set maximum file size limits at both application and web server level
- Store uploaded files outside the webroot — serve through a controller with auth checks
- Rename files on upload — never use the user-supplied filename for storage
- Scan for malware if accepting files from untrusted users
- Set `Content-Disposition: attachment` for downloads to prevent browser rendering

---

## Secrets Management [TESTED]

- Never hardcode secrets in source code, config files, or environment files committed to git
- Use a secrets manager: AWS Secrets Manager, GCP Secret Manager, HashiCorp Vault, 1Password Connect
- Rotate secrets regularly and automatically where possible
- Use short-lived credentials (temporary tokens, STS assume-role) over long-lived API keys
- Audit secret access — log who accessed which secret and when
