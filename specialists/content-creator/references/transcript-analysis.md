# Video & Audio Transcript Analysis

## Extracting Transcripts

### YouTube Transcripts

**Method 1: yt-dlp (preferred — gets auto-generated or manual subtitles)**
```bash
# Install if needed
pip install yt-dlp

# Download subtitles only (no video)
yt-dlp --write-auto-sub --sub-lang en --skip-download -o "%(title)s" "URL"

# Download manual subs if available (higher quality)
yt-dlp --write-sub --sub-lang en --skip-download -o "%(title)s" "URL"

# Get both and prefer manual
yt-dlp --write-sub --write-auto-sub --sub-lang en --sub-format vtt --skip-download -o "%(title)s" "URL"
```

**Method 2: YouTube transcript API (for bulk extraction)**
```bash
pip install youtube-transcript-api

python3 -c "
from youtube_transcript_api import YouTubeTranscriptApi
transcript = YouTubeTranscriptApi.get_transcript('VIDEO_ID')
for entry in transcript:
    print(entry['text'])
"
```

**Method 3: WebFetch fallback**
If tools aren't available, use WebFetch on transcript services or extract from video description + comments for context.

### Meeting Recordings (Zoom, Teams, Google Meet)
- Export transcript from recording platform (usually .vtt or .txt format)
- Zoom: Recording page → Transcript tab → Download
- Teams: Stream → Transcript → Download
- Google Meet: Auto-saved to Google Drive alongside recording

### Podcast / Audio Files
```bash
# Use Whisper for local transcription
pip install openai-whisper
whisper audio.mp3 --model base --language en --output_format txt
```

## Transcript Cleaning

Raw transcripts need cleanup before analysis:

1. **Remove timestamps** (unless timing matters for the analysis)
2. **Fix speaker labels** — replace "Speaker 1" with actual names where identifiable
3. **Merge fragmented sentences** — auto-captions break mid-sentence
4. **Remove filler artifacts** — "um", "uh", "you know" (keep if analysing speech patterns)
5. **Paragraph breaks** — group by topic or speaker turn, not by caption timing

## Content Repurposing from Transcripts

### Video → Blog Post
1. Extract key points and structure from transcript
2. Reorganise into logical sections (video flow ≠ article flow)
3. Add intro/conclusion (videos often start casually; articles need hooks)
4. Replace verbal references ("as I showed earlier") with written equivalents
5. Add links, images, and formatting that video didn't need
6. SEO optimise: title, meta description, headers, internal links

### Video → Social Posts
1. Extract quotable moments (strong opinions, surprising data, clear frameworks)
2. Each quote = one social post with context
3. Add visual (screenshot from video, quote card, or clip)
4. Link back to full video

### Video → Newsletter
1. Summarise key takeaway in 2-3 sentences
2. Extract the "aha moment" — what makes this video worth watching?
3. Include one actionable tip from the transcript
4. CTA: watch the full video for depth

### Podcast → Show Notes
1. Topic list with timestamps
2. Key quotes from guests
3. Resources/links mentioned
4. One-paragraph summary

## Competitive Video Analysis

### Channel Research Workflow
1. **Identify top videos** — sort competitor's channel by most popular
2. **Extract transcripts** from top 5-10 videos
3. **Analyse messaging patterns:**
   - What problems do they address most frequently?
   - What frameworks/methodologies do they teach?
   - What language/terminology resonates with their audience?
   - What CTAs do they use? (subscribe, buy, download)
4. **Check comments** — what questions do viewers ask? (= content gaps)
5. **Note production patterns:**
   - Video length (what's their sweet spot?)
   - Hook structure (first 30 seconds)
   - Thumbnail style
   - Upload frequency

### Output — Competitive Video Report
```markdown
# Competitive Video Analysis: [Channel Name]

## Channel Stats
- Subscribers: [X]
- Average views (last 10 videos): [X]
- Upload frequency: [X per week/month]
- Primary topics: [list]

## Top-Performing Content
| Video | Views | Topic | Hook | Why It Worked |
|---|---|---|---|---|
| [Title] | [X] | [Topic] | [First line] | [Analysis] |

## Messaging Patterns
- Most common pain points addressed: [list]
- Frameworks/models used: [list]
- Language that resonates: [key phrases from titles + transcripts]

## Audience Signals (from comments)
- Top questions: [what viewers want to know more about]
- Content gaps: [what the channel doesn't cover but viewers ask for]

## Opportunities
1. [Topic they don't cover that their audience wants]
2. [Angle they miss on a popular topic]
```

[HYPOTHESIS] — transcript analysis patterns based on industry best practices. Mark as [TESTED] after validating with real channel analyses.
