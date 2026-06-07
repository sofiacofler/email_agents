# Lesson 00 — Welcome: What Are We Building?
**Time: 15 minutes**

---

## What is an AI Agent?

A regular AI chatbot answers one question at a time and forgets everything when the conversation ends.

An **agent** is different in three ways:

| | Chatbot | Agent |
|---|---|---|
| **Memory** | Forgets after every session | Remembers across conversations |
| **Tools** | Can only talk | Can read files, search, call APIs |
| **Identity** | Generic | Has a name, purpose, and rules |

Think of an agent as a specialized employee you hire for one job. You give them:
- A **job description** (what they do)
- **Tools** (what they can access)
- A **desk** (a place to take notes)

---

## What Are We Building Today?

We are building **ARIA** — a personal economic advisor that:

1. Reads the receipts and order confirmations in your Gmail inbox
2. Answers questions about your spending
3. Remembers what it learns about your financial habits over time

By the end of this workshop you will have a working agent running on your laptop.

---

## The Three Files That Make ARIA Work

```
economic-advisor-agent/
│
├── CLAUDE.md              ← The job description (who ARIA is, what she does)
│
├── mcp_gmail_server.py    ← The tool (connects to Gmail, read-only)
│
└── memory/
    └── MEMORY.md          ← The desk (what ARIA remembers between sessions)
```

That's it. No database, no server, no deployment. Everything runs on your laptop.

---

## What is MCP?

**MCP (Model Context Protocol)** is a standard way to give an AI agent access to external tools.

In our case, the MCP server is a small Python program (`mcp_gmail_server.py`) that:
- Connects to Gmail using your credentials
- Exposes two tools to ARIA: `search_emails` and `read_email`
- Runs locally on your machine — your emails never go anywhere unexpected

> **Security note:** We use the `gmail.readonly` OAuth scope. This is a permission enforced by Google's servers. Even if ARIA wanted to delete an email, Google would reject the request. This is not a promise or a setting — it's a cryptographic boundary.

---

## What You Will Do in This Workshop

| # | Lesson | Time | What happens |
|---|---|---|---|
| 01 | Google Cloud Setup | 20 min | Get credentials to read your Gmail |
| 02 | Meet Your Agent | 15 min | Open the folder, customize ARIA |
| 03 | First Conversation | 20 min | Ask ARIA about your spending |
| 04 | Memory Bank | 15 min | Teach ARIA something, watch her remember it |
| 05 | Take Home | 10 min | Ideas for making ARIA yours |

**Total: ~85 minutes + 5 min buffer**

---

*Ready? Open `lessons/01_google_cloud_setup.md` to begin.*
