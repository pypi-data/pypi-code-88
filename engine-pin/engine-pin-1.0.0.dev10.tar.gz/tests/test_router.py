#!/usr/bin/env python3

#BoBoBo#

from pin.router import *

app = pin_app(True)


@route("/pin/test/hello")
def hello(param):
    print(param)
    return "Hello Pin!"


def test_dispatch():
    request = {}
    request['PATH_INFO'] = '/pin/test/hello'
    request['REQUEST_METHOD'] = 'GET'
    request['QUERY_STRING'] = 'param=testparam'

    response = dispatch(request)
    print(response)
    assert response['content'] == "Hello Pin!"


def test_controller_param():
    hello(100)
