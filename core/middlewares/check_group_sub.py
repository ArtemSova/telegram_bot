from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Dict, Any

from core.config_data.config import Config, load_config


config: Config = load_config()

class CheckGroupSubscription(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        chat_member = await event.bot.get_chat_member(config.group.group_id, event.from_user.id)

        if chat_member.status == "left":
            await event.answer("Ты не являешься участником группы. Если ты не знаешь что это за группа, то что ты тут делаешь?")
        else:
            return await handler(event, data)


