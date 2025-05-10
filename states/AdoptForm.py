from aiogram.fsm.state import StatesGroup, State


class AdoptForm(StatesGroup):
    name = State()
    contact = State()
    experience = State()
    living_conditions = State()
    agreement = State()
