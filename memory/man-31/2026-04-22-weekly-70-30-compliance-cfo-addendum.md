# MAN-31 Weekly 70/30 Compliance Review (2026-04-22 AEST)

## Wake context
- Wake reason: issue_commented
- Latest comment: CFO control addendum requiring mandatory sections in weekly reporting
- Effective date: 2026-04-22

## Report posted
- Issue: MAN-31
- Comment id: b13ad352-3b83-4d01-be43-51e09a2511b1
- Status kept: in_progress (recurring weekly cadence)

## Included required CFO sections
- Actual spend by lane vs cap:
  - Codex 0 vs 2,800 AUD
  - Cursor 0 vs 1,200 AUD
  - Total 0 vs 4,000 AUD
- Lane share check vs guardrail:
  - Spend-share N/A (zero denominator)
  - Operational proxy from MAN-41: 76.9% / 23.1% (in-band)
- 2-week rolling projection:
  - Week +1 at risk of >80/20 due dependency delay
  - Week +2 contingent on MAN-41 and MAN-97 clearing
- Escalation trigger flags:
  - >15% lane cap breach: no
  - >4,400 total spend: no
  - two-week guardrail breach: not yet
  - new commitment over thresholds: none recorded
  - forecasted >80/20 due dependency delay: yes (trigger hit)

## Key dependencies referenced
- MAN-13 strategy linkage
- MAN-158 CFO thresholds and evidence package
- MAN-41 execution dependency
- MAN-97 approval/activation dependency

## Notes
- Direct `mempalace_add_drawer` tool was not available as a shell command in this runtime.
- Used mempalace search + mined memory file fallback for durable storage.
