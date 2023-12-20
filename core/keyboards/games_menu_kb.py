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
            KeyboardButton(text='Однорукий бандит 🎰'),
        ],
        [
            KeyboardButton(text='ГЛАВНОЕ МЕНЮ 🔙'),
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)

# Однорукий бандит
one_hand_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'🎰 Потратить 1 монету и крутить.'),
        ],
        [
            KeyboardButton(text='ГЛАВНОЕ МЕНЮ 🔙'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)