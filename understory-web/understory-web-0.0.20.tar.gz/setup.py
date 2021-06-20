# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['understory',
 'understory.mkdn',
 'understory.mm',
 'understory.uri',
 'understory.web',
 'understory.web.framework',
 'understory.web.framework.templates',
 'understory.web.headers',
 'understory.web.response']

package_data = \
{'': ['*'],
 'understory.web.framework': ['static/braid.js',
                              'static/braid.js',
                              'static/braid.js',
                              'static/braid.js',
                              'static/orchid.js',
                              'static/orchid.js',
                              'static/orchid.js',
                              'static/orchid.js',
                              'static/roots.js',
                              'static/roots.js',
                              'static/roots.js',
                              'static/roots.js',
                              'static/solarized.css',
                              'static/solarized.css',
                              'static/solarized.css',
                              'static/solarized.css']}

install_requires = \
['Pillow>=8.2.0,<9.0.0',
 'PyVirtualDisplay>=2.1,<3.0',
 'Unidecode>=1.2.0,<2.0.0',
 'acme-tiny>=4.1.0,<5.0.0',
 'cssselect>=1.1.0,<2.0.0',
 'dnspython>=2.1.0,<3.0.0',
 'feedparser>=6.0.2,<7.0.0',
 'gevent>=21.1.2,<22.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'hstspreload>=2020.12.22,<2021.0.0',
 'httpagentparser>=1.9.1,<2.0.0',
 'jsonpatch>=1.32,<2.0',
 'lxml>=4.6.3,<5.0.0',
 'mf2py>=1.1.2,<2.0.0',
 'mf2util>=0.5.1,<0.6.0',
 'mimeparse>=0.1.3,<0.2.0',
 'networkx>=2.5.1,<3.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'pycryptodome>=3.10.1,<4.0.0',
 'pyscreenshot>=3.0,<4.0',
 'regex>=2021.4.4,<2022.0.0',
 'requests>=2.25.1,<3.0.0',
 'scrypt>=0.8.18,<0.9.0',
 'selenium>=3.141.0,<4.0.0',
 'understory-code>=0.0.44,<0.0.45',
 'understory-db>=0.0.8,<0.0.9',
 'understory-fx>=0.0.5,<0.0.6',
 'understory-term>=0.0.6,<0.0.7',
 'vobject>=0.9.6,<0.10.0',
 'watchdog>=2.1.2,<3.0.0']

entry_points = \
{'console_scripts': ['web = understory.web.__main__:main']}

setup_kwargs = {
    'name': 'understory-web',
    'version': '0.0.20',
    'description': 'Tools for metamodern web development',
    'long_description': '# understory-web\nTools for metamodern web development\n',
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
