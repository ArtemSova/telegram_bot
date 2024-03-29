from __future__ import annotations

from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    bot_token: str

@dataclass
class Group:
    group_id: str

@dataclass
class Admin:
    admin_id: int

@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str

@dataclass
class photo_url:
    saw: str
    start_photo: str
    bbq: str
    open_air: str
    manchkin: str
    helloween: str
    bar: str
    weekend: str
    color_party: str
    utrennik: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
    group: Group
    admin: Admin
    photo_url: photo_url


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            bot_token=env.str('BOT_TOKEN')
        ),
        db=DatabaseConfig(
            database=env.str('DATABASE'),
            db_host=env.str('DB_HOST'),
            db_user=env.str('DB_USER'),
            db_password=env.str('DB_PASSWORD'),
        ),
        group=Group(
            group_id=env.str('GROUP_ID')
        ),
        admin=Admin(
            admin_id=env.int('ADMIN_ID')
        ),
        photo_url=photo_url(
            saw=env.str('saw'),
            start_photo=env.str('start_photo'),
            bbq=env.str('bbq'),
            open_air=env.str('open_air'),
            manchkin=env.str('manchkin'),
            helloween=env.str('helloween'),
            bar=env.str('bar'),
            weekend=env.str('weekend'),
            color_party=env.str('color_party'),
            utrennik=env.str('utrennik'),
        )
    )

