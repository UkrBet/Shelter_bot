from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from utils.validators import validate_phone, validate_email

router = Router()


class AdoptForm(StatesGroup):
    name = State()
    contact = State()
    experience = State()
    living_conditions = State()
    agreement = State()


@router.message(F.text == "Подати заявку")
async def adopt_command(message: Message, state: FSMContext):
    await state.set_state(AdoptForm.name)
    await message.answer("Як вас звати?")


@router.message(AdoptForm.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AdoptForm.contact)
    await message.answer("Будь ласка, вкажіть ваш номер телефону або email для зв'язку.")


@router.message(AdoptForm.contact)
async def process_contact(message: Message, state: FSMContext):
    if validate_phone(message.text) or validate_email(message.text):
        await state.update_data(contact=message.text)
        await state.set_state(AdoptForm.experience)
        await message.answer("Чи був у вас раніше досвід догляду за тваринами?")
    else:
        await message.answer("Невірний формат телефону або email. Будь ласка, введіть ще раз.")


@router.message(AdoptForm.experience)
async def process_experience(message: Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await state.set_state(AdoptForm.living_conditions)
    await message.answer("Які у вас умови проживання (квартира, приватний будинок тощо)?")


@router.message(AdoptForm.living_conditions)
async def process_living_conditions(message: Message, state: FSMContext):
    await state.update_data(living_conditions=message.text)
    await state.set_state(AdoptForm.agreement)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton(text="Так"))
    keyboard.add(KeyboardButton(text="Ні"))
    await message.answer("Чи згодні ви на перевірку умов проживання?", reply_markup=keyboard)


@router.message(AdoptForm.agreement, F.text.in_(["Так", "Ні"]))
async def process_agreement(message: Message, state: FSMContext):
    await state.update_data(agreement=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer(
        f"Дякуємо за заповнення анкети!\n\nВаші дані:\nІм'я: {data['name']}\nКонтакти: {data['contact']}\nДосвід: {data['experience']}\nУмови: {data['living_conditions']}\nЗгода на перевірку: {data['agreement']}",
        reply_markup=ReplyKeyboardRemove())
    # Тут можна викликати функцію для збереження даних з data
    from database.forms import save_adopt_form
    save_adopt_form(data)


@router.message(AdoptForm.agreement)
async def invalid_agreement(message: Message):
    await message.answer("Будь ласка, натисніть 'Так' або 'Ні'.")
