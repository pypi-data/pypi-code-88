# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['theconcierge',
 'theconcierge.listener',
 'theconcierge.main',
 'theconcierge.settings']

package_data = \
{'': ['*']}

install_requires = \
['Telethon>=1.21.1,<2.0.0']

setup_kwargs = {
    'name': 'theconcierge',
    'version': '0.0.3',
    'description': 'The Concierge allows you to create a simple project for the development of a ready-to-use Telegram Bot.',
    'long_description': '# The Concierge\n\nThe Concierge allows you to create a simple project for the development of a ready-to-use Telegram Bot.\n\nThe Concierge hides all the configuration part and allows you to use all your imagination in the business logic of the Telegram Bot.\n\nAll you have to do is put the handlers in the *handlers* folder and specify them in the *settings* file.\n\n## Requirements\n\nThe Concierge is based on the Telethon package. It is a very useful Python package that allows you to use a Telegram MTProto API.\n\nThe purpose of The Concierge is to create a simple and flexible template for rapid prototyping of a Telegram Bot based on Telethon package.\n\nBelow, a list of all required packages:\n\n* [Telethon](https://github.com/LonamiWebs/Telethon)\n\n    ```pip install telethon```\n\n* [TheConcierge](https://github.com/luigimalaguti/TheConcierge)\n\n    ```pip install theconcierge```\n\n## Quick-start\n\nBefore you start programming your bot, you need to get the Telegram App API Id and App API Hash. You can retrieve these data on the [official Telegram website](https://my.telegram.org) when you create an application. For more info see the following [link](https://core.telegram.org/api/obtaining_api_id).\n\nTo get the token needed for the bot, you can visit the official telegram website which explains how to use [BotFather](https://core.telegram.org/bots#6-botfather).\n\nThe structure of your project is as follows:\n\n```\n<PROJECT ROOT>\n    |\n    +-- handlers\n    |   +-- <SOME HANDLER>.py\n    +-- settings\n    |   +-- settings.json\n    +-- <MAIN>.py\n```\n\nIf you want, you can see [TheConciergeTemplate](https://github.com/luigimalaguti/TheConciergeTemplate) for a template to start with. Otherwise, you can run this command:\n\n```\npython -m theconcierge\n```\n\nThis command downloads the template seen above in the current folder of your OS. \n\nPerfect, now you can start programming your Bot.\n\n### Handlers\n\nThe *handlers* folder contains all the handlers that the bot needs to work.\n\nAn handler is a function that will execute when it occurs some events, example a *NewMessage*, *ChatAction* and other (the events is specified into *Telethon* package, see your [documentation](https://docs.telethon.dev/en/latest/) for more details).\n\nSimple handler look like this:\n\n```python\n@events.register(events.NewMessage(pattern="(?i)hi|hello"))\nasync def random_handler(event):\n    await event.respond("Hey!")\n```\n\nOne important note is that Telethon is based on *asyncio* package that allow you run Telegram Bot in async mode, then you must defined your handler function with ```async``` and use *event* methods with ```await```.  \nAll is explained on official Telethon documentation.\n\n### Settings\n\nThe *settings* folder is not request by Telethon, but by The Concierge.\n\nInside the *settings* folder there is the *settings.json* file which contains all the data necessary for The Concierge to register all the handlers automatically, simply by specifying the name of the module and the functions in question.\n\nAn example:\n\n```json\n...\n\n"handlers": {\n    "echo": [\n        "simple_echo_handler",\n        "complex_echo_handler"\n    ],\n    "welcome": [\n        "welcome_italian",\n        "walcome_english"\n    ]\n}\n\n...\n```\n\nNote: All handlers in the setting.json will load, if an handler isn\'t into settings.json, this handler won\'t load.\n\nIn settings.json there is also a field *system* where you can insert your **api_id**, **api_hash** and **bot_token**. The Concierge will load them automatically.\n\nFinally there is a *app* field into settings.json for all data app that you can needed.\n\n### Main\n\nThe *main* is the file where you can launch you bot.\n\n```python\nfrom theconcierge import TheConcierge\n\ndef main():\n    concierge = TheConcierge()\n    concierge.start_bot()\n\nmain()\n```\n\nThis is the bare minimum needed to launch your Telegram Bot based on Telethon and The Concierge.\n',
    'author': 'luigimalaguti',
    'author_email': 'malaguti.luigi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/luigimalaguti/TheConcierge',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
