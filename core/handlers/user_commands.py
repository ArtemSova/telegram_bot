from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from config_db.users_db import UsersSQL
from core.keyboards.main_menu import main_menu_kb, main_menu_admin_kb
from core.config_data.config import Config, load_config


# Создание роутера
router: Router = Router()

# Загрузка конфигурации
config: Config = load_config()

# Реакция на кнопку старт или команду "\start"
@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot):
    # Создаем базу данных
    s = UsersSQL()
    # Добавляем пользователей в БД
    try:
        s.insert(message.from_user.id, message.from_user.first_name, message.from_user.username)
    except:
        pass
    # Ответное приветствие и отображение кнопок из keyboard_start c gif
    if message.from_user.id == config.admin.admin_id:
        await message.answer_animation(animation=config.photo_url.saw, caption=f'Вот ты где, {message.from_user.first_name}! Давай поиграем!', reply_markup=main_menu_admin_kb)
    else:
        await message.answer_animation(animation=config.photo_url.saw, caption=f'Вот ты где, {message.from_user.first_name}! Давай поиграем!', reply_markup=main_menu_kb)


@router.message(F.text == 'ГЛАВНОЕ МЕНЮ 🔙')
async def main_menu(message: Message, bot: Bot):
    if message.from_user.id == config.admin.admin_id:
        await bot.send_message(message.from_user.id, 'Меню админа', reply_markup=main_menu_admin_kb)
    else:
        await bot.send_message(message.from_user.id, 'Основное меню', reply_markup=main_menu_kb)

