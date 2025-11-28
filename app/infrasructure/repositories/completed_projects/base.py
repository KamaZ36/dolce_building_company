from typing import Protocol

from app.application.dtos.completed_projects import (
    CompletedProjectPhotoDTO,
    GetCompletedProjectsListFilters,
)


class BaseCompletedProjectsRepository(Protocol):
    async def get_list(
        self, filters: GetCompletedProjectsListFilters
    ) -> list[CompletedProjectPhotoDTO]: ...

    async def get_total_count(self) -> int: ...
