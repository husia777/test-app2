from fastapi import FastAPI, Depends
import requests
from questions.schema import ResponseModel
from questions.service import QuestionService
app = FastAPI()


@app.post('/')
async def get_question(questions_num: int, service: QuestionService = Depends()):
    return await service.get_question(questions_num)
