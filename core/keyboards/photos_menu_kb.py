from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup


# Клавиатура меню фотографий
photos_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Выбирать фото'),
            KeyboardButton(text='Листать фото'),
        ],
        [
            KeyboardButton(text='ГЛАВНОЕ МЕНЮ 🔙'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)
