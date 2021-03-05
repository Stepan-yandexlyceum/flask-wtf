from flask import Flask, url_for, request, render_template
from flask_login import LoginManager, login_user
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

# from data import db_session

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    elements = ''
    text = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]

    for line in text:
        elements += f'<p>{line}</p>'

    return elements


@app.route('/image_mars')
def image_mars():
    return f'''
        <h1>Жди нас, Марс!</h1>
        <img width="300px" src="{url_for('static', filename='img/mars.jpg')}"
        alt="Тут должно быть изображение марса"/>
        <p>Вот она какая, красная планета.</p>
    '''


@app.route('/promotion_image')
def promotion_image():
    image = url_for('static', filename='img/mars.jpg')
    styles = url_for('static', filename='css/style.css')
    bootstrap = url_for('static', filename='css/bootstrap.min.css')
    text = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]

    return f'''

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="{bootstrap}">
        <link rel="stylesheet" href="{styles}">
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img width="300" src="{image}" alt="Изображение Марса"/>
        <div class="alert alert-dark">{text[0]}</div>
        <div class="alert alert-success">{text[1]}</div>
        <div class="alert alert-info">{text[2]}</div>
        <div class="alert alert-danger">{text[3]}</div>
        <div class="alert alert-warning">{text[4]}</div>
    </body>
    </html>

    '''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        styles = url_for('static', filename='css/style.css')
        bootstrap = url_for('static', filename='css/bootstrap.min.css')
        educations = (
            'Начальное',
            'Среднее',
            'Среднее специальное',
            'Бакалавр',
            'Магистр',
            'Специалитет',
            'Доктор наук'
        )

        professions = (
            'Инженер-исследователь',
            'Инженер-строитель',
            'Пилот',
            'Метеоролог',
            'Инженер по жизнеобеспечению',
            'Инженер по радиационной защите',
            'Врач',
            'Экзобиолог'
        )

        gender = [
            'Мужской',
            'Женский'
        ]

        return f'''
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Отбор астронавтов</title>
            <link rel="stylesheet" href="{bootstrap}">
            <link rel="stylesheet" href="{styles}">
        </head>
        <body>
            <h1 class="header-form">Анкета претендента</h1>
            <h2 class="subheader-form">На участие в миссии</h2>

            <form method="post">
                <input name="surname" type="text" placeholder="Введите фамилию"/>
                <input name="name" type="text" placeholder="Введите имя"/>
                <input name="email" type="email" placeholder="Введите адрес почты"/>
                <label for="education">Какое у Вас образование?</label>
                <select name="edu" id="education">
                    {''.join(create_form_item('option', educations))}
                </select>
                <div class="check check-profession">
                    <p>Какие у Вас есть профессии?</p>
                    {create_checkboxes('checkbox', professions)}
                </div>
                <div class="check check-gender">
                    <p>Укажите пол</p>
                    {create_checkboxes('radio', gender)}
                </div>
                <p>Почему Вы хотите принять участие в миссии?</p>
                <textarea name="motivation"></textarea>
                <label for="file-att">Приложите фотографию</label> 
                <input name="photo" id="file-att" type="file">
                <div class="check check-agree">
                    <label for="agree">Готовы остаться на Марсе?</label>
                    <input name="agree" id="agree" type="checkbox">
                </div>
                <button class="btn btn-primary" type="submit">Отправить</button>
            </form>

        </body>
        </html>
        '''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['edu'])
        print(request.form['profession'])
        print(request.form['gender'])
        print(request.form['motivation'])
        print(request.form['photo'])
        print(request.form['agree'])
        return "Форма отправлена"


def create_form_item(tag_name, items):
    return list(map(lambda x: f'<{tag_name} value="{x}">{x}</{tag_name}>', items))


def create_checkboxes(tag_name, items):
    container = ''
    note_id = 0
    for item in items:
        note_id += 1
        checkbox = f'<input type="{tag_name}" id={tag_name}-{note_id} ' \
                   f'value="{item}"{" name=gender" if tag_name == "radio" else " name=profession"}>'
        label = f'<label for="{tag_name}-{note_id}">{item}</label>'
        container += f'' \
                     f'<div class="{tag_name}">{checkbox + label}</div>'

    return container


@app.route('/choice/<planet_name>')
def choice(planet_name):
    styles = url_for('static', filename='css/style.css')
    bootstrap = url_for('static', filename='css/bootstrap.min.css')
    text = [
        'Эта планета близка к земле',
        'На ней много необходимых ресурсов',
        'На ней есть вода и атмосфера',
        'На ней есть небольшое магнитное поле',
        'Наконец, она просто красива!'
    ]
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h2>Мое предложение:{planet_name}</h2>
                    <div class="alert alert-dark">{text[0]}</div>
                    <div class="alert alert-success">{text[1]}</div>
                    <div class="alert alert-info">{text[2]}</div>
                    <div class="alert alert-danger">{text[3]}</div>
                    <div class="alert alert-warning">{text[4]}</div>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    styles = url_for('static', filename='css/style.css')
    bootstrap = url_for('static', filename='css/bootstrap.min.css')
    text = [
        f'Поздравляем! Ваш рейтинг после {level} этапа отбора',
        f'Составляет {rating}',
        'Желаем удачи'
    ]
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>Пример с несколькими параметрами</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h2>Претендента на учатие в миссии:{nickname}</h2>
                        <div class="alert alert-success">{text[0]}</div>
                        <div class="alert alert-info">{text[1]}</div>
                        <div class="alert alert-warning">{text[2]}</div>
                      </body>
                    </html>'''


@app.route('/carousel')
def carousel():
    styles = url_for('static', filename='css/style.css')
    bootstrap = url_for('static', filename='css/bootstrap.min.css')
    return f'''app.run(port=8080, host='127.0.0.1')
                    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img src="{url_for('static', filename='img/landscape1.jpg')}" class="d-block w-100" alt="slide 1">
                        </div>
                        <div class="carousel-item">
                          <img src="{url_for('static', filename='img/landscape2.jpg')}" class="d-block w-100" alt="slide 2">
                        </div>
                        <div class="carousel-item">
                          <img src="{url_for('static', filename='img/landscape3.jpg')}" class="d-block w-100" alt="slide 3">
                        </div>
                      </div>
                      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls"  data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                      </button>
                      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls"  data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                      </button>
                    </div>'''


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
