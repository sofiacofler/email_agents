# ARIA — Personal Economic Advisor Agent
### A hands-on workshop: building your first AI agent

---

## What Is This?

A fully working AI agent that reads your Gmail receipts and helps you understand your spending. Built with Claude Code and Anthropic's official Gmail connector — no code, no installs beyond Claude itself.

**Workshop duration:** 1.5 hours (hands-on, in-person)
**Audience:** HiTech professionals, no coding experience required
**Pre-workshop setup:** ~10 minutes at home (see Lesson 00)
**Take-home:** Yes — the agent keeps working after the workshop

---

## Lesson Plan

| File | When | Topic | Time |
|---|---|---|---|
| [lessons/00_pre_workshop_setup.md](lessons/00_pre_workshop_setup.md) | **At home, before the workshop** | Install Claude Code, connect Gmail | ~10 min |
| [lessons/01_welcome.md](lessons/01_welcome.md) | Workshop | What is an agent? What are we building? | 15 min |
| [lessons/02_open_your_agent.md](lessons/02_open_your_agent.md) | Workshop | Open the folder, explore files, customize, first run | 20 min |
| [lessons/03_first_conversation.md](lessons/03_first_conversation.md) | Workshop | First conversation — ask ARIA about your spending | 20 min |
| [lessons/04_memory_bank.md](lessons/04_memory_bank.md) | Workshop | Teach ARIA, watch her remember across sessions | 15 min |
| [lessons/05_take_home.md](lessons/05_take_home.md) | Workshop | Make it yours, go further | 10 min |

---

## What You Need Before the Workshop

- [ ] Claude Code (or Claude Desktop) installed and signed in
- [ ] Gmail connected via Anthropic's Gmail connector (see Lesson 00)

Full instructions: [lessons/00_pre_workshop_setup.md](lessons/00_pre_workshop_setup.md)

---

## Folder Structure

```
economic-advisor-agent/
│
├── CLAUDE.md                      ← ARIA's identity, purpose, and rules (edit this)
│
├── memory/
│   ├── MEMORY.md                  ← Index of what ARIA remembers
│   └── user_financial_profile.md  ← Your financial profile (fill this in)
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
| Can ARIA send emails? | No — the Gmail connector is read-only |
| Can ARIA delete emails? | No — same reason |
| Does Anthropic see my emails? | Yes — content is sent to Claude for reasoning (same as pasting into any Claude chat) |
| Does any other server see my emails? | No — the connection goes directly through Anthropic's Gmail connector |
| Can I revoke access? | Yes — in Claude's Settings → Connectors, disconnect Gmail. You can also remove access from your Google Account → Security → Third-party apps |

---

## Quick Troubleshooting

| Problem | Fix |
|---|---|
| ARIA finds no receipts | Try: `"search for emails with the word receipt or invoice"` |
| Gmail connector not working | Settings → Connectors → check Gmail is connected, reconnect if needed |
| ARIA can't access Gmail at all | Make sure the Gmail connector is enabled for this conversation/project |
