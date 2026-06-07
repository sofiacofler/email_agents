# ARIA — Personal Economic Advisor Agent
### A hands-on workshop: building your first AI agent

---

## What Is This?

A fully working AI agent that reads your Gmail receipts and helps you understand your spending. Built with Claude Code and a local Gmail MCP server.

**Workshop duration:** 1.5 hours (hands-on, in-person)
**Audience:** HiTech professionals, no coding experience required
**Pre-workshop setup:** ~25 minutes at home (see Lesson 00)
**Take-home:** Yes — the agent keeps working after the workshop

---

## Lesson Plan

| File | When | Topic | Time |
|---|---|---|---|
| [lessons/00_pre_workshop_setup.md](lessons/00_pre_workshop_setup.md) | **At home, before the workshop** | Install Python, Claude Code, connect Gmail | ~25 min |
| [lessons/01_welcome.md](lessons/01_welcome.md) | Workshop | What is an agent? What are we building? | 15 min |
| [lessons/02_open_your_agent.md](lessons/02_open_your_agent.md) | Workshop | Open the folder, explore files, customize, first run | 20 min |
| [lessons/03_first_conversation.md](lessons/03_first_conversation.md) | Workshop | First conversation — ask ARIA about your spending | 20 min |
| [lessons/04_memory_bank.md](lessons/04_memory_bank.md) | Workshop | Teach ARIA, watch her remember across sessions | 15 min |
| [lessons/05_take_home.md](lessons/05_take_home.md) | Workshop | Make it yours, go further | 10 min |

---

## What You Need Before the Workshop

- [ ] Python 3.9+ installed
- [ ] Claude Code installed and signed in
- [ ] Google Cloud credentials set up (see Lesson 00)
- [ ] `credentials.json` inside this folder
- [ ] `pip install -r requirements.txt` completed
- [ ] Gmail browser authorization done (`token.json` created)

Full instructions: [lessons/00_pre_workshop_setup.md](lessons/00_pre_workshop_setup.md)

---

## Folder Structure

```
economic-advisor-agent/
│
├── CLAUDE.md                      ← ARIA's identity, purpose, and rules (edit this)
├── mcp_gmail_server.py            ← Gmail tool — read-only, pre-built
├── requirements.txt               ← Python dependencies
├── credentials.json.example       ← Template — replace with your own
│
├── memory/
│   ├── MEMORY.md                  ← Index of what ARIA remembers
│   └── user_financial_profile.md  ← Your financial profile (fill this in)
│
├── .claude/
│   └── settings.json              ← Wires the MCP server to Claude Code
│
└── lessons/
    ├── 00_pre_workshop_setup.md
    ├── 01_welcome.md
    ├── 02_open_your_agent.md
    ├── 03_first_conversation.md
    ├── 04_memory_bank.md
    └── 05_take_home.md
```

---

## Security Model

| Question | Answer |
|---|---|
| Can ARIA send emails? | No — `gmail.readonly` scope, enforced by Google's API |
| Can ARIA delete emails? | No — same reason. Attempts return a 403 error from Google |
| Does Anthropic see my emails? | Yes — content is sent to Claude's API for reasoning (same as pasting into any Claude chat) |
| Does any other server see my emails? | No — path is Gmail → your laptop → Claude API only |
| Can I revoke access? | Yes — Google Account → Security → Third-party apps → remove ARIA Advisor |

---

## Quick Troubleshooting

| Problem | Fix |
|---|---|
| `credentials.json not found` | File must be in this folder, not in Downloads |
| Browser doesn't open for auth | Run `python mcp_gmail_server.py` in a terminal first |
| ARIA finds no receipts | Try: `"search for emails with the word receipt or invoice"` |
| MCP not connecting | Close and reopen Claude Code with this folder |
| Token expired | Delete `token.json`, run `python mcp_gmail_server.py` again |
