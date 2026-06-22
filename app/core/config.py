from functools import lru_cache
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Sample REST API"
    DEBUG: bool = False

    DATABASE: str = "sqlite"  
    DB_IP: str = "127.0.0.1"
    DB_NAME: str = "app"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASS: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        db = self.DATABASE.lower()

        if db == "mysql":
            driver = "aiomysql"
            auth = (
                f"{self.DB_USER}:{self.DB_PASS}@"
                if self.DB_PASS
                else f"{self.DB_USER}@"
            )
            return f"mysql+{driver}://{auth}{self.DB_IP}:{self.DB_PORT}/{self.DB_NAME}"

        if db == "postgres":
            driver = "asyncpg"
            auth = (
                f"{self.DB_USER}:{self.DB_PASS}@"
                if self.DB_PASS
                else f"{self.DB_USER}@"
            )
            return f"postgresql+{driver}://{auth}{self.DB_IP}:{self.DB_PORT}/{self.DB_NAME}"

        return "sqlite+aiosqlite:///./app.db"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
