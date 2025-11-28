from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dtos.completed_projects import (
    CompletedProjectPhotoDTO,
    GetCompletedProjectsListFilters,
)
from app.infrasructure.database.models.completed_projects import (
    CompletedProjectsPhotoModel,
)
from app.infrasructure.repositories.completed_projects.base import (
    BaseCompletedProjectsRepository,
)


class SQLAlchemyCompletedProjectsRepository(BaseCompletedProjectsRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_list(
        self, filters: GetCompletedProjectsListFilters
    ) -> list[CompletedProjectPhotoDTO]:
        query = (
            select(CompletedProjectsPhotoModel)
            .limit(filters.limit)
            .offset(filters.offset)
        )
        results = await self._session.execute(query)
        completed_projects_models = results.scalars()
        return [project.to_dto() for project in completed_projects_models]

    async def get_total_count(self) -> int:
        query = select(func.count(CompletedProjectsPhotoModel.id))
        result = await self._session.execute(query)
        return result.scalar()
