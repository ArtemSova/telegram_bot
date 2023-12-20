from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import random

from config_db.board_games import BoardGamesSQL
from core.config_data.config import Config, load_config
from core.keyboards.board_games_menu import board_games_menu_kb
from core.middlewares.check_group_sub import CheckGroupSubscription


# Создание роутера
router: Router = Router()

router.message.middleware(CheckGroupSubscription())

# Загрузка конфигурации
config: Config = load_config()

# Создаем базу данных
new_board_games_dict: dict[str] = {}

class FSMFNewBoardGame(StatesGroup):
    new_board_game = State()


@router.message(F.text == 'Добавить настольную игру в список')
async def keys_list(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, f'Введите название настольной игры')
    await state.set_state(FSMFNewBoardGame.new_board_game)


@router.message(StateFilter(FSMFNewBoardGame.new_board_game))
async def anceta_step_two(message: Message, bot: Bot, state: FSMContext):
    # Сохраняем имя пользователя в словаре
    await state.update_data(new_board_game=message.text)
    new_board_games_dict = await state.get_data()
    BoardGamesSQL().insert_board_games(game=str(new_board_games_dict.get("new_board_game")))
    await state.clear()
    await bot.send_message(message.from_user.id,'Настольная игра добавлена')


@router.message(F.text == 'Выбрать настольную игру')
async def keys_list(message: Message, bot: Bot):
    n = random.choice((BoardGamesSQL().board_games_select()))[0]
    await bot.send_message(config.group.group_id, f'{message.from_user.first_name} попросил выбрать игру. Сегодня играйте в: <b>"{n}"</b> 🃏👾♟')
    await bot.send_message(message.from_user.id, f'Игра выбрана и отправлена в группу', reply_markup=board_games_menu_kb)

