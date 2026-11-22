
# main.py
import json
import secrets
import time
from pathlib import Path
from collections import defaultdict, deque

DATA = Path("data")
DATA.mkdir(exist_ok=True)

LOG = DATA / "sms_logs.json"

LIMIT = 3
WINDOW = 60
requests = defaultdict(deque)


def log_event(event):
    logs = []
    if LOG.exists():
        logs = json.loads(LOG.read_text())

    logs.append(event)
    LOG.write_text(json.dumps(logs, indent=2))


def generate_otp():
    return str(secrets.randbelow(900000) + 100000)


def rate_limit(number):
    now = time.time()
    queue = requests[number]

    while queue and now - queue[0] > WINDOW:
        queue.popleft()

    if len(queue) >= LIMIT:
        return False

    queue.append(now)
    return True


def simulate_sms(number, message):
    if not rate_limit(number):
        print("[!] Rate limit reached.")
        return

    print("\n[SIMULATED SMS]")
    print("Recipient:", number)
    print("Message:", message)
    print("Status: SIMULATED")
    
    log_event({
        "recipient": number,
        "message": message,
        "status": "SIMULATED",
        "timestamp": time.time()
    })


def show_logs():
    if not LOG.exists():
        print("No logs available.")
        return

    print(LOG.read_text())


def menu():
    while True:
        print("""
================================
          SMS-X TOOLKIT
================================
1. Generate mock OTP
2. Simulate SMS
3. View logs
4. Exit
================================
""")

        choice = input("SMS-X > ").strip()

        if choice == "1":
            print("Mock OTP:", generate_otp())

        elif choice == "2":
            number = input("Test recipient label: ")
            message = input("Message: ")
            simulate_sms(number, message)

        elif choice == "3":
            show_logs()

        elif choice == "4":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
