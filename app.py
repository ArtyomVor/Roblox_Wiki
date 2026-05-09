from flask import Flask
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from os import path

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


@app.route("/")
@app.route("/index")
def index():
    return redirect(url_for('welcome'))


@app.route("/about")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


# @app.route("/characters")
# def characters():
#     return "Characters page"
#
#
# @app.route("/character/<name>")
# def character(name):
#     return f"Character page: {name}"
#
#
# @app.route("/mechanics/<thing>")
# def mechanics(thing):
#     return f"Mechanic: {thing}"


@app.route("/secret/authors")
@app.route("/secrets/authors")
def secretAuthors():
    return "Проект Воропаева Артёма и Кузнецова Максима по Любимому Яндекс Лицую❤"


@app.route("/secret/67")
@app.route("/secrets/67")
@app.route("/67")
def secter67():
    return render_template('index67.html')


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')

# TZE ❤😍🤣

# tips
# добавлен(а) в базу данных
# добавить Котика - Авторы
# создать перса Макора
# Что за Mokou

# alembic нам не нужён!



# Исправлен редирект у /about
# Авторизация
# Добавлена ссылка на разработчиков Jujutsu Shenanigans.
# Сделан шаблон для страниц персонажей.


# 11 не будет
# 14 защита
