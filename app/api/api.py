from fastapi import APIRouter
from app.api.endpoints import users, organizations, tests, questions

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(organizations.router, prefix="/organizations", tags=["organizations"])
api_router.include_router(tests.router, prefix="/tests", tags=["tests"])
api_router.include_router(questions.router, prefix="/questions", tags=["questions"])