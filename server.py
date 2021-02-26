from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
# def index(title):
#     return render_template('base.html',title=title)

@app.route('/training/<prof>')
def training(prof):
    title = 'mars'
    if 'инженер' in prof or 'строитель' in prof:
        file = 'img/station.PNG'
    else:
        file = 'img/durka.jpg'
    # return render_template('base.html',title=title)
    file = url_for('static', filename=file)
    return render_template('base.html', title=title, file=file)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
