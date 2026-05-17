from flask import Flask
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask_login import LoginManager
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user
from os import path
from random import randint
from random import seed
from time import time

from forms.userForm import LoginForm
from forms.userForm import RegisterForm
from forms.userForm import AdminForm
from data import db_session
from data.users import User
from data.characters import Character
from db import db_fill

##################### Rest Api Переводчик
import requests


def translate_text(text, target_lang="en"):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"en|{target_lang}"
    }
    response = requests.get(url, params=params).json()


##################### Сам Сайт
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Roblox_Wiki_secret_keyStrongestKey'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')

    return render_template('register.html', title='JJS Wiki Регистрация =)', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='JJS Wiki Авторизация =)', form=form)


@app.route('/profile')
@login_required
def profile():
    params = {}
    params['title'] = 'JJS Wiki Профиль =)'
    params['user'] = current_user
    my_path = url_for('static', filename='users_files/img/' + str(current_user.id) + '_' + current_user.name + '.png')
    if path.exists(my_path[1:]):
        params['image'] = my_path
    else:
        params['image'] = url_for('static', filename='img/emoji/takePhotoEmoji.png')

    return render_template('profile.html', **params)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/profile/became_Admin', methods=['GET', 'POST'])
@login_required
def became_Admin():
    form = AdminForm()

    if form.validate_on_submit():
        db_sess = db_session.create_session()

        current_user.about = form.about.data
        current_user.why_accept = form.why_accept.data

        if form.photo.data:
            file = form.photo.data
            filename = f"{current_user.id}_{current_user.name}.png"
            path = f"static/users_files/img/{filename}"
            with open(path, mode="wb") as f:
                f.write(file.read())

        db_sess.commit()
        return redirect('/profile')

    return render_template('admin_form.html', title='JJS Wiki Форма на становление администратором =)', form=form)


@app.route('/profile/download_photo', methods=['GET', 'POST'])
@login_required
def download_photo():
    return "Скоро..."


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
        params['img_url_Ult_Activation'] = url_for('static',
                                                   filename=f'img/characters/{pers.urlname}/{pers.urlname + "UltActivation"}.png')
        params['img_url_Ult'] = url_for('static', filename=f'img/characters/{pers.urlname}/{pers.urlname + "Ult"}.png')
        params['img_url_Ult2'] = url_for('static',
                                         filename=f'img/characters/{pers.urlname}/{pers.urlname + "Ult2"}.png')
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
    lang = request.args.get("lang", "ru")
    text = "Проект Воропаева Артёма и Кузнецова Максима по Любимому Яндекс Лицую❤"

    if lang != "ru":
        text = translate_text(text, lang)

    return f'''
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
            crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/base.css')}">

        <link rel="icon" type="image/png" href="{url_for('static', filename='img/JJS_Logo.png')}">
        
        <title>JJS Wiki Authors Secret(1/2) =)</title>
    </head>
    <body style='background:#111;color:white;font-family:Segoe UI;padding:40px;'>
        <div class="box">
            <h1>Авторы данного проекта</h1>
            <h3>Cервис перевода бесплатный: если он перегружен, то в качестве перевода вернёт пустую строчку</h3>
            <br>
            <p>{text}</p>

            <div class="lang-buttons">
                <a href="?text={text}&lang=ru">RU</a>
                <a href="?text={text}&lang=en">EN</a>
            </div>
        </div>
    </body>
    </html>
    '''


@app.route("/secret/67")
@app.route("/secrets/67")
@app.route("/67")
def secter67():
    params = {}
    params['title'] = "JJS Wiki Authors Secret(1/2) =)"
    return render_template('index67.html', **params)


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


# ---------------------< Дебаг >---------------------
import traceback


@app.errorhandler(500)
def internal_error(error):
    print(traceback.format_exc())
    return "Ошибка 500, админ скоро всё исправит)", 500


# ---------------------< Main >---------------------
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
