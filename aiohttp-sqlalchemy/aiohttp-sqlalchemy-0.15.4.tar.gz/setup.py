# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohttp_sqlalchemy']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.18,<2.0.0', 'aiohttp>=3.7.4.post0,<4.0.0']

extras_require = \
{'mysql': ['aiomysql>=0.0.21'],
 'postgresql': ['asyncpg>=0.23.0,<0.24.0'],
 'sqlite': ['aiosqlite>=0.17.0,<0.18.0']}

setup_kwargs = {
    'name': 'aiohttp-sqlalchemy',
    'version': '0.15.4',
    'description': 'SQLAlchemy 1.4 / 2.0 support for aiohttp.',
    'long_description': "==================\naiohttp-sqlalchemy\n==================\n|Release| |Python versions| |Downloads count| |Build status| |Test coverage| |Documantation|\n\n.. |Release| image:: https://badge.fury.io/py/aiohttp-sqlalchemy.svg\n  :target: https://pypi.org/project/aiohttp-sqlalchemy/\n  :alt: Release\n\n.. |Python versions| image:: https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue\n  :target: https://pypi.org/project/aiohttp-sqlalchemy/\n  :alt: Python versions\n\n.. |Downloads count| image:: https://img.shields.io/pypi/dm/aiohttp-sqlalchemy\n  :target: https://pypistats.org/packages/aiohttp-sqlalchemy\n  :alt: Downloads count\n\n.. |Build status| image:: https://travis-ci.com/ri-gilfanov/aiohttp-sqlalchemy.svg?branch=master\n  :target: https://travis-ci.com/ri-gilfanov/aiohttp-sqlalchemy\n  :alt: Build status\n\n.. |Test coverage| image:: https://coveralls.io/repos/github/ri-gilfanov/aiohttp-sqlalchemy/badge.svg?branch=master\n  :target: https://coveralls.io/github/ri-gilfanov/aiohttp-sqlalchemy?branch=master\n  :alt: Test coverage\n\n.. |Documantation| image:: https://readthedocs.org/projects/aiohttp-sqlalchemy/badge/?version=latest\n  :target: https://aiohttp-sqlalchemy.readthedocs.io/en/latest/?badge=latest\n  :alt: Documentation\n\n`SQLAlchemy 1.4 / 2.0 <https://www.sqlalchemy.org/>`_ support for `AIOHTTP\n<https://docs.aiohttp.org/>`_.\n\nThe library provides the next features:\n\n* initializing asynchronous sessions through a middlewares;\n* initializing asynchronous sessions through a decorators;\n* simple access to one asynchronous session by default key;\n* preventing attributes from being expired after commit by default;\n* support different types of request handlers;\n* support nested applications.\n\n\nDocumentation\n-------------\nhttps://aiohttp-sqlalchemy.readthedocs.io\n\n\nInstallation\n------------\n::\n\n    pip install aiohttp-sqlalchemy\n\n\nSimple example\n--------------\nInstall ``aiosqlite`` for work with sqlite3: ::\n\n  pip install aiosqlite\n\nCopy and paste this code in a file and run:\n\n.. code-block:: python\n\n  from aiohttp import web\n  import aiohttp_sqlalchemy\n  from aiohttp_sqlalchemy import sa_session\n  from datetime import datetime\n  import sqlalchemy as sa\n  from sqlalchemy import orm\n\n\n  metadata = sa.MetaData()\n  Base = orm.declarative_base(metadata=metadata)\n\n\n  class MyModel(Base):\n      __tablename__ = 'my_table'\n\n      pk = sa.Column(sa.Integer, primary_key=True)\n      timestamp = sa.Column(sa.DateTime(), default=datetime.now)\n\n\n  async def main(request):\n      db_session = sa_session(request)\n\n      async with db_session.begin():\n          db_session.add_all([MyModel()])\n          stmt = sa.select(MyModel)\n          result = await db_session.execute(stmt)\n          items = result.scalars()\n\n      data = {}\n      for item in items:\n          data[item.pk] = item.timestamp.isoformat()\n\n      return web.json_response(data)\n\n\n  async def app_factory():\n      app = web.Application()\n\n      aiohttp_sqlalchemy.setup(app, [\n          aiohttp_sqlalchemy.bind('sqlite+aiosqlite:///'),\n      ])\n      await aiohttp_sqlalchemy.init_db(app, metadata)\n\n      app.add_routes([web.get('/', main)])\n\n      return app\n\n  if __name__ == '__main__':\n      web.run_app(app_factory())\n\n",
    'author': 'Ruslan Ilyasovich Gilfanov',
    'author_email': 'ri.gilfanov@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ri-gilfanov/aiohttp-sqlalchemy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
