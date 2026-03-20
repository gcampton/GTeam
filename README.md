# GTeam

Your AI professional firm — job-based orchestration across social media marketing, web/document design, law, accounting, SEO, and more. Built for Claude Code.

Idea spawned from the brilliant [gstack](https://github.com/gcampton/gstack), which gives you a virtual engineering team. 
Gstack is not just a prompt library, but an actionable set of instructions for Claude.

GTeam expands on that and gives you a virtual professional firm working autonomously, with less human-in-the-loop.

## Quick start

```bash
git clone https://github.com/gcampton/GTeam ~/.claude/skills/gteam
cd ~/.claude/skills/gteam
git submodule update --init
./setup
```

Then in any Claude Code session:

```
/gteam I need to launch my new product next week
```

GTeam routes to the right job and runs all specialists automatically.

## Specialists

| Specialist | What they do |
|---|---|
| Lawyer | Contract review, risk assessment, redlining |
| Accountant | Financial analysis, bookkeeping, tax considerations |
| SEO | Technical audit, keyword strategy, on-page fixes |
| Social Media | Platform strategy, content creation, engagement |
| Email Marketer | Campaign design, sequence writing, deliverability |
| Content Creator | Blog posts, landing copy, long-form guides |

## Jobs (multi-specialist, automatic)

| Job | Runs | Output |
|---|---|---|
| `content-campaign` | SEO + Content + Social | Full campaign package |
| `legal-review` | Lawyer | Redlined doc + risk report |
| `product-launch` | SEO + Content + Social + Lawyer | Complete launch package |

## No API key required

Tier 3 evaluation uses `claude -p` (your existing Claude subscription) with Ollama as fallback. No Anthropic API key needed.

## Development

See [CLAUDE.md](CLAUDE.md) for commands and contribution guidelines.

Inspired by and combined: [gstack](https://github.com/gcampton/gstack), [agency-agents](https://github.com/gcampton/agency-agents), and [skill_seekers](https://github.com/yusufkaraaslan/Skill_Seekers).
