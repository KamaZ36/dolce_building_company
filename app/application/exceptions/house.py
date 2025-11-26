from dataclasses import dataclass
from app.application.exceptions.base import AppError


@dataclass(frozen=True, eq=False)
class HouseNotFound(AppError):
    error_code = "HOUSE_NOT_FOUND"

    @property
    def message(self) -> str:
        return "Дом не найден."
