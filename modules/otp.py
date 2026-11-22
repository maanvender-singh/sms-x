
import secrets
import time
from config import OTP_EXPIRY

otp_store = {}


def generate_otp(number):
    otp = str(secrets.randbelow(900000) + 100000)

    otp_store[number] = {
        "otp": otp,
        "created": time.time()
    }

    return otp


def verify_otp(number, entered):
    record = otp_store.get(number)

    if not record:
        return False

    if time.time() - record["created"] > OTP_EXPIRY:
        otp_store.pop(number, None)
        return False

    if secrets.compare_digest(record["otp"], entered):
        otp_store.pop(number, None)
        return True

    return False
