# Lesson 05 — Take It Home
**Time: 10 minutes**

---

## What You Built Today

You now have a working personal AI agent that:

- Has an identity and rules defined in plain text (`CLAUDE.md`)
- Can read your Gmail receipts with Google-enforced read-only access
- Remembers what it learns across sessions (the `memory/` folder)
- Runs entirely on your laptop — no cloud service, no monthly fee beyond Claude

This is not a demo. This is your agent. It works after the workshop ends.

---

## Ideas for Making It Yours

**Change the agent's behavior — just edit `CLAUDE.md`:**

- Add a rule: *"Always compare this month's spending to last month"*
- Add a rule: *"If you find a charge over 200 euros, always highlight it"*
- Add a focus area: *"I'm particularly interested in travel expenses"*
- Restrict scope: *"Only analyze emails from the last 6 months"*

**Pre-load the memory:**

Open `memory/user_financial_profile.md` and fill in:
- Your actual monthly budget per category
- Subscriptions you already know about (so ARIA skips them or confirms them)
- Vendors to always flag

**Add new query templates to Lesson 03:**

When you find a question that gives great results, write it down. Build your own library of prompts.

---

## Going Further (Optional, Technical)

If you want to extend the agent's capabilities, you can add new tools to `mcp_gmail_server.py`:

**Ideas:**
- `list_senders_by_frequency` — who emails you most often?
- `find_unsubscribe_links` — find emails with unsubscribe buttons (useful for subscription cleanup)
- `extract_amounts` — use regex to pull all currency amounts from a search result
- Connect a second MCP server (e.g., Google Sheets) to export spending data

Each new tool is a Python function with a `@mcp.tool()` decorator — the same pattern as `search_emails` and `read_email`.

---

## Sharing the Agent With a Colleague

1. Zip the `economic-advisor-agent/` folder
2. Make sure `credentials.json` and `token.json` are NOT included (they are personal)
3. Your colleague follows Lesson 01 to get their own credentials
4. They drop their `credentials.json` into the folder
5. They have their own instance, connected to their own Gmail

The agent's identity (`CLAUDE.md`) and structure are the same. Only the Gmail credentials are personal.

---

## The Bigger Picture

What you built today follows the same pattern used to build much more sophisticated agents:

| What you built | Production equivalent |
|---|---|
| `CLAUDE.md` | System prompt / agent configuration |
| `mcp_gmail_server.py` | MCP server / tool integration |
| `memory/*.md` | Vector database / persistent memory store |
| `.claude/settings.json` | Agent runtime configuration |

The concepts scale. A team-level agent would have the same parts — just with more tools, more structured memory, and multiple users.

---

## Troubleshooting Reference

| Problem | Fix |
|---|---|
| "credentials.json not found" | Make sure the file is in the agent folder, not Downloads |
| Gmail asks to re-authorize | Delete `token.json` and re-run `python mcp_gmail_server.py` |
| ARIA doesn't find any emails | Try simpler queries: `receipt`, `invoice`, `order` |
| ARIA forgot something | Check `memory/MEMORY.md` — did she save it? |
| MCP not connecting | Restart Claude Code with the agent folder open |

---

## Thank You

You now know:
- What an agent is and how it differs from a chatbot
- How `CLAUDE.md` defines an agent's identity
- How MCP tools give an agent access to external systems
- How read-only OAuth scopes enforce security at the API level
- How file-based memory persists across conversations

These are the building blocks of every AI agent, from personal tools to enterprise systems.

---

*Questions? Reach out to the workshop organizer. The agent folder is yours to keep.*
