# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mause_rpc']

package_data = \
{'': ['*']}

install_requires = \
['dill>=0.3.1,<0.4.0', 'pika>=1.1.0,<2.0.0', 'retry>=0.9.2,<0.10.0']

setup_kwargs = {
    'name': 'mause-rpc',
    'version': '0.0.20',
    'description': 'A dumb as hell rpc implementation built on rabbitmq',
    'long_description': "Mause RPC\n=========\n\nA dumb as hell rpc implementation built on rabbitmq\n\nNeed to write a server?\n\n```py\nfrom mause_rpc.server import Server\n\nrpc_queue = 'rpc.queue'\nserver = Server(rpc_queue, 'rabbitmq://...')\n\n\n@server.register\ndef hello(name: str) -> str:\n    return 'hello ' + name\n\n\n@server.register('divide')\ndef div(a: int, b: int) -> float:\n    if b == 0:\n        raise ZeroDivisionError()\n    return a / b\n\n\nif __name__ == '__main__':\n    server.serve()\n\n```\n\nNeed a client?\n\n```py\nfrom mause_rpc.client import get_client\n\nrpc_queue = 'rpc.queue'\nclient = get_client(rpc_queue, 'rabbitmq://...')\n\n\ndef test_basic_functionality():\n    assert client.hello('mark') == 'hello mark'\n    assert client.divide(5, 2) == 2.5\n\n    with pytest.raises(ZeroDivisionError):\n        client.divide(5, 0)\n```\n",
    'author': 'Elliana May',
    'author_email': 'me@mause.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Mause/rpc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
