import bcrypt
from fastadmin import SqlAlchemyModelAdmin, register
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, Integer, String, select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app_cadastral.core.db import Base, get_async_session


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)


@register(User, sqlalchemy_sessionmaker=get_async_session)
class UserAdmin(SqlAlchemyModelAdmin):
    exclude = ("hash_password",)
    list_display = ("id", "username", "is_superuser", "is_active")
    list_display_links = ("id", "username")
    list_filter = ("id", "username", "is_superuser", "is_active")
    search_fields = ("username",)

    async def authenticate(self, username, password):
        sessionmaker = self.get_sessionmaker()
        async with sessionmaker() as session:
            query = select(User).filter_by(username=username, password=password, is_superuser=True)
            result = await session.scalars(query)
            user = result.first()
            if not user:
                return None
            if not bcrypt.checkpw(password.encode(), user.hash_password.encode()):
                return None
            return user.id
