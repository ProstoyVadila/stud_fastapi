from fastapi import APIRouter

from blog import blog_api
from user import user_api


routes = APIRouter()

routes.include_router(blog_api.router, prefix='/blog')
routes.include_router(user_api.router, prefix='/user')
