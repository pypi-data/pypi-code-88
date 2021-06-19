# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiogram_forms']

package_data = \
{'': ['*']}

install_requires = \
['aiogram>=2.13,<3.0']

setup_kwargs = {
    'name': 'aiogram-forms',
    'version': '0.1.1',
    'description': 'Forms for aiogram',
    'long_description': "# aiogram-forms\n\n## Introduction\n`aiogram-forms` is an addition for `aiogram` which allows you to create different forms and process user input step by step easily.\n\n## Installation\n```bash\npip install aiogram-forms\n```\n\n## Usage\nCreate form you need by subclassing `aiogram_forms.forms.Form`. Fields can be added with `aiogram_forms.fields.Field` \n```python\nfrom aiogram_forms import forms, fields\nfrom aiogram.types import ReplyKeyboardMarkup, KeyboardButton\n\n\nclass UserForm(forms.Form):\n    LANGUAGE_CHOICES = ('English', 'Russian', 'Chinese')\n    LANGUAGE_KEYBOARD = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*[\n        KeyboardButton(label) for label in LANGUAGE_CHOICES\n    ])\n\n    name = fields.StringField('Name')\n    language = fields.ChoicesField('Language', LANGUAGE_CHOICES, reply_keyboard=LANGUAGE_KEYBOARD)\n    email = fields.EmailField('Email')\n```\n\n## Code of Conduct\n\n## History\nAll notable changes to this project will be documented in [CHANGELOG](CHANGELOG.md) file.\n",
    'author': 'Ivan Borisenko',
    'author_email': 'i.13g10n@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/13g10n/aiogram-forms',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
