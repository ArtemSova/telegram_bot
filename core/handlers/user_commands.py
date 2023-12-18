from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config_db.users_db import UsersSQL
from core.keyboards.main_menu import main_menu_kb
from core.keyboards.special import spec_kb
from core.filters.is_admin import IsAdmin

from core.config_data.config import Config, load_config


# Создание роутера
router: Router = Router()

# router.message.middleware(CheckGroupSubscription())

# Загрузка конфигурации
config: Config = load_config()

# Реакция на кнопку старт или команду "\start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    # Создаем базу данных
    s = UsersSQL()
    # Добавляем пользователей в БД
    try:
        s.insert(message.from_user.id, message.from_user.first_name, message.from_user.username)
    except:
        pass
    # Ответное приветствие и отображение кнопок из keyboard_start c gif
    await message.answer_animation(animation=config.photo_url.saw, caption=f'Вот ты где, {message.from_user.first_name}! Давай поиграем!', reply_markup=main_menu_kb)

# Реакция на кнопки "НАЗАД"
@router.message(F.text == 'ГЛАВНОЕ МЕНЮ 🔙')
async def keys_list(message: Message):
    await message.answer('Основное меню', reply_markup=main_menu_kb)

@router.message(F.text == 'Специальные кнопки', IsAdmin(config.admin.admin_id))
async def keys_list(message: Message):
    await message.answer('спацеальные кнопки', reply_markup=spec_kb)
