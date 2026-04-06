# Model Selection Guide

Quick-reference table for choosing the right model by task type.

## Text Generation

| Model | Provider | Cost Tier | Quality | Latency | Best For |
|---|---|---|---|---|---|
| Claude Opus | Anthropic | High | Excellent | Medium | Complex analysis, research, long-form writing |
| Claude Sonnet | Anthropic | Medium | Very Good | Medium | General-purpose, coding, structured output |
| Claude Haiku | Anthropic | Low | Good | Fast | High-volume chat, classification, simple extraction |
| GPT-4o | OpenAI | Medium-High | Very Good | Medium | Multimodal tasks, general-purpose |
| GPT-4o-mini | OpenAI | Low | Good | Fast | High-volume, cost-sensitive applications |
| Gemini Pro | Google | Medium | Very Good | Medium | Long context (1M+), multimodal |
| Gemini Flash | Google | Low | Good | Fast | High-volume, speed-critical |
| Llama 3 70B | Meta (self-hosted) | Compute | Very Good | Variable | Data sovereignty, fine-tuning, self-hosted |
| Mistral Large | Mistral | Medium | Good | Medium | European data residency, multilingual |

## Embeddings

| Model | Provider | Dimensions | Cost Tier | Best For |
|---|---|---|---|---|
| text-embedding-3-large | OpenAI | 3072 (or reduced) | Low | Highest quality, supports Matryoshka |
| text-embedding-3-small | OpenAI | 1536 (or reduced) | Very Low | Cost-effective, good quality |
| Cohere Embed v3 | Cohere | 1024 | Low | Multilingual, compression support |
| voyage-3 | Voyage AI | 1024 | Low | Code and technical content |
| nomic-embed-text | Nomic (open) | 768 | Free (compute) | Self-hosted, no API dependency |
| BGE-large-en | BAAI (open) | 1024 | Free (compute) | Self-hosted, strong English performance |

## Classification

| Approach | When to Use | Setup Cost | Per-Request Cost | Quality |
|---|---|---|---|---|
| Zero-shot LLM | < 100 examples, rapid prototyping | None | High | Good |
| Few-shot LLM | 5-20 examples available, need fast iteration | Low | High | Very Good |
| Fine-tuned small model | 500+ labelled examples, high volume | High | Very Low | Excellent |
| Traditional ML (sklearn) | Structured features, millions of examples | Medium | Near Zero | Variable |

## Image Generation

| Model | Provider | Cost Tier | Quality | Best For |
|---|---|---|---|---|
| DALL-E 3 | OpenAI | Medium | Very Good | Prompt adherence, text in images |
| Flux Pro | Black Forest Labs | Medium | Excellent | Photorealism, artistic quality |
| Stable Diffusion 3 | Stability AI (self-hosted) | Compute | Good | Self-hosted, fine-tuning, no content restrictions |
| Midjourney | Midjourney | Medium | Excellent | Artistic/creative (API limited) |

## Speech

| Model | Provider | Direction | Cost Tier | Quality | Best For |
|---|---|---|---|---|---|
| Whisper large-v3 | OpenAI / self-hosted | Speech-to-text | Low | Excellent | Transcription, multilingual |
| Deepgram Nova-2 | Deepgram | Speech-to-text | Low | Very Good | Real-time streaming transcription |
| ElevenLabs | ElevenLabs | Text-to-speech | Medium | Excellent | Natural voice, voice cloning |
| OpenAI TTS | OpenAI | Text-to-speech | Low | Good | Cost-effective narration |

## Code Generation

| Model | Provider | Cost Tier | Quality | Best For |
|---|---|---|---|---|
| Claude Sonnet | Anthropic | Medium | Excellent | Complex code, refactoring, debugging |
| GPT-4o | OpenAI | Medium-High | Very Good | General coding, multi-language |
| Codestral | Mistral | Medium | Good | Fast code completion, self-hostable |
| DeepSeek Coder V2 | DeepSeek (self-hosted) | Compute | Very Good | Self-hosted code generation |

## Decision Framework

1. **Start managed, go self-hosted only if forced** by cost (> 1M req/month), data sovereignty, or fine-tuning needs.
2. **Prototype with 2+ models** before committing. Quality varies dramatically by task.
3. **Pin exact model versions** in production (e.g., `claude-sonnet-4-20250514`, not `claude-3-sonnet`).
4. **Build a model abstraction layer** so you can switch providers without rewriting business logic.
5. **Monitor cost per request** from day one. Set budget alerts before you get the first bill.
