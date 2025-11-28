from aiogram.fsm.state import State, StatesGroup


class CreateBidStates(StatesGroup):
    get_phone_number = State()
