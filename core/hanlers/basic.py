from aiogram import Bot, Dispatcher
from aiogram.types import Message
import random
import string
import json


async def get_start(message: Message, bot:Bot):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}!')
#    await message.answer(f'Привет, {message.from_user.first_name}!')  # Вариант ответа без ссылки
#    await message.reply(f'Привет, {message.from_user.first_name}!')  # Вариант ответа со ссылкой на запрос


async def get_image(message: Message, bot:Bot):
    await message.answer(f"Это что картинка? Надеюсь не DickPick...")
    file = await bot.get_file(message.photo[-1].file_id)
    rand_string = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    await bot.download_file(file.file_path, f'images/{message.from_user.id}_{rand_string}.jpg')


async def get_hello(message: Message, bot:Bot):
    await message.answer(f'Кто это тут у нас, {message.from_user.first_name}, я тебя вижу.')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
