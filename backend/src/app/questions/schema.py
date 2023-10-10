from pydantic import BaseModel
from datetime import datetime


class ResponseModel(BaseModel):
    question: str
    answer: str
    created_at: datetime


class AnswerModel(BaseModel):
    question: str
