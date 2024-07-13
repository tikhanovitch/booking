from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.database import get_async_session

from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas.user_schema import (
    UserCreateSchema,
    UserReadSchema, UserUpdateSchema,
)
from src.auth.services.user_service import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user,
)
# from src.database import SessionLocal

router = APIRouter(
    prefix="/users",
    tags=["Auth"]
)


# def get_session():
#     session = SessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()


# create user
@router.post(
    "",
    response_model=UserCreateSchema,
)
async def create_user_handler(
        body: UserCreateSchema,
        session: AsyncSession = Depends(get_async_session),
):
    return await create_user(
        session=session,
        body=body,
    )


@router.get(
    "",
    response_model=list[UserReadSchema]
)
async def read_users_handler(session: AsyncSession = Depends(get_async_session),):
    return await get_users(
        session=session,
    )


@router.get(
    "/{user_id}",
    response_model=UserReadSchema | None
)
async def read_user_handler(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    return await get_user(
        session=session,
        user_id=user_id
    )


@router.put(
    "/{user_id}",
    response_model=UserUpdateSchema
)
async def update_user_handler(
        user_id: int,
        body: UserUpdateSchema,
        session: AsyncSession = Depends(get_async_session),
):
    return await update_user(
        session=session,
        user_id=user_id,
        body=body
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user_handler(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    await delete_user(
        session=session,
        user_id=user_id,
    )
