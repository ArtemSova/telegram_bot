from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Моя анкета 📜'),
            KeyboardButton(text='Заполнить\изменить анкету 🖌')
        ],
        [
            # KeyboardButton(text='Специальные кнопки'),
            KeyboardButton(text='Игры 🃏'),
        ],
        [
            KeyboardButton(text='Ваши фотографии 📸')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

main_menu_admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Моя анкета 📜'),
            KeyboardButton(text='Заполнить\изменить анкету 🖌')
        ],
        [
            # KeyboardButton(text='Специальные кнопки'),
            KeyboardButton(text='Игры 🃏'),
            KeyboardButton(text='Админка 🛑')
        ],
        [
            KeyboardButton(text='Ваши фотографии 📸')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

admin_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Дать/забрать монеты 🤑'),
            KeyboardButton(text='Показать анкету 📃')
        ],
        [
            KeyboardButton(text='ГЛАВНОЕ МЕНЮ 🔙'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)