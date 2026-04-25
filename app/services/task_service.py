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