from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class AppError(Exception):
    error_code: str = "APP_ERROR"

    @property
    def message(self) -> str:
        return "Ошибка приложения."
