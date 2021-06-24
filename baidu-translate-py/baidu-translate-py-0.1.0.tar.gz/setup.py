# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['baidu_translate_py']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8,<2', 'requests>=2.25,<3']

setup_kwargs = {
    'name': 'baidu-translate-py',
    'version': '0.1.0',
    'description': 'Python 翻译 API [当前支持:百度翻译、小牛翻译]',
    'long_description': '# Python 翻译 API\n\n* [百度翻译开放平台](https://fanyi-api.baidu.com/)\n* [小牛翻译](https://niutrans.com/)\n',
    'author': 'dev',
    'author_email': 'dev@qiyutech.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://oss.qiyutech.tech/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
