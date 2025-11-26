from typing import Protocol
from uuid import UUID

from app.application.dtos.house import GetHouseListFilters, HouseDTO, ListHousesDTO


class BaseHouseRepository(Protocol):
    async def create(self, house_data: HouseDTO) -> None: ...

    async def get_by_id(self, house_id: UUID) -> HouseDTO | None: ...

    async def get_list(self, filters: GetHouseListFilters) -> ListHousesDTO: ...

    async def get_total_count(self) -> int: ...
