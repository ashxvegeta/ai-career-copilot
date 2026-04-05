import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
_client = None


def _get_client() -> OpenAI:
    global _client
    if _client is not None:
        return _client
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it to your .env or environment before calling analyze_with_ai."
        )
    _client = OpenAI(api_key=api_key)
    return _client


def analyze_with_ai(resume_text: str, job_description: str):
    
    prompt = f"""
    Analyze the resume and compare with job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Return:
    - Match score (0-100)
    - Missing skills
    - Suggestions
    """
    client = _get_client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
