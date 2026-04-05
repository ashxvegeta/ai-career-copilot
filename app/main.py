from fastapi import FastAPI
# importing:router from career.py Renaming it to career_router
from app.routes.career import router as career_router
# Create app instance
app = FastAPI()
# Include router
app.include_router(career_router)