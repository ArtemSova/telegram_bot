from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from datetime import datetime
import psycopg2

from core.config_data.config import Config, load_config


"""
SQLite
"""
engine = create_engine('sqlite:///tg_bot_SQLite.db')
engine.connect()
metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('user_id', Integer(), unique=True, nullable=False),
    Column('first_name', String(64), nullable=False),
    Column('user_name', String(64), unique=True, nullable=False),
    Column('is_admin', Boolean(), default=False),
    Column('is_block', Boolean(), default=False),
    Column('create_user_date', DateTime(), default=datetime.now()),
)


"""
PostgreSQL
"""
# config: Config = load_config()
# engine = create_engine(f'postgresql+psycopg2://{config.db.db_user}:{config.db.db_password}@{config.db.db_host}/{config.db.database}')
# engine.connect()
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

