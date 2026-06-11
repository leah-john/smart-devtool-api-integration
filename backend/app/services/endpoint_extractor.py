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

        # Stripe
        "Customers",
        "Charges",
        "Refunds",
        "Payment Intents",
        "Checkout Sessions",
        "Subscriptions",
        "Invoices",
        "Products",

        # GitHub
        "Repositories",
        "Issues",
        "Pull Requests",
        "Actions",
        "Workflows",
        "Organizations",
        "Users",
        "Commits",
        "Branches",
        "Webhooks",

        # PayPal
        "Orders",
        "Payments",
        "Payouts",
        "Disputes",
        "Invoicing",
        "Subscriptions",

        # Razorpay
        "Payment Links",
        "QR Codes",
        "Settlements",
        "Customers",
        "Refunds",
        "Invoices",
        "Orders",
        "Payouts"
    ]

    found = set()

    for resource in resource_keywords:
        if resource.lower() in text.lower():
            found.add(resource)

    return list(found)