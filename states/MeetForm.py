from aiogram.fsm.state import StatesGroup, State


class MeetForm(StatesGroup):
    animal = State()
    contact = State()
    time = State()
