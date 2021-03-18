from fastapi import APIRouter

from blog import blog_api


routes = APIRouter()

routes.include_router(blog_api.router, prefix='/blog')
