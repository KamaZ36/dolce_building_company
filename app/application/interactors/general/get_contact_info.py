from dataclasses import dataclass

from app.application.dtos.settings import ContactInfoDTO
from app.infrasructure.repositories.settings.base import BaseSettingsRepository


@dataclass(frozen=True, eq=False)
class GetContactInfoInteractor:
    settings_repository: BaseSettingsRepository

    async def __call__(
        self,
    ) -> ContactInfoDTO:
        settings = await self.settings_repository.get_settings()

        contact_info = ContactInfoDTO(
            contact_phone_number=settings.contact_phone_number,
            contact_email=settings.contact_email,
            contact_address=settings.contact_address,
        )

        return contact_info
