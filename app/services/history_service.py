from app.database.models import AnalysisHistory
from app.database.db import SessionLocal



def get_analysis_history(user_id: int):
    db = SessionLocal()
    try:
        history = db.query(AnalysisHistory).filter(AnalysisHistory.user_id == user_id).all()
        return history
    finally:
        db.close()