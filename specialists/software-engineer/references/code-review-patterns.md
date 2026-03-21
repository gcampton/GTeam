# Code Review Patterns

> **Confidence:** All items are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Common patterns to catch in code review. Each entry follows: **Pattern → Why it's a problem → Example → Fix**.

---

## 1. Race Conditions

### Shared Mutable State Without Locks `[HYPOTHESIS]`

**Why it's a problem:** Two goroutines/threads reading and writing the same variable without synchronisation produce unpredictable results. The bug is often invisible under low load and surfaces in production.

**Example (Go):**
```go
var counter int

func increment() {
    counter++ // read-modify-write: not atomic
}
```

**Fix:**
```go
var mu sync.Mutex
var counter int

func increment() {
    mu.Lock()
    defer mu.Unlock()
    counter++
}
// Or use sync/atomic for simple numerics:
var counter atomic.Int64
counter.Add(1)
```

**In Node.js:** true parallelism is rare, but watch for async operations that read then write the same resource (check DB pattern below).

---

### Async TOCTOU (Time-of-Check to Time-of-Use) `[HYPOTHESIS]`

**Why it's a problem:** A check (e.g., "does this username exist?") and a write (e.g., "create user with this username") are two separate operations. Between the check and the write, another request can create the same username, violating uniqueness.

**Example:**
```js
const exists = await db.userExists(username);
if (!exists) {
  await db.createUser(username); // another request may have created it by now
}
```

**Fix:**
```js
// Use a unique constraint at the database level — it is the only reliable guard
// Catch the constraint violation error instead of pre-checking
try {
  await db.createUser(username);
} catch (err) {
  if (isUniqueViolation(err)) {
    throw new ConflictError('Username already taken');
  }
  throw err;
}
```

---

## 2. Memory Leaks

### Event Listener Cleanup `[HYPOTHESIS]`

**Why it's a problem:** Listeners added to DOM elements, event emitters, or observable streams that are never removed accumulate over the component/object lifetime, preventing garbage collection.

**Example (React):**
```js
function MyComponent() {
  useEffect(() => {
    window.addEventListener('resize', handleResize);
    // no cleanup — listener lives forever after component unmounts
  }, []);
}
```

**Fix:**
```js
useEffect(() => {
  window.addEventListener('resize', handleResize);
  return () => window.removeEventListener('resize', handleResize); // cleanup
}, []);
```

**Example (Node.js EventEmitter):**
```js
emitter.on('data', handler); // use emitter.once() or call emitter.off() later
```

---

### Circular References `[HYPOTHESIS]`

**Why it's a problem:** In environments with reference counting (Python, some JS engines in specific circumstances), A → B → A prevents deallocation. In all environments, circular structures serialised to JSON throw errors.

**Example:**
```js
const parent = { name: 'parent' };
const child = { parent };
parent.child = child; // circular: parent → child → parent
JSON.stringify(parent); // TypeError: circular structure
```

**Fix:** Use weak references where appropriate (`WeakRef`, `WeakMap`). Restructure to a tree (parent holds children; children hold parent ID, not reference). Add `toJSON()` to break the cycle for serialisation.

---

### Unclosed Connections / Handles `[HYPOTHESIS]`

**Why it's a problem:** Database connections, file handles, HTTP clients, and streams that are never closed exhaust OS-level resources (file descriptors, connection pool slots).

**Example:**
```python
def read_config():
    f = open('config.json')
    return json.load(f)
    # f.close() never called; if json.load raises, the handle leaks
```

**Fix:**
```python
def read_config():
    with open('config.json') as f:  # context manager guarantees close
        return json.load(f)
```

**In async code:** prefer `async with` / `using` / `defer` patterns. Verify DB query functions release connections back to the pool in all code paths including error paths.

---

## 3. Error Swallowing

### Bare try/catch With No Logging `[HYPOTHESIS]`

**Why it's a problem:** Errors disappear silently. The caller thinks the operation succeeded. The system moves into a corrupted state. Debugging is nearly impossible because there is no trace.

**Example:**
```js
try {
  await saveUser(user);
} catch (e) {
  // swallowed — caller receives no indication of failure
}
```

**Fix (log and rethrow):**
```js
try {
  await saveUser(user);
} catch (e) {
  logger.error('saveUser failed', { userId: user.id, error: e });
  throw e; // let caller decide how to handle
}
```

**Fix (intentional suppression — must be explicit):**
```js
try {
  await updateAnalytics(event); // failure is acceptable; user flow must not break
} catch (e) {
  logger.warn('analytics update failed, continuing', { error: e });
  // intentionally not rethrown
}
```

---

### Silently Dropping Rejected Promises `[HYPOTHESIS]`

**Why it's a problem:** An unhandled promise rejection logs a warning in Node.js < 15 and crashes the process in Node.js >= 15. A fire-and-forget call with no error handling is a hidden bomb.

**Example:**
```js
sendWelcomeEmail(user.email); // if this rejects, nobody knows
```

**Fix:**
```js
sendWelcomeEmail(user.email).catch(err =>
  logger.error('Welcome email failed', { email: user.email, err })
);
```

---

## 4. N+1 Queries

**Why it's a problem:** Fetching a list of N records then issuing one DB query per record results in N+1 total queries. Under load this can make a page that takes 50ms in development take 5 seconds in production with 100 records.

**Example:**
```js
const orders = await db.getOrders(); // 1 query
for (const order of orders) {
  order.customer = await db.getCustomer(order.customerId); // N queries
}
```

**Fix — batch load:**
```js
const orders = await db.getOrders();
const customerIds = [...new Set(orders.map(o => o.customerId))];
const customers = await db.getCustomersByIds(customerIds); // 1 query
const customerMap = Object.fromEntries(customers.map(c => [c.id, c]));
for (const order of orders) {
  order.customer = customerMap[order.customerId];
}
```

**Fix — join at query level (preferred when possible):**
```sql
SELECT orders.*, customers.name AS customer_name
FROM orders
JOIN customers ON orders.customer_id = customers.id
```

**Fix — use a DataLoader (GraphQL pattern):**
```js
const customerLoader = new DataLoader(ids => db.getCustomersByIds(ids));
// DataLoader automatically batches calls within the same event loop tick
```

**Detecting N+1 in review:** look for `await` inside a `for` loop where the awaited call takes an ID derived from a loop variable. This pattern is almost always N+1.

---

## 5. Boolean Parameter Anti-Pattern

**Why it's a problem:** `doThing(true, false, true)` at the call site is completely opaque. The reader must look up the function signature to understand what is being configured. It also makes partial configuration impossible.

**Example:**
```js
function createUser(name, isAdmin, sendEmail, requireVerification) { ... }

createUser('Alice', true, false, true); // what do these mean?
```

**Fix — use an options object:**
```js
function createUser(name, options = {}) {
  const { isAdmin = false, sendEmail = true, requireVerification = true } = options;
  ...
}

createUser('Alice', { isAdmin: true, requireVerification: true });
// self-documenting at the call site; optional fields have clear defaults
```

**Fix — use named constants for existing boolean APIs you cannot change:**
```js
const SEND_EMAIL = true;
const NO_EMAIL = false;
createUser('Alice', ADMIN, NO_EMAIL, REQUIRE_VERIFICATION);
```

---

## 6. Magic Numbers

**Why it's a problem:** A bare number in code has no semantic meaning. When it appears in multiple places, changing it requires a grep. When it appears once, the next reader has no idea what it represents or why.

**Example:**
```js
if (password.length < 8) throw new Error('Too short');
setTimeout(retry, 3000);
if (score > 0.85) return 'high confidence';
```

**Fix:**
```js
const MIN_PASSWORD_LENGTH = 8;
const RETRY_DELAY_MS = 3000;
const HIGH_CONFIDENCE_THRESHOLD = 0.85;

if (password.length < MIN_PASSWORD_LENGTH) throw new Error('Too short');
setTimeout(retry, RETRY_DELAY_MS);
if (score > HIGH_CONFIDENCE_THRESHOLD) return 'high confidence';
```

**Exceptions:** `0`, `1`, `-1` are often readable as-is in arithmetic contexts. `[HYPOTHESIS]`

---

## 7. God Functions

**Why it's a problem:** A function that does many things is hard to test (you must satisfy all its dependencies at once), hard to read (the reader must context-switch between concerns), and hard to change (a modification for one concern risks breaking another).

**Heuristics for "too large":** `[HYPOTHESIS]`
- More than ~30 lines of logic (excluding comments and blank lines)
- More than 3 distinct responsibilities
- More than 4–5 parameters
- More than 3 levels of nesting
- Hard to name without using "and" or "or"

**Example:**
```js
async function handleCheckout(req, res) {
  // validate cart (10 lines)
  // calculate discounts (15 lines)
  // charge payment (20 lines)
  // update inventory (10 lines)
  // send confirmation email (10 lines)
  // log audit event (5 lines)
}
```

**Fix — extract into focused functions:**
```js
async function handleCheckout(req, res) {
  const cart = await validateCart(req.body.cartId, req.user.id);
  const price = calculatePrice(cart, req.user.discounts);
  const payment = await chargePayment(req.user.paymentMethodId, price);
  await Promise.all([
    updateInventory(cart),
    sendConfirmationEmail(req.user.email, cart, payment),
    logAuditEvent('checkout', { userId: req.user.id, paymentId: payment.id }),
  ]);
  res.json({ success: true, orderId: payment.orderId });
}
```

Each extracted function can be tested independently.

---

## Quick-Reference Table

| Pattern | Signal in diff | Severity |
|---------|---------------|----------|
| Shared mutable state without lock | `counter++` in concurrent code, no mutex/atomic | High |
| Async TOCTOU | `await exists()` then `await create()` | High |
| Unclosed connection | `open(...)` without `with`, DB query without close | Medium |
| Event listener leak | `addEventListener` without matching `removeEventListener` | Medium |
| Error swallowing | Empty `catch` block | High |
| Unhandled promise | Async call with no `.catch()` and no `await` | Medium |
| N+1 query | `await db.query(item.id)` inside `for` loop | High |
| Boolean param | Function call with multiple consecutive booleans | Low |
| Magic number | Bare numeric literal in logic | Low |
| God function | Function > 30 lines with multiple concerns | Medium |
