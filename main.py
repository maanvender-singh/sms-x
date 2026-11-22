
from config import APP_NAME, APP_VERSION

from modules.providers import show_providers
from modules.simulator import simulate_sms
from modules.otp import generate_otp, verify_otp
from modules.consent import (
    add_consent,
    revoke_consent
)
from modules.logger import read_logs


def banner():
    print("""
========================================
       ███████╗███╗   ███╗███████╗
       ██╔════╝████╗ ████║██╔════╝
       ███████╗██╔████╔██║███████╗
       ╚════██║██║╚██╔╝██║╚════██║
       ███████║██║ ╚═╝ ██║███████║
       ╚══════╝╚═╝     ╚═╝╚══════╝

             SMS-X TOOLKIT
========================================
""")


def menu():
    banner()

    while True:
        print(f"\n{APP_NAME} v{APP_VERSION}")
        print("""
[1] Provider Profiles
[2] Generate Mock OTP
[3] Verify Mock OTP
[4] Simulate SMS
[5] Add Recipient Consent
[6] Revoke Recipient Consent
[7] View Activity Logs
[0] Exit
""")

        choice = input("SMS-X >> ").strip()

        if choice == "1":
            show_providers()

        elif choice == "2":
            number = input("Test recipient label: ")
            print("Mock OTP:", generate_otp(number))

        elif choice == "3":
            number = input("Test recipient label: ")
            entered = input("Enter OTP: ")

            if verify_otp(number, entered):
                print("[+] OTP verified.")
            else:
                print("[-] Invalid or expired OTP.")

        elif choice == "4":
            number = input("Recipient label: ")
            message = input("Message: ")
            simulate_sms(number, message)

        elif choice == "5":
            number = input("Recipient label: ")
            add_consent(number)

        elif choice == "6":
            number = input("Recipient label: ")
            revoke_consent(number)

        elif choice == "7":
            logs = read_logs()

            if not logs:
                print("No activity recorded.")
            else:
                for item in logs:
                    print(item)

        elif choice == "0":
            print("Exiting SMS-X.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
