#!/usr/bin/env python3

#BoBoBo#

from pin.router import *

app = pin_app(True)


@route('/pin/test/hello')
def hello_str(param):
    print(param)
    return 'Hello Pin!'


@route('/pin/test/hello2')
def hello_dict(param):
    return {'say': 'Hello Pin!'}


@route('/pin/test/hello3')
def hello_tpl(param):
    return "hello.html", None


def test_dispatch():
    request = {}
    request['PATH_INFO'] = '/pin/test/hello'
    request['REQUEST_METHOD'] = 'GET'
    request['QUERY_STRING'] = 'param=testparam'

    response = dispatch(request)
    print(response)
    assert response['content'] == 'Hello Pin!'

    request['PATH_INFO'] = '/pin/test/hello2'
    response = dispatch(request)
    print(response)
    assert json.loads(response['content']) == {'say': 'Hello Pin!'}

    request['PATH_INFO'] = '/pin/test/hello3'
    response = dispatch(request)
    print(response)
