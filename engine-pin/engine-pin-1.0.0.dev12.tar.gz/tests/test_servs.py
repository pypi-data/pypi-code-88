#!/usr/bin/env python3

#BoBoBo#

from threading import Thread
import time
import pin.kit.rpc.servs as servs
import pin.embed.server as server
from pin.router import *


def test_local():
    result = servs.get_serv('test.rpc2')(param1=11)
    assert result['_pin_return'] == 111
    assert result['_pin_from'] == 'local'


@route("/test/rpc1")
def r1(param1, param2):
    data = {'param1' : str(param1) , 'param2' : str(param2) }
    result = {'code': 0, 'msg': 'succeed', 'data': data}
    return result

@route("/test/rpc2")
def r2(param1):
    return param1 + 100


app = pin_app(True)


def test_remote():
    global app
    t = Thread(target=server.bootstrap, args=(app,), daemon=True)
    t.start()
    print("Waiting server start for 5 seconds...")
    time.sleep(5)

    result = servs.get_serv('test.rpc1')(param1=1, param2=2)
    assert result['code'] == 0
    assert result['data'] == {'param1':'1', 'param2':'2'}
    assert result['_pin_from'] == 'remote'
