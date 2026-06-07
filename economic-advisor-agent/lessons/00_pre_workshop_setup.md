# Before the Workshop — Setup at Home
**Do this before you arrive. Estimated time: 25 minutes.**

---

You only need to do this once. If you run into trouble, contact the workshop organizer in advance — we won't have time to troubleshoot installations during the session.

---

## What You Need to Install

### 1 — Python 3.9 or newer

Check if you already have it:
```
python --version
```
If you see `Python 3.9.x` or higher, skip to step 2.

If not, download from **python.org/downloads** and install it.
During installation on Windows: check the box **"Add Python to PATH"**.

### 2 — Claude Code

Download from **claude.ai/download** and install the desktop app.
Sign in with your Anthropic account (or create a free one).

---

## The Agent Folder

You received a folder called `economic-advisor-agent/`. Place it somewhere easy to find on your computer (Desktop or Documents works fine).

---

## Google Cloud Setup (read-only Gmail access)

We need to tell Google: "I allow this program to read my Gmail."
This uses **OAuth** — the same system as "Sign in with Google" on any website.
The permission is strictly read-only: Google will reject any attempt to send or delete emails.

### Step 1 — Go to Google Cloud Console
Open your browser and go to: **console.cloud.google.com**
Sign in with the Gmail account whose receipts you want to analyze.

### Step 2 — Create a New Project
1. Click the project dropdown at the top (it may say "Select a project")
2. Click **New Project**
3. Name it `aria-advisor` → click **Create**
4. Wait ~10 seconds, then confirm your new project is selected in the dropdown

### Step 3 — Enable the Gmail API
1. Left sidebar → **APIs & Services → Library**
2. Search for `Gmail API`
3. Click it → click **Enable**

### Step 4 — Configure the OAuth Consent Screen
1. Left sidebar → **APIs & Services → OAuth consent screen**
2. Choose **External** → click **Create**
3. Fill in:
   - App name: `ARIA Advisor`
   - User support email: your email
   - Developer contact email: your email
4. Click **Save and Continue** through all remaining steps (defaults are fine)
5. On the **Test users** step: click **Add users** and add your own Gmail address
6. Click **Save and Continue** → **Back to Dashboard**

### Step 5 — Create OAuth Credentials
1. Left sidebar → **APIs & Services → Credentials**
2. Click **+ Create Credentials → OAuth client ID**
3. Application type: **Desktop app**
4. Name: `ARIA Local` → click **Create**
5. Click **Download JSON** in the dialog that appears
6. Rename the downloaded file to exactly: `credentials.json`
7. Move it into the `economic-advisor-agent/` folder

Your folder should now look like this:
```
economic-advisor-agent/
├── CLAUDE.md
├── credentials.json        ← the file you just added
├── mcp_gmail_server.py
├── requirements.txt
...
```

> **Keep this file private.** Do not share it or send it by email. It is your personal access card.

---

## Install Python Dependencies

Open a terminal (on Windows: search for "Command Prompt" or "PowerShell") and navigate to the agent folder:

```
cd path\to\economic-advisor-agent
```

Then run:
```
pip install -r requirements.txt
```

This installs the Gmail library and MCP framework. It takes about a minute.

---

## Authorize Gmail Access (one-time)

Run this command in the same terminal:

```
python mcp_gmail_server.py
```

A browser window will open. Google will ask:

> *"ARIA Advisor wants to: View your email messages and settings"*

Click **Allow**. The terminal will show `Running on stdio` — that means it worked.

Press `Ctrl+C` to stop it. You will not need to do this again — the authorization is saved in a file called `token.json`.

---

## You're Ready

Bring your laptop to the workshop with:

- [ ] Python installed
- [ ] Claude Code installed and signed in
- [ ] The `economic-advisor-agent/` folder on your machine
- [ ] `credentials.json` inside the folder
- [ ] `pip install -r requirements.txt` completed
- [ ] The browser authorization done (token.json created)

**See you at the workshop!**
