# DOO-129 durable finding: CFO QA metrics payload for pricing finalization

Date: 2026-04-23
Issue: DOO-129
Parent: [DOO-124](/DOO/issues/DOO-124)
Posted comment: [4febcd73](/DOO/issues/DOO-129#comment-4febcd73-b3c5-46f8-8114-a0c5bdf9feee)

## Delivered payload summary

- 30-day requested window (`2026-03-24` to `2026-04-23`) with 2 days of available phase-2 QA evidence (`2026-04-22` to `2026-04-23`).
- Reliability evidence:
  - In-window QA runs: `67/67`, `84/84`, `92/92` tests passed.
  - Current run (`npm test`): `21` files, `92` tests, `0` failed.
  - Mobile-loop targeted suites: `workflow` `5/5`, `sync` `7/7`.
- Offline/degraded sync evidence from test assertions:
  - Duplicate residual ops after ack: `0`.
  - Failure-to-retry lease release path: `1/1` success.
  - Conflict ledger open->resolved determinism: `1/1`.
  - Default resolution strategy determinism: `3/3`.
- Open mobile-field critical/high defect query set at report time:
  - `q="mobile field defect"` -> `[]`
  - `q="mobile field bug"` -> `[]`
  - `q="conflict duplication replay"` -> `[]`
- Support burden:
  - Direct observed live-cohort burden unavailable (no live phase-2 pilot cohort evidence yet).
  - Contracting cap held at `<= 1.5 h/account/week` per [DOO-124 pricing guardrails doc](/DOO/issues/DOO-124#document-pricing-guardrails-phase2-mobile-field).

## Confidence position

- Moderate-high confidence for controlled beta contracting now.
- Remaining gap is operational (live support-hours telemetry), not functional correctness in current QA evidence.
- Recommended CFO control: lock now, force post-launch review after first 4 pilot weeks or 10 live accounts.
