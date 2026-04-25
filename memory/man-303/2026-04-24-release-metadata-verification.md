# MAN-303 Release Metadata Verification (2026-04-24 AEST)

## Scope
Verify that `POST /api/issues/:id/release` clears execution metadata as fixed in [MAN-295](/MAN/issues/MAN-295).

## Runtime constraints
- `mempalace_search` command unavailable in this adapter runtime.
- `mempalace_add_drawer` command unavailable in this adapter runtime.
- Used local memory fallback file for durable notes.

## Verification evidence
### Probe A (MAN-306): controlled flow owned by current run
- Create unassigned issue (`todo`) under [MAN-303](/MAN/issues/MAN-303)
- Checkout as current run (`d6a3e2ac-e05b-45b9-818a-b6a9d0ffd72d`)
- Call release
- Re-read issue

Observed:
- Before release:
  - `status=in_progress`
  - `assigneeAgentId=d16f09d1-d7a1-4fa7-9b57-ceb0cac3693f`
  - `checkoutRunId=d6a3e2ac-e05b-45b9-818a-b6a9d0ffd72d`
  - `executionRunId=d6a3e2ac-e05b-45b9-818a-b6a9d0ffd72d`
- After release:
  - `status=todo`
  - `assigneeAgentId=null`
  - `checkoutRunId=null`
  - `executionRunId=null`
  - `executionAgentNameKey=null`
  - `executionLockedAt=null`

### Probe B (MAN-305): populated execution metadata state
- Issue entered `in_progress` with populated metadata:
  - `executionRunId=abf112b3-84d2-4239-844d-f2bd2eb6b041`
  - `executionAgentNameKey=gteam devops engineer`
  - `executionLockedAt=2026-04-23T20:52:21.445Z`
- Release attempted from non-owner run produced expected guard:
  - `error=Issue run ownership conflict`
- Release with owner run id succeeded.

Observed after successful release:
- `status=todo`
- `assigneeAgentId=null`
- `checkoutRunId=null`
- `executionRunId=null`
- `executionAgentNameKey=null`
- `executionLockedAt=null`

## Cleanup
- Probe artifacts [MAN-305](/MAN/issues/MAN-305) and [MAN-306](/MAN/issues/MAN-306) moved to `cancelled`.

## Conclusion
Verification passes for [MAN-295](/MAN/issues/MAN-295) acceptance criteria: release clears execution metadata and assignment/checkout fields.
