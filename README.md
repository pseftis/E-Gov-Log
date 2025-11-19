# E-Governance Server Log System (Django)

A minimal, runnable Django project for uploading server/application/security logs and listing them on a dashboard.

## Quickstart

```bash
python -m venv venv
venv\Scripts\activate  # on Windows
# source venv/bin/activate  # on macOS/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open:
- Upload page: http://127.0.0.1:8000/upload/
- Dashboard: http://127.0.0.1:8000/dashboard/

## Notes
- Files are saved to `media/uploaded_logs/` (created automatically).
- Uses SQLite by default.
