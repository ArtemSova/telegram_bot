from aiogram import Bot, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter
from aiogram.filters import Command, CommandStart

from config_db.users_db import UsersSQL
from core.keyboards.main_menu import main_menu_kb, admin_menu_kb
from core.keyboards.special import spec_kb
from core.filters.is_admin import IsAdmin

from core.config_data.config import Config, load_config


# Создание роутера
router: Router = Router()

coins_dict: dict[int, dict[str, str | int | bool]] = {}
questionnaire_dict: dict[int, dict[str, str | int | bool]] = {}

class FSMCoins(StatesGroup):
    user_name = State()
    coins = State()

class FSMQuestionnaire(StatesGroup):
    user_name = State()

# Загрузка конфигурации
config: Config = load_config()


@router.message(F.text == 'Админка 🛑', IsAdmin(config.admin.admin_id))
async def admin_file(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Хозяин вернулся!!!', reply_markup=admin_menu_kb)

@router.message(F.text == 'Показать анкету 📃', IsAdmin(config.admin.admin_id))
async def show_questionary(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, 'User name(Ник без @) пользователя, анкету которго хотите посмотреть:')
    await state.set_state(FSMQuestionnaire.user_name)

@router.message(StateFilter(FSMQuestionnaire.user_name))
async def show_questionary_step_two(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(user_name=message.text)
    questionnaire_dict[message.from_user.id] = await state.get_data()
    await bot.send_message(message.from_user.id, f'Анкета пользователя: \n'
                         f'<b>user_id:</b> {UsersSQL().admin_user_info(questionnaire_dict.get(message.from_user.id).get("user_name"))[0][0]}\n'
                         f'<b>uer_name:</b> {UsersSQL().admin_user_info(questionnaire_dict.get(message.from_user.id).get("user_name"))[0][1]}\n'
                         f'<b>Имя:</b> {UsersSQL().admin_user_info(questionnaire_dict.get(message.from_user.id).get("user_name"))[0][2]}\n'
                         f'<b>День рождения:</b> {UsersSQL().admin_user_info(questionnaire_dict.get(message.from_user.id).get("user_name"))[0][3]}\n'
                         f'<b>Номер телефона:</b> {UsersSQL().admin_user_info(questionnaire_dict.get(message.from_user.id).get("user_name"))[0][4]}\n'
                         f'<b>Монеты:</b> {UsersSQL().admin_user_info(questionnaire_dict.get(message.from_user.id).get("user_name"))[0][5]}\n',
                         reply_markup=admin_menu_kb,
                         )


@router.message(F.text == 'Дать/забрать монеты 🤑', IsAdmin(config.admin.admin_id))
async def add_coins_step_one(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, 'User name(Ник без @) пользователя, чьи монеты нужно изменить:')
    # Устанавливаем состояние ожидания ввода имени
    await state.set_state(FSMCoins.user_name)

@router.message(StateFilter(FSMCoins.user_name))
async def add_coins_step_two(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(user_name=message.text)
    await bot.send_message(message.from_user.id, 'Сколько монет добавить, если указать с минусом, то убавить?')
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMCoins.coins)

@router.message(StateFilter(FSMCoins.coins), F.text.isdigit())
async def add_coins_step_three(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(coins=message.text)
    coins_dict[message.from_user.id] = await state.get_data()
    wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
    await bot.send_message(message.from_user.id, f'{coins_dict.get(message.from_user.id).get("user_name")}, {wallet}, {coins_dict.get(message.from_user.id).get("coins")}', reply_markup=admin_menu_kb)
    UsersSQL().admin_change_coins(user_name=coins_dict.get(message.from_user.id).get("user_name"), wallet=int(wallet),
                                  coins=int(coins_dict.get(message.from_user.id).get("coins")))
    await bot.send_message(message.from_user.id, 'Монеты добавлены!', reply_markup=admin_menu_kb)
    await state.clear()
