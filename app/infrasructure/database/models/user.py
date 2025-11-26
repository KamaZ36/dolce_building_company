from uuid import UUID

from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from app.infrasructure.database.models.base import BaseModel, CreatedAtMixin


class UserModel(BaseModel, CreatedAtMixin):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, unique=True)
    tg_id: Mapped[int] = mapped_column(BIGINT, unique=True, nullable=False)
