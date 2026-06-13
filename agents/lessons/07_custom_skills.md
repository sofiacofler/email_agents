# Lesson 07 — Bonus: Teaching ARIA a New Skill
**Time: ~15 minutes (optional, only if there's time left)**

---

## Beyond Tools: What's a "Skill"?

In Lesson 01 we said an agent is reasoning + tools + memory. That's enough for almost everything you've done today — you ask, ARIA figures out which tools to use and in what order, every time.

But some tasks aren't one-off questions. They're **workflows** — the same several steps, in the same order, done the same way, every time you run them. Re-explaining a 6-step process from scratch every time you need it is slow and easy to get wrong.

A **Skill** is a saved recipe: written instructions (and optionally small helper files or scripts) that ARIA can follow on demand, so you don't have to re-explain the steps each time.

> This is different from the "Going Further" idea in Lesson 06. Adding a new **connector** gives ARIA access to a new *system* (like Gmail or Google Drive). A **skill** is a saved *workflow* that uses the tools ARIA already has.

---

## When Does a Skill Make Sense?

Ask yourself:
- Will I do this again? (weekly, monthly, once a year — doesn't matter, as long as it repeats)
- Does it involve several steps, in a specific order, across one or more tools?
- Would I get it wrong, or forget a step, if I had to explain it from memory every time?

If yes to all three, it's a good candidate for a skill.

---

## Example: ARIA's "tax-refund" Skill

Imagine a task you'd only do **once a year**, right before filing taxes:

1. Search your work email for payslips (e.g. תלוש משכורת) from the past 12 months
2. Open each payslip PDF — they're password-protected, so the skill needs your password to unlock them
3. Pull out the relevant fields from each one (gross pay, tax withheld, date)
4. Search your email for the annual tax summary your employer sends (Form 106)
5. Add up the tax withheld across all 12 payslips
6. Compare that total against the figure on Form 106
7. Save all the payslips and the Form 106 into a folder in Google Drive, ready for your accountant

That's seven precise steps, using Gmail search, PDF parsing, a calculation, a comparison, and Google Drive — once a year, when you've probably forgotten exactly how you did it last time.

Without a skill, you'd have to re-explain all of this to ARIA every year. With a skill, you set it up once — and next year, you just run it.

---

## Building It With `skill-creator`

You don't write the skill file by hand. Claude Code comes with a built-in skill called **`skill-creator`** whose entire job is to help you build *new* skills through conversation.

To start, just tell ARIA what you want, in plain language:

```
I want to create a skill called "tax-refund". Once a year, it should:
search my email for payslips, open the password-protected PDFs,
pull out the tax withheld from each one, find my annual Form 106,
compare the totals, and save everything to a folder in Google Drive.
```

`skill-creator` will then:
- Ask you clarifying questions — what if a payslip is missing? What format is Form 106 in? Where in Google Drive should things go?
- Draft the skill's instructions for you
- Help you test it and refine it together until it works the way you expect

You stay in control the whole time — nothing is created without you confirming it.

---

## Where It's Saved

A skill is just a folder with a file called `SKILL.md` inside it — plain text, like everything else ARIA uses. `skill-creator` writes this file for you, in one of two places:

- **This project only**: `.claude/skills/tax-refund/SKILL.md` — lives inside this `agents` folder, alongside `financial_agent/`
- **Every project**: `~/.claude/skills/tax-refund/SKILL.md` — in your user folder, so ARIA can use it no matter which project you're in

`SKILL.md` holds the instructions in plain language — the same kind of text you'd write in `CLAUDE.md`. If the skill needs helper files (a script to open a password-protected PDF, a template for the output), those live in the same folder alongside it. You can open and read any of this in Obsidian or VS Code, exactly like the rest of ARIA's files.

---

## How to Call the Skill

Once it's built, the skill is saved as a file ARIA can find later. You can run it two ways:

- **Explicitly** — type `/tax-refund` and ARIA runs the whole workflow
- **Automatically** — if you just ask something that matches what the skill does (e.g. *"time to sort out my taxes"*), ARIA may recognize it and offer to run the skill herself

---

## Try It (If Time Allows)

The tax example needs a Google Drive connection and password-protected PDFs — a bit much for the time we have left. If you want to try the process now, pick something simpler from your own life, for example:

```
I want a skill called "monthly-summary". On the 1st of each month,
it should search my Gmail for last month's receipts, total them up
by category, and give me the result in the same table format every time.
```

Walk through the `skill-creator` conversation and see how far you get.

---

*That's the last building block: identity (`CLAUDE.md`), memory (`memory/`), and now skills — reusable workflows ARIA can run on command.*
