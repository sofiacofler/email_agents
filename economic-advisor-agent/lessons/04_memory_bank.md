# Lesson 04 — The Memory Bank
**Time: 15 minutes**

---

## The Problem With Chatbots

Every time you start a new conversation with a regular chatbot, it has forgotten everything. You have to repeat yourself:
- "My budget for food is 400 euros per month"
- "I prefer summaries in bullet points"
- "I use euros, not dollars"

An agent with memory doesn't have this problem.

---

## How ARIA's Memory Works

ARIA's memory is just a folder of text files:

```
memory/
├── MEMORY.md                    ← the index (what exists)
└── user_financial_profile.md    ← a memory file
    (more files created as needed)
```

When ARIA learns something worth keeping, she:
1. Writes it to a file in `memory/`
2. Adds a line to `MEMORY.md` pointing to it

When you start a new conversation, Claude Code automatically loads `MEMORY.md`. ARIA reads the index and knows what she remembers — and can read any specific file when needed.

**This is not magic. It is a text file.** You can open it, edit it, or delete entries.

---

## Teaching ARIA Something

Try these phrases in the chat:

```
Remember that my monthly budget for food is 500 euros.
```

```
Remember that I don't use any streaming services — 
flag anything that looks like Netflix or Spotify.
```

```
Remember that I work for a company that reimburses travel expenses. 
When you find travel receipts, note which ones might be reimbursable.
```

After each one, open `memory/MEMORY.md` and see what appeared. Then open the linked file to see the full memory entry.

---

## Verifying the Memory Works

Start a **new conversation** (close the chat and open a new one in the same folder). Then ask:

```
What do you remember about my financial preferences?
```

ARIA should be able to answer without you having told her anything in this new session — because she read it from the memory files.

This is the key difference between a chatbot and an agent.

---

## Editing Memory Directly

Memory files are plain text. You can edit them like any document:

1. Open `memory/user_financial_profile.md`
2. Fill in your currency, budget goals, preferences
3. Save the file

The next time you talk to ARIA, she will know what you wrote — no conversation required.

This is powerful: you can pre-load an agent with knowledge before the first conversation.

---

## Forgetting Something

If ARIA saved something incorrect, just tell her:

```
Forget what you saved about my food budget — it was wrong.
```

She will remove the entry from `MEMORY.md` and delete or update the file.

You can also do it manually: open the file, delete the lines, save.

---

## What's Worth Remembering?

Good things to put in memory:
- Budget limits per category
- Currencies and preferred formats
- Vendors you want flagged
- Recurring subscriptions you've confirmed (so she doesn't re-analyze them)
- How you like information presented

Not worth putting in memory:
- Specific past spending (that's in the emails — she can always look it up)
- One-off questions or answers

---

*Done? Open `lessons/05_take_home.md`*
