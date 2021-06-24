# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starsessions']

package_data = \
{'': ['*']}

install_requires = \
['itsdangerous>=2.0.1,<3.0.0', 'starlette>=0.15.0,<0.16.0']

setup_kwargs = {
    'name': 'starsessions',
    'version': '1.0.1',
    'description': 'Pluggable session support for Starlette.',
    'long_description': '## Pluggable session support for Starlette and FastAPI frameworks\n\nThis package based on this long standing [pull request](https://github.com/encode/starlette/pull/499) into the mainstream by the same author.\n\n## Installation\n\nInstall `starsessions` using PIP or poetry:\n\n```bash\npip install starsessions\n# or\npoetry add starsessions\n```\n\n## Quick start\n\nSee example application in `example/` directory of this repository.\n\n## Enable session support\n\nIn order to enable session support add `starsessions.SessionMiddleware` to your application.\n\n```python\nfrom starlette.applications import Starlette\nfrom starlette.middleware import Middleware\nfrom starsessions import SessionMiddleware\n\nmiddleware = [\n    Middleware(SessionMiddleware, secret_key=\'TOP SECRET\'),\n]\n\napp = Starlette(middleware=middleware, **other_options)\n```\n\n### Session autoloading\n\nNote, for performance reasons session won\'t be autoloaded by default,\nyou need to explicitly call `await request.session.load()` before accessing the session otherwise `SessionNotLoaded` exception will be raised.\nYou can change this behavior by passing `autoload=True` to your middleware settings:\n\n```python\nMiddleware(SessionMiddleware, secret_key=\'TOP SECRET\', autoload=True)\n```\n\n### Default session backend\n\nThe default backend is `CookieBackend`.\nYou don\'t need to configure it just pass `secret_key` argument and the backend will be automatically configured for you.\n\n## Change default backend\n\nWhen you want to use a custom session storage then pass a desired backend instance via `backend` argument of the middleware.\n\n```python\nfrom starlette.applications import Starlette\nfrom starlette.middleware.sessions import SessionMiddleware\nfrom starlette.sessions import CookieBackend\n\nbackend = CookieBackend(secret_key=\'secret\', max_age=3600)\n\napp = Starlette()\napp.add_middleware(SessionMiddleware, backend=backend)\n```\n\n## Built-in backends\n\n### InMemoryBackend\n\nSimply stores data in memory. The data is not persisted across requests.\nMostly for use with unit tests.\n\n### CookieBackend\n\nStores session data in a signed cookie on the client.\nThis is the default backend.\n\n## Custom backend\n\nCreate a class which implements the `starsessions.SessionBackend` interface:\n\n```python\nfrom starlette.sessions import SessionBackend\nfrom typing import Dict\n\n# instance of class which manages session persistence\n\nclass InMemoryBackend(SessionBackend):\n    def __init__(self):\n        self._storage = {}\n\n    async def read(self, session_id: str) -> Dict:\n        """ Read session data from a data source using session_id. """\n        return self._storage.get(session_id, {})\n\n    async def write(self, data: Dict, session_id: str=None) -> str:\n        """ Write session data into data source and return session id. """\n        session_id = session_id or await self.generate_id()\n        self._storage[session_id] = data\n        return session_id\n\n    async def remove(self, session_id: str):\n        """ Remove session data. """\n        del self._storage[session_id]\n\n    async def exists(self, session_id: str)-> bool:\n        return session_id in self._storage\n```\n\nNote, `write` has to return the session id.\n',
    'author': 'alex.oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/alex-oleshkevich/starsessions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
