import sqlalchemy

from .db_session import SqlAlchemyBase


class Character(SqlAlchemyBase):
    __tablename__ = 'characters'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    urlname = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    who = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.String, nullable=True, default="Бесплатный")
    health = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    base_only = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    overpowered = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tips = sqlalchemy.Column(sqlalchemy.String, nullable=True, default="Пусто)")
    facts = sqlalchemy.Column(sqlalchemy.String, nullable=True, default="Пусто)")

    is_custom = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    move1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    move2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    move3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    move4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    special = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    # Авейк мув
    base_only_awakening = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    # Авейк мувсет
    awakening = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ult_move1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ult_move2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ult_move3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ult_move4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ult_special = sqlalchemy.Column(sqlalchemy.String, nullable=True)


    def __repr__(self):
        return f"<Character> id={self.id}, name={self.name}"
