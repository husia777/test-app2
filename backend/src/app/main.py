from fastapi import FastAPI, Depends

from app.questions.service import QuestionService

# from questions.service import QuestionService


app = FastAPI()


@app.post('/')
async def get_question(questions_num: int, service:
                       QuestionService = Depends()):
    return await service.get_question(questions_num)
