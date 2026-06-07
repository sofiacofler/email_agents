# Lesson 05 — Take It Home
**Time: 10 minutes**

---

## What You Built Today

You now have a working personal AI agent that:

- Has an identity and rules defined in plain language (`CLAUDE.md`)
- Can read your Gmail receipts with Google-enforced read-only access
- Remembers what it learns across sessions (the `memory/` folder)
- Runs entirely on your laptop — no cloud service required beyond Claude

This is not a demo. This is your agent. It works after the workshop ends.

---

## Make It More Yours — Edit `CLAUDE.md`

Everything in `CLAUDE.md` shapes ARIA's behavior. No code, just text. Ideas:

- **Add a standing rule:** *"Always compare this month's spending to last month"*
- **Add a threshold:** *"Highlight any single expense over 150 euros"*
- **Add a focus area:** *"I am particularly interested in tracking subscription creep"*
- **Change the tone:** Add a line like *"Be direct and give me numbers first, context second"*
- **Restrict scope:** *"Only analyze emails from the past 12 months"*

Every time you save `CLAUDE.md` and start a new conversation, ARIA reflects the change.

---

## Pre-Load the Memory

Open `memory/user_financial_profile.md` and fill in what you already know:
- Your actual monthly budget per category
- Subscriptions you've confirmed (so ARIA doesn't keep re-analyzing them)
- Vendors you always want flagged
- How you like data presented (table vs. bullet points, monthly vs. weekly)

The more you fill in, the less you need to repeat yourself in conversation.

---

## Build Your Own Prompt Library

When you find a question that gives consistently great results, write it down. Over time you'll build a personal set of go-to prompts:

- Your weekly check-in question
- Your end-of-month summary request
- Your subscription audit prompt

There is no special file for this — a sticky note or a note in `CLAUDE.md` under a "My Favorite Questions" section both work.

---

## Share the Agent With a Colleague

1. Copy the `economic-advisor-agent/` folder to their machine
2. Make sure `credentials.json` and `token.json` are **not** included — those are personal
3. They follow Lesson 00 to get their own `credentials.json`
4. They open the folder in Claude Code

The agent's identity and structure are shared. The Gmail credentials are personal to each user.

---

## Going Further (Optional, for the Curious)

ARIA can already answer most financial questions using `search_emails` and `read_email` — she constructs the right queries and reasons over the results herself. You do not need new tools to ask "who sends me the most receipts?" or "find expenses over 200 euros" — just ask her.

The only reason to add a new tool is to connect a **completely different system** that Gmail doesn't cover. For example:
- A Google Sheets MCP to automatically export monthly summaries to a spreadsheet
- A bank statement parser if your bank emails PDF attachments
- A calendar MCP to correlate travel spending with trip dates

That level of extension requires coding. For everything that lives in your inbox, you already have what you need.

---

## The Bigger Picture

What you built today follows the same architecture used in much more sophisticated production agents:

| What you built | Production equivalent |
|---|---|
| `CLAUDE.md` | System prompt / agent configuration |
| `mcp_gmail_server.py` | MCP server / tool integration |
| `memory/*.md` | Persistent memory / knowledge store |
| `.claude/settings.json` | Agent runtime configuration |

The concepts scale. A team-level agent has the same four parts — just with more tools, more structured memory, and access controls for multiple users.

---

## Troubleshooting Reference

| Problem | Fix |
|---|---|
| `credentials.json not found` | File must be inside the agent folder, not in Downloads |
| Gmail asks to re-authorize | Delete `token.json`, run `python mcp_gmail_server.py` in a terminal |
| ARIA finds no emails | Use simpler terms: `receipt`, `invoice`, `order`, `confirmation` |
| ARIA forgot something | Open `memory/MEMORY.md` — did the file get created? |
| MCP not connecting | Close and reopen Claude Code with the agent folder |

---

## Thank You

You now understand:
- What makes an AI agent different from a chatbot
- How `CLAUDE.md` defines an agent's identity in plain language
- How MCP tools give an agent access to external systems
- How `gmail.readonly` enforces security at Google's API level
- How file-based memory persists what an agent learns

These are the building blocks of every AI agent — from a personal tool on a laptop to an enterprise system running at scale.

*The agent folder is yours. Keep building.*
