# API Documentation Audit & Update Plan
**Date:** 2026-04-15  
**Auditor:** GTeam Technical Writer  
**Scope:** Billing API documentation — all published reference pages and the SDK getting-started guide  
**Trigger:** Engineering confirmed ~30% of endpoints have changed since docs were last updated  

---

## Executive Summary

The Billing API documentation covers 14 endpoints across four resources (invoices, customers, tax rates, webhooks) plus an account endpoint and an SDK getting-started guide. Of the 14 documented endpoints, **7 have material documentation problems** — 3 are actively broken (wrong information that will cause integration failures), 4 are missing entirely, and 4 have inaccuracies that will mislead users.

**Estimated remediation effort: 5–7 days of writing time** across 11 work items, prioritised below.

| Tier | Count | Description |
|---|---|---|
| **Broken** | 3 | Wrong information — will cause integration failures if followed |
| **Missing** | 4 | Endpoints exist in production, no documentation at all |
| **Needs improvement** | 4 | Present but inaccurate or incomplete — will mislead users |

---

## 1. Documentation Inventory

### Current doc coverage

| Document | Path | Last known accurate | Status |
|---|---|---|---|
| POST /api/v1/invoices reference | `results/api-docs-post-invoices.md` | 2026-03 | Partially outdated |
| SDK Getting Started guide | `results/sdk-getting-started.md` | 2026-03 | Contains 4 critical errors |
| POST /api/v1/customers reference | — | Never written | Missing |
| GET /api/v1/invoices reference | — | Never written | Missing |
| PATCH /api/v1/invoices/{id} reference | — | Never written | Missing |
| GET /api/v1/tax-rates reference | — | Never written | Missing |
| Payments resource reference | — | Never written | Missing |
| GET /api/v1/account reference | — | Never written | Missing |
| Webhooks event catalogue | — | Never written | Missing |

### Full API surface map

Endpoints identified from source references, error messages, and SDK method calls:

**Invoices**
- `POST /api/v1/invoices` — create
- `GET /api/v1/invoices` — list
- `GET /api/v1/invoices/{id}` — get
- `PATCH /api/v1/invoices/{id}` — update
- `POST /api/v1/invoices/{id}/finalise` — lifecycle action
- `POST /api/v1/invoices/{id}/send` — lifecycle action
- `POST /api/v1/invoices/{id}/void` — lifecycle action

**Customers**
- `POST /api/v1/customers` — create
- `GET /api/v1/customers` — list
- `GET /api/v1/customers/{id}` — get
- `PATCH /api/v1/customers/{id}` — update

**Tax Rates**
- `GET /api/v1/tax-rates` — list
- `GET /api/v1/tax-rates/{id}` — get

**Webhooks**
- `POST /api/v1/webhooks` — register endpoint
- `GET /api/v1/webhooks` — list
- `GET /api/v1/webhooks/{id}` — get
- `DELETE /api/v1/webhooks/{id}` — remove
- `POST /api/v1/webhooks/{id}/trigger` — test fire

**Payments** (implied by webhook events, not yet in docs)
- `GET /api/v1/payments` — list
- `GET /api/v1/payments/{id}` — get

**Account**
- `GET /api/v1/account` — get account details

---

## 2. Audience Matrix

| Audience | Goal | Entry point | Current state |
|---|---|---|---|
| New integrator | Make first authenticated API call | SDK Getting Started | **Broken** — 4 errors in guide |
| Backend developer (REST) | Integrate invoicing end-to-end | POST /api/v1/invoices reference | **Partial** — 4 of 7 invoice endpoints undocumented |
| Backend developer (webhooks) | Receive and validate payment events | SDK Getting Started → Webhooks ref | **Broken** — signature header and algorithm wrong |
| Frontend developer | List and display invoices | GET /api/v1/invoices reference | **Missing** — no reference page exists |
| Ops / support engineer | Look up payments, debug failures | Payments reference | **Missing** — no payments resource documented |

---

## 3. Gap Analysis

### Tier 1 — Broken (fix first; these cause integration failures)

---

#### BROKEN-1: Webhook signature validation is wrong
**Document:** `sdk-getting-started.md`, Step 7 and Python quickstart  
**Severity:** Critical — integrations using this code will reject all webhook events  

**What the docs say:**
```javascript
event = client.webhooks.constructEvent(
  rawBody,
  req.headers["x-billing-signature"],  // ← wrong header name
  WEBHOOK_SECRET
);
```
The Python example uses:
```python
hmac.new(secret.encode(), raw_body, hashlib.sha256).hexdigest()  # ← wrong algorithm
```

**What changed:**
- Header renamed from `x-billing-signature` to `x-billing-signature-v2`
- Algorithm upgraded from HMAC-SHA256 to HMAC-SHA512
- SDK `constructEvent()` signature matches, but the manual Python example is doubly wrong (old header name, old algorithm)

**User impact:** Any developer who copies the webhook receiver code will have `constructEvent()` throw on every event. The catch block returns `400 Bad signature` to the platform, which triggers retries, then disables the endpoint after repeated failures. Silent data loss.

**Fix required:**
1. Update `x-billing-signature` → `x-billing-signature-v2` in the JavaScript example (Step 7a)
2. Update the Python `validate_signature` function to use `hashlib.sha512`
3. Add a migration note for existing integrations: "If your webhook receiver was built before v2.4, update the header name and re-verify your HMAC algorithm."

---

#### BROKEN-2: `GET /api/v1/invoices` pagination API has changed
**Document:** `sdk-getting-started.md`, Step 6 (CRUD Operations → Pagination section)  
**Severity:** High — pagination code in the guide will throw a runtime error  

**What the docs say:**
```javascript
let cursor;
do {
  const page = await client.invoices.list({ limit: 50, cursor });
  cursor = page.next_cursor;  // ← field no longer exists
} while (page.has_more);     // ← field no longer exists
```

**What changed:**  
Pagination migrated from cursor-based to offset-based. Response shape is now:
```json
{
  "data": [...],
  "total": 847,
  "page": 1,
  "per_page": 50,
  "total_pages": 17
}
```
`next_cursor` and `has_more` are no longer returned.

**User impact:** Any developer building a paginated list will copy this loop, get `undefined` on the first iteration, and loop forever (or until they notice `page` never increments).

**Fix required:**
1. Replace cursor pagination example with offset pagination in the SDK guide
2. Document new `page`, `per_page`, `total`, `total_pages` response fields
3. Add note: "Migration: if you were using cursor-based pagination, switch to `page` and `per_page` parameters."

---

#### BROKEN-3: `POST /api/v1/invoices/{id}/finalise` response changed
**Document:** `sdk-getting-started.md`, Step 5; `api-docs-post-invoices.md`, Invoice Lifecycle section  
**Severity:** High — code that reads invoice state immediately after `finalise()` will be wrong  

**What the docs imply:**  
`await client.invoices.finalise(invoice.id)` is shown immediately followed by `await client.invoices.send(invoice.id)` with no async wait. The lifecycle diagram shows `draft → finalised` as a synchronous transition.

**What changed:**  
Finalisation is now asynchronous. The endpoint returns `202 Accepted` with a job object:
```json
{
  "job_id": "job_abc123",
  "status": "pending",
  "invoice_id": "inv_def456"
}
```
The invoice transitions to `finalising` state, then `finalised` once the job completes (typically <2 seconds, but not guaranteed). Calling `send()` immediately after `finalise()` will fail with `422 invoice_not_finalised` if the job hasn't completed yet.

**User impact:** The quickstart script in Step 5 and the Complete Script section will fail intermittently. Developers in production will see sporadic `422` errors on send.

**Fix required:**
1. Update Step 5 to poll for job completion (or use `await client.invoices.waitForFinalise(invoice.id)` if the SDK provides it)
2. Update the lifecycle diagram state labels
3. Document the `GET /api/v1/jobs/{id}` endpoint or SDK polling helper
4. Add a note in the POST /api/v1/invoices reference under "Invoice Lifecycle"

---

### Tier 2 — Missing (fix second; these leave users stranded mid-integration)

---

#### MISSING-1: `POST /api/v1/customers` has no reference page
**Impact:** Customers endpoint is the entry point for every integration — invoked in Step 4 of the getting-started guide, but there is no documentation of what fields it accepts, what it returns, or what errors it throws.  
**Work required:** New reference page (~3 hours). Minimum viable: method, request schema, response schema, error codes, curl example.

---

#### MISSING-2: `PATCH /api/v1/invoices/{id}` has no reference page
**Impact:** Mentioned in the POST /api/v1/invoices notes section ("Draft invoices can be edited freely via `PATCH /api/v1/invoices/{id}`") and used in the SDK CRUD section, but with no documentation of which fields are patchable, what constraints apply, or what errors are returned.  
**Work required:** New reference page (~2.5 hours). Note: line item partial update (`line_items[].id` now accepted) is a new capability that needs documenting.

---

#### MISSING-3: `GET /api/v1/tax-rates` has no reference page
**Impact:** The POST /api/v1/invoices error table tells users "List valid tax rates via `GET /api/v1/tax-rates`" when a tax rate ID is invalid — but clicking that link goes nowhere. Users are sent on a dead-end.  
**Work required:** New reference page (~1.5 hours). Tax rates are read-only so this is a simple list+get pair.

---

#### MISSING-4: Payments resource has no documentation
**Impact:** `payment.received` webhook events include `invoice_id` and `amount`, but users have no way to look up the payment record. `GET /api/v1/payments/{id}` exists in production but is entirely undocumented.  
**Work required:** New reference page for payments resource (~2 hours). Block on confirming full field schema with engineering.

---

### Tier 3 — Needs Improvement (fix third; these mislead but don't hard-block)

---

#### IMPROVE-1: `payment_terms` vs `due_date` precedence is wrong
**Document:** `api-docs-post-invoices.md`, Fields table  
**What docs say:** "Overrides `due_date` if both are provided."  
**What changed:** `due_date` now takes precedence over `payment_terms` when both are supplied. The sentence needs reversing.  
**Fix:** One line change in the fields table. Add a note: "To use `payment_terms` exclusively, omit `due_date`."

---

#### IMPROVE-2: Rate limit stated as 100 req/min, actual limit is 200 req/min
**Documents:** `api-docs-post-invoices.md` (Errors table, `429` row); `sdk-getting-started.md` (Error Handling table)  
**Fix:** Update both occurrences: `100 requests/minute` → `200 requests/minute`. Two-line change across two files.

---

#### IMPROVE-3: `GET /api/v1/invoices` new filter parameters undocumented
**Document:** `sdk-getting-started.md`, Step 6; no standalone reference page  
**What was added:** `date_from`, `date_to` (ISO 8601 date strings), and `customer_id` filter parameters on the list endpoint.  
**Fix:** Document new filters once the GET /api/v1/invoices reference page is created (see MISSING-1). Add brief mention in SDK guide.

---

#### IMPROVE-4: SDK error class `BillingError` was renamed to `ServerError`
**Document:** `sdk-getting-started.md`, Error Handling section  
**What docs say:**
```javascript
} else if (err instanceof errors.BillingError) {  // ← doesn't exist
```
**What changed:** `errors.BillingError` was renamed to `errors.ServerError` in SDK v2.3. The class no longer exists — this catch branch is dead code.  
**Fix:** Update `BillingError` → `ServerError` in the error handling example and the error class table.

---

## 4. Update Plan

Work items ordered by user impact. Effort estimates assume a writer with API access to verify behaviour.

| # | Item | Tier | Effort | Owner | Notes |
|---|---|---|---|---|---|
| 1 | Fix webhook signature docs (header + algorithm) | Broken | 2h | Tech Writer | Verify new header name and algorithm with engineering before publishing |
| 2 | Fix pagination example in SDK guide | Broken | 1.5h | Tech Writer | Confirm offset pagination field names from actual API response |
| 3 | Fix `finalise()` async behaviour in SDK guide + lifecycle diagram | Broken | 3h | Tech Writer | Need to confirm SDK polling helper name, or document manual poll loop |
| 4 | New: POST /api/v1/customers reference page | Missing | 3h | Tech Writer | Pull schema from engineering — check if `tax_id` field is required in any region |
| 5 | New: PATCH /api/v1/invoices/{id} reference page | Missing | 2.5h | Tech Writer | Confirm line-item partial update behaviour (which fields are patchable per state) |
| 6 | New: GET /api/v1/tax-rates reference page | Missing | 1.5h | Tech Writer | Read-only resource; straightforward |
| 7 | New: GET /api/v1/payments + GET /api/v1/payments/{id} | Missing | 2h | Tech Writer | Block: need field schema from engineering |
| 8 | Fix `payment_terms` vs `due_date` precedence | Improve | 0.5h | Tech Writer | One-line fix + add clarifying note |
| 9 | Fix rate limit from 100 → 200 req/min | Improve | 0.5h | Tech Writer | Two files, two occurrences |
| 10 | Document new `GET /api/v1/invoices` filter params | Improve | 1h | Tech Writer | Fold into item 5 if GET /invoices reference page is created |
| 11 | Fix `BillingError` → `ServerError` in SDK guide | Improve | 0.5h | Tech Writer | One-line fix + table update |

**Total estimated effort: ~17.5 hours (~2.5 working days of writing, plus engineering review time)**

---

## 5. Recommended Work Order

### Sprint 1 (Day 1) — Stop the bleeding

Fix the three broken items. These are actively misleading users in production right now.

1. BROKEN-1: Webhook signature (fix header + algorithm, update Python example)
2. BROKEN-2: Pagination (replace cursor loop with offset loop)
3. BROKEN-3: Finalise async behaviour (update Step 5, Complete Script, lifecycle diagram)
4. IMPROVE-11: `BillingError` → `ServerError` (trivial, do it while the file is open)
5. IMPROVE-9: Rate limit 100 → 200 (trivial, do it while the file is open)
6. IMPROVE-8: `payment_terms` precedence (trivial, do it while the file is open)

**Deliverable:** Updated versions of `api-docs-post-invoices.md` and `sdk-getting-started.md`.

### Sprint 2 (Days 2–3) — Close the missing-docs gaps

7. MISSING-3: GET /api/v1/tax-rates (fastest, unblocked)
8. MISSING-1: POST /api/v1/customers (needed by most integrators)
9. MISSING-2: PATCH /api/v1/invoices/{id} (needed for edit flows)
10. IMPROVE-10: Document new GET /api/v1/invoices filter params (fold into invoice reference index)

**Deliverable:** Three new reference pages; update to GET /api/v1/invoices.

### Sprint 3 (Day 4, blocked on eng schema) — Payments

11. MISSING-4: Payments resource documentation

**Deliverable:** GET /api/v1/payments and GET /api/v1/payments/{id} reference pages.

---

## 6. Structural Gaps (out of scope for this sprint, flagged for roadmap)

These are gaps in documentation *structure*, not accuracy. They won't block integrations but they increase support load.

| Gap | Description |
|---|---|
| No API changelog / migration guide | Developers have no way to know what changed between versions. The webhook breaking change (BROKEN-1) would have been preventable with a published changelog entry. |
| No webhooks event catalogue | All event types, their schemas, and trigger conditions are undocumented. The SDK guide covers `payment.received` and `invoice.overdue`, but these are examples, not a complete list. |
| No error index | Errors are documented per-endpoint. A cross-reference page listing all error codes and which endpoints can return them would reduce support tickets significantly. |
| No versioning policy | Docs don't state what constitutes a breaking change, how much notice is given, or how long deprecated versions are supported. |
| GET /api/v1/account undocumented | Used in the SDK guide auth verification step but has no reference page. |
| Webhooks CRUD undocumented | GET, GET/{id}, DELETE on `/api/v1/webhooks` are implied by SDK methods but not documented. |

---

## 7. Engineering Information Needed

Before Sprint 2 and 3 can be completed, the following needs to be confirmed with engineering:

| Item | Question | Blocks |
|---|---|---|
| `POST /api/v1/invoices/{id}/finalise` | Does the SDK `finalise()` method include a built-in polling helper, or must users poll `GET /api/v1/jobs/{id}` manually? What is the job TTL? | BROKEN-3 |
| `POST /api/v1/customers` | Is `tax_id` required? Under what conditions? What is the `billing_address` schema? | MISSING-1 |
| `PATCH /api/v1/invoices/{id}` | Confirm: which fields are patchable in `draft` state vs. after finalisation. Does partial line-item update (passing `id` on existing items) work as described in the engineering notes? | MISSING-2 |
| `GET /api/v1/payments` | Full field schema for payment objects. Is there a `GET /api/v1/payments` list? What filter params does it accept? | MISSING-4 |
| Rate limits | Confirm 200 req/min is now the global limit, or whether limits vary by endpoint. | IMPROVE-9 |

---

## 8. Verification Workflow

No doc fix is publishable until it's been run against a live API. This is the gate between "written" and "shipped."

### For every Broken and Missing item

1. **Get a test API key** scoped to the staging environment (`sk_test_` prefix). Do not verify against production.
2. **Run the exact code from the doc** — copy it verbatim, no edits. If it fails, the doc is still broken.
3. **Record the actual response** (status code, response body, relevant headers). If it doesn't match what the doc says to expect, update the doc before marking it done.
4. **Test the failure paths** — trigger each documented error code deliberately (e.g. omit a required field, use a bad API key, pass an invalid `tax_rate_id`). Confirm the error shape matches the `Error Response Shape` in the doc.

### Item-specific verification steps

| Item | How to verify |
|---|---|
| BROKEN-1 (webhook signature) | Register a test endpoint, trigger a test-fire, log the raw headers. Confirm header is `x-billing-signature-v2`. Compute HMAC-SHA512 manually and compare to header value. |
| BROKEN-2 (pagination) | Call `GET /api/v1/invoices?page=1&per_page=2` against a test account with >2 invoices. Confirm response has `page`, `per_page`, `total`, `total_pages` fields and no `next_cursor` or `has_more`. |
| BROKEN-3 (finalise async) | Call `POST /api/v1/invoices/{id}/finalise`. Confirm response is `202 Accepted` with a `job_id`. Immediately call `GET /api/v1/invoices/{id}` — confirm status is `finalising`, not `finalised`. Poll until `finalised`. |
| MISSING-1 (POST /customers) | Create a customer with all optional fields, then with only required fields. Confirm response shape matches doc. Attempt duplicate `email` if unique — confirm error code. |
| MISSING-4 (payments) | Trigger a successful test payment, then call `GET /api/v1/payments/{id}`. Confirm every field in the response is documented. |
| IMPROVE-9 (rate limit 200/min) | Make 201 requests in 60 seconds. Confirm the 201st returns `429` with a `Retry-After` header. |

### Review gate before publishing

Each fixed or new doc page must be reviewed by one engineer before it goes live. Reviewer checklist:

- [ ] Code examples were executed against staging — output matches what the doc shows
- [ ] All documented error codes were triggered deliberately and match
- [ ] No internal implementation details leaked into descriptions
- [ ] Breaking-change items include a migration note

---

## 9. Decision-Ready Summary

**What changed:** Engineering confirmed ~30% of Billing API endpoints changed since last doc update. This audit identified 11 discrete issues across 2 documents: 3 broken (will fail integrations right now), 4 missing reference pages, 4 inaccuracies that mislead without hard-failing.

**User impact today:** A new integrator following the SDK getting-started guide will encounter three hard failures before they can successfully integrate: webhook receivers will reject all events, pagination loops will run forever, and `send()` after `finalise()` will throw intermittent 422s. These aren't edge cases — they're in the main happy path.

**Recommended next action:**
1. **Today:** Assign Sprint 1 (Day 1 fixes) to a writer with staging API access. All three broken fixes are independently verifiable without engineering input.
2. **This week:** Schedule a 30-minute schema review with engineering to unblock Sprint 2 (customers, patch invoices, payments field schema, rate limit confirmation).
3. **This sprint:** Add a docs-check step to the engineering release process so changelog items that touch API behaviour trigger a doc review ticket automatically.

---

*Audit methodology: reviewed `api-docs-post-invoices.md` and `sdk-getting-started.md` in full; cross-referenced all referenced endpoints against the API surface reported by engineering; verified field descriptions against reported changes. Code examples were not run against a live environment — verification steps are specified in Section 8 above and are required before any fix is published.*
