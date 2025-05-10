from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_animal_card_keyboard(animal_id: int):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Наступна", callback_data="animal_next"),
        InlineKeyboardButton(text="Подати заявку", callback_data=f"animal_adopt_{animal_id}"),
        InlineKeyboardButton(text="Зустрітись", callback_data=f"animal_meet_{animal_id}"),
    )
    return builder.as_markup()
