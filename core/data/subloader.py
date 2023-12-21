import os

from ujson import loads  # pip install ujson
import aiofiles  # pip install aiofiles


async def get_json(filename: str) -> list:
    path = f"core/data/{filename}"

    if os.path.exists(path):
        async with aiofiles.open(path, "r", encoding="utf-8") as file:
            return loads(await file.read())
    return []