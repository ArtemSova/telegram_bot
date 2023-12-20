from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup


from config_db.board_games import BoardGamesSQL
from core.keyboards.board_games_menu import board_games_menu_kb
from core.keyboards.new_board_games import new_board_games_kb
from core.config_data.config import Config, load_config


# Создание роутера
router: Router = Router()


# Загрузка конфигурации
config: Config = load_config()

# Создаем базу данных
new_board_games_dict: dict[str] = {}

class FSMFNewBoardGame(StatesGroup):
    new_board_game = State()


@router.message(F.text == 'Настольные игры')
async def keys_list(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Меню настольных игр', reply_markup=board_games_menu_kb)


@router.message(F.text == 'Игры в коллекции участников')
async def keys_list(message: Message, bot: Bot):
    games_list = '\n'.join([str(element).replace("'", "").replace('(', '').replace(')', '') for element in BoardGamesSQL().board_games_select()])
    await bot.send_message(message.from_user.id, f'Список игр: \n {games_list}', reply_markup=board_games_menu_kb)

@router.message(F.text == 'Новая настольная игра')
async def keys_list(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выбирай', reply_markup=new_board_games_kb)

