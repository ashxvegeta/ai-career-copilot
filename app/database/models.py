from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db import Base
from sqlalchemy import Text

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    skill_name = Column(String, nullable=False)
    task_text = Column(String, nullable=False)
    status = Column(String, default="pending")

class AnalysisHistory(Base):

    __tablename__ = "analysis_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    resume_text = Column(Text)

    job_description = Column(Text)

    analysis_result = Column(Text)