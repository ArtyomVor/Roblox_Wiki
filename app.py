from flask import Flask
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from os import path
from random import randint
from random import seed
from time import time

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
    # db_fill.Aspiring_Mangaka()
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
    return redirect(url_for("about"))


@app.route("/welcome")
@app.route("/about")
def about():
    params = {}
    params['title'] = "JJS Wiki =)"
    return render_template("welcome.html", **params)


# @app.route("/characters")
# def characters():
#     return "Characters page"


@app.route("/characters/<cur_name>")
def character(cur_name):
    db_sess = db_session.create_session()
    pers = db_sess.query(Character).filter(Character.urlname == cur_name).first()

    params = {}
    params['title'] = "JJS Wiki " + pers.urlname + " =)"
    if (pers.awakening != None):
        if (pers.urlname == "Restless_Gambler"):
            seed(time())
            params['backgroung_img_url'] = url_for('static',
filename=f'img/characters/{pers.urlname}/{pers.urlname + "_Background" + str(1 + randint(0, 239) % 3)}.png')
        else:
            params['backgroung_img_url'] = url_for('static',
filename=f'img/characters/{pers.urlname}/{pers.urlname + "_Background"}.png')

        params['name'] = pers.name
        params['description'] = pers.description
        params['img_url1'] = url_for('static', filename=f'img/characters/{pers.urlname}/{pers.urlname}.png')
        params['img_url2'] = url_for('static', filename=f'img/characters/{pers.urlname}/{pers.urlname + "2"}.png')
        params['img_url_Ult_Activation'] = url_for('static', filename=f'img/characters/{pers.urlname}/{pers.urlname + "UltActivation"}.png')
        params['img_url_Ult'] = url_for('static', filename=f'img/characters/{pers.urlname}/{pers.urlname + "Ult"}.png')
        params['img_url_Ult2'] = url_for('static', filename=f'img/characters/{pers.urlname}/{pers.urlname + "Ult2"}.png')
        params['who'] = pers.who
        params['price'] = pers.price
        params['awakening'] = pers.awakening
        params['health'] = pers.health
        params['tips'] = pers.tips
        params['facts'] = pers.facts
        return render_template("character.html", **params)
    else:
        params['backgroung_img_url'] = (url_for('static',
                                filename=f'img/characters/{pers.urlname}/{pers.urlname + "_Background"}.png'))

        params['name'] = pers.name
        params['description'] = pers.description
        params['img_url1'] = url_for('static', filename=f'img/characters/{pers.urlname}/{pers.urlname}.png')
        params['img_url2'] = url_for('static', filename=f'img/characters/{pers.urlname}/{pers.urlname + "2"}.png')
        params['img_url_Ult_Activation'] = url_for('static',
                                                   filename=f'img/characters/{pers.urlname}/{pers.urlname + "UltActivation"}.png')
        params['img_url_Ult'] = url_for('static', filename=f'img/characters/{pers.urlname}/{pers.urlname + "Ult"}.png')
        params['who'] = pers.who
        params['price'] = pers.price
        params['base_only_awakening'] = pers.base_only_awakening
        params['health'] = pers.health
        params['tips'] = pers.tips
        params['facts'] = pers.facts
        return render_template("character.html", **params)


@app.route("/cash")
def cash():
    params = {}
    params['title'] = "JJS Wiki Cash =)"
    return render_template("cash.html", **params)


# @app.route("/mechanics/<thing>")
# def mechanics(thing):
#     return f"Mechanic: {thing}"


@app.route("/secret/authors")
@app.route("/secrets/authors")
def secretAuthors():
    params = {}
    params['title'] = "JJS Wiki Authors Secret(1/2) =)"
    return "Проект Воропаева Артёма и Кузнецова Максима по Любимому Яндекс Лицую❤"


@app.route("/secret/67")
@app.route("/secrets/67")
@app.route("/67")
def secter67():
    params = {}
    params['title'] = "JJS Wiki Authors Secret(1/2) =)"
    return render_template('index67.html', **params)


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')


##### Что сделано:

##### Что осталось сделать:
# Полностью доделана база данных
# Сделаны Приёмы у страниц персонажей
# tips
# добавлен(а) в базу данных
# задний фон персонажей это те прикольные картинки
# Исправлен редирект у /about
# Авторизация
# добавить Котика - Авторы
# создать перса Макора
# Что за Mokou


# TZE ❤😍🤣
# alembic нам не нужён!
