
import json
import time
from config import LOG_FILE

def log_event(event):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    event["timestamp"] = time.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    logs.append(event)

    with open(LOG_FILE, "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=4)


def read_logs():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
