# Lesson 01 — Welcome: What Are We Building?
**Time: 15 minutes**

---

## What is an AI Agent?

A regular AI chatbot answers one question at a time and forgets everything when the conversation ends.

An **agent** is different in three ways:

| | Chatbot | Agent |
|---|---|---|
| **Memory** | Forgets after every session | Remembers across conversations |
| **Tools** | Can only talk | Can read files, call APIs, search systems |
| **Identity** | Generic | Has a name, purpose, and rules you define |

Think of it like hiring a specialist:
- You give them a **job description** — what they do, how they behave, what they're not allowed to do
- You give them **tools** — access to the systems they need
- You give them a **desk** — somewhere to take notes between meetings

---

## What We Built for Today

Meet **ARIA** — Adaptive Receipt & Income Advisor.

ARIA is a personal economic advisor that:
- Reads the receipts and order confirmations in your Gmail inbox
- Answers questions like "How much did I spend on food last month?"
- Tracks subscriptions you may have forgotten
- Remembers your preferences and budget goals across conversations

By the end of this workshop you will have made ARIA your own and had your first real conversation with her about your spending.

---

## The Three Things That Make ARIA an Agent

```
economic-advisor-agent/
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

## What is MCP?

**MCP (Model Context Protocol)** is a standard way to give an AI access to external tools — the same way a browser extension connects a website to your browser.

In our case, the **Gmail connector** is built and hosted by Anthropic. It:
- Connects to your Gmail account (you authorized it in Lesson 00)
- Gives ARIA the ability to search your inbox and read individual emails
- Is read-only — it cannot send, delete, or modify anything

> **The security guarantee:** The connector requests **read-only** access to your Gmail. This is not a setting or a promise — it is enforced by Google's authorization servers. Even if ARIA tried to delete an email, Google would reject the request. Physically impossible.

---

## What You Will Do Today

| # | Lesson | Time |
|---|---|---|
| 02 | Open your agent — explore and customize | 20 min |
| 03 | First conversation — ask ARIA about your spending | 20 min |
| 04 | Memory bank — teach ARIA, watch her remember | 15 min |
| 05 | Take home — make it yours | 10 min |

**Total: ~65 minutes + buffer**

You've already done the hard part at home (setup). Today is all about using and understanding what you built.

---

*Ready? Open `lessons/02_open_your_agent.md`*
