from fastapi import APIRouter, FastAPI
from src.auth.routers.auth_router import router as user_router


router = APIRouter(
    prefix="/api",
    tags=["Auth"]
)


router.include_router(user_router)
