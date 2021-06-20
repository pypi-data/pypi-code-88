#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['cambridge']

package_data = \
{'': ['*']}

install_requires = \
['requests', 'beautifulsoup4', 'rich']

extras_require = \
{'publish': ['flit']}

entry_points = \
{'console_scripts': ['camb = cambridge.cambridge:main']}

setup(name='cambridge',
      version='0.0.11',
      description='Cambridge is a terminal version of Cambridge Dictionary. Its dictionary data comes from https://dictionary.cambridge.org.',
      author='Kate Wang',
      author_email='kate.wang2018@gmail.com',
      url='https://github.com/KateWang2016/cambridge',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points=entry_points,
     )
