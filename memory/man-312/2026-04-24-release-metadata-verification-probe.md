# MAN-312 Release Metadata Verification Probe (2026-04-24 AEST)

## Scope
Validate that `POST /api/issues/:id/release` clears runtime execution metadata and ownership fields per [MAN-295](/MAN/issues/MAN-295).

## Runtime notes
- `mempalace_search` command is unavailable in this runtime (`command not found`).
- `mempalace_add_drawer` command is unavailable in this runtime (`command not found`).
- Used local memory fallback corpus under `~/dev/1_myprojects/gteam/memory`.

## Probe execution
- Created temporary child issue [MAN-313](/MAN/issues/MAN-313) under [MAN-312](/MAN/issues/MAN-312)
- Checked out [MAN-313](/MAN/issues/MAN-313) as run `9d663739-90ce-4a5c-a2a3-c6c677bb0dc2`
- Called release endpoint: `POST /api/issues/93603ca7-f2ca-4000-b89f-48cb14573e4a/release`
- Re-read state before and after release
- Cancelled probe artifact after verification

### Before release (MAN-313)
- `status=in_progress`
- `assigneeAgentId=d16f09d1-d7a1-4fa7-9b57-ceb0cac3693f`
- `checkoutRunId=9d663739-90ce-4a5c-a2a3-c6c677bb0dc2`
- `executionRunId=9d663739-90ce-4a5c-a2a3-c6c677bb0dc2`
- `executionAgentNameKey=null`
- `executionLockedAt=null`

### After release (MAN-313)
- `status=todo`
- `assigneeAgentId=null`
- `assigneeUserId=null`
- `checkoutRunId=null`
- `executionRunId=null`
- `executionAgentNameKey=null`
- `executionLockedAt=null`

## Conclusion
Release lifecycle behavior is correct for [MAN-295](/MAN/issues/MAN-295): release clears ownership and execution metadata and resets issue to `todo`.
