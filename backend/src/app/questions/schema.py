from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class ResponseModel(BaseModel):
    question: str
    answer: str
    created_at: datetime
