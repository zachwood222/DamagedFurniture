# Fowhand Damage Tracker — Render (Postgres) Package

This package is ready for **Render** with **PostgreSQL** and a **persistent disk** for OAuth tokens.

## 1) What’s included
- Flask app with SQLAlchemy models
- Gmail + Drive OAuth2 integrations
- Inline photo previews from Drive
- Status workflow (New / Resolved / Credit Received)
- Cron-friendly endpoints:
  - `GET /tasks/scan?secret=...`  (every 5–10 minutes)
  - `GET /tasks/daily-summary?secret=...` (daily)
- `render.yaml` for one‑click deploy (service + disk)
- `Procfile` and `gunicorn` for production
- `.env.sample` with all required environment variables
- `TOKENS_DIR` support so tokens persist at `/data/tokens`

## 2) Deploy to Render (recommended)
**Option A — One‑click (render.yaml)**
1. Push this folder to a **GitHub repo**.
2. In Render, click **New > Blueprint** and select your repo.
3. After it reads `render.yaml`, open the service and set these **Environment Variables** (Dashboard → Settings → Environment):
   - `DATABASE_URL` → from Render Postgres add‑on
   - `GOOGLE_CLIENT_SECRETS` → keep as `client_secret.json` and **upload the file** to the repo root (or paste JSON into a secret manager and mount).
   - `DRIVE_UPLOAD_FOLDER_ID`
   - `MONITORED_GMAIL_ACCOUNTS` → `zwood@fowhandfurniture.com,kara@fowhandfurniture.com`
   - `SERVICE_GOOGLE_ACCOUNT` → `fowhandorders@gmail.com`
   - `NOTIFY_EMAILS` → your distribution list emails (comma‑separated)
   - `TASKS_SECRET` → long random string
   - `BASE_URL` → your Render URL (e.g., `https://fowhand-damage-tracker.onrender.com`)
4. Render will create a **persistent disk** at `/data`. Tokens are stored at `/data/tokens`.
5. Deploy the service.

**Option B — Manual web service**
1. Click **New > Web Service**, choose this repo.
2. Build Command: `pip install -r requirements.txt`
3. Start Command: `gunicorn app:app --preload --workers=2 --threads=2 --timeout=120`
4. Add a **disk** (1 GB) mounted at `/data`.
5. Add the **environment variables** listed above (including `TOKENS_DIR=/data/tokens`).

## 3) After deploy
1. Open your site and go to `/`.
2. Click **Connect** for each Gmail inbox and for the **Drive/Sender** account.
3. Create a **Cron Job** in Render (or cron‑job.org) to hit:
   - `GET {BASE_URL}/tasks/scan?secret=YOUR_TASKS_SECRET` every 5–10 minutes
   - `GET {BASE_URL}/tasks/daily-summary?secret=YOUR_TASKS_SECRET` once daily

## 4) Local development
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env
flask --app app.py --debug run
```

## Notes
- Make sure `client_secret.json` (Google OAuth client) is present at repo root.
- Drive files are link‑viewable; if you want private links, remove the permission creation in `drive_client.py` and grant your team Drive access.
- If you prefer Twilio for SMS, add it in `tasks.py` when status is set to `CREDIT_RECEIVED`.
