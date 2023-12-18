from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from config_db.users_db import UsersSQL
from core.keyboards.main_menu import main_menu_kb


# Создание роутера

router: Router = Router()

# Создаем базу данных пользователей
user_dict: dict[int, dict[str, str | int | bool]] = {}

class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_birthday = State()
    fill_phone_number = State()



# Реакция на кнопку "Моя анкета"
@router.message(F.text == "Моя анкета")
async def my_questionnaire(message: Message):
    await message.answer(f'Ваша анкета: \n'
                         f'<b>user_name:</b> {UsersSQL().select_user_info(message.from_user.id)[0][0]}\n'
                         f'<b>Имя:</b> {UsersSQL().select_user_info(message.from_user.id)[0][1]}\n'
                         f'<b>День рождения:</b> {UsersSQL().select_user_info(message.from_user.id)[0][2]}\n'
                         f'<b>Номер телефона:</b> {UsersSQL().select_user_info(message.from_user.id)[0][3]}\n'
                         f'<b>Монеты:</b> {UsersSQL().select_user_info(message.from_user.id)[0][4]}\n',
                         reply_markup=main_menu_kb,
                         )

# Реакция на кнопку "Заполнить\изменить анкету"
@router.message(F.text == "Заполнить\изменить анкету")
async def anceta_step_one(message: Message, state: FSMContext):
    await message.answer('Введите свое имя. Можно Ф.И.О')
    # Устанавливаем состояние ожидания ввода имени
    await state.set_state(FSMFillForm.fill_name)

# Анкета второй шаг
@router.message(StateFilter(FSMFillForm.fill_name))
async def anceta_step_two(message: Message, state: FSMContext):
    # Сохраняем имя пользователя в словаре
    await state.update_data(name=message.text)
    await message.answer('Введите свою дату рождения. Формат: ДД.ММ.ГГГГ')
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMFillForm.fill_birthday)

# Анкета третий шаг
@router.message(StateFilter(FSMFillForm.fill_birthday), F.text.regexp(r"^(\d\d.\d\d.\d{4})$"))
async def anceta_step_three(message: Message, state: FSMContext):
    # Сохраняем возраст пользователя в словаре
    await state.update_data(birthday=message.text)
    await message.answer('Введите свой номер телефона. Формат: +7-ХХХ-ХХХ-ХХ-ХХ/8-XXX-XXX-XX-XX')
    # Устанавливаем состояние ожидания ввода номера телефона
    await state.set_state(FSMFillForm.fill_phone_number)

# Анкета четвертый шаг
@router.message(StateFilter(FSMFillForm.fill_phone_number), F.text.regexp(r"^((?:\+7|8)(?:-\d{2,3}){4})$"))
async def anceta_step_four(message: Message, state: FSMContext):
    # Сохраняем номер телефона пользователя в словаре
    await state.update_data(phone_number=message.text)
    await message.answer('Анкета заполнена.')
    # Сохраняем данные в словарь
    user_dict[message.from_user.id] = await state.get_data()
    # Передаем данные в БД
    UsersSQL().update_user_info(user_id=message.from_user.id, first_name=user_dict.get(message.from_user.id).get("name"),
                                birthday=user_dict.get(message.from_user.id).get("birthday"), phone_number=user_dict.get(message.from_user.id).get("phone_number"))
    # Очищаем состояние
    await state.clear()
    # Отправляем сохраненную анкету пользователю
    await message.answer(f'Анкета изменена: \n'
                         f'<b>uer_name:</b> {UsersSQL().select_user_info(message.from_user.id)[0][0]}\n'
                         f'<b>Имя:</b> {UsersSQL().select_user_info(message.from_user.id)[0][1]}\n'
                         f'<b>День рождения:</b> {UsersSQL().select_user_info(message.from_user.id)[0][2]}\n'
                         f'<b>Номер телефона:</b> {UsersSQL().select_user_info(message.from_user.id)[0][3]}\n'
                         f'<b>Монеты:</b> {UsersSQL().select_user_info(message.from_user.id)[0][4]}\n',
                         reply_markup=main_menu_kb,
                         )
