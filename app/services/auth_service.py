from app.database.db import SessionLocal
from app.database.models import User
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable is required")
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password[:72])


def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


def create_token(user_id: int):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)




def register_user(email: str, password: str):
    db = SessionLocal()

    try:
        existing = db.query(User).filter(User.email == email).first()
        if existing:
            return {"error": "User already exists"}

        new_user = User(
            email=email,
            password=hash_password(password)
        )

        db.add(new_user)
        db.commit()

        return {"message": "User registered successfully"}

    finally:
        db.close()



def login_user(email: str, password: str):
    db = SessionLocal()

    try:
        user = db.query(User).filter(User.email == email).first()

        if not user or not verify_password(password, user.password):
            return {"error": "Invalid credentials"}

        token = create_token(user.id)

        return {"access_token": token}

    finally:
        db.close()