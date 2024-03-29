from aiogram.types import InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

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

    # добавление кнопки "Нужет повод потусить?"
    if button_site:
        kb = InlineKeyboardButton(text=button_site, web_app=WebAppInfo(url='https://dzen.ru/a/ZIFNR21BgnT5jeXI'))
        kb_builder.row(kb)

    return kb_builder.as_markup(resize_keyboard=True, selective=True)
