# Lesson 03 — First Conversation
**Time: 20 minutes**

---

## What to Expect

When ARIA searches your Gmail, you will see her:
1. Call the `search_emails` tool with a query
2. Get back a list of results
3. Call `read_email` on specific ones to get the details
4. Synthesize what she found into an answer

You can watch all of this happen in real time. Each tool call is visible in Claude Code — you can expand it to see exactly what was sent and what came back.

---

## Warm-Up Questions (5 minutes)

Start simple. Type these into the chat:

```
Hello! What can you help me with?
```

```
How do you access my Gmail? Can you explain the security?
```

These test that ARIA understands her own identity and can explain herself clearly.

---

## Finding Receipts (10 minutes)

Now try these — adapt them to what you actually buy:

**General receipt search:**
```
Search my Gmail for receipts and invoices from the last 30 days. 
Give me a list grouped by category.
```

**Specific vendor:**
```
How much have I spent on Amazon in the last 3 months?
```

**Subscriptions:**
```
Find all recurring charges or subscriptions in my email. 
List them with the amount and frequency.
```

**Food & delivery:**
```
Find all food delivery receipts (Uber Eats, Wolt, Deliveroo, etc.) 
from this month and total them up.
```

---

## Watch What Happens Under the Hood

In Claude Code, each tool call appears as a collapsible block. Click on one to see:

- **Input:** the Gmail search query ARIA constructed
- **Output:** the raw list of emails returned

This is important: ARIA is not guessing. She is reading actual emails from your account and reasoning about their content. You can verify any answer by finding the email yourself.

---

## Asking Follow-Up Questions (5 minutes)

Agents remember the context of a conversation. Try:

```
Which of those was the most expensive?
```

```
Can you break that down by month?
```

```
Was there anything that surprised you?
```

```
Are there any charges that look unusual or that I might have forgotten about?
```

---

## If ARIA Finds Nothing

Sometimes the search query doesn't match. Try rephrasing:

Instead of: `"find my bills"`  
Try: `"search for emails with the word invoice, receipt, or order confirmation"`

Gmail search is powerful. ARIA uses the same syntax as the Gmail search bar. You can also tell her exactly what to search for:

```
Search for emails from: noreply@amazon.com in the last 60 days
```

---

## A Note on Privacy

Everything you ask ARIA stays in your conversation with Claude. The email content is sent to Anthropic's servers for Claude to reason about — the same as if you had copy-pasted an email into any Claude chat. Anthropic's privacy policy applies.

What does NOT happen: your emails going through any third-party server we built or control. The path is: Gmail → your laptop → Claude's API.

---

*Done? Open `lessons/04_memory_bank.md`*
