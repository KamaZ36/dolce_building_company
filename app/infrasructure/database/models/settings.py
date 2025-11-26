from sqlalchemy.orm import Mapped, mapped_column

from app.infrasructure.database.models.base import BaseModel, UpdatedAtMixin


class SettingsModel(BaseModel, UpdatedAtMixin):
    __tablename__ = "settings"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    contact_phone_number: Mapped[str] = mapped_column(nullable=False)
    contact_address: Mapped[str] = mapped_column(nullable=False)
    contact_email: Mapped[str] = mapped_column(nullable=False)
