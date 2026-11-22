
PROVIDERS = {
    "1": "Twilio",
    "2": "Vonage",
    "3": "Plivo"
}


def show_providers():
    print("\n======= PROVIDER PROFILES =======")

    for key, name in PROVIDERS.items():
        print(f"{key}. {name}")

    print("These are configuration profiles only.")
    print("No messages are sent.")
