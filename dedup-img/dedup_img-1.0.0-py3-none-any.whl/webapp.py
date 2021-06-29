import os
import sys
from getopt import getopt

from flask import Flask, request, jsonify
from flask import render_template

from .dedup_utils import filter_dedup, move_to_dedup, del_from_dedup

app = Flask('imagededup-browser')


@app.get('/')
@app.get('/<alg>')
def index(alg=None):
    return render_template('index.html', alg=alg)


@app.get('/filter/<alg>')
def get_filter(alg='phash'):
    _filter = filter_dedup(app.static_folder, alg)
    return jsonify(_filter)


@app.put('/move')
def move():
    res = move_to_dedup(app.static_folder, request.form.get('img'))
    return jsonify({'result': res})


@app.delete('/delete')
def delete():
    _del = del_from_dedup(app.static_folder, request.form.get('img'))
    return jsonify(_del)


# ################ 测试接口 ###################

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        account = request.form.get('account')
        password = request.form.get('password')
        print('account = %s' % account)
        print('password = %s' % password)
        return render_template('login.html', result='登陆失败')


@app.get('/testget')
def test_get():
    return jsonify(request.args)


@app.post('/testpost')
def test_post():
    print(app.static_folder)
    print(request.form)
    return jsonify(request.form)


def run_server(folder):
    app.static_folder = folder
    app.template_folder = os.path.join(os.path.dirname(__file__), 'templates')
    app.run(host='0.0.0.0', port=8000, debug=True)


def main():
    try:
        opts, args = getopt(sys.argv[1:], '')
        if len(args) == 0:
            raise Exception('please enter image dir')
        image_dir = args[0]
        if not os.path.isdir(image_dir):
            raise Exception("'%s' is not a dir" % image_dir)
        run_server(image_dir)
    except Exception as e:
        print(e)
