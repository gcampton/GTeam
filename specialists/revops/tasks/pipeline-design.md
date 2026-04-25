## Pipeline Design & Hygiene

**Opportunity stage definitions (sales-led):**

| Stage | Definition | Probability | Exit criteria |
|-------|------------|-------------|---------------|
| Discovery | First meeting completed, need confirmed | 20% | Champion identified, problem defined |
| Qualification | MEDDPICC/BANT confirmed, decision process mapped | 35% | Economic buyer engaged, timeline confirmed |
| Proposal | Formal proposal or POC underway | 50% | Proposal sent, next step agreed |
| Negotiation | Legal/commercial terms being reviewed | 75% | Verbal agreement on terms |
| Closed-Won | Contract signed, payment initiated | 100% | — |
| Closed-Lost | Deal lost, reason logged | 0% | Loss reason required (mandatory field) |

**Hygiene rules (automate where possible):**
- No opportunity stays in the same stage for >21 days without a next-step date update → flag to manager
- Close date must be in the future — auto-alert if past due and still open
- Loss reason is a required field (no empty closed-lost records)
- Opportunity amount must be filled before moving past Discovery
- All opportunities must have a contact role (champion, economic buyer, etc.)

**Weekly pipeline review checklist:**
- [ ] Opps with no next-step activity in 14+ days
- [ ] Close dates in the past that are still open
- [ ] Opps stuck in the same stage for >21 days
- [ ] Opps with no amount set
- [ ] Opps without a contact role assigned

Load: Read `~/dev/1_myprojects/gteam/specialists/revops/references/pipeline-design.md`
