from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_filter_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Тип", callback_data="filter_type"))
    builder.row(
        InlineKeyboardButton(text="Вік", callback_data="filter_age"),
        InlineKeyboardButton(text="Розмір", callback_data="filter_size"),
        InlineKeyboardButton(text="Стать", callback_data="filter_gender"),
    )
    builder.row(
        InlineKeyboardButton(text="Вакцинація", callback_data="filter_vaccinated"),
        InlineKeyboardButton(text="Стерилізація", callback_data="filter_sterilized"),
    )
    return builder.as_markup()
