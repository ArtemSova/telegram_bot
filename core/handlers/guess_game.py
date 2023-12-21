from aiogram import Bot, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

import random

from core.keyboards.games_menu_kb import bot_game_kb
from config_db.users_db import UsersSQL


router: Router = Router()

# Создаем базу данных пользователей
user_dict: dict[int, dict[int, int]] = {}

class FSMNumber(StatesGroup):
    my_number = State()
    number_1 = State()
    number_2 = State()
    number_3 = State()
    number_4 = State()
    number_5 = State()
    number_6 = State()
    number_7 = State()
    number_8 = State()
    number_9 = State()


# Игра в Угадайку (комментарии в анкете)
@router.message(F.text == "Угадайка! ❓❓❓")
async def start_game(message: Message, bot: Bot, state: FSMContext):
    my_number = int(random.randint(1, 1000))
    await state.update_data(my_number=my_number)
    user_dict[message.from_user.id] = await state.get_data()
    m_num = user_dict.get(message.from_user.id).get("my_number")
    await bot.send_message(message.from_user.id, f'Я загадал число от 1 до 1000. У тебя 9 попыток угадать его. Введи число:')
    await state.set_state(FSMNumber.number_1)



@router.message(StateFilter(FSMNumber.number_1), F.text.isdigit())
async def turn_2(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(number_1=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    num = user_dict.get(message.from_user.id).get("number_1")
    m_n = user_dict.get(message.from_user.id).get("my_number")
    if int(m_n) > int(num):
        await bot.send_message(message.from_user.id, 'Мое число больше. Осталось 8 попыток')
        await state.set_state(FSMNumber.number_2)
    elif int(m_n) < int(num):
        await bot.send_message(message.from_user.id, 'Мое число меньше. Осталось 8 попыток')
        await state.set_state(FSMNumber.number_2)
    else:
        bounty = int(UsersSQL().coins_count(message.from_user.id)[0][0]) + 100
        UsersSQL().change_coins(message.from_user.id, int(bounty))
        wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
        await bot.send_message(message.from_user.id, f'Угадал! Ты выйграл 100 монет. Теперь у тебя {wallet} монет 💰. Сыграем еще раз?', reply_markup=bot_game_kb)
        await state.clear()


@router.message(StateFilter(FSMNumber.number_2), F.text.isdigit())
async def turn_7(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(number_2=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    num = user_dict.get(message.from_user.id).get("number_2")
    m_n = user_dict.get(message.from_user.id).get("my_number")
    if int(m_n) > int(num):
        await bot.send_message(message.from_user.id, 'Мое число больше. Осталось 7 попыток')
        await state.set_state(FSMNumber.number_3)
    elif int(m_n) < int(num):
        await bot.send_message(message.from_user.id, 'Мое число меньше. Осталось 7 попыток')
        await state.set_state(FSMNumber.number_3)
    else:
        bounty = int(UsersSQL().coins_count(message.from_user.id)[0][0]) + 80
        UsersSQL().change_coins(message.from_user.id, int(bounty))
        wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
        await bot.send_message(message.from_user.id, f'Угадал! Ты выйграл 80 монет 💰. Теперь у тебя {wallet} монет. Сыграем еще раз?',
                             reply_markup=bot_game_kb)
        await state.clear()

@router.message(StateFilter(FSMNumber.number_3), F.text.isdigit())
async def turn_8(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(number_3=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    num = user_dict.get(message.from_user.id).get("number_3")
    m_n = user_dict.get(message.from_user.id).get("my_number")
    if int(m_n) > int(num):
        await bot.send_message(message.from_user.id, 'Мое число больше. Осталось 6 попыток')
        await state.set_state(FSMNumber.number_4)
    elif int(m_n) < int(num):
        await bot.send_message(message.from_user.id, 'Мое число меньше. Осталось 6 попыток')
        await state.set_state(FSMNumber.number_4)
    else:
        bounty = int(UsersSQL().coins_count(message.from_user.id)[0][0]) + 70
        UsersSQL().change_coins(message.from_user.id, int(bounty))
        wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
        await bot.send_message(message.from_user.id, f'Угадал! Ты выйграл 70 монет 💰. Теперь у тебя {wallet} монет. Сыграем еще раз?',
                             reply_markup=bot_game_kb)
        await state.clear()

@router.message(StateFilter(FSMNumber.number_4), F.text.isdigit())
async def turn_9(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(number_4=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    num = user_dict.get(message.from_user.id).get("number_4")
    m_n = user_dict.get(message.from_user.id).get("my_number")
    if int(m_n) > int(num):
        await bot.send_message(message.from_user.id, 'Мое число больше. Осталось 5 попыток')
        await state.set_state(FSMNumber.number_5)
    elif int(m_n) < int(num):
        await bot.send_message(message.from_user.id, 'Мое число меньше. Осталось 5 попыток')
        await state.set_state(FSMNumber.number_5)
    else:
        bounty = int(UsersSQL().coins_count(message.from_user.id)[0][0]) + 60
        UsersSQL().change_coins(message.from_user.id, int(bounty))
        wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
        await bot.send_message(message.from_user.id, f'Угадал! Ты выйграл 60 монет 💵. Теперь у тебя {wallet} монет. Сыграем еще раз?',
                             reply_markup=bot_game_kb)
        await state.clear()

@router.message(StateFilter(FSMNumber.number_5), F.text.isdigit())
async def turn_10(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(number_5=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    num = user_dict.get(message.from_user.id).get("number_5")
    m_n = user_dict.get(message.from_user.id).get("my_number")
    if int(m_n) > int(num):
        await bot.send_message(message.from_user.id, 'Мое число больше. Осталось 4 попытки')
        await state.set_state(FSMNumber.number_6)
    elif int(m_n) < int(num):
        await bot.send_message(message.from_user.id, 'Мое число меньше. Осталось 4 попытки')
        await state.set_state(FSMNumber.number_6)
    else:
        bounty = int(UsersSQL().coins_count(message.from_user.id)[0][0]) + 50
        UsersSQL().change_coins(message.from_user.id, int(bounty))
        wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
        await bot.send_message(message.from_user.id, f'Угадал! Ты выйграл 50 монет 💵. Теперь у тебя {wallet} монет. Сыграем еще раз?',
                             reply_markup=bot_game_kb)
        await state.clear()

@router.message(StateFilter(FSMNumber.number_6), F.text.isdigit())
async def turn_11(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(number_6=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    num = user_dict.get(message.from_user.id).get("number_6")
    m_n = user_dict.get(message.from_user.id).get("my_number")
    if int(m_n) > int(num):
        await bot.send_message(message.from_user.id, 'Мое число больше. Осталось 3 попытки')
        await state.set_state(FSMNumber.number_7)
    elif int(m_n) < int(num):
        await bot.send_message(message.from_user.id, 'Мое число меньше. Осталось 3 попытки')
        await state.set_state(FSMNumber.number_7)
    else:
        bounty = int(UsersSQL().coins_count(message.from_user.id)[0][0]) + 40
        UsersSQL().change_coins(message.from_user.id, int(bounty))
        wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
        await bot.send_message(message.from_user.id, f'Угадал! Ты выйграл 40 монет 💵. Теперь у тебя {wallet} монет. Сыграем еще раз?',
                             reply_markup=bot_game_kb)
        await state.clear()

@router.message(StateFilter(FSMNumber.number_7), F.text.isdigit())
async def turn_12(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(number_7=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    num = user_dict.get(message.from_user.id).get("number_7")
    m_n = user_dict.get(message.from_user.id).get("my_number")
    if int(m_n) > int(num):
        await bot.send_message(message.from_user.id, 'Мое число больше. Осталось 2 попытки')
        await state.set_state(FSMNumber.number_8)
    elif int(m_n) < int(num):
        await bot.send_message(message.from_user.id, 'Мое число меньше. Осталось 2 попытки')
        await state.set_state(FSMNumber.number_8)
    else:
        bounty = int(UsersSQL().coins_count(message.from_user.id)[0][0]) + 30
        UsersSQL().change_coins(message.from_user.id, int(bounty))
        wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
        await bot.send_message(message.from_user.id, f'Угадал! Ты выйграл 30 монет 💵. Теперь у тебя {wallet} монет. Сыграем еще раз?',
                             reply_markup=bot_game_kb)
        await state.clear()

@router.message(StateFilter(FSMNumber.number_8), F.text.isdigit())
async def turn_13(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(number_8=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    num = user_dict.get(message.from_user.id).get("number_8")
    m_n = user_dict.get(message.from_user.id).get("my_number")
    if int(m_n) > int(num):
        await bot.send_message(message.from_user.id, 'Мое число больше. Осталась <b>последняя</b> попытка')
        await state.set_state(FSMNumber.number_9)
    elif int(m_n) < int(num):
        await bot.send_message(message.from_user.id, 'Мое число меньше. Осталась <b>последняя</b> попытка')
        await state.set_state(FSMNumber.number_9)
    else:
        bounty = int(UsersSQL().coins_count(message.from_user.id)[0][0]) + 20
        UsersSQL().change_coins(message.from_user.id, int(bounty))
        wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
        await bot.send_message(message.from_user.id, f'Угадал! Ты выйграл 20 монет 💵. Теперь у тебя {wallet} монет. Сыграем еще раз?',
                             reply_markup=bot_game_kb)
        await state.clear()

@router.message(StateFilter(FSMNumber.number_9), F.text.isdigit())
async def turn_21(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(number_9=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    num = user_dict.get(message.from_user.id).get("number_9")
    m_n = user_dict.get(message.from_user.id).get("my_number")
    if int(m_n) != int(num):
        await bot.send_message(message.from_user.id, 'Ты проиграл и не получаешь монеты 💸, Лузер!!! Хочешь облажаться еще раз?', reply_markup=bot_game_kb)
        await state.clear()
    else:
        bounty = int(UsersSQL().coins_count(message.from_user.id)[0][0]) + 10
        UsersSQL().change_coins(message.from_user.id, int(bounty))
        wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
        await bot.send_message(message.from_user.id, f'Угадал! Ты выйграл 10 монет 💵. Теперь у тебя {wallet} монет. Сыграем еще раз?',
                             reply_markup=bot_game_kb)
        await state.clear()
