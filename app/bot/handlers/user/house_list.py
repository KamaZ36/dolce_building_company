from aiogram import Bot, Router, F
from aiogram.types import Message, InputMediaPhoto, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.application.dtos.house import GetHouseListFilters
from app.application.interactors.house.get_list import GetHouseListInteractor

from app.bot.messages.user_messages import HouseCardMessage
from app.core.dependencies.container import container


router = Router()


async def show_house_by_offset(
    user_id: int, state: FSMContext, bot: Bot, current_offset: int
) -> None:
    media_group_msg_ids = await state.get_value("media_group_msg_ids")
    if media_group_msg_ids:
        await bot.delete_messages(chat_id=user_id, message_ids=media_group_msg_ids)

    info_msg_id = await state.get_value("info_msg_id")
    if info_msg_id:
        await bot.delete_message(chat_id=user_id, message_id=info_msg_id)

    print(current_offset)

    async with container() as req_container:
        filters = GetHouseListFilters(limit=1, offset=current_offset)
        interactor = await req_container.get(GetHouseListInteractor)
        result = await interactor(filters)

    house = result.houses[0]

    media = [InputMediaPhoto(media=photo) for photo in house.photos]

    media_group = await bot.send_media_group(media=media, chat_id=user_id)
    msg = await bot.send_message(
        **HouseCardMessage(
            house=house, total_count=result.total_houses, current_offset=current_offset
        ).pack(),
        chat_id=user_id,
    )

    await state.update_data(
        media_group_msg_ids=[msg.message_id for msg in media_group],
        current_offset=current_offset,
        info_msg_id=msg.message_id,
    )


@router.message(F.text == "📚 Каталог проектов")
async def start_showing_houses(message: Message, state: FSMContext, bot: Bot) -> None:
    await message.delete()
    await show_house_by_offset(
        user_id=message.from_user.id, state=state, bot=bot, current_offset=0
    )


@router.callback_query(F.data == "next_house")
async def show_next_house(callback: CallbackQuery, state: FSMContext, bot: Bot) -> None:
    current_offset = await state.get_value("current_offset")
    if current_offset is None:
        return

    await show_house_by_offset(
        user_id=callback.from_user.id,
        state=state,
        bot=bot,
        current_offset=current_offset + 1,
    )


@router.callback_query(F.data == "prev_house")
async def show_prev_house(callback: CallbackQuery, state: FSMContext, bot: Bot) -> None:
    current_offset = await state.get_value("current_offset")
    if current_offset is None:
        return

    await show_house_by_offset(
        user_id=callback.from_user.id,
        state=state,
        bot=bot,
        current_offset=current_offset - 1,
    )
