from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session

from config_db.base_model import engine, users


class UsersSQL:
    session = Session(engine)

    def insert(self, user_id: int, first_name: str, user_name: str, coins: int = 100, is_admin: bool = False, is_block: bool = False):
        """
        Добавляем пользователей в БД
        """

        ins = insert(users).values(
            user_id=user_id,
            first_name=first_name,
            user_name=user_name,
            coins=coins,
            is_admin=is_admin,
            is_block=is_block,
        )

        self.session.execute(ins)
        self.session.commit()

    def users_id_select(self):
        """
        Забираем id пользователей из БД
        """

        sel = select(users.c.user_id)


        return self.session.execute(sel).fetchall()

print(UsersSQL.users_id_select())

