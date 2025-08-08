import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        'FLASK_SECRET_KEY': os.getenv('FLASK_SECRET_KEY', 'dev-key'),
        # IMPORTANT: set this to your Render URL in the dashboard (e.g., https://fowhand.onrender.com)
        'BASE_URL': os.getenv('BASE_URL', 'http://localhost:5000'),
        # On Render, use the Postgres DATABASE_URL provided by the Add‑On
        'DATABASE_URL': os.getenv('DATABASE_URL', 'sqlite:///damage_tracker.db'),
        'GOOGLE_CLIENT_SECRETS': os.getenv('GOOGLE_CLIENT_SECRETS', 'client_secret.json'),
        'OAUTH_SCOPES': os.getenv('OAUTH_SCOPES', 'email profile https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.send https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive'),
        'DRIVE_UPLOAD_FOLDER_ID': os.getenv('DRIVE_UPLOAD_FOLDER_ID', ''),
        'MONITORED_GMAIL_ACCOUNTS': os.getenv('MONITORED_GMAIL_ACCOUNTS', ''),
        'SERVICE_GOOGLE_ACCOUNT': os.getenv('SERVICE_GOOGLE_ACCOUNT', ''),
        'NOTIFY_EMAILS': os.getenv('NOTIFY_EMAILS', ''),
        'TASKS_SECRET': os.getenv('TASKS_SECRET', ''),
        # Where OAuth tokens are stored. On Render, mount a disk at /data and use /data/tokens
        'TOKENS_DIR': os.getenv('TOKENS_DIR', 'tokens'),
    }
