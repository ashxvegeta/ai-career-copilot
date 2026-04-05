from openai import OpenAI
client = OpenAI()

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
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content