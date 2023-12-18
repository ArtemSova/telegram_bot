import random

from sqlalchemy import insert, select, update, delete, table, column
from sqlalchemy.orm import Session

from config_db.base_model import engine, board_games


class BoardGamesSQL:
    session = Session(engine)

    def insert_board_games(self, game: str):
        ins = insert(board_games).values(
            game=game,
        )

        self.session.execute(ins)
        self.session.commit()

    def board_games_select(self):


        sel = select(board_games.c.game)


        return self.session.execute(sel).fetchall()


# print(random.choice(BoardGamesSQL().board_games_select(5)))