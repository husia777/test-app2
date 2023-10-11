from sqlalchemy import select, exists
from fastapi import Depends
from .schema import ResponseModel, AnswerModel
from .models import Question
from app.db.database import AsyncSessionLocal, get_session
# from db.database import AsyncSessionLocal, get_session


class SqlalchemyRepository:
    def __init__(self,
                 session: AsyncSessionLocal = Depends(get_session)) -> None:
        self.session = session
        self.counter = 0

    async def get_previous_answer_or_none(self) -> ResponseModel | None:
        data = await self.session.execute(select(Question).order_by(
            Question.id.desc()))

        data = data.scalar()
        return AnswerModel(question=data.question)

    async def check_question_and_save(self, batch: ResponseModel) -> None:
        for i in batch:
            exists_query = self.session.execute(
                select(Question).where(Question.id == i['id']).exists())
            if exists_query:
                self.counter += 1
                self.session.add(Question(answer=i["answer"],
                                          question=i["question"],
                                          question_id=i['id']))
        await self.session.commit()
