from aiogram import Bot, Router, F
from aiogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    InputMediaPhoto,
)
from aiogram.fsm.context import FSMContext

from app.application.dtos.completed_projects import GetCompletedProjectsListFilters
from app.application.interactors.completed_project.get_list import (
    GetCompletedProjectsListInteractor,
)
from app.core.dependencies.container import container


router = Router()


def get_pagination_keyboard(
    current_offset: int, total_count: int
) -> InlineKeyboardMarkup:
    pagination_buttons = []

    if current_offset > 0:
        pagination_buttons.append(
            InlineKeyboardButton(text="⬅️ Назад", callback_data="prev_project")
        )

    if current_offset < total_count - 1:
        pagination_buttons.append(
            InlineKeyboardButton(text="Вперёд ➡️", callback_data="next_project")
        )

    return InlineKeyboardMarkup(inline_keyboard=[pagination_buttons])


async def show_completed_projects_with_offset(
    user_id: int, state: FSMContext, bot: Bot, current_offset: int
) -> None:
    completed_project_msg_id = await state.get_value("completed_project_msg_id")

    async with container() as context:
        filters = GetCompletedProjectsListFilters(limit=1, offset=current_offset)
        get_completed_project = await context.get(GetCompletedProjectsListInteractor)
        result = await get_completed_project(filters)

    project = result.projects[0]
    reply_markup = get_pagination_keyboard(
        current_offset=current_offset,
        total_count=result.total_projects,
    )

    if completed_project_msg_id:
        media = InputMediaPhoto(media=project.photo)
        msg = await bot.edit_message_media(
            chat_id=user_id,
            media=media,
            reply_markup=reply_markup,
            message_id=completed_project_msg_id,
        )
    else:
        msg = await bot.send_photo(
            chat_id=user_id, photo=project.photo, reply_markup=reply_markup
        )

    await state.update_data(
        completed_project_msg_id=msg.message_id,
        completed_projects_current_offset=current_offset,
    )


@router.message(F.text == "💎 Завершенные проекты")
async def start_show_completed_projects(
    message: Message, state: FSMContext, bot: Bot
) -> None:
    completed_project_msg_id = await state.get_value("completed_project_msg_id")
    if completed_project_msg_id:
        await state.update_data(completed_project_msg_id=None)
        await bot.delete_message(
            message_id=completed_project_msg_id, chat_id=message.from_user.id
        )

    await message.delete()
    await show_completed_projects_with_offset(
        user_id=message.from_user.id, state=state, bot=bot, current_offset=0
    )


@router.callback_query(F.data == "next_project")
async def show_next_completed_project(
    callback: CallbackQuery, state: FSMContext, bot: Bot
) -> None:
    completed_projects_current_offset = await state.get_value(
        "completed_projects_current_offset", 0
    )

    await show_completed_projects_with_offset(
        user_id=callback.from_user.id,
        state=state,
        bot=bot,
        current_offset=completed_projects_current_offset + 1,
    )


@router.callback_query(F.data == "prev_project")
async def show_prev_completed_project(
    callback: CallbackQuery, state: FSMContext, bot: Bot
) -> None:
    completed_projects_current_offset = await state.get_value(
        "completed_projects_current_offset", 0
    )

    await show_completed_projects_with_offset(
        user_id=callback.from_user.id,
        state=state,
        bot=bot,
        current_offset=completed_projects_current_offset - 1,
    )
