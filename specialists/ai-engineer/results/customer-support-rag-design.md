# RAG System Design: Customer Support Chatbot

**Date:** 2026-04-06
**Specialist:** AI Engineer
**Status:** Design Complete

---

## 1. Requirements Summary

| Requirement | Value |
|---|---|
| Corpus size | ~500 Markdown help articles |
| Update frequency | Weekly |
| Response latency target | < 3 seconds end-to-end |
| Citation requirement | Every answer must cite source article(s) |
| Query types | Factual lookup, how-to, troubleshooting |
| Quality bar | Must be correct — customer-facing, not best-effort |

---

## 2. Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                        INGESTION PIPELINE (weekly)                   │
│                                                                      │
│  Markdown    ──►  Parse &     ──►  Chunk by    ──►  Embed    ──►  Upsert   │
│  articles        extract          section          (3-small)     to DB     │
│                  metadata         + overlap                               │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                        QUERY PIPELINE (per request)                   │
│                                                                      │
│  User     ──►  Query      ──►  Hybrid     ──►  Re-rank  ──►  Assemble  │
│  question      embedding       retrieval       (top 5)      context    │
│                                (top 20)                               │
│                                                         ──►  Generate  │
│                                                              + cite    │
└──────────────────────────────────────────────────────────────────────┘
```

**Latency budget breakdown (< 3s total):**

| Stage | Budget | Notes |
|---|---|---|
| Query embedding | ~50ms | Single API call |
| Hybrid retrieval (top 20) | ~100ms | Vector + BM25, pgvector handles 500 articles trivially |
| Re-ranking (20 → 5) | ~200ms | Cohere Rerank API or local cross-encoder |
| Context assembly | ~10ms | Local string ops |
| LLM generation | ~1500ms | Streaming, Claude Haiku or GPT-4o-mini |
| Network overhead | ~200ms | Two external API round-trips |
| **Total** | **~2060ms** | **~940ms headroom** |

---

## 3. Ingestion Pipeline

### 3.1 Document Preprocessing

```
For each Markdown file:
  1. Extract frontmatter metadata (title, category, last_updated, URL slug)
  2. Preserve heading hierarchy (H1 → H4) as section path
  3. Preserve lists, tables, code blocks — they carry procedural meaning
  4. Strip navigation chrome, sidebars, footer boilerplate
  5. Compute content hash (SHA-256) for change detection
```

### 3.2 Chunking Strategy: Document-Structure with Overlap

**Why document-structure:** Help articles are already well-structured with headings and sections. Splitting by section preserves semantic coherence naturally — a "Billing FAQ" section stays together rather than being arbitrarily cut at 400 tokens.

| Parameter | Value | Rationale |
|---|---|---|
| Strategy | Document-structure (by heading) | Articles are Markdown with clear heading hierarchy |
| Target chunk size | 200–500 tokens | Sweet spot for retrieval precision without losing context |
| Overlap | 50 tokens (~15%) | Covers information at section boundaries |
| Minimum chunk size | 80 tokens | Sections shorter than this merge into the parent |
| Maximum chunk size | 600 tokens | Sections longer than this split recursively by paragraph |

**Each chunk stores:**
```json
{
  "chunk_id": "billing-faq-003",
  "text": "## How do I update my payment method?\n\nGo to Settings → Billing → ...",
  "metadata": {
    "article_id": "billing-faq",
    "article_title": "Billing FAQ",
    "section_path": "Billing FAQ > Payment Methods",
    "category": "billing",
    "source_url": "/help/billing-faq#payment-methods",
    "last_updated": "2026-03-30",
    "content_hash": "a1b2c3..."
  }
}
```

### 3.3 Embedding Model

**Choice: `text-embedding-3-small` (OpenAI)**

| Factor | Value |
|---|---|
| Dimensions | 1536 (or reduce to 512 with Matryoshka for faster search) |
| Cost | ~$0.02 per 1M tokens |
| Corpus cost estimate | 500 articles × ~800 tokens avg = 400K tokens → **$0.008 per full re-index** |
| Quality | Strong for English help content; overkill for this corpus size |

At 500 articles producing ~2,000 chunks, even a full weekly re-index costs under $0.01. Use `text-embedding-3-small` — no need to optimise embedding costs at this scale.

### 3.4 Vector Database

**Choice: pgvector (PostgreSQL extension)**

**Rationale:**
- ~2,000 vectors is trivial — pgvector handles up to 1M comfortably
- No new infrastructure if the application already uses Postgres
- HNSW index gives sub-10ms search at this scale
- Native SQL filtering on metadata columns (category, date)
- If no Postgres exists, use **ChromaDB** for prototyping or **Qdrant** for a standalone production option

**Schema:**
```sql
CREATE TABLE help_chunks (
  id              TEXT PRIMARY KEY,
  article_id      TEXT NOT NULL,
  article_title   TEXT NOT NULL,
  section_path    TEXT NOT NULL,
  category        TEXT NOT NULL,
  source_url      TEXT NOT NULL,
  last_updated    DATE NOT NULL,
  content_hash    TEXT NOT NULL,
  chunk_text      TEXT NOT NULL,
  embedding       vector(1536),
  bm25_tsvector   tsvector GENERATED ALWAYS AS (to_tsvector('english', chunk_text)) STORED
);

CREATE INDEX ON help_chunks USING hnsw (embedding vector_cosine_ops);
CREATE INDEX ON help_chunks USING gin (bm25_tsvector);
CREATE INDEX ON help_chunks (category);
```

### 3.5 Update Strategy: Incremental with Hash Detection

```
Weekly ingestion job:
  1. Scan all Markdown files, compute content hashes
  2. Compare against stored content_hash in help_chunks
  3. For changed articles: delete old chunks, re-chunk, re-embed, insert
  4. For deleted articles: remove all chunks with that article_id
  5. For unchanged articles: skip (no re-embedding cost)
  6. Log: articles_added, articles_updated, articles_deleted, chunks_total
```

This keeps the weekly job under 30 seconds even for a full re-index.

---

## 4. Query Pipeline

### 4.1 Hybrid Retrieval

Combine dense (vector) and sparse (BM25) retrieval with Reciprocal Rank Fusion:

```
1. Embed user query → vector search → top 20 by cosine similarity
2. BM25 search on chunk_text → top 20 by keyword relevance
3. Merge with RRF: score = Σ 1/(k + rank_i), k=60
4. Return top 20 merged candidates
```

**Why hybrid:** Customer queries mix natural language ("how do I change my plan") with exact terms ("error code E-4021", product names). BM25 catches exact matches that embeddings miss.

### 4.2 Re-ranking

**Choice: Cohere Rerank API (or `bge-reranker-base` self-hosted)**

- Input: 20 candidates from hybrid retrieval
- Output: top 5 re-ranked by relevance to the query
- Adds ~200ms but significantly improves precision
- At this query volume, Cohere Rerank is cost-effective (~$1 per 1,000 searches)

### 4.3 Context Assembly

```
For each of the top 5 chunks, format as:

---
[Source: {article_title} — {section_path}]({source_url})
Last updated: {last_updated}

{chunk_text}
---

Context budget: 4,000 tokens max for retrieved content.
If top 5 chunks exceed budget, drop the lowest-ranked chunk.
```

### 4.4 Generation

**Model: Claude 3.5 Haiku or GPT-4o-mini**

| Factor | Haiku | GPT-4o-mini |
|---|---|---|
| Latency (TTFT) | ~300ms | ~400ms |
| Cost per 1K output tokens | $1.25 | $0.60 |
| Instruction following | Strong | Strong |
| Streaming | Yes | Yes |

Either works. Pick based on existing vendor relationship. Stream the response to get first tokens to the user within ~1s.

**System prompt:**

```
You are a customer support assistant. Answer the user's question using ONLY
the provided help article excerpts. Follow these rules strictly:

1. Base your answer exclusively on the provided context. If the context does
   not contain enough information to answer, say: "I don't have enough
   information to answer that. Here are some related articles that might help:"
   and list the source links.

2. Cite every claim with the source article. Use the format:
   [Article Title](source_url)

3. Keep answers concise — aim for 2-4 sentences for simple questions,
   a short list for how-to questions.

4. Never make up information, procedures, prices, or policies not in the context.

5. If the user's question is ambiguous, ask a clarifying question rather than
   guessing.

6. For troubleshooting questions, provide steps in order.
```

**Fallback behaviour:**
- If retrieval returns 0 results above similarity threshold (0.3): skip generation, return "I couldn't find an article about that. Try browsing our help centre at [link] or contact support."
- If the LLM API fails: return the top 3 article links directly with: "I'm having trouble generating an answer right now. These articles may help:"
- If latency exceeds 5s: return partial streamed response + article links

---

## 5. Citation Implementation

Each chunk carries `article_title` and `source_url` in its metadata. The system prompt instructs the model to cite using `[Title](URL)` format. Post-process the response to:

1. **Validate citations:** Check that every cited URL exists in the retrieved chunk metadata. Strip any hallucinated citations.
2. **Append source list:** After the answer, add a "Sources" section listing all cited articles with their last-updated dates.
3. **Link unfamiliar citations:** If the model cites an article not in the retrieved set, replace with the closest matching retrieved source.

**Example output:**
```
To update your payment method, go to **Settings → Billing → Payment Methods**
and click "Edit" ([Billing FAQ](/help/billing-faq#payment-methods)).
You can add a credit card, debit card, or bank account
([Accepted Payment Types](/help/payment-types)).

**Sources:**
- [Billing FAQ](/help/billing-faq#payment-methods) — updated 2026-03-30
- [Accepted Payment Types](/help/payment-types) — updated 2026-03-15
```

---

## 6. Cost Estimates

| Component | Monthly Cost (est.) | Assumptions |
|---|---|---|
| Embedding (ingestion) | < $1 | Weekly re-index, ~400K tokens/run |
| Embedding (queries) | ~$2 | 100K queries × ~20 tokens avg |
| Re-ranking (Cohere) | ~$100 | 100K queries at $1/1K |
| LLM generation | ~$125–200 | 100K queries, ~300 tokens out avg |
| pgvector (Postgres) | $0 incremental | Uses existing DB |
| **Total** | **~$225–300/mo** | **At 100K queries/month** |

Scale linearly with query volume. At 10K queries/month, total drops to ~$25-30.

---

## 7. Evaluation Framework

### 7.1 Offline Eval Dataset

Build a golden set of **75 question-answer-source triples**:
- 25 factual lookups ("What is the refund policy?")
- 25 how-to questions ("How do I export my data?")
- 25 troubleshooting ("Login fails with error E-4021")

### 7.2 Metrics

| Metric | Target | Measurement |
|---|---|---|
| Retrieval recall@5 | > 90% | Gold source document in top 5 retrieved chunks |
| Retrieval precision@5 | > 60% | Majority of top 5 are relevant |
| Answer faithfulness | > 95% | LLM-as-judge: every claim grounded in context |
| Answer relevance | > 90% | LLM-as-judge: answer addresses the question |
| Citation accuracy | > 95% | Cited articles match the retrieved sources |
| "I don't know" rate | < 15% | % of answerable questions where system abstains |
| Latency P95 | < 3s | End-to-end measured |

### 7.3 Regression Testing

Run the 75-question eval suite on every change to:
- Chunking parameters
- Embedding model
- Retrieval/re-ranking configuration
- System prompt

Any faithfulness score drop > 5% blocks deployment.

---

## 8. Monitoring (Production)

| Signal | Alert Threshold | Action |
|---|---|---|
| P95 latency | > 3s | Check LLM API latency, reduce K, switch to faster model |
| "I don't know" rate | > 20% over 24h | Check if new article topics are missing from corpus |
| User thumbs-down rate | > 15% | Sample and review bad responses, update eval set |
| Retrieval empty results | > 5% of queries | Query analysis — are users asking about uncovered topics? |
| LLM API error rate | > 1% | Trigger fallback (return article links directly) |
| Ingestion failures | Any | Alert on-call, stale data risk |

---

## 9. Implementation Phases

### Phase 1: MVP (1–2 weeks)
- Markdown parser + document-structure chunker
- pgvector with `text-embedding-3-small`
- Simple vector search (no hybrid, no re-ranking)
- Claude Haiku generation with citation prompt
- Basic eval set (25 questions)
- **Ship internally for dogfooding**

### Phase 2: Quality (1 week)
- Add BM25 hybrid search + RRF fusion
- Add Cohere Rerank
- Expand eval set to 75 questions
- Citation validation post-processing
- Fallback handling for API failures

### Phase 3: Production (1 week)
- Incremental ingestion pipeline with hash-based change detection
- Monitoring dashboards (latency, error rate, thumbs-down)
- Weekly automated ingestion cron job
- Rate limiting and caching for repeated queries
- Load testing to confirm P95 < 3s under expected traffic

---

## 10. Key Design Decisions & Rationale

| Decision | Choice | Why |
|---|---|---|
| Chunking | Document-structure by heading | Articles are already well-structured Markdown; respects natural semantic boundaries |
| Vector DB | pgvector | 2K vectors is trivial; avoids new infrastructure |
| Embedding | text-embedding-3-small | Cost-effective, strong quality, corpus is tiny |
| Retrieval | Hybrid (vector + BM25) | Customers use both natural language and exact product terms |
| Re-ranking | Cohere Rerank | +200ms latency is within budget; significant precision improvement |
| Generation model | Claude Haiku / GPT-4o-mini | Fast enough for 3s budget; good instruction following for citations |
| Update strategy | Incremental with hash detection | Weekly updates on 500 docs — fast, cheap, simple |
| Fallback | Return article links on failure | Customer always gets something useful, even when AI fails |
