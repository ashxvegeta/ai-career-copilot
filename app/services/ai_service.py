import os
from dotenv import load_dotenv
from openai import OpenAI
import json

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
    Analyze the resume and compare it with the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    IMPORTANT RULES:
    - Return ONLY valid JSON
    - Do NOT add any explanation or text outside JSON
    - match_score must be an integer between 0 and 100

    Expected format:
    {{
        "match_score": 65,
        "missing_skills": ["AWS", "Redis"],
        "suggestions": ["Learn AWS basics", "Build a Redis project"]
    }}
    """

    client = _get_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON from AI",
            "raw_response": content
        }
    
    