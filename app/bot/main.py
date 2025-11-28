import asyncio
import logging

from app.core.config import settings

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.bot.handlers import (
    command_start_router,
    house_show_router,
    contact_info_router,
    completed_projects_show_router,
    create_bid_router,
)


def add_routers(dp: Dispatcher) -> None:
    dp.include_router(command_start_router)
    dp.include_router(house_show_router)
    dp.include_router(contact_info_router)
    dp.include_router(completed_projects_show_router)
    dp.include_router(create_bid_router)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher(storage=MemoryStorage())
    add_routers(dp)

    bot = Bot(token=settings.tg_bot_token)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
