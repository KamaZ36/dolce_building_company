from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from dishka import Provider, provide, Scope

from app.infrasructure.database.connection import async_session_maker
from app.infrasructure.database.transaction_manager.base import TransactionManager
from app.infrasructure.database.transaction_manager.sqlalchemy import (
    SQLAlchemyTransactionManager,
)


class BaseProvider(Provider):
    # DATABASE
    @provide(scope=Scope.REQUEST)
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with async_session_maker() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    async def get_transaction_manager(
        self, session: AsyncSession
    ) -> TransactionManager:
        return SQLAlchemyTransactionManager(session)
