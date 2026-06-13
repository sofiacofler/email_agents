# Lesson 01 — Welcome: What Are We Building?
**Time: 15 minutes**

---

## What is an AI Agent?

An **AI agent** is an AI that can reason through a goal, decide what it needs to do, and act — not just answer one question and stop.

Three things make this possible:

- **Reasoning** — Given a task, it thinks through what it needs to know and do, step by step — like planning before you start.
- **Tools** — It can reach beyond the conversation: read files, search an inbox, call other systems. It decides *on its own*, in the moment, when a tool is needed.
- **Memory** — It can write notes to itself and read them back later, so what it learns in one conversation carries into the next.

Think of it like hiring a specialist:
- You give them a **job description** — what they do, how they behave, what they're not allowed to do
- You give them **tools** — access to the systems they need, and they decide when to reach for each one
- You give them a **desk** — somewhere to take notes between meetings, which they check and update themselves

---

## What We Built for Today

Meet **ARIA** — your personal finance agent.

ARIA is a personal economic advisor that:
- Reads the receipts and order confirmations in your Gmail inbox
- Answers questions like "How much did I spend on food last month?"
- Tracks subscriptions you may have forgotten
- Remembers your preferences and budget goals across conversations

By the end of this workshop you will have made ARIA your own and had your first real conversation with her about your spending.

---

## The Three Things That Make ARIA a Custom Agent

```
financial_agent/
│
├── CLAUDE.md              ← Job description: who ARIA is, her rules
│
├── Gmail connector        ← Her tool: reads Gmail, nothing else
│
└── memory/
    └── MEMORY.md          ← Her desk: notes she keeps between sessions
```

That's it. No database. No cloud server. No deployment. No code.

---

## Where Does ARIA's Knowledge Come From?

Claude — the AI behind ARIA — was trained on a huge snapshot of text from the internet, up to a certain point in time (its "knowledge cutoff"). That's where her general knowledge, language, and reasoning come from.

But three things live outside that training data:
- **Anything that happened after the cutoff** → ARIA can search the web for it
- **Anything about *your* world** — your emails, your spending → ARIA needs **connectors**, like the one we set up in Lesson 03
- **Anything you've told her in past conversations** → ARIA relies on her **memory** files

---

## What is MCP?

**MCP (Model Context Protocol)** is a standard way to give an AI access to external tools.

In our case, the **Gmail connector** is built and hosted by Google. It:
- Connects to your Gmail account (we'll set this up in Lesson 03)
- Gives ARIA the ability to search your inbox and read individual emails

> **The security guarantee:** This connector can technically create drafts and manage labels, in addition to reading mail — but in this workshop we configure Claude to **always allow** read-only tools (search, read threads, list labels) and **always block** anything that creates, sends, or modifies (drafts, labels, etc.). This block is enforced by Claude itself, before any request reaches Google's servers — so even if ARIA tried to draft or modify something, the request never goes out.

---

## How ARIA Loads Her Context

Every time you start a conversation, Claude Code automatically loads two files in full:

1. **`CLAUDE.md`** — ARIA's identity, purpose, and rules (loaded top to bottom, every time)
2. **`memory/MEMORY.md`** — her index of what she's learned about you (the first ~200 lines / ~25KB, which is why this file stays short and mostly just points to other files)

Anything beyond that — like the detail files `MEMORY.md` links to — ARIA reads only when she decides she needs them, using her tools.

The **"My Rules"** section inside `CLAUDE.md` is optional. ARIA works fine without it, but anything you add there becomes part of what she always knows about how to behave.

---

## What You Will Do Today

| # | Lesson | Time |
|---|---|---|
| 02 | Open your agent — explore and customize | 20 min |
| 03 | Connect Gmail | 5 min |
| 04 | First conversation — ask ARIA about your spending | 20 min |
| 05 | Memory bank — teach ARIA, watch her remember | 15 min |
| 06 | Take home — make it yours | 10 min |

**Total: ~70 minutes + buffer**

You've already done the easy part at home (installing Claude Code). Today is all about connecting ARIA to your inbox and using what you built.

---

*Ready? Open `lessons/02_open_your_agent.md`*
