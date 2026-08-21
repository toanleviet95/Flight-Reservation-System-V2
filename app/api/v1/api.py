from fastapi import APIRouter
from app.features.users import router as users_router
from app.features.flights import router as flights_router

api_router = APIRouter()
api_router.include_router(users_router.router)
api_router.include_router(flights_router.router)

