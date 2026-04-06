# Discord Server Template: [Community Name]

## Server Info
- Name: [Community Name]
- Description: [One-line purpose]
- Verification Level: [Low / Medium / High]
- Default Notification: Mentions only

## Categories & Channels

### Welcome
- #rules — [Read-only. Community guidelines.]
- #introductions — [New members introduce themselves]
- #announcements — [Read-only. Official updates.]

### General
- #general — [Main conversation]
- #off-topic — [Non-community-related chat]
- #resources — [Useful links and references]

### Topics
- #[topic-1] — [Description]
- #[topic-2] — [Description]
- #[topic-3] — [Description]

### Support
- #help — [Ask questions, get help from the community]
- #bugs — [Report issues or problems]
- #feature-requests — [Suggest improvements]

### Voice
- General Voice — [Open voice channel]
- [Event] Voice — [Scheduled events]

### Admin (hidden)
- #mod-log — [Bot logs and moderation actions]
- #mod-chat — [Private moderator discussion]
- #bot-commands — [Bot configuration]

## Role Hierarchy (top to bottom)
| Role | Color | Permissions | How Assigned |
|---|---|---|---|
| Admin | Red | All | Manual |
| Moderator | Orange | Manage messages, mute, kick | Manual |
| Contributor | Blue | Send messages, react, voice, embed links | Earned (activity threshold or manual) |
| Verified | Green | Send messages, react, voice | Reaction role / bot |
| Member | Default | Read only until verified | On join |

## Bots
- [Bot 1]: [Purpose, e.g., "Carl-bot — reaction roles, automod, welcome DM"]
- [Bot 2]: [Purpose, e.g., "MEE6 — leveling, moderation, custom commands"]
- [Bot 3]: [Purpose, e.g., "Dyno — logging, automod backup, timed announcements"]

## Automod Rules
- Spam filter: [Delete messages with 3+ duplicate lines]
- Invite filter: [Delete discord.gg links except allowlisted servers]
- Mention limit: [Max 3 user mentions per message]
- Link filter: [New members (<24h) cannot post links]

## Welcome DM Template
```
Welcome to [Community Name]! Start by reading #rules, then introduce yourself in #introductions. [Any other first steps.]
```

## Server Settings
- Explicit media content filter: [Scan messages from all members / members without roles]
- 2FA requirement for moderators: [Yes / No]
- Default channel: #rules (so new members see rules first)
- Community features enabled: [Yes — for Server Discovery, if applicable]

## Onboarding Flow (if using Discord's built-in onboarding)
1. Welcome screen with server description and rules link
2. Channel selection: let members pick topic channels relevant to them
3. Role selection: self-assign interest-based roles
4. Prompt to introduce themselves in #introductions
