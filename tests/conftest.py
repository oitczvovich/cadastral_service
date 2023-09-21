from pathlib import Path

import pytest
import pytest_asyncio
from mixer.backend.sqlalchemy import Mixer as _mixer
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

try:
    from app_cadastral.main import app
except (NameError, ImportError):
    raise AssertionError(
        'Не обнаружен объект приложения `app`.'
        'Проверьте и поправьте: он должен быть доступен в модуле `app.main`.',
    )

try:
    from app_cadastral.core.db import Base, get_async_session
except (NameError, ImportError):
    raise AssertionError(
        'Не обнаружены объекты `Base, get_async_session`. '
        'Проверьте и поправьте: они должны быть доступны в модуле `app.core.db`.',
    )


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent   # /home/oitz/Dev/cadastral_service/app_cadastral


pytest_plugins = [
    'tests.fixtures.user',
    'tests.fixtures.data',
]

TEST_DB = BASE_DIR / 'app_cadastral' / 'data' / 'test.db'
SQLALCHEMY_DATABASE_URL = f'sqlite+aiosqlite:///{str(TEST_DB)}'

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    class_=AsyncSession, autocommit=False, autoflush=False, bind=engine,
)


async def override_db():
    async with TestingSessionLocal() as session:
        yield session


@pytest_asyncio.fixture(autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
def mixer():
    mixer_engine = create_engine(f'sqlite:///{str(TEST_DB)}')
    session = sessionmaker(bind=mixer_engine)
    return _mixer(session=session(), commit=True)