from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, CallbackQuery

router = Router()


class MeetForm(StatesGroup):
    animal = State()
    contact = State()
    time = State()


@router.callback_query(F.data.startswith("animal_meet_"))
async def meet_callback(query: CallbackQuery, state: FSMContext):
    animal_id = query.data.split("_")[-1]
    await state.set_state(MeetForm.animal)
    await state.update_data(animal_id=animal_id)
    await query.message.answer(
        f"Ви хочете зустрітися з твариною ID: {animal_id}. Будь ласка, вкажіть ваш контактний номер телефону або Telegram.")
    await query.answer()


@router.message(F.text == "Зустрітись")
async def meet_command(message: Message, state: FSMContext):
    await state.set_state(MeetForm.animal)
    await message.answer("З якою твариною ви хотіли б зустрітися (введіть ID)?")


@router.message(MeetForm.animal)
async def process_animal(message: Message, state: FSMContext):
    await state.update_data(animal=message.text)
    await state.set_state(MeetForm.contact)
    await message.answer("Будь ласка, вкажіть ваш контактний номер телефону або Telegram для зв'язку.")


@router.message(MeetForm.contact)
async def process_contact(message: Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await state.set_state(MeetForm.time)
    await message.answer("В який зручний для вас час ви хотіли б зустрітися (напишіть текстом або оберіть зі списку)?",
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                             KeyboardButton(text="Сьогодні ввечері"),
                             KeyboardButton(text="Завтра вдень"),
                             KeyboardButton(text="Інший час")
                         ))


@router.message(MeetForm.time)
async def process_time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    data = await state.get_data()
    await state.clear()
    #: Надіслати дані куратору або зберегти
    await message.answer(
        f"Дякуємо! Ваша заявка на зустріч:\nТварина ID: {data.get('animal_id') or data.get('animal')}\nКонтакти: {data['contact']}\nЧас: {data['time']}",
        reply_markup=ReplyKeyboardRemove())
    # Тут можна викликати функцію для збереження даних
    from database.forms import save_meet_form
    save_meet_form(data)
