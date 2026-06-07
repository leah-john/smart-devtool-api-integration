def detect_provider(text):

    text = text.lower()

    providers = {
        "paypal": "PayPal",
        "stripe": "Stripe",
        "phonepe": "PhonePe",
        "google pay": "Google Pay",
        "gpay": "Google Pay",
        "razorpay": "Razorpay",
        "paytm": "Paytm",
        "twilio": "Twilio",
        "openai": "OpenAI",
        "github": "GitHub"
    }

    for keyword, provider in providers.items():

        if keyword in text:
            return provider

    return "Unknown"