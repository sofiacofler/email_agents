# Local Email Task Agent — Installation Guide

Everything runs locally on your machine. No cloud services, no third-party accounts.
Your emails never leave your computer.

---

## What You Need to Install

| Tool | Purpose |
|---|---|
| Python 3.11+ | Runs the agent script |
| Ollama | Runs the local AI model |
| llama3.2 | The AI model that extracts tasks |

---

## Step 1 — Install Python

1. Go to [python.org/downloads](https://python.org/downloads)
2. Download the latest **Python 3.11+** installer (Windows)
3. Run the installer — **check "Add Python to PATH"** before clicking Install
4. Verify in a new terminal:
   ```
   python --version
   ```
   Should print something like `Python 3.11.9`

---

## Step 2 — Install Ollama

1. Go to [ollama.com](https://ollama.com)
2. Click **Download** → download the Windows installer
3. Run the installer — Ollama runs as a background service automatically
4. Verify in a terminal:
   ```
   ollama --version
   ```

---

## Step 3 — Download the AI Model

In a terminal, run:
```
ollama pull llama3.2
```

This downloads the model (~2 GB). You only need to do this once.

To verify it works:
```
ollama run llama3.2
```
Type anything and press Enter — you should get a response. Type `/bye` to exit.

---

## Step 4 — Enable Gmail IMAP

The agent reads your emails via IMAP — you need to turn it on in Gmail.

1. Open [Gmail](https://mail.google.com) → click the gear icon → **See all settings**
2. Go to the **Forwarding and POP/IMAP** tab
3. Under **IMAP access** → select **Enable IMAP**
4. Click **Save Changes**

---

## Step 5 — Create a Gmail App Password

Google does not allow scripts to log in with your real password. You need to create a special **App Password** — a separate 16-character password just for this agent.

**Requirement:** Your Google account must have 2-Step Verification turned on.

1. Go to [myaccount.google.com/security](https://myaccount.google.com/security)
2. Under **How you sign in to Google** → click **2-Step Verification** (turn it on if not already)
3. Go back to Security → scroll down to **App passwords**
   - If you don't see it, search "App passwords" in the search bar at the top
4. Click **Create app password**
   - App name: type anything, e.g. `Email Agent`
5. Google shows you a **16-character password** (format: `xxxx xxxx xxxx xxxx`)
6. Copy it — **you will only see it once**

---

## Step 6 — Create Your Telegram Bot

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

## Step 7 — Set Up the Project

Open a terminal and navigate to this folder:
```
cd path\to\email_agent_A
```

**Allow PowerShell scripts** (if not already done):
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Create and activate a virtual environment:**
```
python -m venv venv
venv\Scripts\activate
```

Your prompt should now show `(venv)`.

**Install dependencies:**
```
pip install -r requirements.txt
```

---

## Step 8 — Configure Your Secrets

Copy the example env file:
```
copy .env.example .env
```

Open `.env` in any text editor and fill in your values:
```
GMAIL_USER=your.email@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
TELEGRAM_BOT_TOKEN=123456789:ABCdef...
TELEGRAM_CHAT_ID=123456789
```

> The App Password can be entered with or without spaces — both work.

---

## Step 9 — Run the Agent

Make sure Ollama is running (it starts automatically on Windows after install).

With your virtual environment active:
```
python agent.py
```

You should see output like:
```
Starting Email Task Agent (Option A — Local)...
Found 12 emails.
Extracting all future tasks with llama3.2...
Found 5 tasks.
tasks_store.json updated — 5 active tasks saved.
Telegram message sent.
```

---

## Step 10 — Schedule Daily Runs (Windows Task Scheduler)

To run the agent automatically every morning:

1. Open **Task Scheduler** (search in Start menu)
2. Click **Create Basic Task**
3. Name: `Email Task Agent`
4. Trigger: **Daily** → set your preferred time (e.g. 8:00 AM)
5. Action: **Start a program**
   - Program: full path to your Python inside venv, e.g.:
     ```
     C:\path\to\email_agent_A\venv\Scripts\python.exe
     ```
   - Arguments:
     ```
     agent.py
     ```
   - Start in:
     ```
     C:\path\to\email_agent_A
     ```
6. Click **Finish**

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `python` not found | Re-install Python and check "Add to PATH" |
| `ollama` not found | Restart terminal after installing Ollama |
| IMAP login failed | Double-check App Password — use the one from Google, not your real password |
| `imaplib.error: LOGIN failed` | Make sure IMAP is enabled in Gmail settings (Step 4) |
| No tasks found | The model may need a warmer prompt — try `ollama run llama3.2` manually first |
| Telegram message not sent | Verify token and chat ID, and make sure you messaged the bot at least once |

---

## Changing the AI Model

Edit line 16 in `agent.py`:
```python
OLLAMA_MODEL = "llama3.2"  # change to "mistral", "phi3", or "llama3.1:8b"
```

Then pull the new model before running:
```
ollama pull mistral
```
