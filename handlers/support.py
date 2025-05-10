from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

router = Router()

@router.message(F.text == "Підтримати")
async def support_command(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton(text="Донат", callback_data="support_donate")],
        # [InlineKeyboardButton(text="Перетримка", callback_data="support_foster")],
        # [InlineKeyboardButton(text="Волонтерство", callback_data="support_volunteer")],
    ])
    await message.answer("Оберіть спосіб підтримки:", reply_markup=keyboard)


@router.callback_query(F.data == "support_donate")
async def donate_callback(query: CallbackQuery):
    # Доробити: Додати реквізити для донату
    await query.message.answer("Ви можете підтримати нас за наступними реквізитами:\nМонобанк: ...\nКарта: ...\nКрипта: ...")
    await query.answer()

# @router.callback_query(F.data == "support_foster")
# async def foster_callback(query: CallbackQuery):
#     # Доробити: Додати посилання на анкету або контакти для перетримки
#     await query.message.answer("Щоб дізнатися про перетримку тварин, будь ласка, заповніть анкету за посиланням: [посилання на анкету] або зв'яжіться з нами @foster_contact")
#     await query.answer()

# @router.callback_query(F.data == "support_volunteer")
# async def volunteer_callback(query: CallbackQuery):
#     # Доробити: Додати інформацію про волонтерство та контакт куратора
#     await query.message.answer("Якщо ви бажаєте стати волонтером, будь ласка, зв'яжіться з нашим куратором: @volunteer_coordinator для отримання детальної інформації.")
#     await query.answer()
