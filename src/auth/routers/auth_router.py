from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.auth.manager import current_active_user, auth_backend, fastapi_users
from src.auth.models import User
from src.auth.schemas.user_schema import UserRead, UserCreate, UserUpdate
from src.database import get_async_session

from sqlalchemy.ext.asyncio import AsyncSession

# from src.auth.schemas.user_schema import (
#     UserCreateSchema,
#     UserReadSchema, UserUpdateSchema,
# )
# from src.auth.services.user_service import (
#     create_user,
#     get_users,
#     get_user,
#     update_user,
#     delete_user,
# )
# from src.database import SessionLocal

router = APIRouter(
    prefix="/users",
    tags=["Auth"]
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["Auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/users",
    tags=["Auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/users",
    tags=["Auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/users",
    tags=["Auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["Auth"],
)


# @router.get("/authenticated-route")
# async def authenticated_route(user: User = Depends(current_active_user)):
#     return {"message": f"Hello {user.email}!"}


# def get_session():
#     session = SessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()

#
# # create user
# @router.post(
#     "",
#     response_model=UserCreateSchema,
# )
# async def create_user_handler(
#         body: UserCreateSchema,
#         session: AsyncSession = Depends(get_async_session),
# ):
#     return await create_user(
#         session=session,
#         body=body,
#     )
#
#
# @router.get(
#     "",
#     response_model=list[UserReadSchema]
# )
# async def read_users_handler(session: AsyncSession = Depends(get_async_session),):
#     return await get_users(
#         session=session,
#     )
#
#
# @router.get(
#     "/{user_id}",
#     response_model=UserReadSchema | None
# )
# async def read_user_handler(
#         user_id: int,
#         session: AsyncSession = Depends(get_async_session),
# ):
#     return await get_user(
#         session=session,
#         user_id=user_id
#     )
#
#
# @router.put(
#     "/{user_id}",
#     response_model=UserUpdateSchema
# )
# async def update_user_handler(
#         user_id: int,
#         body: UserUpdateSchema,
#         session: AsyncSession = Depends(get_async_session),
# ):
#     return await update_user(
#         session=session,
#         user_id=user_id,
#         body=body
#     )
#
#
# @router.delete(
#     "/{user_id}",
#     status_code=status.HTTP_204_NO_CONTENT,
# )
# async def delete_user_handler(
#         user_id: int,
#         session: AsyncSession = Depends(get_async_session),
# ):
#     await delete_user(
#         session=session,
#         user_id=user_id,
#     )
