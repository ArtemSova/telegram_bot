from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from datetime import datetime
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from core.config_data.config import Config, load_config


"""
SQLite
"""
# Подключение к серверу
engine = create_engine('sqlite:///F:\\Python\\telegram_bot\\tg_bot_SQLite.db')
engine.connect()
metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('user_id', Integer(), unique=True, nullable=False),
    Column('user_name', String(64), unique=True, nullable=False),
    Column('first_name', String(64), nullable=False),
    Column('birthday', String(18), default=None),
    Column('phone_number', String(12), default=None, unique=True),
    Column('coins', Integer(), default=100),
    Column('create_user_date', DateTime(), default=datetime.now()),
)

daily_holiday = Table(
    'daily_holiday',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('month', Integer(), nullable=False),
    Column('day', Integer(), nullable=False),
    Column('holiday', Text(), nullable=False),
)

board_games = Table(
    'board_games',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('game', String(64), unique=True, nullable=False),
)



"""
PostgreSQL
"""
# config: Config = load_config()
# engine = create_engine(f'postgresql+psycopg2://{config.db.db_user}:{config.db.db_password}@{config.db.db_host}/{config.db.database}')
# engine.connect()

# # Установка соединения с PostgreSQL
# connection = psycopg2.connect(user={config.db.db_user}, password={config.db.db_password})
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
# # Создаем курсор для выполнения операций с базой данных
# cursor = connection.cursor()
# # Создаем базу данных
# sql_create_database = cursor.execute("create database tg_bot_SQLite")
# # Закрываем соединение
# cursor.close()
# connection.close()
#
#
# metadata = MetaData()
#
# users = Table(
#     'users',
#     metadata,
#     Column('id', Integer(), primary_key=True),
#     Column('user_id', Integer(), unique=True, nullable=False),
#     Column('first_name', String(64), nullable=False),
#     Column('user_name', String(64), unique=True, nullable=False),
#     Column('is_admin', Boolean(), default=False),
#     Column('is_block', Boolean(), default=False),
#     Column('create_user_date', DateTime(), default=datetime.now()),
# )


metadata.create_all(engine)

