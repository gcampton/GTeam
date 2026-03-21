# Contract Review Checklist

> **Confidence:** All assessments are `[HYPOTHESIS]` (reasoned legal best-practice) unless marked `[JURISDICTION-TESTED: jurisdiction]`. Confirm against applicable law before advising a client.

Use this checklist clause by clause. Work top-to-bottom — liability and IP first, boilerplate last. Flag every HIGH item before summarising.

---

## Risk Rating Key

| Rating | Meaning |
|--------|---------|
| HIGH | Material financial or legal exposure — must fix before signing |
| MEDIUM | Meaningful risk — negotiate if possible, document if accepted |
| LOW | Minor or theoretical risk — flag but not a blocker |
| OK | Standard market position — no action needed |

---

## 1. Liability & Indemnification

**Risk default: HIGH unless capped and mutual.**

- [ ] **Liability cap present?** — check for an express cap clause `[HYPOTHESIS]`
  - Uncapped = HIGH. Minimum acceptable: 12 months' fees paid under the contract.
  - Common positions: 12 months fees / total contract value / insurance coverage amount.
  - `[HYPOTHESIS]` Watch for carve-outs that swallow the cap (IP infringement, fraud, death/PI often excluded — that is normal; broad exclusions are not).
- [ ] **Cap applies to both parties?** — one-sided caps = MEDIUM risk.
- [ ] **Consequential loss excluded?** — check for "indirect, consequential, special, punitive" exclusion.
  - If absent and you are the supplier: HIGH.
  - Standard carve-out language: "neither party shall be liable for loss of profits, loss of data, loss of business, or indirect loss."
- [ ] **Indemnification obligations** — who indemnifies whom for what?
  - Third-party IP infringement indemnity by supplier: market standard = OK.
  - Broad indemnity for any breach: HIGH if one-sided.
  - `[HYPOTHESIS]` Mutual indemnity against own negligence is the balanced position.
- [ ] **Insurance requirements specified?** — minimum levels stated? MEDIUM if absent on high-value contracts.

| Scenario | Risk | Action |
|----------|------|--------|
| No liability cap | HIGH | Negotiate cap at 12 months fees |
| Cap exists but carve-outs cover core service | HIGH | Narrow carve-outs |
| Consequential loss not excluded | HIGH (supplier) | Add exclusion |
| One-sided indemnity | MEDIUM | Make mutual |
| Cap below insurance level | LOW | Flag, prefer cap = insurance |

---

## 2. IP Ownership

**Risk default: HIGH if IP not clearly allocated.**

- [ ] **Work product ownership** — who owns deliverables created under the contract?
  - Default in many jurisdictions: creator (contractor) retains IP unless assigned. `[HYPOTHESIS]`
  - Client usually wants: assignment of all work product on payment.
  - Supplier usually wants: licence, not assignment (preserves reuse rights).
- [ ] **Background IP licence** — if supplier uses pre-existing IP (tools, frameworks, templates), is a licence granted?
  - Missing background IP licence = HIGH — client may not be able to use deliverables.
  - `[HYPOTHESIS]` Licence should be: irrevocable, royalty-free, non-exclusive, for the purpose of using the deliverables.
- [ ] **Open source contamination** — do deliverables incorporate GPL/AGPL/LGPL code?
  - Copyleft licences (GPL) can require client to open-source their product = HIGH.
  - `[HYPOTHESIS]` Require supplier warranty that no copyleft code is included without disclosure.
- [ ] **Moral rights waived?** (UK/EU relevant) — LOW if not waived but can affect modification rights.
- [ ] **Employee/contractor chain** — does supplier have assignments from all sub-contractors who created work? MEDIUM if not confirmed.
- [ ] **Improvements / derivative works** — who owns improvements to background IP? Supplier should retain; improvements to deliverables may be shared.

| Scenario | Risk | Action |
|----------|------|--------|
| No IP clause at all | HIGH | Add full IP assignment or licence |
| "All IP we create belongs to us" (supplier) | HIGH (client) | Negotiate assignment of work product |
| No background IP licence | HIGH | Add irrevocable licence |
| GPL code in deliverables | HIGH | Require warranty + indemnity |
| No sub-contractor chain confirmation | MEDIUM | Add warranty of title |

---

## 3. Termination

- [ ] **Termination for cause** — what constitutes a breach triggering termination?
  - Look for: material breach, insolvency, regulatory action.
  - Cure period standard: 14–30 days notice to remedy = OK. Immediate termination for any breach = HIGH (for the non-terminating party).
- [ ] **Termination for convenience** — can either party terminate without cause?
  - Notice period: 30 days minimum; 90 days is common on significant contracts.
  - One-sided convenience termination (only one party can invoke) = MEDIUM.
  - `[HYPOTHESIS]` Check payment obligations on convenience termination — work done to date should be paid.
- [ ] **Notice periods** — are they reasonable and symmetric?
- [ ] **Consequences on termination** — return of data, handover obligations, transition assistance?
  - No data return/destruction clause = MEDIUM (GDPR relevance for EU contracts).
- [ ] **Survival clauses** — which clauses survive termination?
  - Should survive: IP, confidentiality, liability, payment for work done, dispute resolution.
  - `[HYPOTHESIS]` If no survival clause, check governing law default — in many jurisdictions dispute resolution survives anyway but confirm.
- [ ] **Auto-renewal clause** — notice required to prevent auto-renewal? How long?
  - Short notice window (< 30 days) with long auto-renewal term = MEDIUM.

| Scenario | Risk | Action |
|----------|------|--------|
| Immediate termination for minor breach | HIGH | Add cure period (14–30 days) |
| No payment on convenience termination | HIGH (supplier) | Add pro-rata payment obligation |
| No survival clause | MEDIUM | Add list of surviving clauses |
| Auto-renewal with < 30 days notice window | MEDIUM | Extend notice window or remove auto-renewal |

---

## 4. Payment Terms

- [ ] **Milestone triggers** — are milestones clearly defined? Vague milestones (e.g. "satisfactory completion") = HIGH for supplier.
  - `[HYPOTHESIS]` Milestones should be objective and binary — either delivered or not.
- [ ] **Acceptance criteria** — is there a formal acceptance process? How long does client have to accept/reject?
  - Deemed acceptance (silence = accepted after X days) protects supplier = OK for supplier.
  - Unlimited rejection right = HIGH for supplier.
- [ ] **Late payment** — is there a late payment penalty or statutory interest?
  - UK: Late Payment of Commercial Debts Act applies by default — 8% over base rate = OK.
  - US: state-specific; check governing law. `[HYPOTHESIS]`
  - No late payment provision (foreign law): MEDIUM — supplier has no automatic remedy.
- [ ] **Currency** — which currency? Who bears FX risk on multi-currency contracts?
  - FX risk not addressed on cross-border contracts = MEDIUM.
- [ ] **Set-off rights** — can client deduct disputed amounts from invoices?
  - Broad set-off right = HIGH for supplier. Standard position: exclude or limit to undisputed amounts.
- [ ] **Invoice requirements** — specific format, PO number, VAT registration requirements?
  - Missing invoice requirements can cause payment delays in practice = LOW but practical flag.
- [ ] **Expenses** — pre-approved or open-ended? Cap present?

---

## 5. Confidentiality

- [ ] **Scope of confidential information** — is the definition proportionate?
  - Overly broad ("any information shared") = MEDIUM — catches publicly known information.
  - Standard: information marked confidential, or if oral — confirmed in writing within X days.
- [ ] **Duration** — how long does confidentiality survive contract end?
  - 2–5 years post-termination = market standard = OK.
  - Perpetual confidentiality on truly proprietary info (trade secrets) = OK.
  - Perpetual on all information = MEDIUM — burdensome and often unenforceable. `[HYPOTHESIS]`
- [ ] **Carve-outs present?**
  - Standard carve-outs (must be present): publicly known, independently developed, received from third party, required by law/court order/regulator.
  - Missing court order/regulator carve-out = HIGH — party could face contempt vs breach of contract conflict.
- [ ] **Residual knowledge clause** — allows use of information retained in unaided memory. LOW risk; flag if absent in tech contracts (relevant for employee departures).
- [ ] **Return/destruction of information** — required on termination? Timeline?

---

## 6. Warranties

- [ ] **Express warranties** — what does each party warrant?
  - Supplier typically warrants: authority to enter contract, no IP infringement, services meet specification.
  - Client typically warrants: authority, payment ability.
- [ ] **Implied warranties** — check whether governing law implies terms (e.g. UK SGA/SGSA fitness for purpose, satisfactory quality).
  - `[HYPOTHESIS]` In B2B contracts under UK law, implied terms can be excluded but must be reasonable (UCTA 1977 reasonableness test).
  - In consumer contracts, implied terms cannot generally be excluded.
- [ ] **Disclaimer of implied warranties** — "AS IS" disclaimers: check if enforceable under governing law.
  - US UCC implied warranties can be disclaimed with specific language. `[HYPOTHESIS]`
  - UK: cannot exclude liability for death/PI or fraudulent misrepresentation regardless of disclaimer.
- [ ] **Fitness for purpose warranty** — does supplier warrant deliverables are fit for client's specific purpose?
  - If client has communicated specific purpose, absence = MEDIUM.
- [ ] **Warranty period** — how long do warranties last? 30/60/90 days post-delivery is common.
  - No warranty period = MEDIUM (no remedy if defect discovered late).
- [ ] **Remedy for warranty breach** — re-performance, repair, or refund? Priority of remedies stated?

---

## 7. Dispute Resolution

- [ ] **Mechanism** — arbitration, litigation, or escalation then arbitration/litigation?
  - `[HYPOTHESIS]` Arbitration preferred for: cross-border contracts, confidentiality of proceedings, enforceability (New York Convention 168+ countries).
  - Litigation preferred for: injunctive relief urgency, multiple parties, precedent value.
- [ ] **Jurisdiction selection** — which courts have jurisdiction?
  - Check whether jurisdiction clause is exclusive or non-exclusive.
  - Exclusive jurisdiction = both parties can only sue in that forum = OK if balanced.
  - Non-exclusive = either party can choose = can mean parallel proceedings = MEDIUM.
- [ ] **Governing law** — which law governs? May differ from jurisdiction clause.
  - `[HYPOTHESIS]` Governing law and jurisdiction should be aligned or deliberately separated (e.g. English law, arbitration in Singapore).
- [ ] **Escalation procedure** — senior management escalation before formal dispute? LOW but useful for ongoing relationships.
- [ ] **Expert determination** — technical disputes referred to independent expert? Useful for software specification disputes.

---

## 8. Force Majeure

- [ ] **Scope** — what events are covered?
  - Standard: natural disasters, war, government action, pandemic.
  - `[HYPOTHESIS]` Overly broad definitions (e.g. "any event beyond reasonable control" including supply chain delays, strikes, IT failures) = MEDIUM for client.
  - Cyber attacks: expressly included or excluded? Flag either way.
- [ ] **Notification requirement** — party must notify within X days of event?
  - No notification requirement = MEDIUM — abuse risk.
  - Typical: 3–10 business days.
- [ ] **Suspension vs termination** — how long before a force majeure event allows termination?
  - 30–90 days of suspension before termination right = market standard.
  - No termination right after prolonged FM = HIGH (trapped in suspended contract).
- [ ] **Payment during force majeure** — is the affected party still obligated to pay?
  - Supplier FM does not excuse client payment unless services suspended = OK.

---

## 9. Assignment

- [ ] **Consent required for assignment?**
  - "Not to be unreasonably withheld" is market standard = OK.
  - Absolute prohibition = HIGH if either party may need to assign (e.g. on sale of business).
  - Free assignment right (no consent) = MEDIUM for other party.
- [ ] **Change of control clause** — does a change of control trigger a deemed assignment?
  - `[HYPOTHESIS]` Acquisition of a party can be caught by assignment restrictions — check whether change of control is defined and whether it triggers consent or termination rights.
  - Relevant for: VC-backed companies, potential acquisition targets.
- [ ] **Sub-contracting** — is sub-contracting permitted? With or without consent?
  - Sub-contracting without consent = MEDIUM for client (unknown third parties performing services).
  - Supplier remains liable for sub-contractor performance: confirm this is express.

---

## Quick-Reference: Clause → Default Risk → First Ask

| Clause | Default Risk if Silent | First Negotiating Ask |
|--------|----------------------|----------------------|
| Liability cap | HIGH | Cap at 12 months fees, mutual |
| Consequential loss | HIGH (supplier) | Exclude indirect/consequential loss |
| IP ownership | HIGH | Assign work product; licence background IP |
| Termination cure period | HIGH | 14–30 days to remedy material breach |
| Confidentiality carve-outs | HIGH | Add court order / regulator carve-out |
| Payment set-off | HIGH (supplier) | Exclude or limit to undisputed sums |
| Assignment / change of control | MEDIUM | Consent not unreasonably withheld; survive group restructure |
| Force majeure notification | MEDIUM | 5 business days notice requirement |
| Warranty period | MEDIUM | 90 days post-delivery with re-performance remedy |
| Late payment | MEDIUM | Statutory interest or agreed rate |
