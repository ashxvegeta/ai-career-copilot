from app.services.ai_service import (
    analyze_resume_content,
    match_with_job_description,
    generate_tasks_for_skills,
    generate_career_roadmap 
)
from app.services.task_service import save_tasks
def analyze_resume(data):

    resume_text = data.resume_text
    job_desc = data.job_description

    # Step 1: Analyze resume content
    analysis = analyze_resume_content(resume_text)
    # Step 2
    job_match = match_with_job_description(resume_text, job_desc)
    # Step 3 🔥 NEW
    missing_skills = job_match.get("missing_skills", [])
    tasks = generate_tasks_for_skills(missing_skills)
    save_tasks(user_id=1, tasks_dict=tasks)
    # Step 4 🔥 NEW
    roadmap = generate_career_roadmap(tasks)

    return {
        "analysis": analysis,
        "job_match": job_match,
        "tasks": tasks,
        "roadmap": roadmap
    }
