# Testing Strategy Reference

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Use as a reference when designing a test suite, reviewing PRs, or deciding what to write next.

---

## The Testing Pyramid `[HYPOTHESIS]`

```
         /\
        /E2E\         ~10%  — full user journeys, slow, brittle
       /------\
      /  Integ  \     ~20%  — service boundaries, DB, external calls
     /------------\
    /     Unit      \  ~70%  — pure logic, fast, isolated
   /________________\
```

| Layer | What belongs here | What does NOT belong here |
|-------|-------------------|--------------------------|
| **Unit** | Pure functions, business logic, data transformations, edge cases, error paths | Database queries, HTTP calls, file I/O |
| **Integration** | Repository + real DB, HTTP handler + middleware stack, message queue consumer | Full browser rendering, multi-service flows |
| **E2E** | Critical user journeys (sign up → pay → confirm), smoke tests post-deploy | Every edge case, form validation details |

**Pyramid inversion is a smell.** If you have more E2E tests than unit tests, maintenance cost is high and feedback is slow. `[HYPOTHESIS]`

---

## What to Always Test

### Happy Path
- The primary success case with valid, typical input
- Confirms the feature works at all — don't skip it in favour of only testing edge cases

### Empty / Null Input `[HYPOTHESIS]`
- Empty string `""`
- `null` / `undefined` / `None`
- Empty array `[]`, empty object `{}`
- Zero `0` (often treated as falsy unintentionally)

### Boundary Values `[HYPOTHESIS]`
- One below minimum, minimum, maximum, one above maximum
- For strings: empty, 1 char, max-length, max-length + 1
- For dates: epoch, today, far future, leap day (Feb 29)
- For numeric IDs: `0`, `1`, `MAX_INT`, negative

### Error States
- Invalid input returns the correct error code/message — not a 500
- Downstream service unavailable: does the caller handle it gracefully?
- Partial failure in a batch operation: what is rolled back?

### Concurrent Access `[HYPOTHESIS]`
- Shared mutable state: does a race condition produce incorrect results?
- Idempotency: calling the same write operation twice does not double-apply

---

## Common Testing Anti-Patterns

### Testing Implementation, Not Behaviour `[HYPOTHESIS]`
**Problem:** Test breaks when you refactor internals, even if behaviour is unchanged. Creates false confidence and discourages refactoring.

```js
// Bad — tests private method names
expect(service._buildQueryString).toHaveBeenCalledWith(...)

// Good — tests observable output
expect(await service.search('term')).toEqual([{ id: 1, title: 'Result' }])
```

---

### Testing Third-Party Code `[HYPOTHESIS]`
**Problem:** You are testing the library, not your code. These tests break on library upgrades for no good reason.

```python
# Bad — testing that requests.get works
def test_requests_returns_200():
    r = requests.get('https://example.com')
    assert r.status_code == 200

# Good — test your own wrapper's behaviour
def test_fetch_user_returns_parsed_model():
    mock_http.get.return_value = Response(200, '{"id": 1}')
    user = fetch_user(1)
    assert user.id == 1
```

---

### Mocking Everything `[HYPOTHESIS]`
**Problem:** A test where every dependency is a mock tests only that you can write mocks. It provides no confidence that the real system works.

- Unit tests: mock I/O boundaries (DB, HTTP, clock, filesystem) — not domain logic
- Integration tests: use real infrastructure (test DB, local service) — mock only external third parties
- Never mock the thing you are testing

---

### Assertion-Free Tests
**Problem:** A test that never asserts anything always passes — it is a false green.

```js
// Bad
it('processes the order', async () => {
  await processOrder(order); // no expect()
});

// Good
it('marks order as completed', async () => {
  await processOrder(order);
  expect(order.status).toBe('completed');
});
```

---

### Single Assertion Dogma `[HYPOTHESIS]`
**Problem:** "One assertion per test" is a heuristic, not a rule. Multiple related assertions about one behaviour belong together. Splitting them creates artificially long test files.

Group assertions by **behaviour**, not by assertion count.

---

## TDD: Red / Green / Refactor

```
Red    → write a failing test for the behaviour you want
Green  → write the minimum code to make it pass (no more)
Refactor → clean up code and tests; all tests still pass
```

### When TDD helps `[HYPOTHESIS]`
- Unclear or complex business logic — writing the test first forces you to define the contract
- Bug fixes — write a failing test that reproduces the bug first; commit it; then fix
- Public API design — test-first surfaces awkward interfaces before you build them

### When TDD is overkill `[HYPOTHESIS]`
- Exploratory / spike code that will be thrown away
- UI layout and visual design work
- Glue code with no logic (thin wrappers around well-tested libraries)
- When you genuinely do not know the shape of the output yet

---

## Coverage Guidance

| Path type | Target | Rationale |
|-----------|--------|-----------|
| Overall line coverage | ≥ 80% | `[HYPOTHESIS]` — floor, not goal |
| Auth / session logic | 100% | `[HYPOTHESIS]` — no untested security path |
| Payment / billing logic | 100% | `[HYPOTHESIS]` — financial correctness |
| Data mutation (write ops) | 100% | `[HYPOTHESIS]` — data loss is hard to recover |
| Error handling branches | ≥ 90% | `[HYPOTHESIS]` |
| UI rendering | ≥ 60% | `[HYPOTHESIS]` — diminishing returns above this |

**Coverage is a floor, not a score to optimise.** 100% coverage with weak assertions is worse than 80% coverage with strong assertions. `[HYPOTHESIS]`

### What coverage does not catch
- Missing test cases (it cannot tell you what you forgot to test)
- Incorrect assertions
- Race conditions
- Integration with real external systems

---

## Language-Specific Notes

### JavaScript / TypeScript — Jest or Vitest `[HYPOTHESIS]`

```js
// Prefer describe/it blocks over flat test()
describe('UserService', () => {
  describe('getUser', () => {
    it('returns user by id', async () => { ... });
    it('throws NotFoundError when id does not exist', async () => { ... });
  });
});

// Use beforeEach to reset mocks — not beforeAll (state leaks between tests)
beforeEach(() => jest.clearAllMocks());

// Snapshot tests are useful for component output, fragile for business logic
// Avoid snapshots for anything that changes frequently
```

Key flags: `--coverage --collectCoverageFrom='src/**/*.{ts,tsx}'`

Vitest is preferred over Jest for new Vite/ESM projects — same API, faster, native ESM. `[HYPOTHESIS]`

---

### Python — pytest `[HYPOTHESIS]`

```python
# Use fixtures for setup/teardown over setUp/tearDown classes
@pytest.fixture
def user(db_session):
    return User.create(db_session, email="test@example.com")

# Parametrize for boundary values
@pytest.mark.parametrize("value,expected", [
    ("", ValueError),
    ("valid", None),
    ("a" * 256, ValueError),
])
def test_validate_input(value, expected):
    if expected:
        with pytest.raises(expected):
            validate(value)
    else:
        assert validate(value) is not None

# Use pytest-cov for coverage: pytest --cov=src --cov-report=term-missing
```

Avoid `unittest.TestCase` in new code unless inheriting from a framework that requires it. `[HYPOTHESIS]`

---

### Go — `testing` package `[HYPOTHESIS]`

```go
// Table-driven tests are idiomatic
func TestAdd(t *testing.T) {
    cases := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive", 1, 2, 3},
        {"zero", 0, 0, 0},
        {"negative", -1, -1, -2},
    }
    for _, tc := range cases {
        t.Run(tc.name, func(t *testing.T) {
            got := Add(tc.a, tc.b)
            if got != tc.expected {
                t.Errorf("Add(%d,%d) = %d; want %d", tc.a, tc.b, got, tc.expected)
            }
        })
    }
}
```

Use `t.Parallel()` in unit tests to catch race conditions. Run with `-race` flag in CI. `[HYPOTHESIS]`

Coverage: `go test ./... -coverprofile=coverage.out && go tool cover -func=coverage.out`

---

### Java — JUnit 5 `[HYPOTHESIS]`

```java
@ExtendWith(MockitoExtension.class)
class OrderServiceTest {

    @Mock
    private OrderRepository repo;

    @InjectMocks
    private OrderService service;

    @Test
    @DisplayName("should mark order as completed when payment succeeds")
    void completeOrder_success() {
        var order = new Order(1L, Status.PENDING);
        when(repo.findById(1L)).thenReturn(Optional.of(order));

        service.complete(1L);

        assertThat(order.getStatus()).isEqualTo(Status.COMPLETED);
        verify(repo).save(order);
    }

    @ParameterizedTest
    @NullAndEmptySource
    void validate_rejectsBlankInput(String input) {
        assertThrows(IllegalArgumentException.class, () -> service.validate(input));
    }
}
```

Prefer AssertJ over raw JUnit assertions for readability. Use `@DisplayName` for human-readable test names. `[HYPOTHESIS]`

---

## Quick-Reference: Test Smell → Fix

| Smell | Fix |
|-------|-----|
| Test only passes in isolation (order-dependent) | Remove shared mutable state between tests |
| Test is slow (> 1s for a unit test) | Replace real I/O with a mock/fake |
| Test always passes (never fails) | Check assertions exist and are correct |
| Test breaks on refactor with no behaviour change | Test the output/interface, not internals |
| Test is hard to read | Extract setup to fixture/helper, name it clearly |
| Flaky test | Find the non-determinism — clock, network, random, ordering |
