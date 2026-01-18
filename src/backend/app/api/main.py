from fastapi import APIRouter

from backend.app.api.router.home import home

api_router= APIRouter()

api_router.include_router(home.router, tags=["home"])