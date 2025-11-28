from dataclasses import dataclass

from app.application.dtos.completed_projects import (
    CompletedProjectsListDTO,
    GetCompletedProjectsListFilters,
)
from app.infrasructure.repositories.completed_projects.base import (
    BaseCompletedProjectsRepository,
)


@dataclass(frozen=True, eq=False)
class GetCompletedProjectsListInteractor:
    project_repository: BaseCompletedProjectsRepository

    async def __call__(
        self, filters: GetCompletedProjectsListFilters
    ) -> CompletedProjectsListDTO:
        projects = await self.project_repository.get_list(filters=filters)
        total_count = await self.project_repository.get_total_count()

        projects_list = CompletedProjectsListDTO(
            total_projects=total_count, projects=projects
        )

        return projects_list
