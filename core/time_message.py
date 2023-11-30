from aiogram import Bot

from core.lexicon.lexicon_ru import LEXICON_TIME


async def time_message_1(bot: Bot):
    await bot.send_message(329725203, LEXICON_TIME['mes_1'])

