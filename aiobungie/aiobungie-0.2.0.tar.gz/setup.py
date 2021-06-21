# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiobungie', 'aiobungie.objects', 'aiobungie.utils']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['httpx>=0.18.1,<0.19.0']

setup_kwargs = {
    'name': 'aiobungie',
    'version': '0.2.0',
    'description': 'A small async api wrapper for the bungie api',
    'long_description': '## aiobungie\n\nAn Asynchronous API wrapper for the bungie API witten in Python.\n\n\n## Installing\n\n```\npip install aiobungie\n```\n\n## Quick Example\n\n```python\nimport aiobungie\n\n# Without classes.\n\nclient = aiobungie.Client(key=\'YOUR_API_KEY\')\n\nasync def player(name):\n    _player = await client.get_player(name)\n    print(_player.name)\n    print(_player.icon_path)\n    print(_player.id)\n    print(_player.type)\n\nclient.loop.run_until_complete(player("Sweatcicle"))\n\n# With classes\n\nclass PlayerTest(aiobungie.Client):\n    def __init__(self):\n        super().__init__(key=\'YOUR_API_KEY\')\n\n    async def player_data(self, player_name: str):\n        player = await self.get_player(player_name)\n\n        try:\n            print(player.name)\n            print(player.type)\n            print(player.id)\n            print(player.icon_path)\n        except:\n            pass\n\nif __name__ == \'__main__\':\n    plr = PlayerTest()\n    plr.loop.run_until_complete(plr.player_data("DeeJ"))\n```\n\n### Requirements\n* httpx\n',
    'author': 'nxtlo',
    'author_email': 'dhmony-99@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nxtlo/aiobungie',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
