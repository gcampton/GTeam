# Jurisdiction Notes

> **Confidence:** All notes are `[HYPOTHESIS]` (reasoned legal analysis) unless marked `[TESTED: jurisdiction]`. Laws change — verify current position before advising. This is not a substitute for qualified local counsel.

Use this when a contract specifies or involves a particular jurisdiction. Check governing law clause first, then jurisdiction clause — they may differ.

---

## United Kingdom

### Key Legislation to Check

| Act | What It Does | Relevance |
|-----|-------------|-----------|
| Unfair Contract Terms Act 1977 (UCTA) | Controls exclusion/limitation clauses in B2B contracts — must satisfy "reasonableness test" | Liability caps, AS IS disclaimers |
| Consumer Rights Act 2015 (CRA) | Controls unfair terms in B2C contracts — terms must be transparent and not create significant imbalance | Any consumer-facing contract |
| Late Payment of Commercial Debts Act 1998 | Implies 8% over Bank of England base rate on overdue B2B payments | Payment terms |
| Sale of Goods Act / Supply of Goods and Services Act | Implies terms of satisfactory quality, fitness for purpose, reasonable care and skill | Service and goods contracts |
| IR35 (Off-Payroll Working Rules) | Determines whether a contractor is effectively an employee for tax purposes | All contractor/consultancy agreements |
| GDPR (UK GDPR post-Brexit) | Data processing obligations, lawful basis, processor agreements | Any contract involving personal data |

### Key Traps — UK

**UCTA Reasonableness:**
`[HYPOTHESIS]` Even a well-drafted liability cap can be struck down if a court finds it unreasonable. Factors: relative bargaining power, whether the party could insure, whether the cap was negotiated. A cap at 12 months fees is generally considered reasonable in B2B tech contracts — caps below this are riskier.

**Consumer Rights Act 2015 — Unfair Terms:**
- `[HYPOTHESIS]` In consumer contracts, terms are unfair (and void) if they cause significant imbalance contrary to good faith. Key flags: unlimited liability on consumer, auto-renewal with no notice, unilateral price variation.
- Cannot exclude liability for death, personal injury, or breach of the CRA's implied terms.

**IR35 — Contractor Misclassification:**
`[HYPOTHESIS]` Flags that suggest a contractor is inside IR35 (and therefore employment taxes apply):
- Contractor works exclusively for one client for extended periods
- Client controls when, where, and how work is done
- No substitution right (contractor must do the work personally)
- Equipment and tools provided by client
- Ongoing relationship with no fixed deliverable end
**Flag for:** any contractor agreement over 3 months, single client relationships, controlled working arrangements.

**What to flag proactively:**
- Limitation clause: confirm UCTA reasonableness test is met
- Consumer contract: check CRA compliance before signing
- Contractor engagement: assess IR35 risk; recommend CEST tool check
- Data processing: if personal data is involved, UK GDPR processor agreement required
- Dispute resolution: England & Wales courts generally enforce exclusive jurisdiction clauses

---

## United States

### Federal vs State Law

US contract law is primarily state law. Federal law overlays apply for: IP (copyright, patents — federal), employment discrimination, data privacy (HIPAA, COPPA — sectoral).

### California

`[HYPOTHESIS]`

**IP Assignment — Labor Code § 2870:**
- Employee/contractor cannot be required to assign IP developed entirely on their own time, without using employer's resources, that does not relate to employer's business.
- `[HYPOTHESIS]` **Flag:** Any IP assignment clause in a California employment or contractor agreement should carve out § 2870 protected inventions. Failure to include this carve-out makes the assignment clause unenforceable to that extent.

**Non-Competes — Business & Professions Code § 16600:**
- Post-employment non-competes are broadly void in California for employees.
- Trade secrets protection still applies.
- `[HYPOTHESIS]` For commercial (non-employment) contracts between businesses, non-competes are generally enforceable if reasonable — but narrow anyway.
- **Flag:** Any non-compete in a California employment contract — advise client it is likely unenforceable; do not rely on it.

**CCPA / CPRA (California Consumer Privacy Act / California Privacy Rights Act):**
- Applies to for-profit businesses meeting thresholds (>$25M revenue, or >100k consumers' data, or >50% revenue from selling data).
- Rights: access, deletion, opt-out of sale/sharing, correction, portability.
- **Flag:** Any contract involving California consumers' personal data — check if CCPA applies; if so, Data Processing Agreement (DPA) required with service providers; cannot use data beyond stated purpose.

**What to flag proactively (California):**
- IP assignment in employment/contractor agreement: add § 2870 carve-out
- Non-compete: advise it is likely unenforceable in employment context
- Consumer data: check CCPA threshold; add DPA if applicable
- Choice of law clause choosing California: courts will apply California's mandatory rules regardless

### New York

`[HYPOTHESIS]`

**Blue Pencil Rule:**
- New York courts can modify (blue pencil) overly broad restrictive covenants to make them enforceable, rather than voiding them entirely.
- **Implication:** A supplier relying on a non-compete clause being unenforceable in New York may find the court narrows it rather than voids it — partial enforcement is possible.

**Commercial Division:**
- New York Commercial Division handles business disputes over $500k efficiently. Arbitration clauses in New York commercial contracts are generally enforced.
- `[HYPOTHESIS]` New York is a common governing law choice for financial services contracts — sophisticated commercial parties are held to their bargains with less judicial paternalism.

**What to flag proactively (New York):**
- Non-competes: enforceable if reasonable; blue pencil means partial enforcement likely
- Governing law: New York commercial law is predictable and well-developed — generally acceptable choice
- Finance/investment contracts: check securities law compliance separately

### Delaware

`[HYPOTHESIS]`

- Delaware is the dominant jurisdiction for US corporate law. Most major US corporations are incorporated in Delaware regardless of where they operate.
- **Court of Chancery:** Specialist court for corporate/equity disputes — no jury, experienced judges, fast.
- **What to flag:** Shareholder agreements, investment terms, stock option plans governed by Delaware law — generally the gold standard for investor-friendly corporate contracts.
- LLC operating agreements: Delaware allows broad flexibility in LLC agreements — parties can contract out of many default fiduciary duties.
- `[HYPOTHESIS]` **Flag:** If fiduciary duties are waived in an LLC agreement, minority investors lose important protections — always flag and explain implications.

---

## European Union / EEA

### GDPR — General Data Protection Regulation

`[HYPOTHESIS]`

**When it applies:** Any processing of personal data of EU/EEA residents, regardless of where the processor is located.

**Controller vs Processor:**
| Role | Determines purpose & means | Examples |
|------|-----------------------------|---------|
| Controller | Yes | Client instructing a service |
| Processor | No — acts on controller's instructions | SaaS vendor processing client's customer data |
| Joint Controller | Both parties determine purpose | Two companies running a joint campaign |

**What must be in a contract involving EU personal data:**

**If supplier is a processor:**
- Data Processing Agreement (DPA) required — Article 28 GDPR mandates this.
- DPA must include: subject matter, duration, nature and purpose of processing, type of personal data, categories of data subjects, obligations and rights of controller.
- Sub-processor restrictions: processor cannot engage sub-processors without controller's authorisation.
- `[HYPOTHESIS]` Standard Contractual Clauses (SCCs) required for transfers outside EEA (e.g. to US suppliers).

**Key rights to account for in contracts:**
- Right to erasure (right to be forgotten) — does the contract require the supplier to delete data on request? Timeline?
- Data portability — can the client extract their data in a machine-readable format?
- Breach notification — GDPR requires notification to supervisory authority within 72 hours; contract should require supplier to notify client within 24–48 hours of discovering a breach.

**What to flag proactively (EU/GDPR):**
- No DPA: HIGH — add Article 28-compliant DPA
- No SCC for transfers to non-EEA country: HIGH — add SCCs or verify adequacy decision
- No breach notification clause: HIGH — add 24-hour notification obligation on processor
- No sub-processor restrictions: MEDIUM — add requirement for prior written consent or list

### EU VAT — Cross-Border Services

`[HYPOTHESIS]`

- B2B services: reverse charge applies — customer accounts for VAT in their jurisdiction; supplier does not charge VAT if customer provides valid VAT number.
- B2C services: supplier must charge VAT at the rate of the consumer's country (One Stop Shop scheme simplifies filing).
- Digital services to EU consumers: OSS scheme — register once, file quarterly, pay all EU VAT through one return.
- **Flag:** Any contract with EU businesses or consumers involving services — check whether VAT number exchange and reverse charge clauses are in place.

---

## Australia

### Australian Consumer Law (ACL) — Schedule 2, Competition and Consumer Act 2010

`[HYPOTHESIS]`

**Consumer guarantees:**
- Goods: acceptable quality, fit for disclosed purpose, matching description.
- Services: due care and skill, fit for purpose, within reasonable time.
- These guarantees **cannot be excluded** in consumer contracts — any clause purporting to do so is void.
- `[HYPOTHESIS]` For B2B contracts with small businesses (since November 2023 amendments): unfair contract terms provisions now apply more broadly.

**Unfair Contract Terms:**
- Since November 2023: unfair contract terms are void AND attract civil penalties (previously only void).
- Applies to: standard form contracts with small businesses (< 100 employees or < AU$10M turnover) or consumers.
- Unfair term examples: unilateral variation rights, disproportionate exit fees, terms that allow one party to avoid performance.
- `[HYPOTHESIS]` **Flag:** Any standard form contract offered to Australian small businesses — review for unfair terms proactively; civil penalty exposure is significant (up to AU$50M for corporations).

**PPSA — Personal Property Securities Act 2009:**
- If supplying goods on credit or retaining a security interest, registration on the PPSR is required to perfect the interest.
- Unregistered security interests lose priority to a liquidator on insolvency.
- **Flag:** Any contract for supply of goods where payment is deferred or title retention is used — check PPSR registration.

**What to flag proactively (Australia):**
- Consumer contract: check ACL guarantees — cannot exclude
- Small business standard form: unfair terms review — civil penalty risk
- Goods supply with deferred payment: PPSR registration
- Cross-border data: Privacy Act 1988 applies to organisations with > AU$3M turnover; cross-border disclosure rules apply

---

## Quick-Reference: Jurisdiction → Top Three Flags

| Jurisdiction | Flag 1 | Flag 2 | Flag 3 |
|-------------|--------|--------|--------|
| UK | UCTA reasonableness of liability cap | IR35 contractor status | UK GDPR DPA if personal data |
| California | Non-compete likely void (employment) | § 2870 IP assignment carve-out | CCPA DPA if consumer data |
| New York | Non-compete: blue pencil (may be partially enforced) | Commercial Division = fast B2B enforcement | — |
| Delaware | LLC fiduciary duty waivers | Court of Chancery for corporate disputes | Broad LLC agreement flexibility |
| EU/EEA | GDPR DPA required if any personal data | SCCs for non-EEA transfers | 72-hour breach notification chain |
| Australia | ACL guarantees cannot be excluded (consumer) | Unfair terms civil penalties (small business) | PPSR registration for goods on credit |
