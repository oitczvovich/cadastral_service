import bcrypt
from sqlalchemy import Column, Integer, String, Boolean
from core.db import Base


class User(Base):
    """Модель пользователя."""
    username = Column(String(length=255), nullable=False, unique=True)
    password = Column(String(length=255), nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)

    def __str__(self):
        return self.username
