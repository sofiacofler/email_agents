# Lesson 04 — The Memory Bank
**Time: 15 minutes**

---

## The Problem With Regular Chatbots

Every time you start a new conversation with a chatbot, it has forgotten everything:
- "My budget for food is 400 euros per month" — forgotten
- "I prefer bullet points" — forgotten
- "I use euros, not dollars" — forgotten

You repeat yourself every session. An agent with a memory bank doesn't have this problem.

---

## How ARIA's Memory Works

ARIA's memory is a folder of plain text files on your laptop:

```
memory/
├── MEMORY.md                    ← the index (what files exist)
└── user_financial_profile.md    ← one memory file
    (more files appear as ARIA learns things)
```

When ARIA learns something worth keeping, she:
1. Creates or updates a file in `memory/`
2. Adds or updates a line in `MEMORY.md` pointing to it

When you start a new conversation, Claude Code loads `MEMORY.md` automatically. ARIA reads the index and knows what to remember — without you saying anything.

**This is not magic. It is a text file.** You can open it, edit it, delete entries, or pre-fill it before the first conversation.

---

## Teach ARIA Something (5 minutes)

Try these in the chat:

```
Remember that my monthly budget for food is 500 euros.
```

```
Remember that I don't have any streaming service subscriptions.
Flag anything that looks like Netflix, Spotify, or similar.
```

```
Remember that I work somewhere that reimburses travel expenses.
When you find travel receipts, note which ones might be reimbursable.
```

After each one, open `memory/MEMORY.md` in the file explorer and watch what appeared. Then open the linked file to read the full memory entry.

---

## Verify the Memory Works Across Sessions

This is the key demonstration. Do the following:

1. Close the current chat in Claude Code (start a new conversation)
2. Type:

```
What do you remember about my financial preferences?
```

ARIA should answer accurately — without you having said anything in this new session.

That is the difference between a chatbot and an agent.

---

## Edit Memory Directly

Memory files are plain text. You do not need to ask ARIA to update them — you can edit them yourself like any document.

Try it now:
1. Open `memory/user_financial_profile.md`
2. Fill in a few fields: currency, a budget goal, how you like summaries presented
3. Save the file
4. Start a new conversation and ask ARIA what she knows about you

She will reflect what you wrote, without any conversation having happened.

This is powerful for pre-loading an agent before first use.

---

## Correcting a Wrong Memory

If ARIA saved something incorrect, just tell her:

```
Forget what you saved about my food budget — the number was wrong.
```

She will remove or correct it. You can also do it manually: open the file, edit the line, save.

---

## What Is Worth Remembering?

| Good to remember | Not worth remembering |
|---|---|
| Budget limits per category | Specific past purchases (emails are the source of truth) |
| Currency and display preferences | One-off questions or answers |
| Recurring subscriptions confirmed | Anything that changes often |
| Vendors to always flag | |
| How you like summaries presented | |

---

*Done? Open `lessons/05_take_home.md`*
