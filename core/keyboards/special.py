from aiogram.types import KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardMarkup


# Клавиатура спец кнопок
spec_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить геолокацию", request_location=True),
            KeyboardButton(text='Отправить контакт', request_contact=True),
        ],
        [
            KeyboardButton(text='Создать викторину', request_poll=KeyboardButtonPollType(type="quiz")),
            KeyboardButton(text='Создать создать опрос', request_poll=KeyboardButtonPollType(type="regular")),
        ],
        [
            KeyboardButton(text='ГЛАВНОЕ МЕНЮ 🔙')
        ]
    ],
    resize_keyboard=True
)
