import contextlib
import logging

from fastapi_users.exceptions import UserAlreadyExists
from pydantic import EmailStr

from app_cadastral.core.config import settings
from app_cadastral.core.db import get_async_session

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
from app_cadastral.core.user import get_user_db, get_user_manager
from app_cadastral.schemas.user import UserCreate

get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
        username: str, email: EmailStr, password: str, is_superuser: bool = False
):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    await user_manager.create(
                        UserCreate(
                            username=username,
                            email=email,
                            password=password,
                            is_superuser=is_superuser
                        )
                    )
    except UserAlreadyExists:
        logging.exception('User is already exists.')


async def create_first_superuser():
    if (settings.first_superuser_email is not None and
            settings.first_superuser_password is not None):
        await create_user(
            username=settings.admin_name,
            email=settings.first_superuser_email,
            password=settings.first_superuser_password,
            is_superuser=True,
        )
