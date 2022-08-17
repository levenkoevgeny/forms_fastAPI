from app.models import TestData
from typing import List
from sqlalchemy.orm import Session

from sqlalchemy import select


class CRUDTest:
    async def get_all_tests(self, db: Session, skip: int = 0, limit: int = 100) -> List[TestData]:
        result = await db.execute(select(TestData).offset(skip).limit(limit))
        return result.scalars().all()


test_data = CRUDTest()