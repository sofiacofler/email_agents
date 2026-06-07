# Lesson 02 — Meet Your Agent
**Time: 15 minutes**

---

## Opening the Agent in Claude Code

1. Open **Claude Code** (the desktop app or VS Code extension)
2. Open the folder: `economic-advisor-agent/`
3. That's it — Claude Code automatically reads `CLAUDE.md` when it opens a folder

You have just activated ARIA. Every conversation you have in this folder will use her identity, rules, and memory.

---

## What Just Happened?

When Claude Code opened the folder, it read `CLAUDE.md` and loaded:

- ARIA's **name** and **purpose**
- Her **rules** (read-only, no sending, no deleting)
- Instructions for her **memory bank**
- The **tools** available to her (via the MCP server)

Think of it like handing a new employee their job description on day one.

---

## Explore the Files Together

Take 5 minutes to open and read these files:

### `CLAUDE.md`
This is ARIA's brain. Read through it. Notice:
- The rules are written in plain language — no code
- There is a section "How to Talk to Me" with example questions
- At the bottom: *"You can rename me by changing 'ARIA' throughout this file"*

**Try it now:** Change "ARIA" to a name you prefer throughout `CLAUDE.md`. Save the file. The agent is now renamed.

### `memory/MEMORY.md`
This is ARIA's notebook index. Currently it only has the starter profile. Over time, as you talk to ARIA, this file grows.

### `memory/user_financial_profile.md`
A template of what ARIA will learn about you. Fields are empty — she will fill them in.

### `.claude/settings.json`
The technical wiring. It tells Claude Code: "when this folder is open, run `mcp_gmail_server.py` as a tool provider." You don't need to change this.

---

## The Key Insight

> **The agent is the folder.**

There is no app to install, no server to deploy. The combination of:
- `CLAUDE.md` (identity)
- `mcp_gmail_server.py` (tools)
- `memory/` (memory)
- `.claude/settings.json` (wiring)

...is what makes it an agent rather than just a chatbot.

To give this agent to a colleague, you zip the folder and send it. They add their own `credentials.json` and they have their own instance of the agent, connected to their own Gmail.

---

## Customize ARIA Before First Use

Before moving to Lesson 03, make at least one change to `CLAUDE.md`:

1. **Change the name** — find and replace "ARIA" with your preferred name
2. **Set your currency** — find the line `Currency: (not yet set)` in `memory/user_financial_profile.md` and fill it in
3. **Add a rule** — in the "My Rules" section of `CLAUDE.md`, add something personal, e.g.: *"Always show amounts in euros. Flag any expense over 100 euros."*

This is how you shape your agent's behavior — just edit a text file.

---

*Ready? Open `lessons/03_first_conversation.md`*
