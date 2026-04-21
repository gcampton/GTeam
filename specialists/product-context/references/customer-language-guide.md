# Customer Language Guide

Customer language is the highest-value section of the product context file. It's where prospects' own words replace your marketing copy — and their words almost always convert better.

## Why It Matters

Customers describe problems in visceral, specific language that no copywriter invents. "I was drowning in spreadsheets" converts better than "streamline your workflow." Your job is to find the words customers already use and put them back in front of prospects who have the same problem.

The Curse of Knowledge means you (and the company) can no longer imagine NOT knowing how your product works. Customers' words bypass this — they describe the before-state in ways that resonate with people still in it.

## Sources (ranked by quality)

### 1. Review sites (highest ROI for most products)
**G2, Capterra, Trustpilot, App Store, Product Hunt reviews**

What to mine:
- One-star and two-star reviews — customers in these reviews articulate the exact pain they came with and why you didn't solve it. Devastating and useful.
- Five-star reviews — find the specific result language: "used to take me 3 hours, now takes 20 minutes"
- The "what problem were you solving when you found this?" sections

**How to extract:**
```
WebSearch: site:g2.com "[Product Name]" reviews
WebFetch the reviews page and extract all verbatim customer quotes
Look for: specific before/after language, named frustrations, time/money amounts
```

### 2. Sales call transcripts / CRM notes
Champion language from discovery calls. What problem did they describe in their first call? What was the "I'm fed up with..." moment? These are gold.

If available: Read any `calls/`, `notes/`, or `transcripts/` directories in the project.

### 3. Support tickets and chat logs
Where customers describe what's broken in the most unfiltered terms. Also reveals false assumptions (things customers think your product does that it doesn't).

### 4. Win/loss interviews
Post-sale interviews with both new customers ("why did you choose us?") and churned customers ("why did you leave?") produce the clearest articulation of switching forces.

### 5. Community mentions
Reddit, Hacker News, Twitter/X, LinkedIn comments. Search for your product name + "because" or your category + "frustrating" or "wish".

```
WebSearch: site:reddit.com "[Product Name]" OR "[category problem]"
```

### 6. NPS survey verbatims
Especially detractors (0–6). They explain what's broken in plain language. Promoters explain what's working.

## What Good Customer Language Looks Like

**Weak (internal/marketing language):**
- "Streamline your workflows"
- "Improve team collaboration"
- "Powerful analytics at your fingertips"
- "The all-in-one solution for modern teams"

**Strong (customer language):**
- "I used to spend my whole Sunday evening updating the board before Monday standup"
- "My team stopped using our old tool because nobody could find anything"
- "I got my first report out in 20 minutes — I expected it to take a day"
- "Finally stopped getting 'can you resend that spreadsheet' emails"

**Signals that you've found real customer language:**
- It's specific (has a time, a number, a named frustration)
- It describes the before state, not the product
- It sounds like something a person would actually say
- It would not appear in a press release

## Extracting Language From Codebase

If the project has marketing copy files, check them for existing attempts at customer language:

```bash
grep -r "customer" . --include="*.md" -l | head -10
grep -r "testimonial\|quote\|review" . --include="*.md" -l | head -10
```

Read any found files and extract actual customer quotes (look for quotation marks or attribution like "— Customer Name, Title").

## Minimum Viable Customer Language Set

Before writing the context file, aim to have:
- At least 5 verbatim phrases from real customers
- At least 1 phrase describing the before-state pain
- At least 1 phrase describing the after-state result
- At least 1 phrase describing why alternatives failed
- Sources noted for each phrase

If you cannot find verbatim customer language: note this explicitly in the context file. Flag it as a gap the company should address with a customer research session (see: ux-researcher specialist).
