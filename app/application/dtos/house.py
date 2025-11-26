from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True, eq=False)
class HouseDTO:
    id: UUID
    name: str
    description: str
    price: Decimal
    total_area: Decimal
    living_area: Decimal
    photos: list[str]


@dataclass(frozen=True, eq=False)
class ListHousesDTO:
    total_houses: int
    houses: list[HouseDTO]


@dataclass(frozen=True, eq=False)
class GetHouseListFilters:
    limit: int = 5
    offset: int = 0
