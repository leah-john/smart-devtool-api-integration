def recommend_sdk(provider):

    sdk_map = {

        "PayPal": [
            "PayPal Python SDK",
            "PayPal Java SDK",
            "PayPal Node.js SDK"
        ],

        "Stripe": [
            "Stripe Python SDK",
            "Stripe Java SDK",
            "Stripe Node.js SDK"
        ],

        "Twilio": [
            "Twilio Python SDK",
            "Twilio Java SDK",
            "Twilio Node.js SDK"
        ],

        "Razorpay": [
            "Razorpay Python SDK",
            "Razorpay Java SDK",
            "Razorpay Node.js SDK"
        ],

        "PhonePe": [
            "PhonePe Python SDK",
            "PhonePe Java SDK"
        ]
    }

    return sdk_map.get(
        provider,
        ["No SDK recommendations available"]
    )