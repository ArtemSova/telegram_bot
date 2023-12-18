from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session

from config_db.base_model import engine, users


class UsersSQL:
    session = Session(engine)

    def insert(self, user_id: int, user_name: str, first_name: str, birthday: str = None, phone_number: str = None, coins: int = 100):
        """
        Добавляем пользователей в БД
        """

        ins = insert(users).values(
            user_id=user_id,
            user_name=first_name,
            first_name=user_name,
            birthday=birthday,
            phone_number=phone_number,
            coins=coins,
        )

        self.session.execute(ins)
        self.session.commit()

    def update_user_info(self, user_id:int, first_name, birthday, phone_number):
        upd = update(users).where(users.c.user_id == user_id).values(first_name=first_name, birthday=birthday, phone_number=phone_number)
        self.session.execute(upd)
        self.session.commit()

    def select_user_info(self, user_id: int):
        """
        Забираем id пользователей из БД
        """

        sel = select(users.c.user_name, users.c.first_name, users.c.birthday, users.c.phone_number, users.c.coins).where(users.c.user_id == user_id)

        return self.session.execute(sel).fetchall()

# UsersSQL().update_user_info(329725203, 'Артем', '07.05.1989', '+7(999)999-99-99')
# print(f'user_name: {UsersSQL().select_user_info(329725203)[0][0]}')
# print(f'Имя: {UsersSQL().select_user_info(329725203)[0][1]}')
# print(f'День рождения: {UsersSQL().select_user_info(329725203)[0][2]}')
# print(f'Телефон: {UsersSQL().select_user_info(329725203)[0][3]}')
# print(f'Монеты: {UsersSQL().select_user_info(329725203)[0][4]}')
