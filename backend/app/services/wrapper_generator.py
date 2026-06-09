from app.services.llm_service import generate_answer


def generate_wrapper(
    provider,
    authentication,
    endpoints
):

    prompt = f"""
    Provider:
    {provider}

    Authentication:
    {authentication}

    Endpoints:
    {endpoints}

    Generate a Python wrapper class.

    Requirements:
    - Create meaningful method names.
    - Include class definition.
    - Include method stubs.
    - Return only Python code.
    """

    wrapper_code = generate_answer(
        prompt,
        ""
    )
    wrapper_code = wrapper_code.replace(
    "```python",
    ""
)

    wrapper_code = wrapper_code.replace(
        "```",
        ""
    )

    return wrapper_code