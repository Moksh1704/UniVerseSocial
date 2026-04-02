import os

from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    DATABASE_URL = os.getenv("postgresql://universe_db_zkm0_user:is9dVqRZg2w1Oh4RR4kz2nMu9CzMDMs5@dpg-d77198h4tr6s738dsb8g-a/universe_db_zkm0")
    SECRET_KEY: str = "change-this-secret-key-in-production-min-32-chars"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    APP_NAME: str = "UniVerse"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    ALLOWED_ORIGINS: str = "http://localhost:3000,http://localhost:5173"
    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE_MB: int = 5

    @property
    def allowed_origins_list(self) -> List[str]:
        return [o.strip() for o in self.ALLOWED_ORIGINS.split(",")]

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
