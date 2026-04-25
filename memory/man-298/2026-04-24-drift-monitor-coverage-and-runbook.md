# MAN-298 Drift Monitor Coverage + Runbook (2026-04-24 AEST)

## Scope handled this heartbeat
- Continued scoped wake for [MAN-298](/MAN/issues/MAN-298) (`process_lost_retry`) with no pending comments in wake payload.
- Used local memory fallback because `mempalace_search` / `mempalace_add_drawer` commands are unavailable in this runtime.

## Codebase actions
Repository: `/home/garratt/dev/4_repos/paperclip`

1. Added drift monitor regression coverage in `server/src/__tests__/issues-service.test.ts`:
- Asserted release lifecycle path leaves drift count at `0` before and after release for an `in_progress` issue with execution metadata.
- Added dedicated drift-query test validating:
  - only `status != in_progress` rows are counted
  - hidden issues are excluded
  - rows with any populated execution metadata field are included
  - listing honors limit/order and excludes non-drift rows

2. Added dashboard signal coverage in `server/src/__tests__/dashboard-service.test.ts`:
- Added assertions for zero-drift baseline in existing summary test.
- Added dedicated test verifying `executionMetadataDrift` includes:
  - incident count
  - sampled issue IDs
  - incident-ready normalization message
  - runbook path (`doc/execution-semantics.md#52-drift-monitoring-and-normalization-runbook`)
  - lifecycle fix linkage to issue `-295`

3. Added runbook section in `doc/execution-semantics.md`:
- `5.2 Drift Monitoring and Normalization Runbook`
- Includes immediate normalization steps (`POST /api/issues/:issueId/release`, verify nulls, re-checkout if needed)
- Explicitly references [MAN-295](/MAN/issues/MAN-295)

## Validation
- `pnpm --filter @paperclipai/server exec vitest run src/__tests__/issues-service.test.ts src/__tests__/dashboard-service.test.ts`
  - Embedded Postgres suites skipped on this host (`init script exited 127`), but command completed successfully.
- `pnpm --filter @paperclipai/server build`
  - PASS

## Notes
- The runtime already contains in-flight source changes for monitor/query wiring in `issueService` and `dashboardService`; this heartbeat added missing regression coverage and runbook hardening around that behavior.
