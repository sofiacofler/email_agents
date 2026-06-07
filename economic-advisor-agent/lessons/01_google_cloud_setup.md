# Lesson 01 — Google Cloud Setup
**Time: 20 minutes**

---

## What We Are Doing

We need to tell Google: "I allow this program to read my Gmail." Google handles this through a system called **OAuth** — the same system you use when you click "Sign in with Google" on a website.

At the end of this lesson you will have a file called `credentials.json` in the agent folder. That file is ARIA's identity card with Google.

> **Privacy note:** The `credentials.json` file is personal. Do not share it, commit it to git, or send it by email. It is already listed in `.gitignore`.

---

## Step 1 — Go to Google Cloud Console

1. Open your browser and go to: **console.cloud.google.com**
2. Sign in with the Gmail account whose receipts you want to analyze
3. You may be asked to agree to terms of service — accept them

---

## Step 2 — Create a New Project

1. Click the project dropdown at the top of the page (it may say "Select a project")
2. Click **New Project**
3. Name it: `aria-advisor` (or anything you like)
4. Click **Create**
5. Wait ~10 seconds, then make sure your new project is selected in the dropdown

---

## Step 3 — Enable the Gmail API

1. In the left sidebar, go to **APIs & Services → Library**
2. Search for `Gmail API`
3. Click on it, then click **Enable**
4. Wait for it to activate (a few seconds)

---

## Step 4 — Create OAuth Credentials

1. Go to **APIs & Services → Credentials**
2. Click **+ Create Credentials → OAuth client ID**
3. If prompted to configure the OAuth consent screen:
   - Choose **External**
   - Fill in App name: `ARIA Advisor`
   - Fill in your email as the support contact
   - Click **Save and Continue** through all steps (defaults are fine)
   - On the "Test users" step, add your own Gmail address
4. Back on the Credentials page, click **+ Create Credentials → OAuth client ID** again
5. Application type: **Desktop app**
6. Name: `ARIA Local`
7. Click **Create**

---

## Step 5 — Download credentials.json

1. A dialog appears with your Client ID and Secret — click **Download JSON**
2. Rename the downloaded file to exactly: `credentials.json`
3. Move it into the `economic-advisor-agent/` folder (same folder as `CLAUDE.md`)

Your folder should now look like this:
```
economic-advisor-agent/
├── CLAUDE.md
├── credentials.json        ← new file you just added
├── mcp_gmail_server.py
├── requirements.txt
...
```

---

## Step 6 — Install Python Dependencies

Open a terminal in the `economic-advisor-agent/` folder and run:

```bash
pip install -r requirements.txt
```

This installs the Gmail library and the MCP framework. It takes about a minute.

---

## Step 7 — Test the Connection

Run this command in the terminal:

```bash
python mcp_gmail_server.py
```

A browser window will open asking you to sign in with Google and grant permission. You will see:

> "ARIA Advisor wants to: View your email messages and settings"

Click **Allow**. The terminal will show `Running on stdio` — that means it's working.

Press `Ctrl+C` to stop it. You only need to do this browser authorization once. From now on, ARIA will use the saved `token.json` file.

---

## Checkpoint

You should now have these files in the folder:
- `credentials.json` — your Google identity card
- `token.json` — the authorization token (created automatically)

If you see errors, check:
- Did you add your Gmail as a test user in step 4?
- Is the file named exactly `credentials.json` (not `credentials (1).json`)?
- Are you in the right folder when running `pip install`?

---

*Done? Open `lessons/02_meet_your_agent.md`*
