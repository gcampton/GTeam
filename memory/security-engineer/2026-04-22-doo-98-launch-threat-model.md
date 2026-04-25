# DOO-98 Launch threat model + hardening (2026-04-22)

Issue links:
- [DOO-98](/DOO/issues/DOO-98)
- [DOO-94](/DOO/issues/DOO-94)

Delivered:
- Full STRIDE threat model with trust boundaries and ranked severity table.
- Launch-blocking mitigations and owners.
- CTO validation checklist.
- Incident runbook for lost device, local exfiltration, credential compromise.

Top launch blockers:
1. API authN/authZ missing on sensitive endpoints.
2. Key custody relies on plaintext file/env fallback (`keycodes-secret` / `DOOR13_KEYCODES_SECRET`).
3. Upload paths lack malware scanning + strict content validation + robust canonical path checks.
4. Authority proof payloads are stored plaintext in SQLite.
5. Future sync path needs signed, tenant-scoped protocol with replay protection.

Primary code evidence:
- `src/pages/api/**`
- `src/lib/key-codes-crypto.ts`
- `src/pages/api/jobs/[id]/attachments.ts`
- `src/pages/api/jobs/[id]/attachments/[attachmentId].ts`
- `src/pages/api/key-systems/[id]/authority-proofs.ts`
- `src/db/migrations/0030_sync_phase0_foundation.sql`

Notes:
- `mempalace_add_drawer` was not available as a direct runtime command; used file-based durable note + `mempalace mine` fallback.
