from uuid import UUID

from sqlalchemy.orm import selectinload
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dtos.house import GetHouseListFilters, HouseDTO

from app.infrasructure.database.models.house import HouseModel
from app.infrasructure.repositories.house.base import BaseHouseRepository


class SQLHouseRepository(BaseHouseRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, house_data: HouseDTO) -> None:
        house_model = HouseModel(
            id=house_data.id,
            name=house_data.name,
            description=house_data.description,
            price=house_data.price,
            total_area=house_data.total_area,
            living_area=house_data.living_area,
        )
        self._session.add(house_model)

    async def get_by_id(self, house_id: UUID) -> HouseDTO | None:
        query = select(HouseModel).where(HouseModel.id == house_id)
        result = await self._session.execute(query)
        house_model = result.scalar_one_or_none()
        return house_model.to_dto() if house_model else None

    async def get_list(self, filters: GetHouseListFilters) -> list[HouseDTO]:
        query = (
            select(HouseModel)
            .options(selectinload(HouseModel.photos))
            .limit(filters.limit)
            .offset(filters.offset)
        )
        results = await self._session.execute(query)
        house_models = results.scalars()
        return [house.to_dto() for house in house_models]

    async def get_total_count(self) -> int:
        query = select(func.count(HouseModel.id))
        result = await self._session.execute(query)
        return result.scalar()
