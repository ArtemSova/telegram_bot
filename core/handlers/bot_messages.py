from aiogram import Router, F
from aiogram.types import Message

from core.keyboards import main_menu, special, games_menu_kb


router = Router()

@router.message()
async def echo(message: Message):
    msg = message.text.lower()


    if msg == 'игры 🃏':
        await message.answer('Игры', reply_markup=games_menu_kb.games_menu_kb)
    elif msg == 'игры бота':
        await message.answer('В игре "Угадайка! можно заработать монеты, если победишь"', reply_markup=games_menu_kb.bot_game_kb)
    # elif msg == 'специальные кнопки':
    #     await message.answer('Спец. кнопки', reply_markup=special.spec_kb)
    elif msg == "главное меню 🔙":
        await message.answer("Главное меню!", reply_markup=main_menu.main_menu_kb)
    else:
        # Реакция на неопознанную команду
        await message.answer(f'Ты втираешь мне какую-то дичь...')

