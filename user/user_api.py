from datetime import timedelta
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from core.db import get_db
from core.security.models import Token
from config import ACCESS_TOKEN_EXPIRES_MINUTES
from core.security.security import create_access_token
from user.auth import authenticate_user

router = APIRouter()


@router.post('/token', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(get_db)):

    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token = create_access_token(
        data={
            'sub': user.name
        },
        expires_delta=access_token_expires
    )
    return {
        'access_token': access_token,
        'token_type': 'Bearer'
    }


@router.get('/me')
async def get_current_user():
    ...
