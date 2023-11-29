from __future__ import annotations

from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    bot_token: str
    admin_id: int


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            bot_token=env.str('BOT_TOKEN'),
            admin_id=env.int("ADMIN_ID")
        )
    )
