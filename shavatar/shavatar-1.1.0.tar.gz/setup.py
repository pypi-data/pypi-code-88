# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shavatar']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.2.0,<9.0.0']

setup_kwargs = {
    'name': 'shavatar',
    'version': '1.1.0',
    'description': 'SHA-based avatar generation.',
    'long_description': '# SHAvatar\n\nSHA-based avatar generation.\n\n## Example Usage\n\n```py\nfrom shavatar import generate\n\n\nimage = generate("vcokltfre", size=1024)\nimage.save("vcokltfre.png")\n```\n',
    'author': 'vcokltfre',
    'author_email': 'vcokltfre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
