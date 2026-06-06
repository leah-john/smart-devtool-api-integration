def detect_authentication(text):

    text = text.lower()

    if (
        "oauth" in text
        or "client id" in text
        or "client secret" in text
    ):
        return "OAuth 2.0"

    elif (
        "api-key" in text
        or "x-api-key" in text
        or "api_key" in text
    ):
        return "API Key"

    elif "jwt" in text:
        return "JWT"

    elif "basic auth" in text:
        return "Basic Authentication"

    return "Unknown"