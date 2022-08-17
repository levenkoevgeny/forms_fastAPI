from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.db.session import async_session
from app.models import User
router = APIRouter()


@router.get("/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100) -> Any:
    async with async_session() as session:
        return await crud.user.get_all_users(session, skip=skip, limit=limit)


@router.post("/", response_model=schemas.User)
async def create_user(user_in: schemas.UserCreate) -> User:
    async with async_session() as session:
        async with session.begin():
            return await crud.user.create(session, obj_in=user_in)
