## API Documentation

Document every endpoint with:

- **Method + path** at the top (`POST /v1/orders`)
- **Description** — what it does and when to use it, not how it's implemented
- **Request parameters table** — name / type / required / description / example value
- **Request body schema** — field-by-field with types, constraints, and examples
- **Response schema** — success and error shapes, with example responses
- **Error codes** — each code, what causes it, and how to fix it
- **Working code example** — curl plus at least one SDK language

Put authentication upfront in its own section before any endpoint docs. Document rate limits, pagination, and versioning at the top of the reference, not buried in individual endpoints.

The test: a developer who has never seen this API must be able to make a successful authenticated request within 10 minutes using only your docs.
