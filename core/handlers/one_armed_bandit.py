from aiogram import Bot, Router, F
from aiogram.types import Message

import asyncio

from core.keyboards.games_menu_kb import one_hand_kb
from core.data.get_dice_result import get_result_text
from config_db.users_db import UsersSQL



router: Router = Router()


@router.message(F.text == "Однорукий бандит 🎰")
async def start_game(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Испытай удачу, нажми на кнопку.', reply_markup=one_hand_kb)


@router.message(F.text == "🎰 Потратить 1 монету и крутить.")
async def get_game(message: Message, bot: Bot):
    result_dice = await message.answer_dice(emoji='🎰')
    await asyncio.sleep(2)
    game_result = get_result_text(result_dice=result_dice.dice.value, bid=1)
    bounty = int(UsersSQL().coins_count(message.from_user.id)[0][0]) - 1 + int(game_result)
    UsersSQL().change_coins(message.from_user.id, int(bounty))
    wallet = UsersSQL().coins_count(message.from_user.id)[0][0]
    if game_result == 0:
        if str(wallet)[-1] == '1':
            await bot.send_message(message.from_user.id, f'Не повезло. У тебя осталась {wallet} монета. Сыграем еще раз?',
                                   reply_markup=one_hand_kb)
        elif str(wallet)[-1] in ['2', '3', '4']:
            await bot.send_message(message.from_user.id, f'Не повезло. У тебя осталось {wallet} монеты. Сыграем еще раз?',
                                   reply_markup=one_hand_kb)
        else:
            await bot.send_message(message.from_user.id, f'Не повезло. У тебя осталось {wallet} монет. Сыграем еще раз?',
                                   reply_markup=one_hand_kb)
    else:
        if str(wallet)[-1] == '1':
            if game_result == '7':
                await bot.send_message(message.from_user.id, f'Удача! Ты выйграл {game_result} монет. Теперь у тебя {wallet} монета. Сыграем еще раз?',
                                       reply_markup=one_hand_kb)
            else:
                await bot.send_message(message.from_user.id, f'Удача! Ты выйграл {game_result} монеты. Теперь у тебя {wallet} монета. Сыграем еще раз?',
                                       reply_markup=one_hand_kb)
        elif str(wallet)[-1] in ['2', '3', '4']:
            if game_result == '7':
                await bot.send_message(message.from_user.id, f'Удача! Ты выйграл {game_result} монет. Теперь у тебя {wallet} монеты. Сыграем еще раз?',
                                       reply_markup=one_hand_kb)
            else:
                await bot.send_message(message.from_user.id, f'Удача! Ты выйграл {game_result} монеты. Теперь у тебя {wallet} монеты. Сыграем еще раз?',
                                       reply_markup=one_hand_kb)
        else:
            if game_result == '7':
                await bot.send_message(message.from_user.id, f'Удача! Ты выйграл {game_result} монет. Теперь у тебя {wallet} монет. Сыграем еще раз?',
                                       reply_markup=one_hand_kb)
            else:
                await bot.send_message(message.from_user.id, f'Удача! Ты выйграл {game_result} монеты. Теперь у тебя {wallet} монет. Сыграем еще раз?',
                                       reply_markup=one_hand_kb)



