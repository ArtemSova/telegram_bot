from typing import List
from aiogram.types import Message, CallbackQuery
from aiogram.filters import BaseFilter


class IsAdmin(BaseFilter):

    def __init__(self, user_ids: int | List[int]) -> None:
        self.user_ids = user_ids

    # Проверка id пользователей
    async def __call__(self, message: Message) -> bool:
        # Один id
        if isinstance(self.user_ids, int):
            return message.from_user.id == self.user_ids
        # Список id
        return message.from_user.id in self.user_ids