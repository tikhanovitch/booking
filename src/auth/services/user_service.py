from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.models import User
from src.auth.schemas.user_schema import (
    UserCreateSchema, UserUpdateSchema
)


async def create_user(
        session: AsyncSession,
        body: UserCreateSchema
) -> User:
    user = User(
        first_name=body.first_name,
        last_name=body.last_name,
        role=body.role,
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_users(session: AsyncSession):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users


async def get_user(session: AsyncSession, user_id: int):
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    return user


async def update_user(
        session: AsyncSession,
        user_id: int,
        body: UserUpdateSchema
) -> User:
    user = await get_user(
        session=session,
        user_id=user_id
    )
    user.first_name = body.first_name
    user.last_name = body.last_name
    user.role = body.role
    await session.commit()
    await session.refresh(user)
    return user


async def delete_user(
    session: AsyncSession,
    user_id: int,
):
    user = await get_user(
        session=session,
        user_id=user_id
    )
    await session.delete(user)
    await session.commit()
