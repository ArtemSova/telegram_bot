from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from core.lexicon.lexicon_ru import LEXICON_INLINE


def create_inline_key(width: int, *args: str, **kwargs: str):
    # инициализация объекта клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    # инициализация списка кнопок
    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(text=LEXICON_INLINE[button] if button in LEXICON_INLINE else button, callback_data=button))

    if kwargs:
        for key, val in kwargs.items():
            buttons.append(InlineKeyboardButton(text=val, callback_data=key))

    # добавление кнопок
    kb_builder.row(*buttons, width=width)

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


