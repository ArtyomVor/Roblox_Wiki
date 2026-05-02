from flask import Flask

from data import db_session
from data.users import User
from data.characters import Character
from db import db_fill

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Roblox_Wiki_secret_key==StrongestKey'


def main():
    db_session.global_init("db/Jujutsu_Shenanigans.db")

    # db_fill.Honored_One()
    # db_fill.Vessel()
    # db_fill.Restless_Gambler()
    # db_fill.Ten_Shadows()
    # db_fill.Perfection()
    # db_fill.Blood_Manipulator()
    # db_fill.Switcher()
    # db_fill.Defense_Attorney()
    # db_fill.Cursed_Partners()
    # db_fill.Puppet_Master()
    # db_fill.Head_of_the_Hei()
    # db_fill.Salaryman()
    # db_fill.Disaster_Plant()
    # db_fill.True_Cannon()

    # db_fill.Locust_Guy()
    # db_fill.Star_Rage()
    # db_fill.Lucky_Coward()
    # db_fill.Crow_Charmer()

    # db_fill.Strongest_Of_History()
    # db_fill.Monkey_Kid()

    # db_sess = db_session.create_session()
    # pers = db_sess.query(Character).filter(Character.id==5).first()
    # pers.tips = '''
    # '''
    # db_sess.commit()
    # print(f"{pers.name}: tips updated")


if __name__ == '__main__':
    main()
    # app.run(port=8080, host='127.0.0.1')

# tips
# добавлен(а) в базу данных
# создать перса Макора
# Что за Mokou

# alembic нам не нужён!
