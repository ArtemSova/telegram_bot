from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup


# Клавиатура меню игр
games_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Настольные игры'),
            KeyboardButton(text='Игры бота'),
        ],
        [
            KeyboardButton(text='ГЛАВНОЕ МЕНЮ 🔙'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)

# Клавиатура меню игр бота
bot_game_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Угадайка! ❓❓❓'),
        ],
        [
            KeyboardButton(text='ГЛАВНОЕ МЕНЮ 🔙'),
        ]

    ]
)