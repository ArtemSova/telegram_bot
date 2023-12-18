from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter

import random

from config_db.board_games import BoardGamesSQL
from core.keyboards.board_games_menu import board_games_menu_kb
from core.keyboards.new_board_games import new_board_games_kb
from core.config_data.config import Config, load_config


# Создание роутера
router: Router = Router()

# router.message.middleware(CheckGroupSubscription())

# Загрузка конфигурации
config: Config = load_config()

# Создаем базу данных
new_board_games_dict: dict[str] = {}

class FSMFNewBoardGame(StatesGroup):
    new_board_game = State()


@router.message(F.text == 'Настольные игры')
async def keys_list(message: Message):
    await message.answer('Меню настольных игр', reply_markup=board_games_menu_kb)

@router.message(F.text == 'Выбрать настольную игру')
async def keys_list(message: Message):
    n = random.choice((BoardGamesSQL().board_games_select())[0])
    await message.answer(f'<b>Сегодня играйте в:</b> {n}', reply_markup=board_games_menu_kb)

@router.message(F.text == 'Игры в коллекции участников')
async def keys_list(message: Message):
    games_list = '\n'.join([str(element).replace("'", "").replace('(', '').replace(')', '') for element in BoardGamesSQL().board_games_select()])
    await message.answer(f'Список игр: \n {games_list}', reply_markup=board_games_menu_kb)

@router.message(F.text == 'Новая настольная игра')
async def keys_list(message: Message):
    await message.answer(f'Выбирай', reply_markup=new_board_games_kb)
