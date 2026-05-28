from app.services.ai_service import (
    analyze_resume_content,
    match_with_job_description,
    generate_tasks_for_skills,
    generate_career_roadmap 
)
from app.services.task_service import save_tasks
from app.database.models import AnalysisHistory
from app.database.db import SessionLocal
import json
def analyze_resume(data, user_id):

    resume_text = data.resume_text
    job_desc = data.job_description

    # Step 1: Analyze resume content
    analysis = analyze_resume_content(resume_text)
    # Step 2
    job_match = match_with_job_description(resume_text, job_desc)
    # Step 3 🔥 NEW
    missing_skills = job_match.get("missing_skills", [])
    tasks = generate_tasks_for_skills(missing_skills)
    save_tasks(user_id=user_id, tasks_dict=tasks)
    # Step 4 🔥 NEW
    roadmap = generate_career_roadmap(tasks)

    result = {
        "analysis": analysis,
        "job_match": job_match,
        "tasks": tasks,
        "roadmap": roadmap
    }

    db = SessionLocal()
    history  = AnalysisHistory(
        user_id=user_id,
        resume_text=resume_text,
        job_description=job_desc,
        analysis_result=json.dumps(result)
    )
    db.add(history)
    db.commit()
    db.close()

    return result
