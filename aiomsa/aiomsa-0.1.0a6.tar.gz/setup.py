# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiomsa', 'aiomsa.mock', 'aiomsa.mock.e2', 'aiomsa.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp-swagger>=1.0.9,<2.0.0',
 'aiohttp>=3.5.4,<4.0.0',
 'prometheus-async>=19.2.0,<20.0.0']

extras_require = \
{'docs': ['furo>=2021.2.21b25,<2022.0.0',
          'sphinx>=3.4.3,<4.0.0',
          'sphinx-autodoc-typehints>=1.11.1,<2.0.0',
          'sphinxcontrib-openapi>=0.7.0,<0.8.0']}

setup_kwargs = {
    'name': 'aiomsa',
    'version': '0.1.0a6',
    'description': 'Asynchronous xApp framework',
    'long_description': '# aiomsa\n[![build](https://github.com/facebookexternal/aiomsa/actions/workflows/build.yml/badge.svg)](https://github.com/facebookexternal/aiomsa/actions/workflows/build.yml)\n[![style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n![PyPI - Downloads](https://img.shields.io/pypi/dw/aiomsa)\n\n*aiomsa* is a Python 3.7+ framework built using `asyncio`. At its core, *aiomsa*\nprovides a simple and standardized way to write xApps that can be deployed as\nmicroservices in Python.\n\n## Installation\n*aiomsa* can be installed from PyPI.\n```bash\npip install aiomsa\n```\n\nYou can also get the latest code from GitHub.\n```bash\npoetry add git+https://github.com/facebookexternal/aiomsa\n```\n\n## Getting Started\nThe follwing example shows how to use *aiomsa* to create a simple xApp for subscribing\nto the E2T service for a particular custom service model.\n\n```python\nimport asyncio\n\nimport aiomsa\nimport aiomsa.abc\nfrom onos_ric_sdk_py import E2Client, SDLClient\n\nfrom .models import MyModel\n\n\nasync def run(e2: aiomsa.abc.E2Client, e2_node_id: str) -> None:\n   subscription = await e2.subscribe(\n      e2_node_id,\n      service_model_name="my_model",\n      service_model_version="v1",\n      subscription_id="my_app-my_model-sub",\n      trigger=bytes(MyModel(param="foo")),\n      actions=[\n         aiomsa.abc.RICAction(\n            id=1,\n            type=aiomsa.abc.RICActionType.REPORT,\n            subsequent_action_type=aiomsa.abc.RICSubsequentActionType.CONTINUE,\n            time_to_wait=aiomsa.abc.RICTimeToWait.ZERO,\n         )\n      ],\n   )\n\n   async for (_header, message) in subscription:\n      print(message)\n\n\nasync def main() -> None:\n   async with E2Client(app_id="my_app", e2t_endpoint="e2t:5150") as e2, SDLClient(\n      topo_endpoint="topo:5150"\n   ) as sdl:\n      async for e2_node in sdl.watch_e2_connections():\n         asyncio.create_task(run(e2, e2_node.id))\n\n\nif __name__ == "__main__":\n   aiomsa.run(main())\n```\n',
    'author': 'Facebook Connectivity',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/facebookexternal/aiomsa',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
