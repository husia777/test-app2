from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):

    postgres_user: str
    postgres_db: str
    postgres_password: str
    sqlalchemy_database_url: str

    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    app_settings = Settings(
        _env_file="./.env",
        _env_file_encoding="utf-8"
    )
    return app_settings


settings = get_settings()
