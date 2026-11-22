
from modules.consent import has_consent
from modules.rate_limiter import allowed
from modules.logger import log_event


def simulate_sms(number, message):

    if not has_consent(number):
        print("[!] Recipient has not given consent.")
        return False

    if not allowed(number):
        print("[!] Rate limit reached.")
        log_event({
            "recipient": number,
            "status": "RATE_LIMITED"
        })
        return False

    print("\n========== SMS PREVIEW ==========")
    print("Recipient:", number)
    print("Message:", message)
    print("Status: SIMULATED")
    print("=================================\n")

    log_event({
        "recipient": number,
        "message": message,
        "status": "SIMULATED"
    })

    return True
