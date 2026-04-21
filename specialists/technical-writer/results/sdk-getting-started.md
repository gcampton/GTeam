# Getting Started with the Billing SDK

**Time to first API call: ~10 minutes.**

You'll install the SDK, authenticate, create a customer and invoice (CRUD), and set up a webhook to receive payment events — all against the test environment, so nothing real is charged.

---

## What You'll Build

By the end of this guide you'll have a script that:

1. Creates a customer
2. Creates a draft invoice for that customer with two line items
3. Finalises and sends the invoice
4. Receives a `payment.received` webhook event and logs the payload

---

## Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Node.js | 18+ | `node --version` to check |
| npm or bun | any | Examples use npm |
| A Billing account | — | [Sign up free](https://app.example.com/signup) — no credit card needed |

If you're on Python, skip to the [Python quickstart](#python-quickstart). TypeScript users: the Node.js SDK ships with full type definitions — no separate `@types` package needed.

---

## Step 1 — Install the SDK

```bash
npm install @example/billing-sdk
```

Verify the install:

```bash
node -e "const { BillingClient } = require('@example/billing-sdk'); console.log('OK');"
# OK
```

---

## Step 2 — Get Your API Keys

1. Open the [API Keys page](https://app.example.com/settings/api-keys)
2. Click **Generate test key**
3. Copy the key — it starts with `sk_test_`

> **Test vs. live keys**  
> `sk_test_` keys hit the sandbox. No real money moves. `sk_live_` keys hit production. This guide uses test keys throughout. Never commit either key to source control — use environment variables.

Store your key:

```bash
export BILLING_API_KEY=sk_test_your_key_here
```

---

## Step 3 — Authenticate

Create `index.js`:

```javascript
const { BillingClient } = require("@example/billing-sdk");

const client = new BillingClient({
  apiKey: process.env.BILLING_API_KEY,
});

async function main() {
  const account = await client.account.get();
  console.log(`Authenticated as: ${account.name} (${account.id})`);
}

main().catch(console.error);
```

Run it:

```bash
node index.js
# Authenticated as: Acme Corp (acc_abc123)
```

If you see `AuthenticationError: Invalid API key`, double-check that:
- The environment variable is set in the same shell session (`echo $BILLING_API_KEY`)
- The key starts with `sk_test_` (not `sk_live_`)

---

## Step 4 — Create a Customer

```javascript
const customer = await client.customers.create({
  name: "Jane Smith",
  email: "jane@example.com",
  currency: "AUD",
});

console.log(`Customer created: ${customer.id}`);
// Customer created: cus_xyz789
```

**What just happened:** The SDK sent `POST /api/v1/customers` with your payload and returned the created customer object. `customer.id` is what you'll pass to invoice creation.

---

## Step 5 — Create and Send an Invoice

This is a two-step process: create a draft, then finalise and send it.

```javascript
// Create draft invoice
const invoice = await client.invoices.create({
  customer_id: customer.id,
  currency: "AUD",
  due_date: "2026-05-15",
  line_items: [
    {
      description: "Web development — April 2026",
      quantity: 40,
      unit_price: 15000,       // $150.00 AUD (always in cents)
      tax_rate_id: "txr_gst_10",
    },
    {
      description: "Hosting (monthly)",
      quantity: 1,
      unit_price: 4900,        // $49.00 AUD
    },
  ],
  notes: "Payment due within 30 days.",
});

console.log(`Invoice created: ${invoice.id} — status: ${invoice.status}`);
// Invoice created: inv_def456 — status: draft

// Finalise then send
await client.invoices.finalise(invoice.id);
await client.invoices.send(invoice.id);

console.log("Invoice sent.");
```

> **Monetary values are always integers (cents).** `15000` = $150.00 AUD. See [Working with money](#working-with-money) if this is unfamiliar.

Expected output:

```
Invoice created: inv_def456 — status: draft
Invoice sent.
```

---

## Step 6 — CRUD Operations

The SDK exposes the standard five operations on every resource. Here's the pattern for invoices — customers, tax rates, and other resources follow the same shape:

```javascript
// Create
const invoice = await client.invoices.create({ ... });

// Read one
const fetched = await client.invoices.get("inv_def456");
console.log(fetched.status); // "sent"

// List (paginated)
const page = await client.invoices.list({ status: "draft", limit: 20 });
for (const inv of page.data) {
  console.log(`${inv.id} — ${inv.invoice_number} — $${inv.total / 100}`);
}

// Update (draft invoices only)
const updated = await client.invoices.update("inv_def456", {
  notes: "Please pay by EFT.",
});

// Delete (draft invoices only — production delete is void)
await client.invoices.void("inv_def456");
```

### Pagination

All list endpoints are cursor-paginated. Use `page.has_more` and `page.next_cursor` to walk pages:

```javascript
let cursor;
do {
  const page = await client.invoices.list({ limit: 50, cursor });
  for (const inv of page.data) {
    process(inv);
  }
  cursor = page.next_cursor;
} while (page.has_more);
```

---

## Step 7 — Set Up Webhooks

Webhooks let the platform push events to your server instead of you polling. You need a publicly reachable URL — use [ngrok](https://ngrok.com/) or [smee.io](https://smee.io) to expose localhost during development.

### 7a — Start a local receiver

Create `webhook-server.js`:

```javascript
const http = require("http");
const { BillingClient } = require("@example/billing-sdk");

const client = new BillingClient({ apiKey: process.env.BILLING_API_KEY });
const WEBHOOK_SECRET = process.env.BILLING_WEBHOOK_SECRET;

const server = http.createServer(async (req, res) => {
  if (req.method !== "POST" || req.url !== "/webhooks") {
    res.writeHead(404);
    res.end();
    return;
  }

  // Collect raw body (signature validation requires raw bytes)
  const chunks = [];
  for await (const chunk of req) chunks.push(chunk);
  const rawBody = Buffer.concat(chunks);

  // Validate the signature — reject anything that fails
  let event;
  try {
    event = client.webhooks.constructEvent(
      rawBody,
      req.headers["x-billing-signature"],
      WEBHOOK_SECRET
    );
  } catch (err) {
    console.error("Webhook signature invalid:", err.message);
    res.writeHead(400);
    res.end("Bad signature");
    return;
  }

  // Handle the event
  console.log(`Event received: ${event.type}`);
  console.log(JSON.stringify(event.data, null, 2));

  switch (event.type) {
    case "payment.received":
      const { invoice_id, amount, currency } = event.data;
      console.log(`Payment of ${amount / 100} ${currency} received for ${invoice_id}`);
      break;
    case "invoice.overdue":
      console.log(`Invoice ${event.data.invoice_id} is overdue`);
      break;
    default:
      console.log(`Unhandled event type: ${event.type}`);
  }

  // Always respond 200 quickly — processing can happen async
  res.writeHead(200);
  res.end("OK");
});

server.listen(3000, () => console.log("Webhook server listening on :3000"));
```

### 7b — Expose it publicly

```bash
# In a second terminal:
npx ngrok http 3000
# → Forwarding: https://abc123.ngrok.io -> http://localhost:3000
```

### 7c — Register the endpoint

```javascript
const endpoint = await client.webhooks.create({
  url: "https://abc123.ngrok.io/webhooks",
  events: ["payment.received", "invoice.overdue", "invoice.finalised"],
});

console.log(`Webhook secret: ${endpoint.secret}`);
// Save this — you won't see it again
```

Store the secret:

```bash
export BILLING_WEBHOOK_SECRET=whsec_...
```

### 7d — Trigger a test event

```bash
node webhook-server.js &
# Then in a second terminal:
```

```javascript
await client.webhooks.trigger(endpoint.id, "payment.received");
```

Your webhook server prints:

```
Event received: payment.received
{
  "invoice_id": "inv_test_abc",
  "amount": 664900,
  "currency": "AUD"
}
Payment of 6649.00 AUD received for inv_test_abc
```

> **Always validate the signature.** Calling `constructEvent` with the raw body and the `x-billing-signature` header verifies the payload came from the platform and wasn't tampered with. Skipping this check opens you to spoofed events.

---

## Complete Script

Putting it all together — save as `quickstart.js` and run with `node quickstart.js`:

```javascript
const { BillingClient } = require("@example/billing-sdk");

const client = new BillingClient({
  apiKey: process.env.BILLING_API_KEY,
});

async function main() {
  // Verify auth
  const account = await client.account.get();
  console.log(`Authenticated as: ${account.name}`);

  // Create customer
  const customer = await client.customers.create({
    name: "Jane Smith",
    email: "jane@example.com",
    currency: "AUD",
  });
  console.log(`Customer: ${customer.id}`);

  // Create invoice
  const invoice = await client.invoices.create({
    customer_id: customer.id,
    currency: "AUD",
    due_date: "2026-05-15",
    line_items: [
      { description: "Web development — April 2026", quantity: 40, unit_price: 15000 },
      { description: "Hosting (monthly)", quantity: 1, unit_price: 4900 },
    ],
  });
  console.log(`Invoice ${invoice.invoice_number} created (${invoice.status})`);

  // Send it
  await client.invoices.finalise(invoice.id);
  await client.invoices.send(invoice.id);
  console.log("Invoice sent.");

  // List all sent invoices
  const { data: sent } = await client.invoices.list({ status: "sent" });
  console.log(`Sent invoices: ${sent.length}`);
}

main().catch(console.error);
```

Expected output:

```
Authenticated as: Acme Corp
Customer: cus_xyz789
Invoice INV-2026-0088 created (draft)
Invoice sent.
Sent invoices: 1
```

---

## Python Quickstart

```bash
pip install billing-sdk
```

```python
import os
from billing_sdk import BillingClient

client = BillingClient(api_key=os.environ["BILLING_API_KEY"])

# Auth check
account = client.account.get()
print(f"Authenticated as: {account.name}")

# Create customer
customer = client.customers.create(
    name="Jane Smith",
    email="jane@example.com",
    currency="AUD",
)

# Create and send invoice
invoice = client.invoices.create(
    customer_id=customer.id,
    currency="AUD",
    due_date="2026-05-15",
    line_items=[
        {"description": "Web development — April 2026", "quantity": 40, "unit_price": 15000},
        {"description": "Hosting (monthly)", "quantity": 1, "unit_price": 4900},
    ],
)
client.invoices.finalise(invoice.id)
client.invoices.send(invoice.id)
print(f"Invoice {invoice.invoice_number} sent")
```

Webhook validation in Python:

```python
import hmac, hashlib

def validate_signature(raw_body: bytes, signature_header: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature_header)
```

---

## Working with Money

All monetary values in the API are integers representing the **smallest currency unit** — cents for AUD/USD/EUR, pence for GBP. This avoids floating-point rounding errors.

| You want | Pass | Display |
|---|---|---|
| $150.00 AUD | `15000` | `(15000 / 100).toFixed(2)` → `"150.00"` |
| $0.99 USD | `99` | `(99 / 100).toFixed(2)` → `"0.99"` |

Never pass decimals. `150.00` will return a `400 invalid_request` error.

---

## Error Handling

The SDK throws typed errors — catch the specific type you care about:

```javascript
const { BillingClient, errors } = require("@example/billing-sdk");

try {
  await client.invoices.create({ ... });
} catch (err) {
  if (err instanceof errors.AuthenticationError) {
    console.error("Check your API key");
  } else if (err instanceof errors.ValidationError) {
    // Field-level details
    for (const e of err.errors) {
      console.error(`${e.field}: ${e.message}`);
    }
  } else if (err instanceof errors.RateLimitError) {
    const retryAfter = err.retryAfter; // seconds
    console.error(`Rate limited — retry after ${retryAfter}s`);
  } else {
    throw err; // unexpected — let it bubble
  }
}
```

| Error class | HTTP status | When |
|---|---|---|
| `AuthenticationError` | 401 | Invalid or missing API key |
| `ValidationError` | 400 | Request body failed validation |
| `NotFoundError` | 404 | Resource ID doesn't exist |
| `RateLimitError` | 429 | Exceeded 100 requests/minute |
| `BillingError` | 5xx | Platform error — safe to retry with backoff |

---

## Next Steps

| I want to… | Read… |
|---|---|
| Understand every invoice field | [POST /api/v1/invoices reference](./api-docs-post-invoices.md) |
| Handle all webhook event types | [Webhook Events Reference](#) |
| Apply tax rates and discounts | [Tax & Discounts Guide](#) |
| Go to production | [Production Checklist](#) |
| Use the REST API directly (no SDK) | [API Reference](#) |

---

## Troubleshooting

**`AuthenticationError: Invalid API key`**  
The key isn't being read. Run `echo $BILLING_API_KEY` in the same terminal. If empty, re-export it. Check the key prefix — test keys start `sk_test_`, live keys start `sk_live_`.

**`ValidationError: line_items[0].unit_price must be an integer`**  
You passed a decimal (`150.00`). Pass cents: `15000`.

**`NotFoundError: customer not found`**  
The `customer_id` doesn't exist in your account. List customers with `client.customers.list()` to confirm the ID.

**Webhook signature invalid**  
You're likely reading the body as a string rather than raw bytes. The signature is computed over the raw bytes — any encoding change (e.g. JSON re-serialisation) breaks it. Pass the raw `Buffer` (Node.js) or `bytes` (Python) to `constructEvent`.

**Webhook server not receiving events**  
Check your ngrok tunnel is still open (`ngrok` sessions expire after 2 hours on the free plan). Re-register the endpoint with the new URL if the tunnel restarts.
