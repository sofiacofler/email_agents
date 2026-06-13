# Lesson 03 — Connect Gmail
**Time: 5 minutes**

---

ARIA needs permission to read your Gmail before she can do anything useful. We use Google's Gmail connector — the same kind of "Sign in with Google" flow you've used on other websites. A few clicks, no files to download, no code.

---

## Step 1 — Open Settings

In Claude Code (or Claude Desktop), open **Settings → Connectors**.

---

## Step 2 — Add the Gmail connector

1. Find **Gmail** in the list of connectors and click **Connect** (or **Add**)
2. A browser window will open and ask you to sign in with the Google account whose receipts you want to analyze
3. Review the permissions screen — Google may list more than just reading (e.g., managing drafts). That's expected; Step 3 below locks down what ARIA is actually allowed to use
4. Click **Allow**

---

## Step 3 — Set tool permissions (important)

This connector technically *can* create drafts, in addition to reading mail. We're going to lock that down so ARIA can only read — never write.

1. Still in **Settings → Connectors**, click on the **Gmail** connector to open its details
2. Find the **Tool permissions** section — it lists each tool the connector can use
3. For these tools, set the permission to **Always allow**:
   - `get_thread`
   - `search_threads`
   - `list_labels`
   - `list_drafts`
4. For this tool, set the permission to **Blocked**:
   - `create_draft`

With this setup, ARIA can search and read your inbox freely, but if she ever tried to create a draft, Claude would block the request before it's sent — it would never reach Google's servers.

> **Note:** If you reconnect the Gmail connector later or update Claude, it's worth double-checking these settings are still in place.

---

## Step 4 — Confirm it's connected

Back in Claude Code, the Gmail connector should now show as **Connected**.

---

*Done? Open `lessons/04_first_conversation.md` to have your first conversation with ARIA.*
