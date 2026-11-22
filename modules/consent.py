
import json
from pathlib import Path

CONSENT_FILE = Path("data/consent.json")


def load_data():
    if not CONSENT_FILE.exists():
        return {}

    try:
        return json.loads(CONSENT_FILE.read_text())
    except json.JSONDecodeError:
        return {}


def save_data(data):
    CONSENT_FILE.write_text(
        json.dumps(data, indent=4)
    )


def add_consent(number):
    data = load_data()
    data[number] = True
    save_data(data)
    print("[+] Consent recorded.")


def revoke_consent(number):
    data = load_data()
    data[number] = False
    save_data(data)
    print("[+] Consent revoked.")


def has_consent(number):
    return load_data().get(number, False)
