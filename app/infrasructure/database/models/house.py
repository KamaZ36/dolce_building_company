from decimal import Decimal
from uuid import UUID

from app.core.config import settings

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.application.dtos.house import HouseDTO
from app.infrasructure.database.models.base import (
    BaseModel,
    CreatedAtMixin,
    UpdatedAtMixin,
)


class HouseModel(BaseModel, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "houses"

    id: Mapped[UUID] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[Decimal] = mapped_column(nullable=False)
    total_area: Mapped[Decimal] = mapped_column(nullable=False)
    living_area: Mapped[Decimal] = mapped_column(nullable=False)

    photos: Mapped[list["HousePhotoModel"]] = relationship(
        back_populates="house",
        cascade="all, delete-orphan",
        order_by="HousePhotoModel.sort_order",
    )

    def to_dto(self) -> HouseDTO:
        return HouseDTO(
            id=self.id,
            name=self.name,
            description=self.description,
            price=int(self.price),
            total_area=self.total_area,
            living_area=self.living_area,
            photos=[
                settings.file_storage_url + photo.file_name for photo in self.photos
            ],
        )


class HousePhotoModel(BaseModel, CreatedAtMixin):
    __tablename__ = "house_photos"

    id: Mapped[UUID] = mapped_column(primary_key=True, unique=True)
    house_id: Mapped[UUID] = mapped_column(ForeignKey("houses.id"), nullable=False)
    file_name: Mapped[str] = mapped_column(nullable=False)
    sort_order: Mapped[int] = mapped_column(
        default=0, server_default="0", nullable=False
    )

    house: Mapped["HouseModel"] = relationship(back_populates="photos")
