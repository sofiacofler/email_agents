// Google Email Task Agent
// Google Apps Script + Gemini API
//
// Setup:
//   1. Go to script.google.com → New project → paste this code
//   2. Project Settings → Script Properties → add:
//        GEMINI_API_KEY     → your key from aistudio.google.com
//        TELEGRAM_BOT_TOKEN → your bot token
//        TELEGRAM_CHAT_ID   → your chat ID
//   3. Run setupTrigger() once to schedule daily execution
//   4. On first run, approve Gmail + Drive permissions when prompted

const PROPS        = PropertiesService.getScriptProperties();
const GEMINI_MODEL = 'gemini-2.5-flash';
const SUMMARY_DAYS = 5;
const SHEET_NAME   = 'Email Agent Tasks';

const CATEGORIES = ['school', 'work', 'household', 'goodies', 'health', 'other'];

const CATEGORY_EMOJI = {
  school:    '🏫',
  work:      '💼',
  household: '🏠',
  goodies:   '🎁',
  health:    '🏥',
  other:     '📌'
};


// ── Entry point ───────────────────────────────────────────────────────────────

function runAgent() {
  const emailTexts = fetchYesterdaysEmails();
  if (emailTexts.length === 0) {
    console.log('No emails found for yesterday.');
    return;
  }

  const newTasks = extractTasksWithGemini(emailTexts);
  console.log(`Extracted ${newTasks.length} tasks from emails.`);

  const allTasks = storeTasks(newTasks);
  const message  = buildSummaryMessage(allTasks);

  console.log(message);
  sendTelegram(message);
}


// ── Gmail fetch ───────────────────────────────────────────────────────────────

function fetchYesterdaysEmails() {
  const yesterday = new Date();
  yesterday.setDate(yesterday.getDate() - 1);

  const fmt    = date => Utilities.formatDate(date, 'UTC', 'yyyy/MM/dd');
  const query  = `after:${fmt(yesterday)} before:${fmt(new Date())}`;
  const threads = GmailApp.search(query, 0, 20);

  const emailTexts = [];
  for (const thread of threads) {
    for (const msg of thread.getMessages()) {
      const body = msg.getPlainBody().substring(0, 2000);
      emailTexts.push(
        `Subject: ${msg.getSubject()}\nFrom: ${msg.getFrom()}\n\n${body}`
      );
    }
  }
  console.log(`Fetched ${emailTexts.length} emails.`);
  return emailTexts;
}


// ── Gemini task extraction ────────────────────────────────────────────────────

function extractTasksWithGemini(emailTexts) {
  const today   = Utilities.formatDate(new Date(), 'UTC', 'yyyy-MM-dd');
  const combined = emailTexts.slice(0, 20).join('\n\n---\n\n');

  const prompt = `You are a personal assistant. Today is ${today}.
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
${combined}`;

  const apiKey = PROPS.getProperty('GEMINI_API_KEY');
  const url    = `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent?key=${apiKey}`;

  const response = UrlFetchApp.fetch(url, {
    method:      'post',
    contentType: 'application/json',
    payload:     JSON.stringify({
      contents:         [{ parts: [{ text: prompt }] }],
      generationConfig: { temperature: 0.1 }
    })
  });

  const result = JSON.parse(response.getContentText());
  let raw = result.candidates[0].content.parts[0].text.trim();

  if (raw.startsWith('```')) {
    raw = raw.split('```')[1];
    if (raw.startsWith('json')) raw = raw.slice(4);
  }

  try {
    const tasks = JSON.parse(raw);
    // Ensure category is always one of the allowed values
    return tasks.map(t => ({
      ...t,
      category: CATEGORIES.includes(t.category) ? t.category : 'other'
    }));
  } catch (e) {
    console.log('Could not parse Gemini response as JSON:\n' + raw);
    return [];
  }
}


// ── Task storage (Google Sheet) ───────────────────────────────────────────────

function storeTasks(newTasks) {
  const sheet = getOrCreateSheet();
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  // Load + prune past tasks
  let active = loadTasksFromSheet(sheet).filter(
    t => parseDateLocal(t.deadline) >= today
  );

  // Merge new tasks, deduplicate by title + deadline
  const keys = new Set(active.map(t => `${t.title}_${t.deadline}`));
  for (const task of newTasks) {
    const key = `${task.title}_${task.deadline}`;
    if (!keys.has(key)) {
      active.push(task);
      keys.add(key);
    }
  }

  saveTasksToSheet(sheet, active);
  console.log(`Sheet updated — ${active.length} active tasks stored.`);
  return active;
}

function getOrCreateSheet() {
  const files = DriveApp.getFilesByName(SHEET_NAME);
  if (files.hasNext()) {
    return SpreadsheetApp.open(files.next()).getSheetByName('Tasks');
  }
  const ss    = SpreadsheetApp.create(SHEET_NAME);
  const sheet = ss.getActiveSheet();
  sheet.setName('Tasks');
  sheet.appendRow(['title', 'deadline', 'category', 'source']);
  sheet.setFrozenRows(1);
  return sheet;
}

function loadTasksFromSheet(sheet) {
  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return [];
  const headers = data[0];
  return data.slice(1).map(row => {
    const obj = {};
    headers.forEach((h, i) => { obj[h] = row[i]; });
    return obj;
  });
}

function saveTasksToSheet(sheet, tasks) {
  sheet.clearContents();
  sheet.appendRow(['title', 'deadline', 'category', 'source']);
  for (const t of tasks) {
    sheet.appendRow([t.title, t.deadline, t.category, t.source]);
  }
}


// ── Telegram summary (next 5 days only) ──────────────────────────────────────

function buildSummaryMessage(allTasks) {
  const today  = new Date();
  const cutoff = new Date();
  cutoff.setDate(today.getDate() + SUMMARY_DAYS);

  const upcoming = allTasks.filter(t => {
    const d = parseDateLocal(t.deadline);
    return d >= today && d <= cutoff;
  });

  const tz      = Session.getScriptTimeZone();
  const dateStr = Utilities.formatDate(today, tz, 'EEEE, dd MMM yyyy');
  const timeStr = Utilities.formatDate(today, tz, 'HH:mm');

  const lines = [
    `📋 *Daily Task Summary — ${dateStr}*`,
    `_Tasks due in the next ${SUMMARY_DAYS} days — ${allTasks.length} total stored_\n`
  ];

  if (upcoming.length === 0) {
    lines.push('No tasks due in the next 5 days.');
  } else {
    // Sort upcoming tasks by deadline (soonest first) within each category
    upcoming.sort((a, b) => parseDateLocal(a.deadline) - parseDateLocal(b.deadline));

    const byCategory = {};
    for (const cat of CATEGORIES) byCategory[cat] = [];
    for (const t of upcoming) {
      const cat = CATEGORIES.includes(t.category) ? t.category : 'other';
      byCategory[cat].push(t);
    }

    for (const cat of CATEGORIES) {
      const group = byCategory[cat];
      if (group.length === 0) continue;
      lines.push(`\n${CATEGORY_EMOJI[cat]} *${cat.toUpperCase()}*`);
      for (const t of group) {
        lines.push(`  • ${t.title} — due ${formatDeadline(t.deadline, tz)}`);
        lines.push(`    _from: ${t.source || 'unknown'}_`);
      }
    }
  }

  lines.push(`\n_Agent run at ${timeStr}_`);
  return lines.join('\n');
}

// Parse YYYY-MM-DD as local date (avoids UTC midnight shifting the day)
function parseDateLocal(dateStr) {
  const [y, m, d] = dateStr.split('-').map(Number);
  return new Date(y, m - 1, d);
}

// Format deadline as "Mon, 26 May 2026"
function formatDeadline(dateStr, tz) {
  const d = parseDateLocal(dateStr);
  return Utilities.formatDate(d, tz, 'EEE, dd MMM yyyy');
}


// ── Telegram sender ───────────────────────────────────────────────────────────

function sendTelegram(message) {
  const token  = PROPS.getProperty('TELEGRAM_BOT_TOKEN');
  const chatId = PROPS.getProperty('TELEGRAM_CHAT_ID');
  if (!token || !chatId) {
    console.log('Telegram not configured — skipping notification.');
    return;
  }
  UrlFetchApp.fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
    method:      'post',
    contentType: 'application/json',
    payload:     JSON.stringify({ chat_id: chatId, text: message, parse_mode: 'Markdown' })
  });
  console.log('Telegram message sent.');
}


// ── Daily trigger setup (run once manually) ───────────────────────────────────

function setupTrigger() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'runAgent')
    .forEach(t => ScriptApp.deleteTrigger(t));

  ScriptApp.newTrigger('runAgent')
    .timeBased()
    .everyDays(1)
    .atHour(8)
    .create();

  console.log('Daily trigger set for 8:00 AM.');
}
