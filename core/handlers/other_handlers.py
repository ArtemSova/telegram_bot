from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from core.keyboards.keyboards import create_key, create_inline_key
from core.lexicon.lexicon_ru import LEXICON_MENU, LEXICON_INLINE


router: Router = Router()
# Отображение кнопок, create_key(количество кнопок в строке(линии), источник кнопок)
keyboard_start = create_key(2, **LEXICON_MENU)
keyboard_inline = create_inline_key(2, 'Some Site', **LEXICON_INLINE)

# Создаем базу данных пользователей
user_dict: dict[int, dict[str, str | int | bool]] = {}

class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_age = State()
    fill_phone = State()

# Реакция на кнопку старт или команду "\start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    # Ответное приветствие и отображение кнопок из keyboard_start
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=keyboard_start)

# Реакция на приветствия
@router.message(F.text.lower() == "привет")
async def hi(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Поиграем!!!')


# Реакция на кнопку "Список кнопок"
@router.message(F.text == 'Список кнопок')
async def keys_list(message: Message):
    await message.answer('Вот они', reply_markup=keyboard_inline)

# Реакция на Первую кнопку LEXICON_INLINE
@router.callback_query(F.data == '1')
async def inline_button_1(callback: CallbackQuery):
    # Сообщение в чат, заменяет предыдущее сообщение
    try:
        await callback.message.edit_text('Нажата первая кнопка', reply_markup=keyboard_inline)
    except:
        await callback.answer('Первая кнопка уже нажата', reply_markup=keyboard_inline)


# Реакция на кнопку "Заполнить анкету"
@router.message(F.text == "Заполнить анкету")
async def anceta_step_one(message: Message, state: FSMContext):
    await message.answer('Введите свое имя')
    # Устанавливаем состояние ожидания ввода имени
    await state.set_state(FSMFillForm.fill_name)

# Анкета второй шаг
@router.message(StateFilter(FSMFillForm.fill_name), F.text.isalpha())
async def anceta_step_two(message: Message, state: FSMContext):
    # Сохраняем имя пользователя в словаре
    await state.update_data(name=message.text)
    await message.answer('Введите свой возраст')
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMFillForm.fill_age)

# Анкета третий шаг
@router.message(StateFilter(FSMFillForm.fill_age))
async def anceta_step_three(message: Message, state: FSMContext):
    # Сохраняем возраст пользователя в словаре
    await state.update_data(age=message.text)
    await message.answer('Введите свой номер телефона')
    # Устанавливаем состояние ожидания ввода номера телефона
    await state.set_state(FSMFillForm.fill_phone)

# Анкета четвертый шаг
@router.message(StateFilter(FSMFillForm.fill_phone))
async def anceta_step_four(message: Message, state: FSMContext):
    # Сохраняем номер телефона пользователя в словаре
    await state.update_data(phone=message.text)
    await message.answer('Ваша анкета заполнена, спасибо!')
    # Сохраняем данные в словарь
    user_dict[message.from_user.id] = await state.get_data()
    # Очищаем состояние
    await state.clear()
    # Отправляем сохраненную анкету пользователю
    if message.from_user.id in user_dict:
        await message.answer(f'Ваша анкета:\n'
                             f'Имя: {user_dict[message.from_user.id]["name"]}\n'
                             f'Возраст: {user_dict[message.from_user.id]["age"]}\n'
                             f'Номер телефона: {user_dict[message.from_user.id]["phone"]}')
    else:
        await message.answer(f'Ваша анкета не заполнена', reply_markup=keyboard_start)




