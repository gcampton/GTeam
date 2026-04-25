# MAN-31 Corrective Allocation Entry Applied (2026-04-23)

- Source comment: cd8a32f3 (MAN-256 corrective allocation entry)
- Concrete action taken:
  - Updated document current-week-compliance-loop-2026-04-22 (revision 2) with Corrective Allocation Ledger Update section
  - Posted checkpoint comment: 38434590-c7db-4a1a-ad4d-601027530000

Ledger state captured:
- MAN-255 = +1 Codex exception
- MAN-258 = compensating +1 Cursor slot (in_progress)
- Net delta currently +1 Codex until MAN-258 reaches done

Unblock owner/action captured:
- Owner: local-board on MAN-97
- Action: clear Cursor approval queue so MAN-258 can complete
- Follow-through: post same-cycle neutralization confirmation on MAN-31 once MAN-258 is done
