from fastadmin import fastapi_app as admin_app
from fastapi import FastAPI

from app_cadastral.api.routers import main_router
from app_cadastral.core.config import settings
from app_cadastral.core.init_db import create_first_superuser
# from app_cadastral.core.user import create_superuser

app = FastAPI(
    title=settings.app_title,
    description=settings.description,
)

app.include_router(main_router)
app.mount("/admin", admin_app)


@app.on_event('startup')
async def startup():
    await create_first_superuser()
