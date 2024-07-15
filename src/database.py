from fastapi import Depends
from src.auth.models import User
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src import settings

sync_engine = create_engine(settings.SYNC_URL, echo=settings.ECHO)
async_engine = create_async_engine(settings.ASYNC_URL, echo=settings.ECHO)

SessionLocal = sessionmaker(autocommit=settings.AUTOCOMMIT, autoflush=settings.AUTOFLUSH, bind=sync_engine)


async def get_async_session():
    async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
