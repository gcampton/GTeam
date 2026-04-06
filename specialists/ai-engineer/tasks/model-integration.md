### Model Selection

**Decision tree — start with task type, then narrow:**

| Task Type | Model Family | When to Use | Cost Tier |
|---|---|---|---|
| Complex reasoning, analysis, code | Claude Opus/Sonnet, GPT-4o | Tasks requiring deep understanding, multi-step reasoning, long context | High |
| Fast text generation, chat | Claude Haiku, GPT-4o-mini, Gemini Flash | High-volume, latency-sensitive, simpler tasks | Low |
| Open-source text generation | Llama 3, Mistral, Qwen | Self-hosted, data sovereignty, fine-tuning needed | Variable |
| Text embeddings | text-embedding-3-small/large, Cohere Embed v3 | Semantic search, RAG, clustering | Low |
| Open-source embeddings | sentence-transformers, nomic-embed | Self-hosted embeddings, offline use | Free (compute) |
| Classification | Fine-tuned model OR few-shot with LLM | Few-shot first; fine-tune only with 500+ labelled examples | Variable |
| Image generation | DALL-E 3, Flux, Stable Diffusion 3 | Creative assets, prototyping, product images | Medium-High |
| Speech-to-text | Whisper (OpenAI or open-source) | Transcription, voice commands | Low-Medium |
| Text-to-speech | ElevenLabs, OpenAI TTS | Voice interfaces, narration, accessibility | Medium |

**Selection criteria (in priority order):**
1. **Quality** — does it meet the accuracy bar for this use case?
2. **Latency** — can it respond within the UX requirement? (chat < 2s TTFT, batch can be minutes)
3. **Cost** — what's the cost per 1K requests at expected volume?
4. **Data privacy** — does data leave your infrastructure? Is that acceptable?
5. **Vendor lock-in** — how hard is it to switch models later?

**Rule: always prototype with 2+ models before committing.** Model quality varies by task. A 5-minute comparison saves months of regret.

---

### API Integration Patterns

**Streaming vs batch:**
- Streaming: use for chat/interactive UX. Implement SSE or WebSocket forwarding. Handle partial JSON in streamed tool calls.
- Batch: use for background processing, bulk classification, data enrichment. Queue-based with retry.

**Retry logic (mandatory):**
```
- 429 (rate limit): exponential backoff starting at 1s, max 60s, with jitter
- 500/502/503: retry up to 3 times with 2s delay
- 400 (bad request): do NOT retry — fix the request
- Timeout: set per-model (Claude 120s, GPT 60s default), retry once
```

**Rate limiting:**
- Track tokens-per-minute and requests-per-minute against provider limits
- Implement a token bucket or leaky bucket client-side
- For burst traffic: queue requests, don't drop them

**Client architecture:**
- Abstract the model provider behind an interface — never call provider SDKs directly from business logic
- Factory pattern: `getModel(task, priority)` returns the right client
- All model calls go through a single gateway that handles auth, retry, logging, and cost tracking

---

### Error Handling & Fallbacks

**Model degradation strategy (design this before building):**

| Failure Mode | Detection | Fallback |
|---|---|---|
| API timeout | Response exceeds timeout threshold | Retry once, then return cached/default response |
| Rate limit exceeded | 429 response | Queue and retry with backoff; serve stale cache if available |
| Content filter triggered | Refusal response or empty output | Log for review; return safe default message |
| Malformed output | JSON parse failure, schema validation error | Retry with stricter prompt; fall back to regex extraction |
| Quality degradation | Eval score drops below threshold | Alert; route to backup model; flag for human review |
| Provider outage | Consecutive failures > threshold | Switch to backup provider automatically |

**Never let a model failure crash the application.** Every model call must have a `try/catch` with a meaningful fallback.

---

### Cost Optimisation

**Prompt caching:** Use provider caching features (Claude prompt caching, GPT cached prompts) for repeated system prompts. Can reduce costs 50-90% for high-volume use cases.

**Model routing (tiered approach):**
1. Route to cheapest model first (Haiku, GPT-4o-mini)
2. If confidence is low or task is complex, escalate to expensive model (Opus, GPT-4o)
3. Implement a classifier or heuristic to decide routing — don't send everything to the big model

**Token budgeting:**
- Set max_tokens per request type (chat response: 1024, analysis: 4096, summary: 512)
- Track daily/monthly spend with alerts at 50%, 80%, 100% of budget
- Log cost per request in your observability stack

**Embedding cost reduction:**
- Cache embeddings — never re-embed the same content
- Use dimensionality reduction (Matryoshka embeddings) for lower storage cost
- Batch embedding requests (most APIs support batch of 100+)
