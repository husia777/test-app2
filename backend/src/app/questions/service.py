from fastapi import Depends
import requests

from .repositories import SqlalchemyRepository


class QuestionService:
    def __init__(self,  repository: SqlalchemyRepository = Depends()) -> None:
        self.repository = repository

    async def get_question(self, questions_num: int):
        data = requests.get(
            f'https://jservice.io/api/random?count={questions_num}'
        ).json()
        while self.repository.counter == 0:
            await self.repository.check_question_and_save(data)
        self.repository.counter = 0
        return await self.repository.get_previous_answer_or_none()
