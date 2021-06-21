# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['understory',
 'understory.indieweb',
 'understory.indieweb.indieauth',
 'understory.indieweb.indieauth.templates',
 'understory.indieweb.micropub',
 'understory.indieweb.micropub.templates',
 'understory.indieweb.microsub',
 'understory.indieweb.microsub.templates',
 'understory.indieweb.templates',
 'understory.indieweb.webmention',
 'understory.indieweb.websub']

package_data = \
{'': ['*'],
 'understory.indieweb.templates': ['cache/*', 'content/*'],
 'understory.indieweb.webmention': ['templates/*'],
 'understory.indieweb.websub': ['templates/*']}

install_requires = \
['understory-web>=0.0.20,<0.0.21']

entry_points = \
{'console_scripts': ['loveliness = understory.loveliness:main'],
 'web.apps': ['content = understory.indieweb:content',
              'indieauth-client = understory.indieweb.indieauth:client',
              'indieauth-server = understory.indieweb.indieauth:server',
              'micropub = understory.indieweb.micropub:server',
              'microsub = understory.indieweb.microsub:server',
              'webmention = understory.indieweb.webmention:receiver',
              'websub = understory.indieweb.websub:hub']}

setup_kwargs = {
    'name': 'understory',
    'version': '0.0.37',
    'description': 'The tools that power the canopy',
    'long_description': '# understory\nThe tools that power the canopy\n\n## Install\n\n    pip install understory\n\nand/or\n\n    npm install understory.js\n\n## Usage\n\n### A simple web application\n\nInstall [Python Poetry][0] and configure it.\n\nCreate a directory for your project and create a module `hello.py` inside:\n\n    from understory import web\n\n    app = web.application("HelloWorld")\n\n    @app.route(r"")\n    class SayHey:\n        def get(self):\n            return "What\'s up world?"\n\nFrom inside your project directory:\n\n    poetry init\n    poetry add understory\n    poetry run web install hello:app hello_app\n    poetry run web serve hello_app\n    poetry version prerelease\n    poetry build\n    poetry publish\n\nHost using [Ghost][1].\n\n#### Add support for the IndieWeb\n\nIndieAuth client/server, Micropub client/server, Microsub, WebSub, Webmention\n\n    from understory import indieweb\n\n    app.mount(indieweb.indieauth.server)\n    app.mount(indieweb.micropub.server)\n    app.mount(indieweb.content)\n\n[0]: https://python-poetry.org\n[1]: https://gh.ost.lol\n',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@lahacker.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
