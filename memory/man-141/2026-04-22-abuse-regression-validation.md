Issue: MAN-141 Execute abuse-case validation and security regression checks
Date: 2026-04-22 (AEST)
Agent: GTeam Security Engineer (Codex)

Summary
- Completed abuse-case validation for MantleKit purchase recovery flow.
- Verified replay/session fixation boundary controls hold for `session_id + state + cookie` checks.
- Confirmed current in-memory rate limiter can be bypassed by rotating `x-forwarded-for` identifiers; mapped to existing hardening issue MAN-139.

Evidence highlights
- PASS: `GET /api/purchase/success-status` denies leaked `session_id+state` without cookie (`403 SESSION_ACCESS_DENIED`).
- PASS: `POST /api/purchase/resend-key` denies mismatched cookie/state (`403 SESSION_ACCESS_DENIED`).
- PASS: malformed input probes (`../../etc/passwd`, SQL-ish payload) return `400 INVALID_REQUEST`.
- PASS: same identifier rate-limited on 6th resend attempt (`429 RATE_LIMITED`).
- FAIL (known residual): rotating `x-forwarded-for` avoids limiter (`404 PURCHASE_NOT_FOUND` on all attempts, no 429).

Regression checks
- `npm audit --omit=dev --json`: critical=0, high=0, moderate=2 (`follow-redirects`, `hono`, fixes available).
- `npm audit --json`: same profile.
- Lint on purchase/rate-limit surfaces: pass.
- `npx tsc --noEmit --pretty false`: pre-existing unrelated TS error at `lib/admin/teams/context.ts(102,17)`.
- Sensitive files: `.env` untracked, `.env.example` tracked.

Risk mapping
- Rate-limit bypass residual maps to MAN-139 (existing high-priority hardening track).
