# MAN-17 Closeout (2026-04-22)

Issue: MAN-17 Set up deployment checks for preview and production gates
Wake reason: issue_commented

## Verified completion

- Confirmed new workflow exists: `.github/workflows/deploy-preview.yml`.
- Confirmed production workflow hardening in `.github/workflows/deploy-production.yml`.
- Verified expected controls are present:
  - Preview deploy contract preflight via `npm run env:preflight -- --stage production --scope deploy`.
  - Preview deploy through `./scripts/deploy-vercel.sh preview`.
  - Preview health verification against `/<root>` with retries.
  - Preview artifacts uploaded (`artifacts/*.log`, `artifacts/*.json`).
  - Production job bound to `environment: production` for gate approvals.
  - Post-deploy health verification for production deploy.
  - Post-rollback health verification in both auto and manual rollback jobs.
- Local validation run:
  - `bash -n scripts/deploy-vercel.sh scripts/rollback-vercel.sh` => pass.
  - Node YAML parse for both workflow files => pass.

## Outcome

- MAN-17 marked done in Paperclip after verification.
- Completion comment posted with verification evidence.

## Notes

- `mempalace_search` and `mempalace_add_drawer` commands were unavailable in this runtime.
- Used local GTeam memory file as durable fallback record.
