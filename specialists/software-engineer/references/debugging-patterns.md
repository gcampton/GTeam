# Debugging Patterns Reference

Common bug archetypes and their diagnostic signatures. When a bug matches a pattern here, jump straight to the targeted fix — don't start from scratch.

---

## Off-by-One Errors

**Symptoms:** Loops that run one too many or too few times; array index out of bounds; last or first element always missing or duplicated; pagination returning wrong page.

**Causes:** `<` vs `<=`; 0-indexed vs 1-indexed confusion; slice/range end-exclusivity forgotten.

**Diagnostic:** Log the boundary values (loop counter, array index, start/end of slice) on each iteration. Does the last iteration access `array[length]` instead of `array[length-1]`?

**Fix:** Review every loop bound. Ask: "What should happen on the very first and very last iteration?" Write the test case for both.

---

## Race Conditions

**Symptoms:** Bug only appears under load or with concurrent requests; intermittent failures that can't be reproduced reliably; state corruption after multiple simultaneous operations; test flakiness that correlates with parallel test execution.

**Causes:** Shared mutable state accessed without locking; read-modify-write sequences not atomic; assuming sequential execution in async code.

**Diagnostic:** Add logging with timestamps and request IDs. Can you reproduce with two concurrent requests to the same endpoint? Is the failure rate proportional to concurrency?

**Fix:** Identify the shared resource. Use a mutex/lock, database transaction with correct isolation level, or make the state immutable. In JS/TS: avoid relying on the order of uncoordinated Promises.

---

## Async/Await Mistakes

**Symptoms:** Code runs before data is available; function returns `undefined` or an unresolved Promise; callback-style APIs mixed with async/await; `.then()` chains that don't propagate errors.

**Causes:** Missing `await`; async function called without `await` by the caller; error not caught in async context; `forEach` used instead of `for...of` for async iteration.

**Diagnostic:** Add `console.log` before and after each `await`. Does the order match expectations? Is the returned value a Promise object when you expected a value?

**Fix pattern:** Every `async` function must be `await`ed by its caller. Use `for...of` (not `forEach`) for async iteration. Wrap top-level async calls in try/catch or `.catch()`.

---

## Type Coercion Bugs (JavaScript/TypeScript)

**Symptoms:** Comparisons that should be true are false or vice versa; `0`, `""`, `null`, `undefined`, `false` treated interchangeably; numeric strings behave as numbers unexpectedly.

**Causes:** `==` instead of `===`; implicit type coercion in arithmetic; `parseInt` on non-numeric strings returning `NaN`; `NaN !== NaN`.

**Diagnostic:** `typeof` check on the values involved. Log the actual value and type: `console.log(typeof x, x)`.

**Fix:** Always use `===`. Check for `null` and `undefined` explicitly. Use `Number.isNaN()` not `isNaN()`. Parse inputs at the boundary, not deep in logic.

---

## Stale Closure

**Symptoms:** Event handler or callback sees outdated variable value; state updates in React don't reflect latest state inside a callback; loop captures the same value for all iterations.

**Causes:** Function closes over a variable at definition time; the variable later changes but the closure doesn't see it; `var` in loops vs `let`.

**Diagnostic:** Log the captured variable both inside and outside the closure. Are they different after a state change?

**Fix in React:** Use a ref (`useRef`) to hold the latest value, or use the functional updater form of `setState`. In loops: use `let` instead of `var`. In general: pass values as arguments instead of relying on closure capture.

---

## N+1 Query Problem

**Symptoms:** Page load is slow and gets dramatically worse as data grows; profiler shows hundreds of near-identical queries; ORM lazy-loading triggered in a loop.

**Causes:** Fetching a list, then fetching related data for each item individually inside the loop.

**Diagnostic:** Log or profile all SQL queries during a request. Count queries. Does the count grow linearly with the number of items returned?

**Fix:** Use eager loading (JOIN, `include`, `.populate()`). Batch the secondary queries. Use `WHERE id IN (...)` to fetch all related records in one query. Cache repeated lookups within the request lifecycle.

---

## Missing Null / Undefined Check

**Symptoms:** `TypeError: Cannot read property 'X' of null/undefined`; crash on first use with empty data; works in dev but fails in prod where data may be absent.

**Causes:** Assuming a value will always be present; API response structure changed; optional chaining not used; DB record deleted between reads.

**Diagnostic:** Which variable is null? Trace back to where it's set. Is it an API response that can legitimately be empty?

**Fix:** Use optional chaining (`?.`) and nullish coalescing (`??`). Add explicit null checks at system boundaries. Never assume a DB record still exists between read and use.

---

## Scope / Variable Shadowing

**Symptoms:** Variable has different value than expected; change to a variable doesn't seem to have effect; two variables with the same name exist in nested scopes.

**Causes:** Inner scope re-declares a variable with the same name; parameter shadows a module-level variable; destructuring creates a new binding.

**Diagnostic:** Search for all declarations of the variable name. Are there two? Which one is the code actually reading?

**Fix:** Rename one of the variables. Use linter rules (`no-shadow`) to prevent future occurrences.

---

## Memory Leaks

**Symptoms:** Application memory grows over time and never drops; Node.js heap exhausted after extended run; browser tab slows down and crashes after extended use.

**Causes:** Event listeners added but never removed; intervals/timers not cleared; closures holding references to large objects; global caches that grow without eviction; WebSocket connections not cleaned up.

**Diagnostic:** Take heap snapshots before and after an action. Compare — which objects are growing? Are there unexpected retained references?

**Fix:** Always pair `addEventListener` with `removeEventListener`. Clear intervals (`clearInterval`) in cleanup. Use `WeakMap`/`WeakRef` for caches. Implement TTL or LRU eviction on in-memory caches.

---

## Configuration / Environment Issues

**Symptoms:** Works locally but not in CI or prod; env variable is `undefined`; feature behaves differently across environments.

**Causes:** Missing env var in deployment; `.env` file not loaded; different Node/runtime version; case-sensitive filesystem issue (Linux vs macOS).

**Diagnostic:** Log the value of the suspect env var at startup. Check the deployment environment's env var configuration. Compare `node --version` across environments.

**Fix:** Validate required env vars at startup and fail fast with a clear error message if any are missing. Use a config validation library (`zod`, `joi`) for env var schemas.

---

## Flaky Tests

**Symptoms:** Tests pass sometimes and fail other times with no code change; test order matters; failures correlate with time of day or system load.

**Causes:** Shared state between tests not reset; test relies on external network call; hardcoded timestamps or random seeds; race condition in async test; file system state not cleaned up.

**Diagnostic:** Run the failing test in isolation (`--testNamePattern`). Does it fail? Then it's self-contained. Does it only fail in the full suite? Then it's state pollution from another test.

**Fix:** Reset all shared state in `beforeEach`/`afterEach`. Mock all external dependencies. Use deterministic seeds for randomness. Set explicit timeouts on async operations.
