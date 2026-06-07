# ARIA — Personal Economic Advisor Agent
### A hands-on workshop: building your first AI agent

---

## What Is This?

A fully working AI agent that reads your Gmail receipts and helps you understand your spending. Built with Claude Code + a local Gmail MCP server.

**Workshop duration:** 1.5 hours  
**Audience:** HiTech professionals, no coding experience required  
**Take-home:** Yes — the agent works after the workshop

---

## Quick Start (Workshop)

Follow the lessons in order:

| File | Topic | Time |
|---|---|---|
| [lessons/00_welcome.md](lessons/00_welcome.md) | What is an agent? | 15 min |
| [lessons/01_google_cloud_setup.md](lessons/01_google_cloud_setup.md) | Connect to Gmail (read-only) | 20 min |
| [lessons/02_meet_your_agent.md](lessons/02_meet_your_agent.md) | Meet and customize ARIA | 15 min |
| [lessons/03_first_conversation.md](lessons/03_first_conversation.md) | First conversation with ARIA | 20 min |
| [lessons/04_memory_bank.md](lessons/04_memory_bank.md) | Teach ARIA, watch her remember | 15 min |
| [lessons/05_take_home.md](lessons/05_take_home.md) | Make it yours, go further | 10 min |

---

## What You Need Before the Workshop

- [ ] Claude Code installed (desktop app or VS Code extension)
- [ ] Python 3.9+ installed (`python --version` to check)
- [ ] A Google account (Gmail) whose receipts you want to analyze
- [ ] Internet connection

---

## Folder Structure

```
economic-advisor-agent/
│
├── CLAUDE.md                    ← ARIA's identity, purpose, and rules
├── mcp_gmail_server.py          ← Gmail tool (read-only, pre-built)
├── requirements.txt             ← Python dependencies
├── credentials.json.example     ← Template — replace with your own
│
├── memory/
│   ├── MEMORY.md                ← What ARIA remembers (index)
│   └── user_financial_profile.md ← Your financial profile template
│
├── .claude/
│   └── settings.json            ← Wires the MCP server to Claude Code
│
└── lessons/
    ├── 00_welcome.md
    ├── 01_google_cloud_setup.md
    ├── 02_meet_your_agent.md
    ├── 03_first_conversation.md
    ├── 04_memory_bank.md
    └── 05_take_home.md
```

---

## Security Model

| Question | Answer |
|---|---|
| Can ARIA send emails? | No — `gmail.readonly` scope, enforced by Google's API |
| Can ARIA delete emails? | No — same reason |
| Does Anthropic see my emails? | Yes — email content is sent to Claude's API for reasoning (same as pasting into any Claude chat) |
| Does any other server see my emails? | No — path is Gmail → your laptop → Claude API |
| Can I revoke access? | Yes — Google Account → Security → Third-party apps |

---

## Setup (After the Workshop)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Add your credentials.json (from Google Cloud Console — see Lesson 01)

# 3. Open this folder in Claude Code
#    ARIA activates automatically when the folder is open
```

---

## Customization

**Change ARIA's behavior:** Edit `CLAUDE.md` — plain text, no coding needed.

**Pre-load memory:** Edit `memory/user_financial_profile.md` directly.

**Add tools:** Add a Python function with `@mcp.tool()` in `mcp_gmail_server.py`.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `credentials.json not found` | File must be in this folder, not in Downloads |
| Browser doesn't open for auth | Run `python mcp_gmail_server.py` manually first |
| ARIA finds no receipts | Try: `"search for emails with the word receipt or invoice"` |
| MCP not connecting | Restart Claude Code with this folder open |
| Token expired | Delete `token.json`, restart Claude Code |
