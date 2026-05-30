from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone
import os

templates = Jinja2Templates(directory="app/templates")

# Get version information
VERSION = os.environ.get("VERSION", "unknown")
GIT_COMMIT = os.environ.get("GIT_COMMIT", "unknown")

# Capture the restart time as UTC ISO 8601 once at import time; the client converts to local timezone
RESTART_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
templates.env.globals["restart_time"] = RESTART_TIME
