from fastadmin import fastapi_app as admin_app
from fastapi import FastAPI

from api.routers import main_router
from core.config import settings

from sqlalchemy import select


from fastadmin import SqlAlchemyModelAdmin, register
from core.db import AsyncSessionLocal
from models.user import User
from models.land_plot import LandPlot


app = FastAPI(
    title=settings.app_title,
    description=settings.description,
)

app.include_router(main_router)
app.mount("/admin", admin_app)


@register(User, sqlalchemy_sessionmaker=AsyncSessionLocal)
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
            if not password==user.password:
                return None
            return user.id


@register(LandPlot, sqlalchemy_sessionmaker=AsyncSessionLocal)
class LandPlot(SqlAlchemyModelAdmin):
    list_display = ("cadastral_number", "lat", "long", "answer_server")
    list_display_links = ("cadastral_number",)
    list_filter = ("cadastral_number", "lat", "long", "answer_server")
    search_fields = ("cadastral_number",)
