from datetime import datetime, timedelta
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

from config import CRYPT_ALGORITHM, SECRET_KEY


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_pass(plain_pass: str, hashed_pass: str):
    return pwd_context.verify(plain_pass, hashed_pass)


def get_pass_hash(password: str):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'expire': expire})
    return jwt.encode(to_encode, SECRET_KEY, CRYPT_ALGORITHM)
