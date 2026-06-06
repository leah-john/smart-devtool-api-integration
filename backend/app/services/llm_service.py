import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question, context):

    prompt = f"""
    You are an API Integration Expert.

    Answer ONLY using the provided documentation context.

    Documentation Context:
    {context}

    User Question:
    {question}

    Provide a clear and beginner-friendly answer.
    """

    response = model.generate_content(prompt)

    return response.text