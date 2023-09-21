import pytest
from tests.conftest import (
    app, get_async_session, override_db
)
from fastapi.testclient import TestClient

from app_cadastral.models.user import User

superuser = User(
    id=1,
    is_active=True,
    is_superuser=True,
)

@pytest.fixture
def superuser_client():
    app.dependency_overrides = {}
    app.dependency_overrides[get_async_session] = override_db
    with TestClient(app) as client:
        yield client