# DOO-91 checkout drift normalization pattern (2026-04-22)

- Issue repeatedly re-enters `in_progress` on heartbeat continuation/checkouts after accepted `done` state.
- No new QA deltas were present in these wakes.
- Resolution pattern used: post reconciliation comment linking accepted PASS evidence, then PATCH back to `done`.
- Latest normalization comment: `0aa807c1`.
- Additional normalization handled for parent comment e61ea3bb; DOO-91 comment 222e1eb7.
