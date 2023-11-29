from aiogram import Bot, Dispatcher
from datetime import datetime

import asyncio
import logging


from core.config_data.config import Config, load_config
from core.handlers import other_handlers
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.time_message import time_message_1


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

    #Сообщения по-расписанию
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    # corn - раз в сутки
    scheduler.add_job(time_message_1, trigger='cron', hour=12, minute=12, start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.start()

    # Регистрируем роутеры в диспетчере
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

