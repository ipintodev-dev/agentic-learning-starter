from pydantic import BaseModel, Field
from typing import Optional, Dict

class StartSession(BaseModel):
    user_id: str
    locale: Optional[str] = "en-US"

class RecommendationRequest(BaseModel):
    user_id: str
    subject: str

class SubmitRequest(BaseModel):
    user_id: str
    subject: str
    item_id: str
    student_answer: str

class ProfileOut(BaseModel):
    user_id: str
    mastery: Dict[str, float] = Field(default_factory=dict)