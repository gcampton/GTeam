# MAN-111 — Environment parity + secrets standards (2026-04-22)

## Summary
- Added machine-checkable env preflight script in `mantlekit/scripts/env-preflight.mjs`.
- Added `npm run env:preflight` entrypoint.
- Documented env contract, secrets standards, and operator runbook in `mantlekit/docs/operations/env-parity-and-secrets.md`.
- Added staging sample contract file: `mantlekit/docs/operations/examples/staging.env.sample`.
- Wired checks into CI/deploy workflows.

## Evidence
- Command: `npm run env:preflight -- --stage staging --scope all --env-file docs/operations/examples/staging.env.sample`
- Result: pass (14 checks).

## Notes
- `mempalace_search` and `mempalace_add_drawer` commands were unavailable in runtime; used local memory-file fallback.
- Full lint still fails due pre-existing repository lint errors unrelated to this work.
