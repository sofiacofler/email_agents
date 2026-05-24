# Google Email Task Agent — Installation Guide

No installation required. Everything runs in your browser on Google's servers.
Your emails stay within Google's infrastructure.

---

## What You Need

| Tool | Purpose | Cost |
|---|---|---|
| Google account | Runs the script + reads Gmail | Free |
| Gemini API key | The AI model that extracts tasks | Free |
| Telegram bot | Receives your daily summary | Free |

---

## Step 1 — Get a Free Gemini API Key

1. Go to [aistudio.google.com](https://aistudio.google.com) and sign in with your Google account
2. Click **Get API key** (top left)
3. Click **Create API key** → select any project (or create one)
4. Copy the key — keep it somewhere safe, you'll need it in Step 4

---

## Step 2 — Create Your Telegram Bot

The agent sends your daily summary to Telegram.

1. Open Telegram → search for **@BotFather** → start a chat
2. Send the command `/newbot`
3. Choose a name (e.g. `My Task Agent`) and a username ending in `bot` (e.g. `mytaskagent_bot`)
4. BotFather gives you a **token** — copy it (looks like `123456789:ABCdef...`)

**Get your Chat ID:**
1. Send any message to your new bot
2. Open this URL in your browser (replace `YOUR_TOKEN`):
   ```
   https://api.telegram.org/botYOUR_TOKEN/getUpdates
   ```
3. Find `"chat":{"id":...}` in the response — that number is your Chat ID

---

## Step 3 — Create the Apps Script Project

1. Go to [script.google.com](https://script.google.com) and sign in
2. Click **New project** (top left)
3. Click the project name **"Untitled project"** at the top → rename it to `Email Task Agent`
4. Delete all the default code in the editor
5. Open the file `agent.gs` from this folder → copy the entire contents
6. Paste it into the Apps Script editor
7. Click the **Save** icon (or press `Ctrl+S`)

---

## Step 4 — Add Your Secrets

Never paste API keys directly into the code. Apps Script has a built-in secrets manager called **Script Properties**.

1. In the Apps Script editor, click the **gear icon** (Project Settings) in the left sidebar
2. Scroll down to **Script Properties**
3. Click **Add script property** and add these three properties one by one:

| Property name | Value |
|---|---|
| `GEMINI_API_KEY` | Your key from Step 1 |
| `TELEGRAM_BOT_TOKEN` | Your bot token from Step 2 |
| `TELEGRAM_CHAT_ID` | Your Chat ID from Step 2 |

4. Click **Save script properties**

---

## Step 5 — Approve Permissions

The script needs permission to access your Gmail and Google Drive. This only happens once.

1. In the editor, click the function dropdown (next to the Run button) and select **`runAgent`**
2. Click **Run**
3. A popup appears: **"Authorization required"** → click **Review permissions**
4. Choose your Google account
5. You may see **"Google hasn't verified this app"** — click **Advanced** → **Go to Email Task Agent (unsafe)**
   - This is normal for personal scripts you write yourself
6. Review the permissions and click **Allow**

The script will run for the first time. Check the **Execution log** at the bottom for output.

---

## Step 6 — Set Up the Daily Trigger

This makes the agent run automatically every morning without you doing anything.

1. In the function dropdown, select **`setupTrigger`**
2. Click **Run**
3. You should see in the log: `Daily trigger set for 8:00 AM.`

To verify:
- Click the **clock icon** (Triggers) in the left sidebar
- You should see one trigger: `runAgent` — Time-driven — Day timer — 8am to 9am

To change the time, edit line 193 in the script:
```javascript
.atHour(8)   // change to any hour 0–23
```
Then run `setupTrigger` again.

---

## Step 7 — Verify It Works

Run the agent manually to confirm everything is connected:

1. Select **`runAgent`** in the function dropdown
2. Click **Run**
3. Watch the **Execution log** — you should see:
   ```
   Fetched 12 emails.
   Extracted 5 tasks from emails.
   Sheet updated — 5 active tasks stored.
   Telegram message sent.
   ```
4. Check your Telegram — the summary should arrive within a few seconds
5. Check your Google Drive — a spreadsheet called **"Email Agent Tasks"** should appear with all extracted tasks

---

## What Gets Created Automatically

| Item | Where |
|---|---|
| **Email Agent Tasks** spreadsheet | Your Google Drive (root folder) |
| **Daily trigger** | Apps Script → Triggers |

The spreadsheet stores all future tasks with columns: `title`, `deadline`, `category`, `source`. You can open and edit it directly in Google Sheets at any time.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `Exception: Invalid argument` on Gemini call | Check your `GEMINI_API_KEY` in Script Properties |
| No emails found | The search covers yesterday only — run on a day after you received emails |
| Telegram message not sent | Verify `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`, and make sure you messaged the bot at least once |
| Permission denied on Gmail | Re-run Step 5 — delete the script and re-paste if needed |
| Trigger not firing | Check the Triggers panel — delete and re-run `setupTrigger` |
| "Could not parse Gemini response as JSON" | Gemini returned unexpected output — try running again, it's usually a one-off |

---

## Changing the AI Model

Edit line 14 in `agent.gs`:
```javascript
const GEMINI_MODEL = 'gemini-2.5-flash';  // or 'gemini-2.0-flash', 'gemini-2.5-pro'
```

Available free-tier models: `gemini-2.5-flash` (recommended), `gemini-2.0-flash`, `gemini-2.5-pro` (slower, smarter).

---

## Changing the Summary Window

Edit line 15 in `agent.gs`:
```javascript
const SUMMARY_DAYS = 5;  // change to any number of days
```

All future tasks are always stored — this only affects how many days appear in the Telegram summary.
