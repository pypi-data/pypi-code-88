import json
import logging

from flask import Flask, request, Response, jsonify, render_template, session as Fsession, redirect, url_for
from functools import wraps
from markupsafe import escape
from typing import Callable, TypeVar, cast

from src.sql.model import Variable
from src.sql.settings import create_session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)

log = logging.getLogger(__name__)

session = None


T =TypeVar("T", bound=Callable)


def requires_authentication(function: T):
    @wraps(function)
    def decorated():
        return True
    return cast(T, decorated)


@app.route("/test")
def test():
    return jsonify(status='OK')


@app.route("/")
def index():
    if 'username' in Fsession:
        return 'Logged in as %s' % escape(Fsession['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Fsession['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route("/api/variables")
def get_all_variables():
    result = Variable.select_all(session=session)
    return jsonify([e.serialize() for e in result])


@app.route('/api/variables/<key>', methods=['GET'])
@requires_authentication
def get_by_id(key):
    log.debug("Key: {}".format(key))
    item = Variable.get_by_key(key=key)
    return Response(json.dumps(item.serialize()), mimetype='application/json')


@app.route("/api/create_variable", methods=['POST'])
def create_variable():
    content = request.get_json(silent=True)
    Variable.create(key=content['key'], value=content['value'], is_encrypted=content['is_encrypted'])
    return '', 200


@app.route("/api/variables/<key>", methods=['DELETE'])
def delete(key):
    Variable.delete(key=key)
    return '', 204


if __name__ == '__main__':
    session = create_session()
    app.run(debug=True)