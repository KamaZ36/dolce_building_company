from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dtos.user import UserDTO

from app.infrasructure.database.models.user import UserModel
from app.infrasructure.repositories.user.base import BaseUserRepository


class SQLUserRepository(BaseUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, user_data: UserDTO) -> None:
        user_model = UserModel(id=user_data.id, tg_id=user_data.tg_id)
        self._session.add(user_model)
