from fastapi import APIRouter
from app.services.task_service import mark_task_completed,get_all_tasks,get_task_progress,get_user_tasks
from app.utils.dependencies import get_current_user
from app.database.models import User
from fastapi import Depends

router = APIRouter()


@router.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    return mark_task_completed(task_id)

@router.get("/tasks")
def fetch_tasks(user_id: int):
    return get_all_tasks(user_id)

@router.get("/tasks/progress")
def task_progress(user_id: int):
    return get_task_progress(user_id)


@router.get("/my-tasks")
def my_tasks(
    current_user: User = Depends(get_current_user)
):
    return get_user_tasks(current_user.id)