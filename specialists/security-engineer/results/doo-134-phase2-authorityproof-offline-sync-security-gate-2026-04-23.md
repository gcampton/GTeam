# DOO-134 Security Gate: Phase-2 AuthorityProof + Offline Sync Controls

**Date:** 2026-04-23  
**Reviewer:** Security Engineer (GTeam)  
**Scope:** AuthorityProof storage/verification, mobile offline lifecycle/locks, sync outbox replay/idempotency, override-control coverage, event/audit integrity.

## Gate Decision

**FAIL (release-blocking)**  
QA in [DOO-123](/DOO/issues/DOO-123) should **not** proceed until HIGH findings are remediated and re-validated.

## Evidence Snapshot

- Targeted tests run:
  - `npm test -- src/db/sync.test.ts src/core/mobile-field/workflow.test.ts`
  - Result: 12/12 passing (functional baseline only; does not cover abuse paths identified below).
- Reviewed implementation paths:
  - `src/pages/api/key-systems/[id]/authority-proofs.ts`
  - `src/pages/api/authority-proofs/[id].ts`
  - `src/pages/api/mobile/assignment-locks/index.ts`
  - `src/pages/api/mobile/jobs/[id]/lifecycle.ts`
  - `src/pages/api/mobile/sync/outbox.ts`
  - `src/db/migrations/0022_phase3_compatibility_authority_proofs.sql`
  - `src/core/mobile-field/workflow.ts`

## Findings (Severity Ordered)

### 1) AuthorityProof self-verification and verifier identity forgery
**Severity:** HIGH  
**Evidence:**
- `POST /api/key-systems/[id]/authority-proofs` accepts caller-provided `state`, including `VERIFIED` (`src/pages/api/key-systems/[id]/authority-proofs.ts:69`).
- Same route allows `operator` role to create proofs (`src/pages/api/key-systems/[id]/authority-proofs.ts:56`).
- Caller-provided `verified_by_user_id` is persisted directly (`src/pages/api/key-systems/[id]/authority-proofs.ts:83`, `src/pages/api/authority-proofs/[id].ts:47-49`).
- Lifecycle and issuance paths trust only `proof.state === VERIFIED` (`src/pages/api/mobile/jobs/[id]/lifecycle.ts:189-193`, `src/pages/api/key-transactions/index.ts:218`).

**Impact:** A non-approver can mint or patch a proof to VERIFIED and bypass authority gate policy with forged approval identity.

**Required fix:**
- Forbid `VERIFIED` on create.
- Restrict verify transition to explicit approver roles only.
- Derive verifier identity from authenticated principal, not request body.
- Enforce state machine (`DRAFT -> SUBMITTED -> VERIFIED/REJECTED/REVOKED`) server-side.

### 2) AuthorityProof sensitive payload is plaintext at rest and in API responses
**Severity:** HIGH  
**Evidence:**
- Schema stores `payload_json TEXT NOT NULL` without envelope/signature fields (`src/db/migrations/0022_phase3_compatibility_authority_proofs.sql:32-44`).
- List and detail endpoints return full payload JSON (`src/pages/api/key-systems/[id]/authority-proofs.ts:44-52`, `src/pages/api/authority-proofs/[id].ts:30-35`, `:64-70`).

**Impact:** Full proof material exposure (PII/evidence) to any permitted API reader; local DB exfiltration directly reveals proof contents.

**Required fix:**
- Store encrypted envelope (ciphertext + key id + nonce/tag) and integrity metadata.
- Return only preview/safe metadata by default; gated decrypt endpoint for approved roles.
- Add access logging for decrypt operations.

### 3) Assignment lock bearer token leakage and audit provenance spoofing
**Severity:** HIGH  
**Evidence:**
- Lock token is written to mobile event payload and audit metadata (`src/pages/api/mobile/assignment-locks/index.ts:297`, `:312`, `:365`).
- Lifecycle transition payload also records `assignment_lock_token` (`src/pages/api/mobile/jobs/[id]/lifecycle.ts:225`).
- Client can override `actor_subject`/`actor_role` in lock and lifecycle APIs (`src/pages/api/mobile/assignment-locks/index.ts:43-44`, `:265-266`, `:345-346`; `src/pages/api/mobile/jobs/[id]/lifecycle.ts:141-142`).

**Impact:** Anyone with log/event read access can replay bearer tokens; audit trail can be falsified by caller-supplied actor fields.

**Required fix:**
- Never persist raw lock tokens in event/audit payloads (store one-way hash/reference only).
- Ignore caller actor fields; always bind actor identity/role from authenticated principal/session.
- Bind lock ownership checks to actor/device when consuming lock tokens.

### 4) Supervisor override separation-of-duties controls are absent from phase-2 state machine
**Severity:** HIGH  
**Evidence:**
- Mobile lifecycle model has no override-specific states/events (`src/core/mobile-field/workflow.ts:3-29`).
- No `override.approved` audit event implementation surfaced in API/state paths under `src/pages/api/mobile` and key issuance APIs.

**Impact:** Contracted control (“scoped override with self-approval blocked and distinct audit naming both actors”) is not enforceable.

**Required fix:**
- Implement explicit override request/approval workflow with dual-actor checks.
- Hard-block self-approval server-side.
- Emit immutable `override.approved` events with both requester and approver identities.

### 5) Replay/idempotency hardening is incomplete for mobile lifecycle and sync operations
**Severity:** MEDIUM  
**Evidence:**
- Lifecycle accepts same-state transitions (`currentState === nextState`) and still appends events/audit entries (`src/core/mobile-field/workflow.ts:59`, `src/pages/api/mobile/jobs/[id]/lifecycle.ts:215-244`).
- No idempotency key/request nonce enforcement in lifecycle or lock endpoints.
- Sync outbox control API allows broad `ack`/`fail` by op IDs with optional lease binding (`src/pages/api/mobile/sync/outbox.ts:94-117`).

**Impact:** Duplicate/replayed requests can create duplicate state events, noisy/confusing audit chains, and weak worker isolation.

**Required fix:**
- Require idempotency key per mutating mobile request and dedupe server-side.
- Reject replayed lifecycle transitions within bounded window unless explicitly marked retry-safe.
- Require lease ownership on all `ack`/`fail` operations and enforce actor/device binding.

## Deterministic Acceptance Checks (Post-Fix)

1. **AuthorityProof verify gate (negative):** Operator attempts to create/patch proof as VERIFIED -> expect `403`.
2. **Verifier identity binding (negative):** Caller supplies mismatched `verified_by_user_id` -> persisted verifier must equal principal subject.
3. **Payload confidentiality (negative):** DB and API list/detail must not expose plaintext proof payload.
4. **Lock token secrecy (negative):** Search audit/mobile event payloads for raw `lock_token` -> expect none.
5. **Actor spoof prevention (negative):** Send forged `actor_subject`/`actor_role` in request body -> stored actor must remain authenticated principal.
6. **Override SoD (negative):** Requester attempts self-approval -> expect deny + audit event.
7. **Replay/idempotency (negative):** Re-send same lifecycle request idempotency key -> second request must not append event.
8. **Sync lease isolation (negative):** Worker B attempts to ack Worker A leased op -> expect reject/no change.

## Remediation Timeline

- **Immediate (blocker before QA proceed):** Findings 1, 2, 3, 4.
- **Pre-release (must complete before production release):** Finding 5.
- **Backlog hardening:** Extended abuse-case tests (fuzzing replay windows, lock-token brute-force telemetry, outbox anomaly alerts).
