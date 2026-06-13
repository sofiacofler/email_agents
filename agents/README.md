# ARIA — Personal Economic Advisor Agent
### A hands-on workshop: building your first AI agent

---

## What Is This?

A fully working AI agent that reads your Gmail receipts and helps you understand your spending. Built with Claude Code and Google's Gmail connector — no code, no installs beyond Claude itself (plus a notes app to browse the files).

**Workshop duration:** 1.5 hours (hands-on, in-person)
**Audience:** HiTech professionals, no coding experience required
**Pre-workshop setup:** ~15 minutes at home (see Lesson 00)
**Take-home:** Yes — the agent keeps working after the workshop

---

## Lesson Plan

| File | When | Topic | Time |
|---|---|---|---|
| [lessons/00_pre_workshop_setup.md](lessons/00_pre_workshop_setup.md) | **At home, before the workshop** | Install Claude Code + Obsidian, get the agent folder | ~15 min |
| [lessons/01_welcome.md](lessons/01_welcome.md) | Workshop | What is an agent? What are we building? | 15 min |
| [lessons/02_open_your_agent.md](lessons/02_open_your_agent.md) | Workshop | Open the folder, explore files, customize | 20 min |
| [lessons/03_connect_gmail.md](lessons/03_connect_gmail.md) | Workshop | Connect Gmail and lock down tool permissions | 5 min |
| [lessons/04_first_conversation.md](lessons/04_first_conversation.md) | Workshop | First conversation — ask ARIA about your spending | 20 min |
| [lessons/05_memory_bank.md](lessons/05_memory_bank.md) | Workshop | Teach ARIA, watch her remember across sessions | 15 min |
| [lessons/06_take_home.md](lessons/06_take_home.md) | Workshop | Make it yours, go further | 10 min |
| [lessons/07_custom_skills.md](lessons/07_custom_skills.md) | Workshop (bonus, only if time allows) | Build a reusable Skill for repeatable tasks | ~15 min |

---

## What You Need Before the Workshop

- [ ] Claude Code (or Claude Desktop) installed and signed in
- [ ] Obsidian or VS Code installed (to browse the agent's files)
- [ ] The `workshop_agent.zip` extracted on your machine

Full instructions: [lessons/00_pre_workshop_setup.md](lessons/00_pre_workshop_setup.md)

Gmail is connected together at the start of the workshop (Lesson 03).

---

## Folder Structure

```
.
├── README.md
│
├── financial_agent/
│   ├── CLAUDE.md                      ← ARIA's identity, purpose, and rules (edit this)
│   └── memory/
│       ├── MEMORY.md                  ← Index of what ARIA remembers
│       └── user_financial_profile.md  ← Your financial profile (fill this in)
│
└── lessons/
    ├── 00_pre_workshop_setup.md
    ├── 01_welcome.md
    ├── 02_open_your_agent.md
    ├── 03_connect_gmail.md
    ├── 04_first_conversation.md
    ├── 05_memory_bank.md
    ├── 06_take_home.md
    └── 07_custom_skills.md    ← bonus, only if time allows
```

---

## Security Model

| Question | Answer |
|---|---|
| Can ARIA send or delete emails? | No — neither action is one of the connector's tools |
| Can ARIA create drafts or change labels? | The connector technically can, but Lesson 03 configures Claude to **block** those tools — the request never reaches Google |
| Does Anthropic see my emails? | Yes — content is sent to Claude for reasoning (same as pasting into any Claude chat) |
| Does any other server see my emails? | No — the connection goes directly through Google's Gmail connector |
| Can I revoke access? | Yes — in Claude's Settings → Connectors, disconnect Gmail. You can also remove access from your Google Account → Security → Third-party apps |

---

## Quick Troubleshooting

| Problem | Fix |
|---|---|
| ARIA finds no receipts | Try: `"search for emails with the word receipt or invoice"` |
| Gmail connector not working | Settings → Connectors → check Gmail is connected, reconnect if needed |
| ARIA can't access Gmail at all | Make sure the Gmail connector is enabled for this conversation/project |
