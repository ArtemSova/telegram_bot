from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import random

from core.keyboards.photo_inline_menu import *
from core.lexicon.lexicon_ru import LEXICON_INLINE
from config_db.users_db import UsersSQL
from config_db.board_games import BoardGamesSQL
from core.filters.is_admin import IsAdmin
from core.config_data.config import Config, load_config
from core.middlewares.check_group_sub import CheckGroupSubscription


# Создание роутера
router: Router = Router()


# router.message.middleware(CheckGroupSubscription())

# Загрузка конфигурации
config: Config = load_config()

# Отображение клавиатур, create_key(количество кнопок в строке(линии), источник кнопок)
  # Добавлена доп кнопка для сайта ее логика в keyboards
keyboard_inline = create_inline_key(2, 'Ищешь игры?', **LEXICON_INLINE)

# Реакция на кнопку "Отчеты"
@router.message(F.text == 'Отчеты')
async def keys_list(message: Message):
    await message.answer('Посмотрим фоточки', reply_markup=keyboard_inline)


# Реакция на Первую кнопку LEXICON_INLINE
@router.callback_query(F.data == '1')
async def inline_button_1(callback: CallbackQuery):
    # Сообщение в чат, заменяет предыдущее сообщение
    try:
        await callback.message.edit_text('Нажата первая кнопка', reply_markup=keyboard_inline)
    except:
        await callback.answer('Первая кнопка уже нажата', reply_markup=keyboard_inline)

@router.callback_query(F.data == '2')
async def inline_button_1(callback: CallbackQuery):
    # Сообщение в чат, заменяет предыдущее сообщение
    try:
        await callback.message.edit_text('Нажата вторая кнопка', reply_markup=keyboard_inline)
    except:
        await callback.answer('Вторая кнопка уже нажата', reply_markup=keyboard_inline)

@router.callback_query(F.data == '3')
async def inline_button_1(callback: CallbackQuery):
    # Сообщение в чат, заменяет предыдущее сообщение
    try:
        await callback.message.edit_text('Нажата третья кнопка', reply_markup=keyboard_inline)
    except:
        await callback.answer('Третья кнопка уже нажата', reply_markup=keyboard_inline)




