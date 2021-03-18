from datetime import date

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str


class PostList(PostBase):
    id: int
    created_at: date

    class Config:
        orm_mode = True
