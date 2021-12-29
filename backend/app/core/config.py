import logging
from enum import Enum
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn

load_dotenv("../.env")

logger = logging.getLogger(__name__)


class EnvironmentEnum(str, Enum):
    PRODUCTION = "production"
    LOCAL = "local"


class GlobalConfig(BaseSettings):
    ENVIRONMENT: EnvironmentEnum
    DEBUG: bool = False
    TESTING: bool = False
    TIMEZONE: str
    TITLE: str
    DESCRIPTION: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SECRET_KEY: str
    DATABASE_URL: Optional[
        PostgresDsn
    ] = "postgresql://postgres:postgres@localhost:5432/postgres"  # just so it work locally
    DB_ECHO_LOG: bool = False

    # Api V1 prefix
    API_V1_STR: str

    @property
    def async_database_url(self) -> Optional[str]:
        return (
            self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
            if self.DATABASE_URL
            else self.DATABASE_URL
        )


    class Config:
        case_sensitive = True
        env_prefix = ""
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = GlobalConfig()
