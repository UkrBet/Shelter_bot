import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

FAQ_QUESTIONS = {
    "Як подати заявку на усиновлення?": "Перейдіть в розділ 'Подати заявку' в головному меню та заповніть анкету.",
    "Які тварини зараз доступні?": "Натисніть кнопку 'Переглянути тварин' в головному меню.",
    "Як допомогти притулку?": "Натисніть кнопку 'Підтримати' для інформації про донати та волонтерство.",
    # Додайте інші питання та відповіді
}

@router.message(F.text == "FAQ")
@router.message(Command("faq"))
async def faq_command(message: Message):
    builder = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for question in FAQ_QUESTIONS:
        builder.add(KeyboardButton(text=question))
    builder.add(KeyboardButton(text="Написати волонтеру"))
    await message.answer("Оберіть питання, що вас цікавить:", reply_markup=builder.as_markup())

@router.message(F.text.in_(FAQ_QUESTIONS))
async def answer_faq(message: Message):
    await message.answer(FAQ_QUESTIONS[message.text])

@router.message(F.text == "Написати волонтеру")
async def contact_volunteer(message: Message):
    #: Замінити на реальний контакт волонтера (username або forward)
    await message.answer("Ви можете зв'язатися з волонтером через Telegram: @volunteer_username")

# Обробка повідомлень не по темі (пересилати волонтеру або логувати)
@router.message()
async def handle_unhandled_messages(message: Message, bot):
    #: Пересилати повідомлення адміністратору або волонтеру для обробки
    admin_id = 123456789  # Замініть на ID адміністратора з config.py
    try:
        await bot.forward_message(chat_id=admin_id, from_chat_id=message.chat.id, message_id=message.message_id)
        await message.answer("Ваше повідомлення передано волонтеру. Будь ласка, зачекайте на відповідь.")
    except Exception as e:
        logging.error(f"Помилка пересилання повідомлення: {e}")
        await message.answer("Виникла помилка при передачі вашого повідомлення.")