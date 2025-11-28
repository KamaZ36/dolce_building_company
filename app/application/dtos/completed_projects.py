from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, eq=False)
class CompletedProjectPhotoDTO:
    id: UUID
    photo: str


@dataclass(frozen=True, eq=False)
class GetCompletedProjectsListFilters:
    limit: int = 5
    offset: int = 0


@dataclass(frozen=True, eq=False)
class CompletedProjectsListDTO:
    total_projects: int
    projects: list[CompletedProjectPhotoDTO]
