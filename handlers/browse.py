from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup
from database.animals import get_all_animals, get_filtered_animals
from keyboards.filters import create_filter_keyboard
from keyboards.animal_card import create_animal_card_keyboard

router = Router()

# Словник для зберігання поточної позиції користувача та фільтрів
user_animal_data = {}

async def send_animal_card(chat_id: int, animal: dict, keyboard: InlineKeyboardMarkup, bot):
    caption = f"<b>{animal['name']}</b>\n\n"
    caption += f"Історія: {animal['story']}\n"
    caption += f"Характер: {animal['character']}\n\n"
    caption += f"<b>Тип:</b> {animal['type']}\n"
    caption += f"<b>Стать:</b> {animal['gender']}\n"
    caption += f"<b>Вік:</b> {animal['age']}\n"
    caption += f"<b>Розмір:</b> {animal['size']}\n"
    if animal['vaccinated']:
        caption += "✅ Вакцинований\n"
    else:
        caption += "❌ Не вакцинований\n"
    if animal['sterilized']:
        caption += "✅ Стерилізований"
    else:
        caption += "❌ Не стерилізований"

    # Припустимо, що 'photo' - це шлях до файлу або URL
    try:
        await bot.send_photo(chat_id, photo=animal['photo'], caption=caption, reply_markup=keyboard)
    except Exception as e:
        await bot.send_message(chat_id, caption, reply_markup=keyboard)
        print(f"Помилка відправки фото: {e}")

@router.message(F.text == "Переглянути тварин")
async def browse_animals_handler(message: Message, bot):
    animals = get_all_animals()
    if animals:
        user_animal_data[message.from_user.id] = {"animals": animals, "index": 0, "filters": {}}
        animal = animals[0]
        keyboard = create_animal_card_keyboard(animal['id'])
        await send_animal_card(message.chat.id, animal, keyboard, bot)
        await message.answer("Використовуйте кнопки під фото для навігації.", reply_markup=create_filter_keyboard())
    else:
        await message.answer("Наразі немає доступних тварин.")

@router.callback_query(F.data.startswith("filter_"))
async def filter_callback(query: CallbackQuery):
    filter_type, filter_value = query.data.split("_")[1:]
    user_id = query.from_user.id
    if user_id not in user_animal_data:
        await query.answer("Спочатку скористайтеся кнопкою 'Переглянути тварин'.", show_alert=True)
        return

    user_animal_data[user_id]["filters"][filter_type] = filter_value
    filtered_animals = get_filtered_animals(user_animal_data[user_id]["filters"])
    user_animal_data[user_id]["animals"] = filtered_animals
    user_animal_data[user_id]["index"] = 0

    if filtered_animals:
        animal = filtered_animals[0]
        keyboard = create_animal_card_keyboard(animal['id'])
        await send_animal_card(query.message.chat.id, animal, keyboard, query.bot)
        await query.answer()
    else:
        await query.message.answer("Не знайдено тварин за цими критеріями.")
        await query.answer()

@router.callback_query(F.data.startswith("animal_"))
async def animal_card_callback(query: CallbackQuery, bot):
    action, animal_id = query.data.split("_")[1:]
    user_id = query.from_user.id
    if user_id not in user_animal_data:
        await query.answer("Спочатку скористайтеся кнопкою 'Переглянути тварин'.", show_alert=True)
        return

    animals = user_animal_data[user_id]["animals"]
    current_index = user_animal_data[user_id]["index"]

    if action == "next":
        user_animal_data[user_id]["index"] = (current_index + 1) % len(animals)
        animal = animals[user_animal_data[user_id]["index"]]
        keyboard = create_animal_card_keyboard(animal['id'])
        await query.message.edit_caption(caption=f"<b>{animal['name']}</b>...", reply_markup=keyboard) # Тимчасово, краще оновити всю картку
        await query.message.edit_media(media=...) # Потрібно передавати нове фото
        await send_animal_card(query.message.chat.id, animal, keyboard, bot) # Повна перевідправка (простіше, але менш ефективно)
        await query.answer()
    elif action == "adopt":
        #: Запустити FSM для подачі заявки
        await query.message.answer(f"Ви обрали тварину з ID: {animal_id}. Розпочинаємо оформлення заявки...")
        await query.answer()
    elif action == "meet":
        #: Запустити FSM для запису на зустріч
        await query.message.answer(f"Ви хочете познайомитись з твариною з ID: {animal_id}. Заповніть форму...")
        await query.answer()