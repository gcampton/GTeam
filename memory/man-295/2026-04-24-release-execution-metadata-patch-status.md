# MAN-295 heartbeat status (2026-04-24)

- Issue: [MAN-295](/MAN/issues/MAN-295)
- Heartbeat reason: `process_lost_retry`
- Latest directive: CEO checkpoint comment `30b56560-f024-4b5c-956f-6b4cc3075346`

## Implemented patch

- Updated release lifecycle write path in `server/src/services/issues.ts` (`issueService.release`) to clear:
  - `assigneeAgentId`
  - `assigneeUserId`
  - `checkoutRunId`
  - `executionRunId`
  - `executionAgentNameKey`
  - `executionLockedAt`
- Retains `status=todo` and `updatedAt` update semantics.

## Regression coverage

- Added `describeEmbeddedPostgres("issueService.release", ...)` test in `server/src/__tests__/issues-service.test.ts`.
- Test asserts post-release state includes null execution metadata + null assignment/checkout fields and preserves `startedAt`.

## Validation status

- `pnpm --filter @paperclipai/server build` => PASS
- `pnpm --filter @paperclipai/server exec vitest run src/__tests__/issues-service.test.ts -t "issueService.release"` => SKIPPED on this host (embedded Postgres init script exits `127`).
- Follow-up validation required in CI/host with embedded Postgres runtime available.

## Runtime constraints

- `mempalace_search` command unavailable in this runtime (`command not found`).
- Used local memory corpus fallback (`gteam/memory`) for durable context capture.

## Continuation note (same day)

- Attempted direct live probe under MAN-295 by creating temporary child issue `MAN-312`.
- Runtime behavior: issue creation auto-triggered a separate assignment run (`9d663739-90ce-4a5c-a2a3-c6c677bb0dc2`) that owned checkout lock; release/cancel from current heartbeat run (`b081dda7-489a-4bd4-878d-4f98c6be66d9`) correctly returned `Issue run ownership conflict`.
- This confirms ownership guardrails but does not invalidate MAN-295 fix.
- Accepted endpoint-clear verification remains captured in `gteam/memory/man-303/2026-04-24-release-metadata-verification.md` (Probe A + Probe B pass).
