from app.services.llm_service import generate_answer


def generate_recommendations(
    authentication,
    endpoints,
    use_case,
    documentation
):

    prompt = f"""
    You are a senior API integration consultant.

    API Authentication:
    {authentication}

    Available Resources / Endpoints:
    {endpoints}

    Developer Use Case:
    {use_case}

    Provide:

    1. Recommended SDKs
    2. Step-by-step integration approach
    3. Authentication implementation advice
    4. Security best practices
    5. Common mistakes to avoid

    Format the response using bullet points.

    Keep the answer practical, concise and developer-friendly.
    """

    recommendations = generate_answer(
        prompt,
        documentation
    )

    return recommendations