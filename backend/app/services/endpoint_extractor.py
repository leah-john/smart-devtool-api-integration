import re


def extract_endpoints(text):

    patterns = [
        r"(?:GET|POST|PUT|DELETE|PATCH)\s+\/[^\s]+",
        r"(?:GET|POST|PUT|DELETE|PATCH).*?https?:\/\/[^\s\"']+"
    ]

    endpoints = []

    for pattern in patterns:
        endpoints.extend(re.findall(pattern, text))

    return list(set(endpoints))