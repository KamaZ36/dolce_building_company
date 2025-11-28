from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.bot.messages.create_bid_messages import (
    GetBudgetMessage,
    GetBuildingPlaceMessage,
    GetHouseAreaMessage,
    GetIsReadyProjectMessage,
    GetMortgageMessage,
    GetNumberFloorsMessage,
    GetPhoneNumberUserMessage,
)
from app.bot.states.user import CreateBidStates


router = Router()


@router.message(F.text == "📊 Расчитать стоимость")
async def ask_floors_number(message: Message, state: FSMContext) -> None:
    await message.answer(**GetNumberFloorsMessage().pack())


@router.callback_query(F.data.startswith("bid:floors:"))
async def get_floors_number(callback: CallbackQuery, state: FSMContext) -> None:
    floors_number = callback.data.split(":")[-1]  # type: ignore
    await state.update_data(floors=floors_number)

    await callback.message.edit_text(**GetBuildingPlaceMessage().pack())  # type: ignore


@router.callback_query(F.data.startswith("bid:place:"))
async def get_building_place(callback: CallbackQuery, state: FSMContext) -> None:
    building_place = bool(callback.data.split(":")[-1])  # type: ignore
    await state.update_data(place=building_place)

    await callback.message.edit_text(**GetMortgageMessage().pack())  # type: ignore


@router.callback_query(F.data.startswith("bid:mortgage:"))
async def get_is_mortgage(callback: CallbackQuery, state: FSMContext) -> None:
    is_mortgage = bool(callback.data.split(":")[-1])  # type: ignore
    await state.update_data(is_mortgage=is_mortgage)

    await callback.message.edit_text(**GetHouseAreaMessage().pack())  # type: ignore


@router.callback_query(F.data.startswith("bid:area:"))
async def get_house_area(callback: CallbackQuery, state: FSMContext) -> None:
    house_area = callback.data.split(":")[-1]  # type: ignore
    await state.update_data(area=house_area)

    await callback.message.edit_text(**GetIsReadyProjectMessage().pack())  # type: ignore


@router.callback_query(F.data.startswith("bid:project:"))
async def get_is_ready_project(callback: CallbackQuery, state: FSMContext) -> None:
    is_ready_project = bool(callback.data.split(":")[-1])  # type: ignore
    await state.update_data(is_ready_project=is_ready_project)

    await callback.message.edit_text(**GetBudgetMessage().pack())  # type: ignore


@router.callback_query(F.data.startswith("bid:budget:"))
async def get_budget(callback: CallbackQuery, state: FSMContext) -> None:
    budget = callback.data.split(":")[-1]  # type: ignore
    await state.update_data(budget=budget)

    await callback.message.edit_text(**GetPhoneNumberUserMessage().pack())  # type: ignore
    await state.set_state(CreateBidStates.get_phone_number)


@router.message(F.text)
async def get_phone_number_user(message: Message, state: FSMContext) -> None:
    phone_number = message.text

    await state.clear()
