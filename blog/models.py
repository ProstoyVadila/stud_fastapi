from sqlalchemy import Column, String, Integer, DateTime, Text

from core.db import Base


class Post(Base):
    __tablename__ = 'blog_posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(Text)
    created_at = Column(DateTime)

