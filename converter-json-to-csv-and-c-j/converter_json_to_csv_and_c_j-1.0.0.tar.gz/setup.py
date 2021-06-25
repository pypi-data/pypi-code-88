# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['converter_json_to_csv_and_c_j']
setup_kwargs = {
    'name': 'converter-json-to-csv-and-c-j',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'Mimikrim',
    'author_email': 'andreyblokhin010@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
