from asyncio import Protocol

from app.application.dtos.settings import SettingsDTO


class BaseSettingsRepository(Protocol):
    async def get_settings(self) -> SettingsDTO: ...
