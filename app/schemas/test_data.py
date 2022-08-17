from typing import Optional
from pydantic import BaseModel


class OrganizationBase(BaseModel):
    organization_name: str

    class Config:
        orm_mode = True


class TestDataBase(BaseModel):
    test_name: str
    extra_data: Optional[str] = None
    index_number: Optional[int] = None
    introduction: Optional[str] = None
    is_active: Optional[bool] = True
    # organization: OrganizationBase

    class Config:
        orm_mode = True