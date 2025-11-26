from typing import Protocol

from app.application.dtos.user import UserDTO


class BaseUserRepository(Protocol):
    async def create(self, user_data: UserDTO) -> None: ...
