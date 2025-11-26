from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.core.dependencies.container import container

from app.application.dtos.user import CreateUserDTO
from app.application.interactors.user.create import CreateUserInteractor

from app.bot.messages.user_messages import WelcomeMessage


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    try:
        async with container() as req_container:
            create_user_dto = CreateUserDTO(tg_id=message.from_user.id)
            create_user_interactor = await req_container.get(CreateUserInteractor)
            await create_user_interactor(create_user_dto)
    except Exception:
        pass

    await message.answer(**WelcomeMessage().pack())
