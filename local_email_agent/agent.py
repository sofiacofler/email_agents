import email
import imaplib
import json
import os
from datetime import datetime, timedelta
from email.header import decode_header
from pathlib import Path
from dotenv import load_dotenv

import httpx
import ollama

load_dotenv()

TASKS_FILE   = Path("tasks_store.json")
OLLAMA_MODEL = "llama3.2"  # or "mistral", "llama3.2", "phi3", "llama3.1:8b"
SUMMARY_DAYS = 5

CATEGORIES = ["school", "work", "household", "goodies", "health", "other"]

CATEGORY_EMOJI = {
    "school":    "🏫",
    "work":      "💼",
    "household": "🏠",
    "goodies":   "🎁",
    "health":    "🏥",
    "other":     "📌",
}


# ── Gmail fetch (IMAP) ────────────────────────────────────────────────────────

def decode_mime_header(value: str) -> str:
    parts = decode_header(value or "")
    result = []
    for part, encoding in parts:
        if isinstance(part, bytes):
            result.append(part.decode(encoding or "utf-8", errors="replace"))
        else:
            result.append(part)
    return "".join(result)


def extract_body(msg) -> str:
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and not part.get("Content-Disposition"):
                charset = part.get_content_charset() or "utf-8"
                return part.get_payload(decode=True).decode(charset, errors="replace")
    else:
        charset = msg.get_content_charset() or "utf-8"
        return msg.get_payload(decode=True).decode(charset, errors="replace")
    return ""


def fetch_yesterdays_emails() -> list[str]:
    gmail_user = os.getenv("GMAIL_USER")
    gmail_pass = os.getenv("GMAIL_APP_PASSWORD")

    yesterday = (datetime.now() - timedelta(days=1)).strftime("%d-%b-%Y")
    today     = datetime.now().strftime("%d-%b-%Y")

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(gmail_user, gmail_pass)
    mail.select("inbox")

    _, data = mail.search(None, f'(SINCE "{yesterday}" BEFORE "{today}")')
    message_ids = data[0].split()
    print(f"Found {len(message_ids)} emails.")

    email_texts = []
    for msg_id in message_ids[:15]:
        _, msg_data = mail.fetch(msg_id, "(RFC822)")
        raw_email  = msg_data[0][1]
        msg        = email.message_from_bytes(raw_email)

        subject = decode_mime_header(msg["Subject"])
        sender  = decode_mime_header(msg["From"])
        body    = extract_body(msg)[:2000]

        email_texts.append(f"Subject: {subject}\nFrom: {sender}\n\n{body}")

    mail.logout()
    return email_texts


# ── Telegram ──────────────────────────────────────────────────────────────────

def send_telegram(message: str):
    token   = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("Telegram not configured — skipping notification.")
        return
    httpx.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    )
    print("Telegram message sent.")


# ── Task storage ──────────────────────────────────────────────────────────────

def load_tasks() -> dict:
    if TASKS_FILE.exists():
        return json.loads(TASKS_FILE.read_text())
    return {}


def save_tasks(tasks: dict):
    TASKS_FILE.write_text(json.dumps(tasks, indent=2))


def prune_past_tasks(tasks: dict) -> dict:
    today = datetime.now().date()
    return {k: v for k, v in tasks.items() if datetime.fromisoformat(v["deadline"]).date() >= today}


# ── Ollama extraction ─────────────────────────────────────────────────────────

def extract_tasks_with_ollama(email_texts: list[str]) -> list[dict]:
    combined = "\n\n---\n\n".join(email_texts[:20])

    prompt = f"""You are a personal assistant. Today is {datetime.now().strftime('%Y-%m-%d')}.
Below are emails received yesterday.
Extract every actionable task that needs to be done at any point in the future.
Include tasks due next week, next month, or further ahead — not just the next 5 days.

For each task return a JSON object with:
- "title": short task name
- "deadline": ISO date string (YYYY-MM-DD), your best estimate of when this must be done
- "category": one of exactly these values: school, work, household, goodies, health, other
- "source": the email subject or sender

Return ONLY a valid JSON array. No markdown, no explanation.

EMAILS:
{combined}
"""
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response["message"]["content"].strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    try:
        tasks = json.loads(raw)
        for t in tasks:
            if t.get("category") not in CATEGORIES:
                t["category"] = "other"
        return tasks
    except json.JSONDecodeError:
        print(f"Could not parse LLM response as JSON:\n{raw}")
        return []


# ── Telegram summary (next 5 days only) ──────────────────────────────────────

def format_deadline(date_str: str) -> str:
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%a, %d %b %Y")


def build_summary_message(all_tasks: list[dict]) -> str:
    today  = datetime.now()
    cutoff = today + timedelta(days=SUMMARY_DAYS)

    upcoming = sorted(
        [t for t in all_tasks if today.date() <= datetime.fromisoformat(t["deadline"]).date() <= cutoff.date()],
        key=lambda t: t["deadline"]
    )

    lines = [f"📋 *Daily Task Summary — {today.strftime('%A, %d %b %Y')}*"]
    lines.append(f"_Tasks due in the next {SUMMARY_DAYS} days — {len(all_tasks)} total stored_\n")

    if not upcoming:
        lines.append("No tasks due in the next 5 days.")
    else:
        by_category = {cat: [] for cat in CATEGORIES}
        for t in upcoming:
            cat = t.get("category", "other")
            by_category[cat if cat in CATEGORIES else "other"].append(t)

        for cat in CATEGORIES:
            group = by_category[cat]
            if group:
                lines.append(f"\n{CATEGORY_EMOJI[cat]} *{cat.upper()}*")
                for t in group:
                    lines.append(f"  • {t['title']} — due {format_deadline(t['deadline'])}")
                    lines.append(f"    _from: {t.get('source', 'unknown')}_")

    lines.append(f"\n_Agent run at {today.strftime('%H:%M')}_")
    return "\n".join(lines)


# ── Main agent ────────────────────────────────────────────────────────────────

def run_agent():
    print("Starting Local Email Task Agent...")

    email_texts = fetch_yesterdays_emails()
    if not email_texts:
        print("No email content to process.")
        return

    print(f"Extracting all future tasks with {OLLAMA_MODEL}...")
    new_tasks = extract_tasks_with_ollama(email_texts)
    print(f"Found {len(new_tasks)} tasks.")

    stored = load_tasks()
    stored = prune_past_tasks(stored)
    for task in new_tasks:
        key = f"{task['title']}_{task['deadline']}"
        stored[key] = task
    save_tasks(stored)
    print(f"tasks_store.json updated — {len(stored)} active tasks saved.")

    all_tasks = list(stored.values())
    message   = build_summary_message(all_tasks)
    print("\n" + message + "\n")

    send_telegram(message)


if __name__ == "__main__":
    run_agent()
