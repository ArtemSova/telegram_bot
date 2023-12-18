from aiogram.types import KeyboardButton, InlineKeyboardButton, WebAppInfo, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, ReplyKeyboardMarkup


# Клавиатура меню игр
board_games_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Выбрать настольную игру'),
            KeyboardButton(text='Игры в коллекции участников'),
        ],
        [
            KeyboardButton(text='Добавить настольную игру в список'),
            KeyboardButton(text='Новая настольная игра'),
        ],
        [
            KeyboardButton(text='ГЛАВНОЕ МЕНЮ 🔙'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)

