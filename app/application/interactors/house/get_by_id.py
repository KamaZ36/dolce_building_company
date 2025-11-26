from dataclasses import dataclass
from uuid import UUID

from app.application.dtos.house import HouseDTO
from app.application.exceptions.house import HouseNotFound

from app.infrasructure.repositories.house.base import BaseHouseRepository


@dataclass(frozen=True, eq=False)
class GetHouseByIdInteractor:
    house_repository: BaseHouseRepository

    async def __call__(self, house_id: UUID) -> HouseDTO:
        house = await self.house_repository.get_by_id(house_id)

        if house is None:
            raise HouseNotFound()

        return house
