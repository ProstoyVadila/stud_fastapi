from sqlalchemy.orm import Session

from . import schemes
from .models import User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, limit: int = 100):
    return db.query(User).limit(limit).all()


def create_user(db: Session, user: schemes.UserInDB):
    ...
