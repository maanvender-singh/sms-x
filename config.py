
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

APP_NAME = os.getenv("APP_NAME", "SMS-X")
APP_VERSION = os.getenv("APP_VERSION", "1.0")

RATE_LIMIT = int(os.getenv("SMS_RATE_LIMIT", "3"))
RATE_WINDOW = int(os.getenv("SMS_RATE_WINDOW", "60"))
OTP_EXPIRY = int(os.getenv("OTP_EXPIRY", "300"))

DATA_DIR = BASE_DIR / "data"
LOG_FILE = DATA_DIR / "sms_logs.json"

DATA_DIR.mkdir(exist_ok=True)

if not LOG_FILE.exists():
    LOG_FILE.write_text("[]", encoding="utf-8")
