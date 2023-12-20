from contextlib import suppress  # заменяет try-except

from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto
from aiogram.exceptions import TelegramBadRequest

from core.keyboards import fabrics
from core.data.subloader import get_json

router = Router()


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["prev", "next"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    photos = await get_json("photos.json")

    # непосредственно пагинация (логика), зациклена по-кругу
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else (len(photos) - 1)  # заменить (len(photos) - 1) на 0, не по-кругу а от 0 до последней и обратно

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(photos) - 1) else 0  # заменить (len(photos) - 1) на page_num, не по-кругу а от 0 до последней и обратно

    # отрисовка
    with suppress(TelegramBadRequest):
        await call.message.edit_media(
            InputMediaPhoto(media=photos[page][1], caption=photos[page][0]),
            reply_markup=fabrics.paginator(page)
        )
    await call.answer()

        # await call.message.edit_text(
        #     f"{photos[page][0]} <b>{photos[page][1]}</b>",
        #     reply_markup=fabrics.paginator(page)
