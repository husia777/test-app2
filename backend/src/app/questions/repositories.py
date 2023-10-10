from db.database import get_session, AsyncSession
from fastapi import Depends
from questions.schema import ResponseModel
from sqlalchemy import select
from questions.models import Question


class SqlalchemyRepository:
    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        self.session = session

    async def get_previous_answer_or_none(self):
        await self.session.execute(select(Question).order_by(
            Question.id.desc())).one_or_none()

    async def save(self, batch: ResponseModel):
        objects = []
        for i in batch:
            print(i["answer"], i["question"])
            self.session.add(Question(answer=i["answer"],
                                                 question=i["question"]))
        await self.session.commit()
