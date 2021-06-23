# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['find_url']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'find-url',
    'version': '1.0.7',
    'description': 'С помощью этой библиотеки, вы сможете парсить информацию с сайта',
    'long_description': '<a href="https://discord.gg/TGD5nVX" rel="nofollow">\n\t<img alt="Discord server invite" src="https://i.ibb.co/GP8CDby/2021-06-23-114238.png">\n</a>\n<h1>О библиотеке</h1>\n<p>Пока что эта библиотека в разработке, вот что умеет эта библиотека:</p>\n<p>С помощью - import find_url вы импортируете библиотеку.</p>\n<p>Чтоб начать находить информацию, пишите find_url.url.find(url, f, f2).</p>\n<p>Сдесь url это ссылка которую надо парсить, f это на что начинается то, что вы хотите получить. f2 - На что заканчивается то, что вы хотите получить.</p>\n<p>Так же если вы получили готовый html код, используйте find_url.url.html(html, f, f2).</p>\n<p>Например, я хочу получить с сайта https://pypi.org/project/find-url/ название, то есть в html коде - <title>find-url · PyPI</title>.</p>\n<p>В этом случие То что мы хотим получить начинается на <title>, и заканчивается на </title>.</p>\n<p>То есть - find_url.url.find(\'https://pypi.org/project/find-url/\', \'<title>\', \'</title>\').</p>\n<p>Всё это выдаст "find-url · PyPI"</p>\n<h2>Пример кода</h2>\n\n<pre>\n\t<span class="c1">import find_url\n\t</span>find_url.url.find(\'https://pypi.org/project/find-url/\', \'<title>\', \'</title>\') # find-url · PyPI\n\t<span class="c1">import requests\n\t</span>html_text = requests.get(https://pypi.org/project/find-url/).text\n\tfind_url.url.html(html_text, \'<title>\', \'</title>\') # find-url · PyPI\n</pre>',
    'author': 'Sergey039',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
