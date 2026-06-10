import re

def extract_endpoints(text):

    endpoints = []

    patterns = [
        r"(?:GET|POST|PUT|DELETE|PATCH)\s+\/[^\s]+",
        r"\/v\d+\/[a-zA-Z0-9_\-/]+"
    ]

    for pattern in patterns:
        endpoints.extend(re.findall(pattern, text))

    if endpoints:
        return list(set(endpoints))

    resource_keywords = [
        "Customers",
        "Charges",
        "Refunds",
        "Payment Intents",
        "Checkout Sessions",
        "Subscriptions",
        "Invoices",
        "Products"
    ]

    found = []

    for resource in resource_keywords:
        if resource.lower() in text.lower():
            found.append(resource)

    return found