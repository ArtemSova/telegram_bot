from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Моя анкета 📜'),
            KeyboardButton(text='Заполнить\изменить анкету 🖌')
        ],
        [
            # KeyboardButton(text='Специальные кнопки'),
            KeyboardButton(text='Игры 🃏')
        ],
        [
            KeyboardButton(text='Отчеты 📸')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)