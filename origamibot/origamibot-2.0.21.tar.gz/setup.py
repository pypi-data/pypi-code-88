# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['origamibot',
 'origamibot.core',
 'origamibot.core.teletypes',
 'origamibot.core.teletypes.base',
 'origamibot.core.teletypes.inline_query_result']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'origamibot',
    'version': '2.0.21',
    'description': 'Library for creating bots for telegram with Python.',
    'long_description': "\n\n\n\n![](https://media.githubusercontent.com/media/cmd410/OrigamiBot/master/imgs/logo.png)\n\nLibrary for creating bots for telegram with [Python](https://www.python.org/). \n\n**OrigamiBot** aims to make development of Telegram bots as easy and flexible as possible.\n\n![Upload Python Package](https://github.com/cmd410/OrigamiBot/workflows/Upload%20Python%20Package/badge.svg)\n\n## Installation\n\nOrigamibot is published in [PyPI](https://pypi.org/project/origamibot/), so it can be installed with one simple command:\n\n```\npip install origamibot\n```\n\n## Basic concepts\n\n**OrigamiBot** class is thing that will get updates form the server and dispatch them to your **command holders** and **event listeners**.\n\n- **Command Holder** is a custom class that you create that exposes its methods as commands for bot\n  command holder can be attached to bot using `bot.add_commands(your_command_holder_class())`\n- **Event listener** is a class that inherits from `origamibot.util.Listener` and performs some actions on certain events(when its `on_<something>` methods are called from **OrigamiBot**). Event listener can be added to bot with `bot.add_listener(your_listener_object)` \n\n## Usage example\n\nHere goes a simple example of a bot:\n\n```python\nfrom sys import argv\nfrom time import sleep\n\nfrom origamibot import OrigamiBot as Bot\nfrom origamibot.listener import Listener\n\n\nclass BotsCommands:\n    def __init__(self, bot: Bot):  # Can initialize however you like\n        self.bot = bot\n\n    def start(self, message):   # /start command\n        self.bot.send_message(\n            message.chat.id,\n            'Hello user!\\nThis is an example bot.')\n\n    def echo(self, message, value: str):  # /echo [value: str] command\n        self.bot.send_message(\n            message.chat.id,\n            value\n            )\n\n    def add(self, message, a: float, b: float):  # /add [a: float] [b: float]\n        self.bot.send_message(\n            message.chat.id,\n            str(a + b)\n            )\n\n    def _not_a_command(self):   # This method not considered a command\n        print('I am not a command')\n\n\nclass MessageListener(Listener):  # Event listener must inherit Listener\n    def __init__(self, bot):\n        self.bot = bot\n        self.m_count = 0\n\n    def on_message(self, message):   # called on every message\n        self.m_count += 1\n        print(f'Total messages: {self.m_count}')\n\n    def on_command_failure(self, message, err=None):  # When command fails\n        if err is None:\n            self.bot.send_message(message.chat.id,\n                                  'Command failed to bind arguments!')\n        else:\n            self.bot.send_message(message.chat.id,\n                                  'Error in command:\\n{err}')\n\n\nif __name__ == '__main__':\n    token = (argv[1] if len(argv) > 1 else input('Enter bot token: '))\n    bot = Bot(token)   # Create instance of OrigamiBot class\n\n    # Add an event listener\n    bot.add_listener(MessageListener(bot))\n\n    # Add a command holder\n    bot.add_commands(BotsCommands(bot))\n\n    # We can add as many command holders\n    # and event listeners as we like\n\n    bot.start()   # start bot's threads\n    while True:\n        sleep(1)\n        # Can also do some useful work i main thread\n        # Like autoposting to channels for example\n```\n\nCommands are added as methods of an object(be it class or instance of it), if their names don't start with `_` which makes it possible to also contain some utility functions inside command container. \n\nFor the command to be called two conditions must be met:\n\n1. command name must match with method name\n2. command's arguments must match signature of a method\n\nMethod signature supports any number of arguments with simple typing(`str`, `int`, `float`, `bool`) or without a typing(in this case all arguments are strings by default), as well as variable number of arguments `*args`. More complex types(as lists, tuples, custom object classes) are not supported, as bot does not know how to parse them, and I don't want to enforce my own parsing algorithm, but bot will still attempt to convert it like `cls(argument)`, but a correct result is not guaranteed.\n\n> **Boolean** values are considered True if their string representation is in `{'True', 'true', '1'}`, and False if in `{'False', 'false', '0'}`\n\n",
    'author': 'Crystal Melting Dot',
    'author_email': 'stresspassing@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cmd410/OrigamiBot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
