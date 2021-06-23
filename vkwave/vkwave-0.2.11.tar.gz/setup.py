# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vkwave',
 'vkwave.api',
 'vkwave.api.methods',
 'vkwave.api.token',
 'vkwave.api.utils',
 'vkwave.bots',
 'vkwave.bots.addons',
 'vkwave.bots.addons.cache',
 'vkwave.bots.addons.easy',
 'vkwave.bots.core',
 'vkwave.bots.core.dispatching',
 'vkwave.bots.core.dispatching.cast',
 'vkwave.bots.core.dispatching.dp',
 'vkwave.bots.core.dispatching.dp.middleware',
 'vkwave.bots.core.dispatching.events',
 'vkwave.bots.core.dispatching.extensions',
 'vkwave.bots.core.dispatching.extensions.callback',
 'vkwave.bots.core.dispatching.filters',
 'vkwave.bots.core.dispatching.handler',
 'vkwave.bots.core.dispatching.router',
 'vkwave.bots.core.tokens',
 'vkwave.bots.core.types',
 'vkwave.bots.fsm',
 'vkwave.bots.storage',
 'vkwave.bots.storage.storages',
 'vkwave.bots.utils',
 'vkwave.bots.utils.keyboards',
 'vkwave.bots.utils.uploaders',
 'vkwave.client',
 'vkwave.http',
 'vkwave.longpoll',
 'vkwave.streaming',
 'vkwave.types',
 'vkwave.vkscript',
 'vkwave.vkscript.handlers']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6,<4.0', 'pydantic>=1.7,<2.0', 'typing_extensions>=3.7.4,<4.0.0']

extras_require = \
{'all': ['aioredis>=1.3,<2.0'], 'storage-redis': ['aioredis>=1.3,<2.0']}

setup_kwargs = {
    'name': 'vkwave',
    'version': '0.2.11',
    'description': "Framework for building high-performance & easy to scale projects interacting with VK's API.",
    'long_description': '![vkwave](https://user-images.githubusercontent.com/28061158/75329873-7f738200-5891-11ea-9565-fd117ea4fc9e.jpg)\n\n> Уважаем все остальные библиотеки. VKWave здесь.\n\n# VkWave\n\nVKWave - это фреймворк для создания производительных и лёгких в расширении проектов, взаимодействующих с API ВКонтакте.\n\nVKWave вдохновлен многими библиотеками, в частности: [aiogram](https://github.com/aiogram/aiogram), vk.py и многими другими.\n\n**Текущий мейнтейнер** проекта: [@kesha1225](https://github.com/kesha1225)\n\n[Документация](https://fscdev.github.io/vkwave/)\n\n[Примеры использования](https://github.com/fscdev/vkwave/tree/master/examples)\n\n# Почему VKWave?\n\n- Максимальная кастомизация\n- Полная асинхронность\n- Использование аннотаций типов\n\n# Установка\n\nС GitHub, со всеми свежими обновлениями:\n```\npip install https://github.com/fscdev/vkwave/archive/master.zip\n```\n\nИли с PyPI (не рекомендуется, давно не обновлялась):\n\n```\npip install vkwave\n```\n\n# Производительность\n\nVKWave - это не самая быстрая библиотека, из-за нашей уверенности в том, что лёгкая настройка под себя, а также удобство при использовании во всех задачах являются более важными характеристиками библиотеки, чем скорость.\n\nНо мы всегда заинтересованы в улучшении производительности, поэтому не стесняйтесь делать Pull Request-ы и обсуждать проблемы производительности.\n\n# Сообщество\n\nVKWave - это очень молодой проект.\n\n[Простая библиотека для быстрого доступа к API](https://github.com/prostomarkeloff/vkwave-api)\n\n[Телеграм чат](https://t.me/vkwave)\n\n[Учебники для лёгкого старта](https://github.com/VodoGamer/vkwave-textbooks/tree/master/textbooks)\n\n## Дополнения\n\nЕсли вы хотите создать дополнение для VKWave (например, более простой способ написания ботов, даже проще `vkwave.bots.addons.easy`), то вам следует назвать свой проект так: `vkwave-bots-really-easy`.\n\nОбщий паттерн для дополнений: `vkwave-<часть-vkwave>-<название-проекта>`.\n\n',
    'author': 'prostomarkeloff',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fscdev/vkwave',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
