from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config_db.board_games import BoardGamesSQL
from core.config_data.config import Config, load_config
from core.middlewares.check_group_sub import CheckGroupSubscription


# Создание роутера
router: Router = Router()

# router.message.middleware(CheckGroupSubscription())

# Загрузка конфигурации
config: Config = load_config()

# Создаем базу данных
new_board_games_dict: dict[str] = {}

class FSMFNewBoardGame(StatesGroup):
    new_board_game = State()

@router.message(F.text == 'Добавить настольную игру в список')
async def keys_list(message: Message, state: FSMContext):
    await message.answer(f'Введите название настольной игры')
    await state.set_state(FSMFNewBoardGame.new_board_game)


@router.message(StateFilter(FSMFNewBoardGame.new_board_game))
async def anceta_step_two(message: Message, state: FSMContext):
    # Сохраняем имя пользователя в словаре
    await state.update_data(new_board_game=message.text)
    new_board_games_dict = await state.get_data()
    BoardGamesSQL().insert_board_games(game=str(new_board_games_dict.get("new_board_game")))
    await state.clear()
    await message.answer('Настольная игра добавлена')
