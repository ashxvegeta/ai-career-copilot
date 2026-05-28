from fastapi import FastAPI
# importing:router from career.py Renaming it to career_router
from app.routes.career import router as career_router
from app.routes.task import router as task_router
from app.routes import auth
from app.routes.dashboard import router as dashboard_router
from app.routes.recommendation import router as recommendation_router
from app.routes.history import router as history_router
# Create app instance
app = FastAPI()
# Include router
app.include_router(career_router)
app.include_router(task_router)
app.include_router(auth.router)
app.include_router(dashboard_router)
app.include_router(recommendation_router)
app.include_router(history_router)