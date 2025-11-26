from aiogram import Router, F
from aiogram.types import Message

from app.application.interactors.general.get_contact_info import (
    GetContactInfoInteractor,
)
from app.bot.messages.user_messages import ContactInfoMessage
from app.core.dependencies.container import container


router = Router()


@router.message(F.text == "🏢 Контакты")
async def get_contact_info_handler(message: Message) -> None:
    async with container() as context:
        get_contact_info = await context.get(GetContactInfoInteractor)
        contact_info = await get_contact_info()

    await message.answer(**ContactInfoMessage(contact_info).pack())
