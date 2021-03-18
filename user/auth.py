from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from starlette import status

from config import ACCESS_TOKEN_EXPIRES_MINUTES, SECRET_KEY, CRYPT_ALGORITHM
from core.security.models import TokenData
from core.security.security import verify_pass
from .schemes import User, UserInDB


fake_users_db = {
    'valera': ''
}


def get_user(db, name: str):
    if name in db:
        user_dict = db[name]
        return UserInDB(**user_dict)


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_pass(password, user.hashed_pass):
        return False
    return user


# async def get_current_user(token: str = Depends()):
#     credential_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail='Could not validate credentials',
#         headers={'WWW-Authenticate': 'Bearer'}
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[CRYPT_ALGORITHM])
#         username: str = payload.get('sub')
#         if username is None:
#             raise credential_exception
#         token_data = TokenData(username=username)
#
#     except JWTError:
#         raise credential_exception
#
#     user = get_user(fake_users_db, name=token_data.username)
#     if user is None:
#         raise credential_exception
#
#     return user
#
#
# async def get_current_active_user(cur_user: User = Depends(get_current_user)):
#     if cur_user.disabled:
#         raise HTTPException(status_code=400, detail='Inactive user')
#     return cur_user
