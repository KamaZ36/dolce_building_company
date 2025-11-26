from pydantic_settings import BaseSettings


class TgBotSettings(BaseSettings):
    tg_bot_token: str
