from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session

from config_db.base_model import engine, users


class SQL:
    session = Session(engine)

    def INSERT(self, user_id: int, first_name: str, user_name: str, is_admin: bool = False, is_block: bool = False):
        """
        Добавляем пользователей в БД
        """

        ins = insert(users).values(
            user_id=user_id,
            first_name=first_name,
            user_name=user_name,
            is_admin=is_admin,
            is_block=is_block,
        )

        self.session.execute(ins)
        self.session.commit()

