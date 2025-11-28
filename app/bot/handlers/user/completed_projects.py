from aiogram import Router, F
from aiogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
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


@router.message(F.text == "💎 Завершенные проекты")
async def start_show_completed_projects(message: Message, state: FSMContext) -> None:
    await message.delete()

    completed_projects_current_offset = 0
    await state.update_data(
        completed_projects_current_offset=completed_projects_current_offset
    )

    async with container() as context:
        filters = GetCompletedProjectsListFilters(limit=1, offset=0)
        get_completed_project = await context.get(GetCompletedProjectsListInteractor)
        result = await get_completed_project(filters)

    project = result.projects[0]

    reply_markup = get_pagination_keyboard(
        current_offset=completed_projects_current_offset,
        total_count=result.total_projects,
    )

    await message.answer_photo(photo=project.photo, reply_markup=reply_markup)


@router.callback_query(F.data == "next_project")
async def show_next_completed_project(
    callback: CallbackQuery, state: FSMContext
) -> None:
    completed_projects_current_offset = await state.get_value(
        "completed_projects_current_offset"
    )
    if completed_projects_current_offset is None:
        return
