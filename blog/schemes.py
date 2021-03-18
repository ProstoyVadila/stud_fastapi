from datetime import date

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str
    created_at: date

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int


class PostCreate(PostBase):
    pass
