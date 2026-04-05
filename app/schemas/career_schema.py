from pydantic import BaseModel
class CareerBase(BaseModel):
   resume_text: str
   job_description: str