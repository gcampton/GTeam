## Kubernetes & Containerisation

**Dockerfile best practices:**
1. **Multi-stage builds** — build in a full SDK image, copy only artefacts to a minimal runtime image (`alpine`, `distroless`)
2. **Minimal base images** — prefer `node:20-alpine` over `node:20`; prefer `gcr.io/distroless/static` for Go binaries
3. **Non-root user** — add `RUN addgroup -S app && adduser -S app -G app` then `USER app` before `CMD`
4. **`.dockerignore`** — exclude `node_modules`, `.git`, `*.md`, test fixtures, local env files
5. **Pin versions** — pin base image to digest or specific patch version, not `:latest`
6. **Layer ordering** — copy dependency manifests first, install, then copy source (maximise cache hits)

**K8s manifest patterns:**

| Resource | Purpose | Key fields |
|----------|---------|------------|
| Deployment | Stateless workload with rolling updates | `replicas`, `strategy`, `resources`, probes |
| Service | Stable network endpoint for pods | `selector`, `port`, `targetPort` |
| Ingress | External HTTP routing + TLS termination | `host`, `path`, `tls` |
| ConfigMap | Non-sensitive config (env vars, config files) | Mount as env or volume |
| Secret | Sensitive config (credentials, tokens) | Base64-encoded; use external secrets operator in prod |
| HPA | Auto-scale pods on metrics | `minReplicas`, `maxReplicas`, `targetCPUUtilizationPercentage` |

**Helm vs raw manifests:**
- **Raw manifests** — < 5 resources, single environment, team understands K8s YAML
- **Helm** — multiple environments (dev/staging/prod), need templated values, want rollback via `helm rollback`
- **Kustomize** — middle ground: overlays per environment, no template language

**Pod resource sizing:**
- `requests` = observed P95 usage (guarantees scheduling)
- `limits` = 2x requests (prevents noisy-neighbour; allows burst)
- Review monthly — over-provisioning wastes cost, under-provisioning causes OOM kills

**Probe design:**

| Probe | Purpose | What to check | What NOT to check |
|-------|---------|---------------|-------------------|
| **Readiness** | Can this pod serve traffic? | App + dependencies (DB, cache) | External third-party APIs |
| **Liveness** | Is the process healthy? | Process is alive, not deadlocked | Dependencies (causes cascading restarts) |
| **Startup** | Has the app finished booting? | App responds to health endpoint | Use for slow-starting apps only |
