from typing import Any
from aiogram.types import Message, CallbackQuery
from aiogram.filters import BaseFilter
from aiogram.filters import CommandObject


class CheckForDigit(BaseFilter):
    async def __call__(self, message: Message, **kwargs: Any) -> bool:
        command: CommandObject = kwargs.get("command")
        arg = command.args

        if arg.isnumeric() or arg.isdecimal():
            return True
        return False

