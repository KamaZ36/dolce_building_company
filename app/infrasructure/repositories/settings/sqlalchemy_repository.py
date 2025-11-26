from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dtos.settings import SettingsDTO
from app.infrasructure.database.models.settings import SettingsModel
from app.infrasructure.repositories.settings.base import BaseSettingsRepository


class SQLalchemySettingsRepository(BaseSettingsRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_settings(self) -> SettingsDTO:
        query = select(SettingsModel).limit(1)
        result = await self._session.execute(query)
        settings_model = result.scalar()
        return SettingsDTO(
            contact_address=settings_model.contact_address,
            contact_email=settings_model.contact_email,
            contact_phone_number=settings_model.contact_phone_number,
        )
