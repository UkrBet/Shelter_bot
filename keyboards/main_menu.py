from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Переглянути тварин")
    builder.button(text="Подати заявку")
    builder.button(text="Підтримати")
    builder.button(text="FAQ")
    builder.adjust(2)  # Розташування кнопок в два стовпці
    return builder.as_markup(resize_keyboard=True)
