from sqlalchemy import insert, select, update, delete, table, column
from sqlalchemy.orm import Session
from datetime import datetime

from config_db.base_model import engine, daily_holiday


class HolidaySQL:
    session = Session(engine)

    def holidays(self, day: int, month: int, holiday: str):
        """
        Добавляем праздники в БД
        """

        ins = insert(daily_holiday).values(
            day=day,
            month=month,
            holiday=holiday,
        )

        self.session.execute(ins)
        self.session.commit()

    def holidays_select(self):
        """
        Выводим праздники из БД
        """

        today = datetime.today()
        month, day, year = today.month, today.day, today.year

        sel = select(daily_holiday.c.holiday).where(daily_holiday.c.day == day, daily_holiday.c.month == month)


        return self.session.execute(sel).fetchall()[0][0]









