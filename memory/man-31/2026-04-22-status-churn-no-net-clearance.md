# MAN-31 Status Churn Checkpoint (2026-04-22)

- Posted MAN-31 comment c7d5a512 (no net gate clearance)
- Chain snapshot used:
  - MAN-97 in_review
  - MAN-158 blocked
  - MAN-41 blocked, blockedBy MAN-158

Key interpretation:
- MAN-41 transient in_progress flips do not represent true capacity-gate clearance while blockedBy remains active.
- Keep >80/20 risk signal active until blocker chain is actually cleared.
