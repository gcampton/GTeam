# Redline Patterns

> **Confidence:** All redlines are `[HYPOTHESIS]` (reasoned drafting positions) unless marked `[JURISDICTION-TESTED: jurisdiction]`. Adapt to governing law before using verbatim.

Each pattern follows the format:
1. **Problem** — what the current clause does and why it is problematic
2. **Current text (typical)** — representative language from real contracts
3. **Suggested redline** — proposed replacement or addition
4. **Risk eliminated** — what exposure is removed by the change

---

## Pattern 1 — Unlimited Liability → Cap at 12 Months Fees

`[HYPOTHESIS]`

**Problem:** No liability cap means a single breach could expose a party to damages exceeding the entire contract value or more.

**Current text (typical):**
> "Each party shall be liable for all losses, damages, costs, and expenses arising out of or in connection with this Agreement."

**Suggested redline:**
> "~~Each party shall be liable for all losses, damages, costs, and expenses arising out of or in connection with this Agreement.~~
>
> **The total aggregate liability of either party to the other under or in connection with this Agreement, whether arising in contract, tort (including negligence), misrepresentation, or otherwise, shall not exceed the greater of (a) the total fees paid or payable by the Client to the Supplier in the twelve (12) months immediately preceding the event giving rise to the claim, or (b) [£/$/€ X]. Neither party shall be liable to the other for any indirect, consequential, special, or punitive losses, including loss of profits, loss of revenue, loss of data, or loss of business opportunity, even if advised of the possibility of such loss.**"

**Notes on carve-outs from the cap (standard market):**
- Death or personal injury caused by negligence: uncapped (required by law in many jurisdictions)
- Fraud or fraudulent misrepresentation: uncapped
- IP infemnification: sometimes uncapped but resist if possible — offer separate higher cap (e.g. 200% of fees)
- Payment obligations: sometimes carved out — OK if it means client cannot use cap to avoid paying

**Risk eliminated:** Unlimited liability exposure; consequential loss (lost profits, lost data) claims.

---

## Pattern 2 — Broad IP Assignment → Limit to Work Product Only

`[HYPOTHESIS]`

**Problem:** "Anything created" language assigns pre-existing IP (tools, frameworks, libraries, methodologies) that the supplier developed before or outside this engagement. This can leave the supplier unable to use their own tools for other clients.

**Current text (typical):**
> "All intellectual property rights in any work, materials, or inventions created by the Supplier in connection with this Agreement shall vest in and be assigned to the Client with full title guarantee."

**Suggested redline (supplier-friendly):**
> "~~All intellectual property rights in any work, materials, or inventions created by the Supplier in connection with this Agreement shall vest in and be assigned to the Client with full title guarantee.~~
>
> **All intellectual property rights in the Deliverables (as defined in Schedule [X]) created specifically for the Client under this Agreement ("Work Product") shall be assigned to the Client upon receipt of full payment. For the avoidance of doubt, this assignment does not extend to the Supplier's Background IP.**
>
> **"Background IP" means all intellectual property rights owned by or licensed to the Supplier prior to the commencement of this Agreement, or developed by the Supplier independently of this Agreement, including without limitation the Supplier's tools, frameworks, methodologies, and pre-existing code libraries.**
>
> **The Supplier hereby grants the Client a non-exclusive, irrevocable, royalty-free licence to use the Background IP to the extent necessary to make full use of the Deliverables for the Client's internal business purposes.**"

**Risk eliminated (supplier):** Loss of pre-existing tools and frameworks; inability to reuse methodologies for other clients.

**Risk eliminated (client):** Deliverables that cannot be used without a licence (because Background IP is embedded) — the licence clause addresses this.

---

## Pattern 3 — Unilateral Amendment Rights → Require Written Consent

`[HYPOTHESIS]`

**Problem:** Clauses allowing one party (usually a platform or large enterprise) to amend the agreement by notice allow material changes to pricing, scope, or terms without the other party's agreement.

**Current text (typical):**
> "We reserve the right to modify these terms at any time. Your continued use of the service following notification of changes constitutes acceptance."

**Or in B2B service agreements:**
> "The Supplier may update these terms on thirty (30) days' written notice to the Client."

**Suggested redline:**
> "~~We reserve the right to modify these terms at any time. Your continued use of the service following notification of changes constitutes acceptance.~~
>
> **No amendment or variation to this Agreement shall be effective unless it is in writing and signed (or executed by electronic signature) by an authorised representative of each party.**"

**If the other party insists on a unilateral amendment right, narrow it:**
> "The Supplier may update operational procedures and security standards on thirty (30) days' written notice, provided such updates do not materially increase the Client's obligations or reduce the Supplier's obligations. Any amendment to pricing, payment terms, liability, or intellectual property provisions requires the written consent of both parties."

**Risk eliminated:** Surprise price increases; removal of agreed protections; unilateral scope changes mid-engagement.

---

## Pattern 4 — Broad Non-Compete → Narrow to Direct Competitors, Time-Limited

`[HYPOTHESIS]`

**Problem:** Broad non-compete clauses can prevent a party (often a supplier or contractor) from working in an entire industry sector, or for any company the other party considers a competitor — potentially including companies that are only tangentially competitive.

**Current text (typical):**
> "During the term of this Agreement and for a period of two (2) years following termination, the Supplier shall not provide services to any business that competes with the Client."

**Suggested redline:**
> "~~During the term of this Agreement and for a period of two (2) years following termination, the Supplier shall not provide services to any business that competes with the Client.~~
>
> **During the term of this Agreement and for a period of [six (6) / twelve (12)] months following termination, the Supplier shall not provide [specifically defined services, e.g. "payment processing software development services"] directly to [named direct competitors listed in Schedule [X]] ("Restricted Competitors"). The Supplier shall not be restricted from providing services to any business not named as a Restricted Competitor, including businesses operating in adjacent markets or industries.**"

**Additional protections to add:**
> "The parties acknowledge that the restrictions in this clause are reasonable and necessary to protect the legitimate business interests of the Client. If any restriction is found to be unenforceable, it shall be modified to the minimum extent necessary to make it enforceable, and the remaining restrictions shall continue in full force."

**Notes:**
- `[HYPOTHESIS]` California: non-competes in commercial contracts (not employment) are generally enforceable if reasonable; in employment, largely unenforceable (Business & Professions Code § 16600).
- UK: courts apply a reasonableness test — geographic scope, duration, and activity must all be justified.
- EU: check national implementing laws; garden leave provisions during notice period may be an alternative.

**Risk eliminated:** Inability to take on any work in a broad sector; loss of livelihood for an independent contractor.

---

## Pattern 5 — One-Sided Indemnification → Make Mutual

`[HYPOTHESIS]`

**Problem:** Clauses requiring only one party (typically the supplier or smaller party) to indemnify the other for any breach, claim, or loss create asymmetric exposure and do not reflect balanced commercial risk allocation.

**Current text (typical):**
> "The Supplier shall indemnify, defend, and hold harmless the Client and its officers, directors, employees, and agents from and against any and all claims, damages, losses, costs, and expenses (including reasonable legal fees) arising out of or relating to: (a) the Supplier's breach of this Agreement; (b) the Supplier's negligence or wilful misconduct; (c) the Supplier's infringement of any third-party intellectual property rights."

**Suggested redline:**
> "**Each party ("Indemnifying Party") shall indemnify, defend, and hold harmless the other party and its officers, directors, employees, and agents ("Indemnified Party") from and against any third-party claims, damages, losses, costs, and expenses (including reasonable legal fees) arising out of or relating to: (a) the Indemnifying Party's material breach of this Agreement; (b) the Indemnifying Party's negligence or wilful misconduct; or (c) the Indemnifying Party's infringement of any third-party intellectual property rights.**
>
> **The Indemnified Party shall: (i) promptly notify the Indemnifying Party in writing of any claim for which indemnification is sought; (ii) give the Indemnifying Party sole control of the defence and settlement of the claim (provided the Indemnifying Party does not settle any claim that imposes obligations on the Indemnified Party without the Indemnified Party's prior written consent); and (iii) provide reasonable cooperation at the Indemnifying Party's cost.**"

**What this adds:**
- Mutual obligation (both parties indemnify each other for their own wrongdoing)
- Notification requirement (prevents ambush indemnity claims)
- Control of defence (indemnifying party drives defence cost-efficiently)
- Consent to settlement (prevents the other party from agreeing to obligations on your behalf)

**Risk eliminated:** One-sided exposure to third-party claims; surprise indemnity demands; loss of control over defence strategy.

---

## Pattern 6 — "Entire Agreement" Clause Missing or Inadequate

`[HYPOTHESIS]`

**Problem:** Without a clear entire agreement clause, prior representations made during negotiations (e.g. sales promises, email commitments) may be incorporated into the contract by implication.

**Current text (typical — missing or weak):**
> "This Agreement sets out the understanding of the parties."

**Suggested redline:**
> "**This Agreement (together with any Schedules and Order Forms) constitutes the entire agreement between the parties relating to its subject matter and supersedes all prior agreements, representations, warranties, negotiations, and understandings (whether written or oral) between the parties relating to that subject matter. Each party acknowledges that in entering into this Agreement it has not relied on any representation or warranty (whether made innocently or negligently) not expressly set out in this Agreement. Nothing in this clause shall limit liability for fraud or fraudulent misrepresentation.**"

**Risk eliminated:** Pre-contractual representation claims; disputes about verbal commitments made during sales process.

---

## Quick-Reference: Redline Summary

| Issue | Risk Level | Core Fix |
|-------|-----------|---------|
| No liability cap | HIGH | Add mutual cap at 12 months fees + exclude consequential loss |
| IP assigns everything | HIGH | Limit to Work Product; add Background IP licence |
| Unilateral amendment right | HIGH | Require written consent of both parties |
| Broad non-compete | MEDIUM–HIGH | Named competitors only, time-limited, specific activities only |
| One-sided indemnity | MEDIUM–HIGH | Make mutual; add notification + defence control mechanics |
| No entire agreement clause | MEDIUM | Add full merger/integration clause with fraud carve-out |
