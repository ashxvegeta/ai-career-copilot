from fastapi import APIRouter
from app.services.task_service import mark_task_completed

router = APIRouter()


@router.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    return mark_task_completed(task_id)