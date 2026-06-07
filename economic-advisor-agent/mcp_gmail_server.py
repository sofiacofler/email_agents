"""
Gmail MCP Server — Read Only
============================
This server exposes two tools to Claude:
  - search_emails: search for emails by keyword/query
  - read_email: read the full body of a specific email

Security: Only the gmail.readonly OAuth scope is requested.
Google enforces this at the API level — this server cannot send,
delete, or modify emails even if instructed to.

Participants: you do not need to modify this file.
"""

import json
import base64
import asyncio
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# ── Security boundary ─────────────────────────────────────────────────────────
# This is the only Gmail permission we request. Google will reject any
# attempt to send, delete, or modify emails with a 403 error.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

BASE_DIR = Path(__file__).parent
CREDENTIALS_FILE = BASE_DIR / "credentials.json"
TOKEN_FILE = BASE_DIR / "token.json"

# ── Gmail authentication ──────────────────────────────────────────────────────

def get_gmail_service():
    """Authenticate with Gmail and return a service object."""
    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                raise FileNotFoundError(
                    "credentials.json not found.\n"
                    "Please follow lesson 01 to set up your Google Cloud credentials."
                )
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


# ── MCP server setup ──────────────────────────────────────────────────────────

mcp = FastMCP("gmail-readonly")


@mcp.tool()
def search_emails(query: str, max_results: int = 10) -> str:
    """
    Search Gmail for emails matching a query.
    Returns a list of emails with subject, sender, date, and a short preview.

    Args:
        query: Gmail search syntax, e.g. "receipt OR invoice from:amazon"
        max_results: How many results to return (max 50)
    """
    service = get_gmail_service()
    max_results = min(max_results, 50)

    results = service.users().messages().list(
        userId="me",
        q=query,
        maxResults=max_results
    ).execute()

    messages = results.get("messages", [])
    if not messages:
        return json.dumps({"count": 0, "emails": [], "note": "No emails found for this query."})

    emails = []
    for msg in messages:
        msg_data = service.users().messages().get(
            userId="me",
            id=msg["id"],
            format="metadata",
            metadataHeaders=["Subject", "From", "Date"]
        ).execute()

        headers = {h["name"]: h["value"] for h in msg_data["payload"]["headers"]}
        emails.append({
            "id": msg["id"],
            "subject": headers.get("Subject", "(no subject)"),
            "from": headers.get("From", ""),
            "date": headers.get("Date", ""),
            "preview": msg_data.get("snippet", "")
        })

    return json.dumps({"count": len(emails), "emails": emails}, indent=2, ensure_ascii=False)


@mcp.tool()
def read_email(message_id: str) -> str:
    """
    Read the full content of a specific email.
    Use the message ID returned by search_emails.

    Args:
        message_id: The Gmail message ID from search_emails results
    """
    service = get_gmail_service()

    msg = service.users().messages().get(
        userId="me",
        id=message_id,
        format="full"
    ).execute()

    headers = {h["name"]: h["value"] for h in msg["payload"]["headers"]}

    body = _extract_body(msg["payload"])

    return json.dumps({
        "id": message_id,
        "subject": headers.get("Subject", "(no subject)"),
        "from": headers.get("From", ""),
        "date": headers.get("Date", ""),
        "body": body[:4000]  # cap at 4000 chars to stay within context limits
    }, indent=2, ensure_ascii=False)


def _extract_body(payload: dict) -> str:
    """Recursively extract plain text body from a Gmail message payload."""
    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                data = part["body"].get("data", "")
                if data:
                    return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
        # fallback: recurse into first part
        for part in payload["parts"]:
            result = _extract_body(part)
            if result:
                return result

    data = payload.get("body", {}).get("data", "")
    if data:
        return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")

    return ""


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
