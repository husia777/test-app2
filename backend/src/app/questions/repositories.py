from sqlalchemy import select
from fastapi import Depends
from .schema import ResponseModel, AnswerModel
from .models import Question
from app.db.database import AsyncSessionLocal, get_session


class SqlalchemyRepository:
    def __init__(self,
                 session: AsyncSessionLocal = Depends(get_session)) -> None:
        self.session = session

    async def get_previous_answer_or_none(self) -> ResponseModel | None:
        data = await self.session.execute(select(Question).order_by(
            Question.id.desc()))

        data = data.scalar()
        print(data)
        print(data)
        print(data)
        print(data)
        print(data)
        print(data)
        print(data)
        print(data)
        print(data)
        print(data)
        print(data)
        return AnswerModel(question=data.question)

    async def save(self, batch: ResponseModel) -> None:
        for i in batch:
            self.session.add(Question(answer=i["answer"],
                                      question=i["question"]))
        await self.session.commit()
