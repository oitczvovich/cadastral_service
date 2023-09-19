from typing import Optional
from pydantic import EmailStr
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: Optional[EmailStr]
