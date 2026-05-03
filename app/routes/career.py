from app.database.models import User
from fastapi import APIRouter, Depends
from app.schemas.career_schema import ResumeInput
from app.services.resume_service import analyze_resume
from app.utils.dependencies import get_current_user

router = APIRouter()


@router.post("/career/analyze")
def analyze(
    data: ResumeInput,
    current_user: User = Depends(get_current_user)
):
    return analyze_resume(data, current_user.id)