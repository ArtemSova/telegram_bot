from aiogram.types import KeyboardButton, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from core.lexicon.lexicon_ru import LEXICON_INLINE


def create_inline_key(width: int, button_site: str | None = None, *args: str, **kwargs: str):
    # инициализация объекта клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    # инициализация списка кнопок (запаковка)
    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(text=LEXICON_INLINE[button] if button in LEXICON_INLINE else button, callback_data=button))

    if kwargs:
        for key, val in kwargs.items():
            buttons.append(InlineKeyboardButton(text=val, callback_data=key))

    # добавление кнопок из lexicon_ru (распаковка)
    kb_builder.row(*buttons, width=width)

    # добавление кнопки, указанной в "other_handlers.py" с переходом на сайт внутри телеграм (БЕЗ РОУТЕРА В other_handlers.py)
    if button_site:
        kb = InlineKeyboardButton(text=button_site, web_app=WebAppInfo(url='https://market.yandex.ru/brands--hobby-world/10829828'))
        kb_builder.row(kb)

    return kb_builder.as_markup()


def create_key(width: int, *args: str, **kwargs: str):
    # инициализация объекта клавиатуры
    menu: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

    # инициализация списка кнопок
    buttons: list[KeyboardButton] = []

    if args:
        for button in args:
            buttons.append(KeyboardButton(text=button))

    if kwargs:
        for key, val in kwargs.items():
            buttons.append(KeyboardButton(text=val))

    # добавление кнопок
    menu.row(*buttons, width=width)

    return menu.as_markup(resize_keyboard=True)


