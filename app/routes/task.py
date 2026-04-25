from fastapi import APIRouter
from app.services.task_service import mark_task_completed,get_all_tasks

router = APIRouter()


@router.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    return mark_task_completed(task_id)

@router.get("/tasks")
def fetch_tasks():
    return get_all_tasks()