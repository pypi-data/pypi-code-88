# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['classyconf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'classyconf',
    'version': '0.5.2',
    'description': 'Extensible library for separation of settings from code.',
    'long_description': '# ClassyConf\n\n![PyPI](https://img.shields.io/pypi/v/classyconf?style=flat-square)\n![Run tests](https://github.com/hernantz/classyconf/workflows/Run%20tests/badge.svg?event=push)\n[![codecov](https://codecov.io/gh/hernantz/classyconf/branch/master/graph/badge.svg)](https://codecov.io/gh/hernantz/classyconf)\n\n\n![carbon](https://user-images.githubusercontent.com/613512/84096088-53f74c00-a9d7-11ea-9353-25d2910abc02.png)\n\n\n\n**ClassyConf is the configuration architecture solution for perfectionists with deadlines.**\n\nIt provides a declarative way to define settings for your projects contained\nin a class that can be extended, overriden at runtime, config objects can be\npassed around modules and settings are lazily loaded, plus some other\ngoodies.\n\nYou can find out more documentation at [Read the\nDocs](https://classyconf.readthedocs.io/en/latest/index.html) website, and\nthe [intro post](http://hernantz.github.io/configuration-is-an-api-not-an-sdk.html) here to understand the motivations behind it.\n\nHere is a preview of how to use it:\n\n```python\nfrom classyconf import Configuration, Value, Environment, IniFile, as_boolean, EnvPrefix\n\nclass AppConfig(Configuration):\n    """Configuration for My App"""\n    class Meta:\n        loaders = [\n            Environment(keyfmt=EnvPrefix("MY_APP_")),\n            IniFile("/etc/app/conf.ini", section="myapp")\n        ]\n\n    DEBUG = Value(default=False, cast=as_boolean, help="Toggle debugging mode.")\n    DATABASE_URL = Value(default="postgres://localhost:5432/mydb", help="Database connection.")\n```\n\nLater this object can be used to print settings\n\n```python\n>>> config = AppConfig()\n>>> print(config)\nDEBUG=True - Toggle debugging mode.\nDATABASE_URL=\'postgres://localhost:5432/mydb\' - Database connection.\n```\n\nor with `__repr__()`\n\n```python\n>>> config = AppConfig()\n>>> config\nAppConf(loaders=[Environment(keyfmt=EnvPrefix("MY_APP_"), EnvFile("main.env")])\n```\n\nextended\n\n```python\nclass TestConfig(AppConfig):\n    class Meta:\n        loaders = [IniFile("test_settings.ini"), EnvFile("main.env")]\n```\n\noverridden at runtime\n\n```python\n>>> dev_config = AppConfig(loaders=[IniFile("dev_settings.ini")])\n>>> dev_config.DEBUG\nTrue\n```\n\naccessed as dict or object\n\n```python\n>>> config.DEBUG\nFalse\n>>> config["DEBUG"]\nFalse\n```\n\niterated\n\n```python\n >>> for setting in config:\n...     print(setting)\n...\n(\'DEBUG\', Value(key="DEBUG", help="Toggle debugging on/off."))\n(\'DATABASE_URL\', Value(key="DATABASE_URL", help="Database connection."))\n```\n\nor passed around\n\n```python\ndef do_something(cfg):\n    if cfg.DEBUG:   # this is evaluated lazily\n         return\n```\n',
    'author': 'Hernan Lozano',
    'author_email': 'hernantz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hernantz/classyconf',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
