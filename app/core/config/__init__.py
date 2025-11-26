from pydantic_settings import BaseSettings
from app.core.config.database import DataBaseSettings
from app.core.config.tg_bot import TgBotSettings


class AppSettings(DataBaseSettings, TgBotSettings, BaseSettings):
    app_name: str
    debug: bool

    file_storage_url: str

    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"


settings = AppSettings()
