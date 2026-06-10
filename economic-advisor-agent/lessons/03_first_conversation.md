# Lesson 03 — First Conversation
**Time: 20 minutes**

---

## What to Expect

When ARIA searches your Gmail, you will see her:
1. Call the Gmail search tool with a query she constructs
2. Get back a list of results (subject, sender, date, preview)
3. Open specific emails to get the full content
4. Synthesize everything into a human answer

You can watch all of this in real time. Each tool call appears as a collapsible block in Claude Code — click it to see exactly what was sent and what came back. There is nothing hidden.

---

## Warm-Up: Ask ARIA to Introduce Herself (2 minutes)

Start with something simple to confirm she knows who she is:

```
Hello! What can you help me with?
```

```
How do you access my Gmail? Can I trust that you won't delete anything?
```

ARIA should explain herself clearly, including the read-only security boundary of the Gmail connector.

---

## Finding Receipts (10 minutes)

Try these questions — adapt them to what you actually buy:

**General overview:**
```
Search my Gmail for receipts and invoices from the last 30 days.
Group them by category and give me a summary.
```

**Specific vendor:**
```
How much have I spent on Amazon in the last 3 months?
```

**Subscriptions:**
```
Find all recurring charges or subscriptions in my email.
List them with the amount and frequency if you can find it.
```

**Food and delivery:**
```
Find all food delivery receipts from this month and total them up.
```

**Biggest expenses:**
```
What is the most expensive single purchase you can find in my inbox
from the last 6 months?
```

---

## Watch the Tool Calls

In Claude Code, each time ARIA searches or opens an email, a block appears in the chat. Click to expand it.

You will see:
- **Input:** the exact Gmail search query she used
- **Output:** the raw list of emails returned

This matters for two reasons:
1. You can verify any answer by finding the email yourself
2. You can correct her search if she used the wrong query: *"Try searching for 'factura' too, I have Spanish receipts"*

---

## Follow-Up Questions (5 minutes)

Agents maintain context across a conversation. Try building on what she found:

```
Which of those was the most expensive single item?
```

```
Can you break the food spending down by month?
```

```
Are there any charges that look unfamiliar or that I might have forgotten about?
```

```
If I wanted to reduce spending by 10%, where would you start?
```

---

## If ARIA Finds Nothing

Gmail search is case-insensitive and supports operators. If she gets no results, guide her:

Instead of: *"find my bills"*
Try telling her: *"search for emails containing the words invoice, receipt, or order confirmation"*

Or be more specific:
```
Search for emails from noreply@amazon.com in the last 90 days
```

---

## A Note on Privacy

Email content is sent to Anthropic's servers for Claude to reason about — the same as if you copy-pasted an email into any Claude chat. Anthropic's standard privacy policy applies.

What does NOT happen: your emails going through any server we built or control. The path is strictly: **Gmail → Anthropic's Gmail connector → Claude**.

---

*Done? Open `lessons/04_memory_bank.md`*
