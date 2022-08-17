from fastapi import APIRouter
from typing import List, Any
from app import schemas, crud
from app.db.session import async_session

router = APIRouter()


@router.get("/", response_model=List[schemas.TestDataBase])
async def read_tests(skip: int = 0, limit: int = 100) -> Any:
    async with async_session() as session:
        return await crud.test_data.get_all_tests(session, skip=skip, limit=limit)