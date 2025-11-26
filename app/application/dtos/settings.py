from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class SettingsDTO:
    contact_phone_number: str
    contact_address: str
    contact_email: str


@dataclass(frozen=True, eq=False)
class ContactInfoDTO:
    contact_phone_number: str
    contact_address: str
    contact_email: str
