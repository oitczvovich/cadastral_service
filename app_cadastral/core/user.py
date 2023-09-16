from typing import Optional, Union
import bcrypt
from sqlalchemy import select
from fastadmin import SqlAlchemyModelAdmin, register

from app_cadastral.core.config import settings
from app_cadastral.models.user import User
from app_cadastral.models.land_plot import LandPlot
from app_cadastral.core.db import AsyncSessionLocal
from fastapi import Depends, Request
from fastapi_users import (BaseUserManager, FastAPIUsers, IntegerIDMixin,
                           InvalidPasswordException)
from fastapi_users.authentication import (AuthenticationBackend,
                                          BearerTransport, JWTStrategy)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app_cadastral.core.config import settings
from app_cadastral.core.db import get_async_session
from app_cadastral.schemas.user import UserCreate


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

bearer_transport = BearerTransport(tokenUrl='auth/jwt/login')


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.secret, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 3:
            raise InvalidPasswordException(
                reason='Password should be at least 3 characters'
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason='Password should not contain e-mail'
            )

    async def on_after_register(
            self, user: User, request: Optional[Request] = None
    ):
        print(f'Пользователь {user.email} зарегистрирован.')


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)


@register(User, sqlalchemy_sessionmaker=AsyncSessionLocal)
class UserAdmin(SqlAlchemyModelAdmin):
    exclude = ("hashed_password",)
    list_display = ("id", "username", "is_superuser", "is_active")
    list_display_links = ("id", "username")
    list_filter = ("id", "username", "is_superuser", "is_active")
    search_fields = ("username",)

    async def authenticate(self, username, password):
        sessionmaker = self.get_sessionmaker()
        async with sessionmaker() as session:
            query = select(User).filter_by(username=username, is_superuser=True)   # убрал фильтр по hash_password
            print('\nQEUR\n', query)
            result = await session.scalars(query)
            user = result.first()
            print('RESult', user)
            if not user:
                return None
            if not bcrypt.checkpw(password.encode(), user.hashed_password):
                return None
            return user.id


@register(LandPlot, sqlalchemy_sessionmaker=AsyncSessionLocal)
class LandPlot(SqlAlchemyModelAdmin):
    list_display = ("cadastral_number", "lat", "long", "answer_server")
    list_display_links = ("cadastral_number",)
    list_filter = ("cadastral_number", "lat", "long", "answer_server")
    search_fields = ("cadastral_number",)


# superuser = User(
#     username='admin12', 
#     is_superuser=True,
#     is_active=True,
#     email='superTest@mailuser.com',
#     hashed_password=bcrypt.hashpw('admin123'.encode(), bcrypt.gensalt()),
#     is_verified=True,
# )

# # Сохранение суперпользователя в базе данных
# async def create_superuser():
#     sessionmaker = AsyncSessionLocal
#     async with sessionmaker() as session:
#         session.add(superuser)
#         await session.commit()

