from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Глобальные настройки приложения (читаются из .env при наличии)."""

    # Общие
    app_name: str = "Portable DocSearch"
    debug: bool = True
    host: str = "127.0.0.1"
    port: int = 8000

    # Безопасность
    secret_key: str = "change-me-please"
    access_token_expire_min: int = 30
    refresh_token_expire_min: int = 43200  # 30 дней

    # Пути (по умолчанию — относительно текущей рабочей директории проекта)
    db_path: str = "var/db/docsearch.db"
    storage_dir: str = "var/storage"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )

    @property
    def database_url(self) -> str:
        path = Path(self.db_path)
        if not path.is_absolute():
            path = Path.cwd() / path
        path.parent.mkdir(parents=True, exist_ok=True)
        # Важно: для sqlite три слеша для абсолютного пути
        return f"sqlite:///{path.as_posix()}"

    @property
    def storage_path(self) -> Path:
        p = Path(self.storage_dir)
        if not p.is_absolute():
            p = Path.cwd() / p
        p.mkdir(parents=True, exist_ok=True)
        return p


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Кэшированная загрузка настроек."""
    return Settings()
