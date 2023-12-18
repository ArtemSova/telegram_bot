from aiogram.types import KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardMarkup


# Меню сайтов новых настольных игр
new_board_games_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Hobby Games', web_app=WebAppInfo(url='https://hobbygames.ru/')),
            KeyboardButton(text='Чей Ход', web_app=WebAppInfo(url='https://cheihod.ru/')),
            KeyboardButton(text='Crow Games', web_app=WebAppInfo(url='https://www.crowdgames.ru/collection/all')),
        ],
        [
            KeyboardButton(text='Стиль жизни', web_app=WebAppInfo(url='https://lifestyleltd.ru/?ysclid=lnvdzj7di8620405738')),
            KeyboardButton(text='Мосигра', web_app=WebAppInfo(url='https://www.mosigra.ru/')),
            KeyboardButton(text='Лавка Игр', web_app=WebAppInfo(url='https://www.lavkaigr.ru/')),
            KeyboardButton(text='ZVEZDA', web_app=WebAppInfo(url='https://zvezda.org.ru/catalog/nastolnye_igry/')),
        ],
        [
            KeyboardButton(text='ГЛАВНОЕ МЕНЮ 🔙')
        ]
    ],
    resize_keyboard=True
)

# настроенное меню сайтов покупки новых игр???
# def new_board_games_kb():
#     items = [
#         'Hobby Games', 'Чей Ход', 'Crow Games',
#         'Стиль жизни', 'Мосигра', 'Лавка Игр', 'ZVEZDA',
#     ]
#
#     builder = ReplyKeyboardBuilder()
#     [builder.button(text=item) for item in items]
#     builder.button(text='НАЗАД 🔙')
#     builder.adjust(3, 4)
#
#
#     return builder.as_markup(resize_keyboard=True, one_time_keyboard=True, selective=True)