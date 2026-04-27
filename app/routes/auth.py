from fastapi import APIRouter
from app.services.auth_service import register_user, login_user
from app.schemas.auth_schema import UserAuth

router = APIRouter()


@router.post("/register")
def register(data: UserAuth):
    return register_user(data.email, data.password)


@router.post("/login")
def login(data: UserAuth):
    return login_user(data.email, data.password)