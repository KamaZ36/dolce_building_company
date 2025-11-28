from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from app.core.config import settings

from app.application.dtos.completed_projects import CompletedProjectPhotoDTO
from app.infrasructure.database.models.base import BaseModel, CreatedAtMixin


class CompletedProjectsPhotoModel(BaseModel, CreatedAtMixin):
    __tablename__ = "completed_projects_photos"

    id: Mapped[UUID] = mapped_column(primary_key=True, unique=True)
    file_name: Mapped[str] = mapped_column(nullable=False)

    def to_dto(self) -> CompletedProjectPhotoDTO:
        return CompletedProjectPhotoDTO(
            id=self.id, photo=settings.file_storage_url + self.file_name
        )
