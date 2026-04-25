## Scrape from API

**Use when:** User provides an API to document (REST, GraphQL, OpenAPI spec).

**Step 1 — Check Skill-Seekers API first:**
```bash
curl -s "https://api.skillseekersweb.com/api/configs?tag=<api-name>" | python3 -m json.tool
```

**Step 2 — Check for OpenAPI/Swagger spec:**
```bash
curl -s "https://<domain>/openapi.json" | python3 -m json.tool | head -100
curl -s "https://<domain>/swagger.json" | python3 -m json.tool | head -100
curl -s "https://<domain>/api-docs" | head -100
```
If found, download and parse into reference markdown:
```bash
curl -s "https://<domain>/openapi.json" -o /tmp/<name>-openapi.json
```
Extract: base URL, auth method, all endpoints (method + path + description + params + response schema), rate limits, error codes.

**Step 3 — If no spec:** Use WebFetch to scrape the API reference docs using the URL workflow above.

**Step 4 — For JSON/data dumps provided by the user:** Read the file, extract structure, summarize schemas, document all fields and types.
