from fastapi import Depends
import requests
from questions.schema import ResponseModel
from questions.repositories import SqlalchemyRepository


class QuestionService:
    def __init__(self,  repository: SqlalchemyRepository = Depends()) -> None:
        self.repository = repository

    async def get_question(self, questions_num: int):
        data = requests.get(
            f'https://jservice.io/api/random?count={questions_num}'
        ).json()
        await self.repository.save(data)

        return await self.repository.get_previous_answer_or_none()
