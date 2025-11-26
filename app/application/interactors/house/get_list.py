from dataclasses import dataclass

from app.application.dtos.house import GetHouseListFilters, ListHousesDTO
from app.infrasructure.repositories.house.base import BaseHouseRepository


@dataclass(frozen=True, eq=False)
class GetHouseListInteractor:
    house_repository: BaseHouseRepository

    async def __call__(self, filters: GetHouseListFilters) -> ListHousesDTO:
        houses = await self.house_repository.get_list(filters=filters)
        total_count = await self.house_repository.get_total_count()

        return ListHousesDTO(total_houses=total_count, houses=houses)
