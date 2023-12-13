from aiogram import Bot

from core.config_data.config import Config, load_config
from core.lexicon.lexicon_ru import LEXICON_TIME
from config_db.daily_holiday_db import HolidaySQL

# Загружаем конфигурации в переменную config
config: Config = load_config()

async def time_message_1(bot: Bot):
    await bot.send_message(config.group.group_id, LEXICON_TIME['mes_1'])


async def today_holiday(bot: Bot):
    await bot.send_message(config.group.group_id, f'Сегодня празднуем {HolidaySQL().holidays_select()} Бухаем или играем?')


