from fastapi import APIRouter
from app.services.auth_service import register_user, login_user
from app.schemas.auth_schema import UserAuth
from app.utils.dependencies import get_current_user
from app.database.models import User
from fastapi import Depends

router = APIRouter()


@router.post("/register")
def register(data: UserAuth):
    return register_user(data.email, data.password)


@router.post("/login")
def login(data: UserAuth):
    return login_user(data.email, data.password)


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "email": current_user.email
    }