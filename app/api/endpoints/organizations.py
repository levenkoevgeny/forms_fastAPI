from fastapi import APIRouter
from typing import List, Any
from app import schemas, crud, models
from app.db.session import async_session
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload


router = APIRouter()


@router.get("/", response_model=List[schemas.OrganizationBase])
async def read_organizations(skip: int = 0, limit: int = 100) -> Any:
    async with async_session() as session:
        async with session.begin():
            stmt = select(models.Organization).options(selectinload(models.Organization.tests))
            # print('stmt', stmt)

            # AsyncSession.execute() is used for 2.0 style ORM execution
            # (same as the synchronous API).
            result = await session.execute(stmt)
            # print('res', result)

            # result is a buffered Result object.
            # for a1 in result.scalars():
            #     print(a1)
            #     print(f"created at: {a1.data_created}")
            #     for b1 in a1.tests:
            #         print('test', b1)

            return result.scalars().all()

            # return await crud.test_data.get_all_organizations(session, skip=skip, limit=limit)