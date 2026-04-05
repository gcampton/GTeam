# Jurisdiction Sources

> **Purpose:** Authoritative source catalog for legal research by jurisdiction and domain. Use this to verify claims, cite sources correctly, and maintain confidence marking discipline.

---

## Verified Reference Catalog

### Primary Sources by Jurisdiction

| Jurisdiction | Primary Source | Secondary Source | URL Pattern |
|---|---|---|---|
| UK | legislation.gov.uk | gov.uk guidance, Hansard | legislation.gov.uk/ukpga |
| EU | EUR-Lex | N-Lex (national transposition) | eur-lex.europa.eu |
| US (Federal) | congress.gov, law.cornell.edu | Federal Register, GPO | uscode.house.gov |
| US (California) | leginfo.legislature.ca.gov | California State Bar | leginfo.legislature.ca.gov |
| US (New York) | nysenate.gov/legislation | NY State Bar Association | nysenate.gov |
| US (Delaware) | delcode.delaware.gov | Delaware Court of Chancery | delcode.delaware.gov |
| Australia (Federal) | legislation.gov.au | Federal Register of Legislation | legislation.gov.au |
| Australia (QLD) | legislation.qld.gov.au | QLD Law Society | legislation.qld.gov.au |
| Australia (NSW) | legislation.nsw.gov.au | NSW Law Society | legislation.nsw.gov.au |
| Australia (VIC) | legislation.vic.gov.au | Law Institute of Victoria | legislation.vic.gov.au |
| Canada (Federal) | laws-lois.justice.gc.ca | Department of Justice | laws-lois.justice.gc.ca |
| Canada (Ontario) | ontario.ca/laws | Law Society of Ontario | ontario.ca/laws |
| New Zealand | legislation.govt.nz | NZ Law Society | legislation.govt.nz |
| Singapore | sso.agc.gov.sg | Law Society of Singapore | sso.agc.gov.sg |
| Hong Kong | elegislation.gov.hk | HK Law Society | elegislation.gov.hk |

---

## Key Legislation by Domain

### Employment

| Jurisdiction | Key Legislation | Reference |
|---|---|---|
| UK | Employment Rights Act 1996, Equality Act 2010, TUPE 2006 | legislation.gov.uk |
| US (Federal) | FLSA, Title VII, ADA, FMLA, WARN Act | law.cornell.edu |
| US (California) | Labor Code (incl. s 2870 IP), FEHA, Cal/OSHA | leginfo.legislature.ca.gov |
| Australia | Fair Work Act 2009, Work Health & Safety Act 2011 | legislation.gov.au |
| EU | Working Time Directive 2003/88/EC, Transfer of Undertakings Directive | eur-lex.europa.eu |
| NZ | Employment Relations Act 2000, Health & Safety at Work Act 2015 | legislation.govt.nz |

### Contracts

| Jurisdiction | Key Legislation | Reference |
|---|---|---|
| UK | UCTA 1977, Consumer Rights Act 2015, Sale of Goods Act 1979, SGSA 1982 | legislation.gov.uk |
| US | UCC (state-adopted), Restatement (Second) of Contracts | law.cornell.edu |
| Australia | ACL (Schedule 2, CCA 2010), Contract Review Act 1980 (NSW) | legislation.gov.au |
| EU | Consumer Rights Directive 2011/83/EU, Rome I Regulation (applicable law) | eur-lex.europa.eu |

### Intellectual Property

| Jurisdiction | Key Legislation | Reference |
|---|---|---|
| UK | Copyright, Designs and Patents Act 1988, Patents Act 1977, Trade Marks Act 1994 | legislation.gov.uk |
| US | Copyright Act (17 USC), Patent Act (35 USC), Lanham Act (15 USC) | law.cornell.edu |
| Australia | Copyright Act 1968, Patents Act 1990, Trade Marks Act 1995 | legislation.gov.au |
| EU | Copyright Directive 2019/790, EU Trade Mark Regulation 2017/1001 | eur-lex.europa.eu |

### Privacy & Data Protection

| Jurisdiction | Key Legislation | Reference |
|---|---|---|
| UK | UK GDPR, Data Protection Act 2018 | legislation.gov.uk |
| EU | GDPR (Regulation 2016/679), ePrivacy Directive 2002/58/EC | eur-lex.europa.eu |
| US (Federal) | HIPAA, COPPA, FERPA (sectoral — no federal general privacy law) | law.cornell.edu |
| US (California) | CCPA / CPRA (Civil Code s 1798.100 et seq.) | leginfo.legislature.ca.gov |
| Australia | Privacy Act 1988, APPs, Notifiable Data Breaches scheme | legislation.gov.au |
| NZ | Privacy Act 2020 | legislation.govt.nz |
| Canada | PIPEDA (federal), provincial privacy statutes | laws-lois.justice.gc.ca |

### Corporate & Commercial

| Jurisdiction | Key Legislation | Reference |
|---|---|---|
| UK | Companies Act 2006, Partnership Act 1890, LLP Act 2000 | legislation.gov.uk |
| US (Delaware) | Delaware General Corporation Law (Title 8), LLC Act (Title 6 Ch 18) | delcode.delaware.gov |
| Australia | Corporations Act 2001 | legislation.gov.au |
| EU | Societas Europaea Regulation, Cross-Border Mergers Directive | eur-lex.europa.eu |

### Tax (Overview Only)

| Jurisdiction | Key Legislation | Reference |
|---|---|---|
| UK | Income Tax Act 2007, Corporation Tax Act 2009, VAT Act 1994 | legislation.gov.uk |
| US | Internal Revenue Code (26 USC) | law.cornell.edu |
| Australia | Income Tax Assessment Act 1997, GST Act 1999 | legislation.gov.au |
| EU | VAT Directive 2006/112/EC | eur-lex.europa.eu |

> **Note:** Tax advice requires specialist expertise. Flag for referral to a tax adviser or accountant specialist for anything beyond basic identification of tax regime.

---

## Citation Format

When citing legislation in deliverables, use this format:

**Acts / Statutes:**
> [Short Title] [Year], [section/article] ([Jurisdiction]) — accessed [date]

Examples:
- Employment Rights Act 1996, s 86 (UK) — accessed 2026-04-05
- California Labor Code s 2870 (US-CA) — accessed 2026-04-05
- Fair Work Act 2009, s 385 (AU) — accessed 2026-04-05
- GDPR, Art 28 (EU) — accessed 2026-04-05

**Regulations / Statutory Instruments:**
> [Title] [Year/Number], [regulation/rule number] ([Jurisdiction])

**Case law (when referenced — use sparingly, verify existence):**
> [Case name] [Year] [Court] [Citation] — note: `[HYPOTHESIS]` unless case verified against official report

---

## Verification Checklist

Before marking any claim as `[JURISDICTION-TESTED]`:

1. **Identify the claim** — what specific legal rule or obligation is being stated?
2. **Look up the relevant act/regulation** in the primary source for that jurisdiction
3. **Check currency** — is this the latest version? Has the section been amended or repealed?
4. **Confirm applicability** — does the act apply to the situation (B2B vs B2C, thresholds, territorial scope)?
5. **Mark with appropriate confidence tag:**
   - `[JURISDICTION-TESTED: XX]` — verified against primary source
   - `[HYPOTHESIS]` — general principle applied without jurisdiction-specific confirmation
   - `[CROSS-JURISDICTION]` — universal principle confirmed across multiple systems

**If source not found or currency uncertain:**
- Mark as `[HYPOTHESIS]` and note: "Source not confirmed as current — verify before relying"
- If jurisdiction is entirely outside scope: "This jurisdiction is outside my verified sources — engage local counsel"
