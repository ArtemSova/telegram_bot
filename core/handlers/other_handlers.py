from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from core.keyboards.keyboards import create_key, create_inline_key
from core.lexicon.lexicon_ru import LEXICON_MENU, LEXICON_INLINE


router: Router = Router()
# Отображение кнопок, create_key(количество кнопок в строке(линии), источник кнопок)
keyboard_start = create_key(2, **LEXICON_MENU)
keyboard_inline = create_inline_key(3, **LEXICON_INLINE)

# Реакция на кнопку старт или \start
@router.message(CommandStart())
async def process_start_command(message: Message):
    # Ответное приветствие и отображение кнопок из keyboard_start
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=keyboard_start)

# Реакция на приветствия
@router.message(F.text.lower() == "hi")
async def hi(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Поиграем!!!')

# Реакция на кнопку "Сказать привет"
@router.message(F.text == "Сказать привет")
async def hi(message: Message):
    await message.answer('Привет')

# Реакция на кнопку "Список кнопок"
@router.message(F.text == 'Список кнопок')
async def keys_list(message: Message):
    await message.answer('Вот они', reply_markup=keyboard_inline)

# Реакция на Первую кнопку LEXICON_INLINE
@router.callback_query(F.data == '1')
async def inline_button_1(callback: CallbackQuery):
    # Сообщение в чат, заменяет предыдущее сообщение
    try:
        await callback.message.edit_text('Нажата первая кнопка', reply_markup=keyboard_inline)
    except:
        await callback.answer('Первая кнопка уже нажата', reply_markup=keyboard_inline)
