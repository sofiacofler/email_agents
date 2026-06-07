# Lesson 02 — Open Your Agent
**Time: 20 minutes**

---

## Step 1 — Activate ARIA in Claude Code

1. Open **Claude Code** (the desktop app)
2. Click **Open Folder** and select the `economic-advisor-agent/` folder
3. Claude Code reads `CLAUDE.md` automatically on startup

That's it. ARIA is now active. Every conversation in this folder uses her identity, rules, and memory.

---

## Step 2 — Explore the Files

Take 10 minutes to open and read these files. You do not need to change anything yet.

### `CLAUDE.md` — The Job Description
This is the most important file. Open it and read through it.

Notice:
- The rules are written in plain language — no code
- There is a "How to Talk to Me" section with example questions
- At the bottom: *"You can rename me by changing 'ARIA' throughout this file"*

**This file is your control panel.** Anything you write here shapes ARIA's behavior.

### `memory/MEMORY.md` — The Notebook Index
ARIA's notes. Currently it only has the starter profile. As you have conversations, this grows. Each entry is a link to a file with more detail.

### `memory/user_financial_profile.md` — The Profile Template
A template of what ARIA will learn about you. Fields are empty — she fills them in during conversations, or you can fill them in directly right now.

### `.claude/settings.json` — The Wiring
The technical connection. It tells Claude Code: "when this folder is open, run `mcp_gmail_server.py` as a tool." You do not need to change this.

---

## Step 3 — Customize ARIA (5 minutes)

Make at least two changes to make this agent yours:

**Change 1: Rename the agent**
Open `CLAUDE.md`. Find every instance of "ARIA" and replace it with a name you prefer. Save the file.

**Change 2: Set your currency**
Open `memory/user_financial_profile.md`. Find the line:
```
- **Currency:** (not yet set — tell ARIA your preferred currency)
```
Change it to your currency (e.g., `EUR`, `USD`, `ILS`). Save the file.

**Optionally: Add a personal rule**
In `CLAUDE.md`, find the "My Rules" section and add something like:
- *"Always flag any single expense over 200 euros"*
- *"I am interested in food delivery more than anything else"*
- *"Never show more than 10 results at a time"*

---

## Step 4 — First Run: Verify Everything Works

Let's confirm the Gmail connection is working. Type this into the chat:

```
Can you search my email for the word "receipt" and show me the 3 most recent results?
```

You should see ARIA:
1. Call the `search_emails` tool (visible as a collapsible block in the chat)
2. Return a list of emails with subject, sender, and date
3. Summarize what she found

**If it works:** great — move to Lesson 03.

**If you see an error:**

| Error message | Fix |
|---|---|
| `credentials.json not found` | The file is missing from the folder — see Lesson 00 |
| `token.json` not found / auth error | Run `python mcp_gmail_server.py` in a terminal, complete the browser auth |
| MCP not connecting | Close and reopen Claude Code with this folder |
| No results found | Try: `"search for invoice OR order OR confirmation"` |

---

## The Key Insight

> **The agent is the folder.**

To share ARIA with a colleague:
1. Copy the folder to their machine
2. They add their own `credentials.json`
3. They open it in Claude Code
4. They have their own instance, connected to their own Gmail

The agent's identity and behavior travel with the folder. The only personal part is the credentials.

---

*Everything working? Open `lessons/03_first_conversation.md`*
