from fastapi import APIRouter, Depends
from app.database.models import User
from app.utils.dependencies import get_current_user
from app.services.history_service import get_analysis_history

router = APIRouter()

@router.get("/analysis-history")
def analysis_history(
    current_user : User = Depends(get_current_user)
):
    return get_analysis_history(current_user.id)