from datetime import date
from typing import List

from pydantic.main import BaseModel

from blog.schemes import Post


class UserBase(BaseModel):
    name: str
    email: str
    created_at: date


class UserInDB(UserBase):
    hashed_pass: str


class User(UserBase):
    id: int
    is_active: bool
    posts: List[Post] = []

    class Config:
        orm_mode = True
