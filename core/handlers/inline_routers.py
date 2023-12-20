from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto



from core.keyboards.photo_inline_menu import *
from core.lexicon.lexicon_ru import LEXICON_INLINE

from core.config_data.config import Config, load_config


# Создание роутера
router: Router = Router()

# router.message.middleware(CheckGroupSubscription())

# Загрузка конфигурации
config: Config = load_config()

# Отображение клавиатур, create_key(количество кнопок в строке(линии), источник кнопок)
  # Добавлена доп кнопка для сайта ее логика в keyboards
keyboard_inline = create_inline_key(2, 'Нужен повот потусить? 🥳', **LEXICON_INLINE)

# Реакция на кнопку "Отчеты"
@router.message(F.text == 'Выбирать фото')
async def keys_list(message: Message):
    await message.reply_photo(photo=config.photo_url.start_photo, caption='Выбирай', reply_markup=keyboard_inline)


# Реакция на Первую кнопку LEXICON_INLINE
@router.callback_query(F.data == '1')
async def inline_button_1(callback: CallbackQuery):
    # Сообщение и фото в чате, заменяют предыдущие
    try:
        await callback.message.edit_media(InputMediaPhoto(media=config.photo_url.bbq, caption='Отдых на природе'),  reply_markup=keyboard_inline)
    except:
        await callback.answer('Выбери другое фото', reply_markup=keyboard_inline)

@router.callback_query(F.data == '2')
async def inline_button_1(callback: CallbackQuery):
    try:
        await callback.message.edit_media(InputMediaPhoto(media=config.photo_url.open_air, caption='Летние игры'),
                                          reply_markup=keyboard_inline)
    except:
        await callback.answer('Выбери другое фото', reply_markup=keyboard_inline)

@router.callback_query(F.data == '3')
async def inline_button_1(callback: CallbackQuery):
    try:
        await callback.message.edit_media(InputMediaPhoto(media=config.photo_url.manchkin, caption='Все ненавидят Манчкин'),
                                          reply_markup=keyboard_inline)
    except:
        await callback.answer('Выбери другое фото', reply_markup=keyboard_inline)

@router.callback_query(F.data == '4')
async def inline_button_1(callback: CallbackQuery):
    try:
        await callback.message.edit_media(InputMediaPhoto(media=config.photo_url.helloween, caption='Halloween'),
                                          reply_markup=keyboard_inline)
    except:
        await callback.answer('Выбери другое фото', reply_markup=keyboard_inline)

@router.callback_query(F.data == '5')
async def inline_button_1(callback: CallbackQuery):
    try:
        await callback.message.edit_media(InputMediaPhoto(media=config.photo_url.bar, caption='В Щуке'),
                                          reply_markup=keyboard_inline)
    except:
        await callback.answer('Выбери другое фото', reply_markup=keyboard_inline)

@router.callback_query(F.data == '6')
async def inline_button_1(callback: CallbackQuery):
    try:
        await callback.message.edit_media(InputMediaPhoto(media=config.photo_url.weekend, caption='Выездная вечеринка'),
                                          reply_markup=keyboard_inline)
    except:
        await callback.answer('Выбери другое фото', reply_markup=keyboard_inline)

@router.callback_query(F.data == '7')
async def inline_button_1(callback: CallbackQuery):
    try:
        await callback.message.edit_media(InputMediaPhoto(media=config.photo_url.color_party, caption='Цветная вечеринка'),
                                          reply_markup=keyboard_inline)
    except:
        await callback.answer('Выбери другое фото', reply_markup=keyboard_inline)

@router.callback_query(F.data == '8')
async def inline_button_1(callback: CallbackQuery):
    try:
        await callback.message.edit_media(InputMediaPhoto(media=config.photo_url.utrennik, caption='Кто потерял сироток?'),
                                          reply_markup=keyboard_inline)
    except:
        await callback.answer('Выбери другое фото', reply_markup=keyboard_inline)



