from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Кадастровый сервис'
    database_url: str
    secret: str = 'SECRET'
    description: str = 'Сервис уточняет свободен ли земельный участок.'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    ADMIN_USER_MODEL: str = 'SuperUser'
    ADMIN_USER_MODEL_USERNAME_FIELD: str = 'username'
    ADMIN_SECRET_KEY: str
    admin_name: str

    class Config:
        env_file = '.env'


settings = Settings()
