from aiogram import Bot, Dispatcher
from datetime import datetime

import asyncio
import logging

from core.config_data.config import Config, load_config
from core.handlers import questionnaire, add_board_game, user_commands, bot_messages, games_menu, inline_routers
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from time_message import time_message_1, today_holiday



# Инииализация логгера
logger = logging.getLogger(__name__)

# Функция конфигурации и запуска бота
async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='(%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s',
    )

    # Выводим в консоль информацию о начале запуска
    logger.info('Bot started')

    # Загружаем конфигурации в переменную config
    config: Config = load_config()

    # Инициализируем бота и диспетчера
    bot: Bot = Bot(token=config.tg_bot.bot_token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Регистрируем роутеры в диспетчере
    dp.include_routers(user_commands.router, add_board_game.router, questionnaire.router, games_menu.router, inline_routers.router, bot_messages.router)

    #Сообщения по-расписанию
    # scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    # # corn - раз в сутки
    # scheduler.add_job(time_message_1, trigger='cron', hour=20, minute=39, start_date=datetime.now(), kwargs={'bot': bot})
    # scheduler.start()

    # Сообщения о ежедневном празднике
    selebrate = AsyncIOScheduler(timezone='Europe/Moscow')
    selebrate.add_job(today_holiday, trigger='cron', hour=8, minute=38, start_date=datetime.now(), kwargs={'bot': bot})
    selebrate.start()

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

