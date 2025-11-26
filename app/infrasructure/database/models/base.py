from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from app.utils.time_now_remove_tz import get_time_now_remove_tz


class BaseModel(DeclarativeBase):
    pass


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=get_time_now_remove_tz()
    )


class UpdatedAtMixin:
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        server_onupdate=func.now(),
        default=get_time_now_remove_tz(),
    )
