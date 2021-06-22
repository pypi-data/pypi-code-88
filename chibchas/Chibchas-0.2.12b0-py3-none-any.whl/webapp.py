from flask import Flask, render_template, flash, request, session, url_for, redirect
from wtforms import Form, TextField, validators
from flask_bootstrap import Bootstrap
import pathlib
from chibchas.tools import main
import uuid
import tempfile
import shutil
import sys
import time

# App config.
DEBUG = True
app = Flask(__name__, template_folder=str(
    pathlib.Path(__file__).parent.absolute()) + '/templates/')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid1())

Bootstrap(app)

gdrive_path = ""


class WebForm(Form):
    name = TextField('Usuario:', validators=[validators.required()])
    password = TextField('Contraseña:', validators=[
                         validators.required(), validators.Length(min=3, max=35)])


@app.route("/", methods=['GET', 'POST'])
def index():
    form = WebForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("user logged in")

        session.clear()
        session['username'] = username
        session['password'] = password
        return redirect(url_for('processing'))

    if form.validate():
        # Save the comment here.
        flash('Thanks for logging in ' + username)
    else:
        flash('Error: All the form fields are required. ')

    return render_template('login.html', form=form)


@app.route("/processing", methods=['GET', 'POST'])
def processing():
    if "username" not in session.keys() and "password" not in session.keys():
        return redirect(url_for('index'))
    return render_template('processing.html')


@app.route("/executor", methods=['GET', 'POST'])
def executor():
    if "username" not in session.keys() and "password" not in session.keys():
        return redirect(url_for('index'))
    print(session)
    username = session['username']
    password = session['password']
    tmp_path = tempfile.gettempdir() + "/chibchas/" + username
    print("Saving data on temporal folder {}".format(tmp_path))
    max_tries = 10
    for n in range(max_tries):
        try:
            LOGIN = main(username, password, tmp_path, end = None)
            if not LOGIN:
                break
            
            for i in range(max_tries):
                try:
                    shutil.copytree(tmp_path, gdrive_path, dirs_exist_ok=True)
                    #shutil.rmtree(tmp_path)
                    break
                except Exception as e:
                    time.sleep(5)
                    print("Unexpected error:", sys.exc_info()[0], " ", e)
            break
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0], " ", e)
            print('=' * 80)
            print(f'try {n}/{max_tries}')
            print('=' * 80)

    return redirect(url_for('index'))


def run_server(ip, port, gdrive_path_):  # to do ip and port
    global gdrive_path
    gdrive_path = gdrive_path_
    app.run(host=ip, port=port)
