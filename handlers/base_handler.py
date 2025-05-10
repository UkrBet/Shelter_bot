from aiogram import Router
from aiogram.types import Message, CallbackQuery

# Створіть роутер для базових обробників (за потреби)
router = Router()


@router.message()
async def unknown_command(message: Message):
    await message.answer("Вибачте, я не розумію цієї команди.")


# Або обробник для невідомих callback-ів:
@router.callback_query()
async def unknown_callback(query: CallbackQuery):
    await query.answer("Вибачте, цей запит не обробляється.", show_alert=True)
