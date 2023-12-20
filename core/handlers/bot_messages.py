from aiogram import Bot, Router, F
from aiogram.types import Message

from core.keyboards import main_menu, special, games_menu_kb, fabrics, photos_menu_kb
from core.config_data.config import Config, load_config
from core.data.subloader import get_json


router = Router()

config: Config = load_config()

@router.message()
async def echo(message: Message, bot: Bot):
    msg = message.text.lower()
    photos = await get_json("photos.json")

    # СТОИТ ФИЛЬТР НА МАЛЕНЬКИЕ БУКВЫ!!! (изменить?)
    if msg == 'игры 🃏':
        await bot.send_message(message.from_user.id, f'Игры', reply_markup=games_menu_kb.games_menu_kb)
    elif msg == 'игры бота':
        await bot.send_message(message.from_user.id, 'В игре "Угадайка! можно заработать монеты, если победишь"', reply_markup=games_menu_kb.bot_game_kb)
    elif msg == 'ваши фотографии 📸':
        await bot.send_message(message.from_user.id, 'Я следил за вами. Как хотите смотреть фото?', reply_markup=photos_menu_kb.photos_menu_kb)
    elif msg == 'листать фото':
        # await message.answer(f'{photos[0][0]} {photos[0][1]}', reply_markup=fabrics.paginator())
        await message.reply_photo(photo=photos[0][1], caption='Отдых на природе', reply_markup=fabrics.paginator())
    # elif msg == 'специальные кнопки':
    #     await message.answer('Спец. кнопки', reply_markup=special.spec_kb)
    elif msg == 'админка 🛑':
        await bot.send_message(message.from_user.id, 'Ты разве админ бота? Вроде нет. Значит не тычь куда не надо!', reply_markup=main_menu.main_menu_kb)
    else:
        # Реакция на неопознанную команду
        await bot.send_message(message.from_user.id, f'Ты втираешь мне какую-то дичь...', reply_markup=main_menu.main_menu_kb)

