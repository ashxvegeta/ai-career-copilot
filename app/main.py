from fastapi import FastAPI
# importing:router from career.py Renaming it to career_router
from app.routes.career import router as career_router
from app.routes.task import router as task_router
from app.routes import auth
# Create app instance
app = FastAPI()
# Include router
app.include_router(career_router)
app.include_router(task_router)
app.include_router(auth.router)