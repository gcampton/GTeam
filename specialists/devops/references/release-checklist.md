# Release Checklist

> **Confidence:** All items are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Work top to bottom. Do not skip sections for "small" releases — most incidents are caused by "small" changes. `[HYPOTHESIS]`

---

## Pre-Ship: Code Readiness

- [ ] Working tree is clean (`git status` shows nothing unexpected)
- [ ] All CI checks are green on the branch being shipped
- [ ] Diff has been reviewed by at least one other person (or self-reviewed with fresh eyes after a break)
- [ ] The branch is up to date with the target base branch (`git log origin/main..HEAD` shows only your commits)
- [ ] No debug code, commented-out blocks, or `console.log` left in

---

## Pre-Ship: Version & Changelog

- [ ] Version bumped according to semver rules (see table below)
- [ ] `CHANGELOG.md` updated in user-facing language (see format below)
- [ ] Git tag created or queued to be created on the merge commit (`v1.2.3`)

### Semver Rules `[HYPOTHESIS]`

| Change type | Version bump | Example |
|------------|-------------|---------|
| Bug fix, no API change | Patch (`1.0.x`) | Fix login redirect loop |
| New feature, backward compatible | Minor (`1.x.0`) | Add export-to-CSV button |
| Breaking change (removed/changed API) | Major (`x.0.0`) | Remove `/v1/` endpoints |
| Security patch with no behaviour change | Patch (`1.0.x`) | Update dep with CVE |
| Breaking security fix (forced logout, schema change) | Minor or Major | Rotate all session tokens |

When in doubt: bump minor. Under-bumping a breaking change is worse than over-bumping. `[HYPOTHESIS]`

---

### CHANGELOG Format `[HYPOTHESIS]`

Write for the user, not the developer. Describe what changed, not how.

```markdown
## [1.4.0] - 2026-03-20

### Added
- Users can now export their order history to CSV from the account page

### Changed
- Search results now default to sorting by relevance instead of date

### Fixed
- Fixed a bug where discount codes were not applied to subscription orders
- Fixed broken pagination on the mobile product listing page

### Removed
- Removed the legacy `/api/v1/orders` endpoint (use `/api/v2/orders`)
```

**Rules:**
- Group under Added / Changed / Fixed / Removed / Security
- Past tense, active voice: "Fixed a bug where..." not "Fix bug with..."
- Link to issue or PR where helpful: `(#432)`
- Never: "misc fixes", "various improvements", "updated dependencies" without detail

---

## Pre-Ship: PR Quality

- [ ] PR description includes **what** changed, **why** it changed, and **how to test it**
- [ ] Screenshots or screen recordings included for any UI changes
- [ ] No secrets, credentials, or tokens appear anywhere in the diff (including test fixtures)
- [ ] Breaking changes are called out explicitly in the PR description
- [ ] Database migrations: confirmed reversible or rollback plan documented

**PR description template:**
```
## What
[1-3 sentences describing the change]

## Why
[Context: bug, feature request, tech debt — link to issue]

## How to test
1. [Step-by-step testing instructions]
2. ...

## Screenshots (if UI change)
[Before / After]

## Rollback plan
[How to undo this if it causes problems]
```

---

## Post-Ship

- [ ] Deployment confirmed in the target environment (staging or production)
- [ ] Smoke test / health check passed post-deploy
- [ ] Monitoring dashboards checked for anomalies in the 15 minutes following deploy
- [ ] Error rate, latency, and saturation metrics are within normal range
- [ ] Documentation updated to reflect the change (API docs, README, wiki)
- [ ] TODOs added in this release are tracked in the issue tracker
- [ ] Rollback plan is still documented and accessible if something surfaces later

---

## Emergency Rollback Procedure

Choose the right tool for the situation:

| Situation | Approach |
|-----------|----------|
| Bad code, no DB migration | `git revert <sha>` + redeploy |
| Bad code, reversible migration | Revert migration first, then `git revert` |
| Bad code, irreversible migration | Hotfix branch (forward-fix), not revert |
| Feature is problematic but hard to remove | Feature flag off, then hotfix |
| Infra misconfiguration (not code) | Restore previous infra state / terraform apply previous version |

### git revert vs hotfix branch `[HYPOTHESIS]`

**Use `git revert`** when:
- The bad commit is the tip of the branch
- There are no DB migrations to undo first
- The revert does not have merge conflicts
- Speed matters more than commit history cleanliness

```bash
git revert <sha>   # creates a new commit that undoes <sha>
git push origin main
# redeploy
```

**Use a hotfix branch** when:
- The problem requires a targeted fix, not a full revert
- An irreversible migration means you must go forward, not back
- Multiple commits are involved and reverting all of them would undo unrelated work

```bash
git checkout -b hotfix/fix-payment-crash main
# make fix
git push origin hotfix/fix-payment-crash
# PR → merge → deploy
```

**Use a feature flag** when:
- Infrastructure for flags is already in place
- The underlying code should stay (it is correct) but the feature should be hidden
- Rollout needs to be gradual or per-user

---

## Quick-Reference: Common Mistakes

| Mistake | Why it matters |
|---------|----------------|
| Merging without reading the full diff | Secrets, debug code, and logic errors are missed |
| Skipping changelog for "internal" changes | Future you cannot trace why something changed |
| Shipping Friday afternoon | No one is monitoring; incident response is degraded |
| Forgetting to check post-deploy metrics | Problems surface slowly; you stop watching too early |
| Reverting without checking for migrations | Revert + old schema = data corruption |
