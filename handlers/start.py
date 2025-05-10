from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    builder = ReplyKeyboardBuilder()
    for text in ["Переглянути тварин", "Подати заявку", "Підтримати", "FAQ"]:
        builder.button(text=text)
    await message.answer(
        "Вітаємо у нашому притулку! Що вас цікавить?",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
