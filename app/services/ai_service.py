import os
from dotenv import load_dotenv
from openai import OpenAI
import json
import re

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


def clean_json_response(content: str):
    # Remove extra spaces and newlines
    content = content.strip()

    # Remove markdown ```json ```
    # Remove markdown wrappers if they exist (some models wrap JSON in markdown)
    content = re.sub(r"```json|```", "", content).strip()

    # Extract only JSON part if extra text exists
    match = re.search(r"\{.*\}", content, re.DOTALL)
    if match:
        return match.group(0)

    return content


def analyze_resume_content(resume_text: str):

    prompt = f"""
    Analyze this resume:

    {resume_text}

    IMPORTANT:
    - Return ONLY valid JSON
    - Do NOT wrap in markdown
    - Do NOT add any explanation
    - Do NOT leave any field empty
    - If data is missing, make reasonable assumptions
    - Keep responses concise and relevant

    Rules:
    - "experience_level" must be one of: "junior", "mid", "senior"
    - Provide at least 2 strengths and 2 weaknesses
    
    {{
        "skills": ["skill1", "skill2"],
        "experience_level": "junior",
        "strengths": ["strength1", "strength2"],
        "weaknesses": ["weakness1", "weakness2"]
    }}
    """

    client = _get_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content
    # 🔥 ADD THIS LINE (same as job_match)
    content = clean_json_response(content)

    try:
        return json.loads(content)
    except:
        return {"error": "Invalid JSON", "raw": content}
    


def match_with_job_description(resume: str, job: str):

    prompt = f"""
    Compare resume with job description.

    Resume:
    {resume}

    Job:
    {job}

    IMPORTANT:
    - Return ONLY valid JSON
    - Do NOT wrap in markdown (no ```)
    - match_score must be an integer between 0 and 100

    {{
        "match_score": 65,
        "missing_skills": ["skill1"],
        "suggestions": ["suggestion1"]
    }}
    """

    client = _get_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    # 🔥 ADD THIS (you were missing this)
    content = clean_json_response(content)

    try:
        return json.loads(content)
    except:
        return {"error": "Invalid JSON", "raw": content}
    
def  generate_tasks_for_skills(skills: list):

    prompt = f"""
    For each skill, generate 2-3 actionable tasks.

    Skills:
    {skills}

    Format:
    {{
        "AWS": ["task1", "task2"],
        "Redis": ["task1", "task2"]
    }}
    """

    client = _get_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    # Clean the response to ensure it's valid JSON
    content = clean_json_response(content)

    try:
        return json.loads(content)
    except:
        return {"error": "Invalid JSON", "raw": content}

def  generate_career_roadmap(tasks:dict):

    prompt = f"""
    Create a 4-week career improvement plan based on the following tasks.

    Tasks:
    {tasks}

    Important:
   - Return ONLY valid JSON
   - Do NOT wrap in markdown
   

    Format:
    {{
        "week_1": ["task1", "task2"],
        "week_2": ["task1"],
        "week_3": ["task1"],
        "week_4": ["task1"]
    }}
    """

    client = _get_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    # Clean the response to ensure it's valid JSON
    content = clean_json_response(content)

    try:
        return json.loads(content)
    except:
        return {"error": "Invalid JSON", "raw": content}