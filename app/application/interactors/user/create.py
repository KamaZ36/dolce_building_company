from dataclasses import dataclass
from app.utils import uuid7

from app.application.dtos.user import CreateUserDTO, UserDTO
from app.infrasructure.database.transaction_manager.base import TransactionManager
from app.infrasructure.repositories.user.base import BaseUserRepository


@dataclass(frozen=True, eq=False)
class CreateUserInteractor:
    user_repository: BaseUserRepository
    transaction_manager: TransactionManager

    async def __call__(self, user_data: CreateUserDTO):
        user_dto = UserDTO(id=uuid7(), tg_id=user_data.tg_id)
        await self.user_repository.create(user_dto)
        await self.transaction_manager.commit()
