import sqlalchemy

from .db_session import SqlAlchemyBase


class Skill(SqlAlchemyBase):
    __tablename__ = 'skills'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    base = sqlalchemy.Column(sqlalchemy.Boolean)

    damage = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cooldown = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    character = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f"<Skill> id={self.id}, name={self.name}, character={self.character}"
