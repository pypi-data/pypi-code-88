# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['statcord']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0', 'discord.py>=1.7.1,<2.0.0', 'psutil>=5.8.0,<6.0.0']

setup_kwargs = {
    'name': 'betterstatcord.py',
    'version': '1.5.2',
    'description': 'A better Statcord API library for Python + Discord.py',
    'long_description': "# BetterStatcord.py\nA better Statcord API library for Python + Discord.py\n\n## Advantages\n- **It's blazin fast**: The official library is full of inefficient, slow, and unnecessary code which does nothing **except slow your bot down**.\n- **Cleaner and smaller codebase**: BetterStatcord.py is smaller and cleaner, making it much more reliable and understandable.\n- **Easier to use**: For its basic functionality, all you need is **one** line of code to set it up!\n- **More accurate**: This library has more accurate statistics than the official one.\n\n## Examples\n- Check out the [examples folder](https://github.com/Iapetus-11/betterstatcord.py/tree/main/examples)\n",
    'author': 'Milo Weinberg',
    'author_email': 'iapetus011@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Iapetus-11/betterstatcord.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
