from sqlalchemy.ext.asyncio import AsyncSession

from dishka import Provider, Scope, provide

from app.infrasructure.repositories.completed_projects.base import (
    BaseCompletedProjectsRepository,
)
from app.infrasructure.repositories.completed_projects.sqlalchemy_repository import (
    SQLAlchemyCompletedProjectsRepository,
)
from app.infrasructure.repositories.house.base import BaseHouseRepository
from app.infrasructure.repositories.house.sqlalchemy_repository import (
    SQLHouseRepository,
)
from app.infrasructure.repositories.settings.base import BaseSettingsRepository
from app.infrasructure.repositories.settings.sqlalchemy_repository import (
    SQLalchemySettingsRepository,
)
from app.infrasructure.repositories.user.base import BaseUserRepository
from app.infrasructure.repositories.user.sqlalchemy_repository import SQLUserRepository


class RepositoriesProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_user_repository(self, session: AsyncSession) -> BaseUserRepository:
        return SQLUserRepository(session)

    @provide
    def get_house_repository(self, session: AsyncSession) -> BaseHouseRepository:
        return SQLHouseRepository(session)

    @provide
    def get_settings_repository(self, session: AsyncSession) -> BaseSettingsRepository:
        return SQLalchemySettingsRepository(session)

    @provide
    def get_completed_project_repository(
        self, session: AsyncSession
    ) -> BaseCompletedProjectsRepository:
        return SQLAlchemyCompletedProjectsRepository(session)
