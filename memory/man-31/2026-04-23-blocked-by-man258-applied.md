# MAN-31 Blocked-by MAN-258 Applied (2026-04-23)

Concrete action:
- Set MAN-31 status to blocked with first-class blocker relation:
  - blockedByIssueIds = [MAN-258]

Evidence:
- MAN-31 update comment: 7b0d6d65-1f31-4b53-aedd-1bb8af38b967
- MAN-31 now shows blockedBy relation to MAN-258 in issue payload

Reasoning captured:
- Avoid passive polling while MAN-258 corrective offset slot is blocked
- Resume condition is explicit: when MAN-258 done, resume MAN-31 neutralization confirmation

Unblock owner/action chain captured:
- CTO on MAN-258
- local-board on MAN-97 (upstream approval queue)
