import logging
from typing import Optional
import asyncpg
from pydantic import BaseSettings, PostgresDsn, Field, SecretStr
from dotenv import load_dotenv
import os


load_dotenv()

logger = logging.getLogger(__name__)

class GlobalConfig(BaseSettings):
    TITLE: str = "Tutorial"
    DESCRIPTION: str = "This is a tutorial project for my blog"

    DEBUG: bool = True
    TESTING: bool = False
    TIMEZONE: str = "UTC"
    DB_ECHO_LOG: bool = False

    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: SecretStr = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_HOST: str = Field(..., env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(..., env="POSTGRES_PORT")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")

    DATABASE_URL: Optional[
        PostgresDsn
    ] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    DB_ECHO_LOG: bool = False

    @property
    def async_database_url(self) -> Optional[str]:
        return (
            self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
            if self.DATABASE_URL
            else self.DATABASE_URL
        )

    # Api V1 prefix
    API_V1_STR = "/v1"

    class Config:
        case_sensitive = True
        env_prefix = ""
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = GlobalConfig()
