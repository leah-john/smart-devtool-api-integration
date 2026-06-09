from app.services.llm_service import generate_answer


def generate_recommendations(
    authentication,
    endpoints,
    use_case
):

    prompt = f"""
    Authentication Method:
    {authentication}

    Available Endpoints:
    {endpoints}

    Intended Use Case:
    {use_case}

    Based on the above information:

    1. Recommend suitable SDKs
    2. Suggest REST API alternatives
    3. Provide integration steps
    4. Mention best practices

    Keep the response concise and developer friendly.
    """

    recommendations = generate_answer(
        prompt,
        ""
    )

    return recommendations