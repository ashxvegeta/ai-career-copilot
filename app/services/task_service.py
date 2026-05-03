from app.database.db import SessionLocal
from app.database.models import Task


def save_tasks(user_id: int, tasks_dict: dict):
    db = SessionLocal()

    try:
        for skill, task_list in tasks_dict.items():
            for task in task_list:
                new_task = Task(
                    user_id=user_id,
                    skill_name=skill,
                    task_text=task,
                    status="pending"
                )
                db.add(new_task)

        db.commit()
        print("Tasks saved successfully")

    except Exception as e:
        db.rollback()
        print("Error saving tasks:", e)

    finally:
        db.close()


def mark_task_completed(task_id: int):
    db = SessionLocal()

    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            print(f"Task with id {task_id} not found")
            return {"error": "Task not found"}
        task.status = "completed"
        db.commit()
        return {"message": "Task marked as completed"}
    except Exception as e:
        db.rollback()
        print("Error marking task as completed:", e)
        return {"error": "An error occurred while updating the task"}
    

def get_all_tasks(user_id: int):
    db = SessionLocal()

    try:
        tasks = db.query(Task).filter(Task.user_id == user_id).all()

        result = []
        for t in tasks:
            result.append({
                "id": t.id,
                "user_id": t.user_id,
                "skill": t.skill_name,
                "task": t.task_text,
                "status": t.status
            })

        return result

    finally:
        db.close()

def get_task_progress(user_id: int):
    db = SessionLocal()

    try:
        total = db.query(Task).filter(Task.user_id == user_id).count()
        completed = db.query(Task).filter(Task.user_id == user_id, Task.status == "completed").count()
        pending = total - completed

        progress = (completed / total) * 100 if total > 0 else 0

        return {
            "total_tasks": total,
            "completed_tasks": completed,
            "pending_tasks": pending,
            "progress_percentage": progress
        }

    finally:
        db.close()


def get_user_tasks(user_id: int):

    db = SessionLocal()

    try:
        tasks = db.query(Task).filter(Task.user_id == user_id).all()

        return tasks

    finally:
        db.close()