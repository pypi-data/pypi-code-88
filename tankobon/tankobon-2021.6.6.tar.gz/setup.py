#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['tankobon', 'tankobon.gui', 'tankobon.iso639', 'tankobon.sources']

package_data = \
{'': ['*'],
 'tankobon': ['.mypy_cache/*',
              '.mypy_cache/3.9/*',
              '.mypy_cache/3.9/PySide6/*',
              '.mypy_cache/3.9/_typeshed/*',
              '.mypy_cache/3.9/click/*',
              '.mypy_cache/3.9/collections/*',
              '.mypy_cache/3.9/concurrent/*',
              '.mypy_cache/3.9/concurrent/futures/*',
              '.mypy_cache/3.9/ctypes/*',
              '.mypy_cache/3.9/distutils/*',
              '.mypy_cache/3.9/email/*',
              '.mypy_cache/3.9/http/*',
              '.mypy_cache/3.9/importlib/*',
              '.mypy_cache/3.9/json/*',
              '.mypy_cache/3.9/logging/*',
              '.mypy_cache/3.9/multiprocessing/*',
              '.mypy_cache/3.9/os/*',
              '.mypy_cache/3.9/requests/*',
              '.mypy_cache/3.9/requests/packages/*',
              '.mypy_cache/3.9/requests/packages/urllib3/*',
              '.mypy_cache/3.9/requests/packages/urllib3/packages/*',
              '.mypy_cache/3.9/requests/packages/urllib3/packages/ssl_match_hostname/*',
              '.mypy_cache/3.9/requests/packages/urllib3/util/*',
              '.mypy_cache/3.9/tankobon/*',
              '.mypy_cache/3.9/tankobon/gui/*',
              '.mypy_cache/3.9/tankobon/iso639/*',
              '.mypy_cache/3.9/tankobon/parsers/*',
              '.mypy_cache/3.9/tankobon/sources/*',
              '.mypy_cache/3.9/urllib/*'],
 'tankobon.gui': ['.mypy_cache/*',
                  '.mypy_cache/3.9/*',
                  '.mypy_cache/3.9/PySide6/*',
                  '.mypy_cache/3.9/_typeshed/*',
                  '.mypy_cache/3.9/click/*',
                  '.mypy_cache/3.9/collections/*',
                  '.mypy_cache/3.9/concurrent/*',
                  '.mypy_cache/3.9/concurrent/futures/*',
                  '.mypy_cache/3.9/ctypes/*',
                  '.mypy_cache/3.9/email/*',
                  '.mypy_cache/3.9/http/*',
                  '.mypy_cache/3.9/importlib/*',
                  '.mypy_cache/3.9/json/*',
                  '.mypy_cache/3.9/logging/*',
                  '.mypy_cache/3.9/multiprocessing/*',
                  '.mypy_cache/3.9/os/*',
                  '.mypy_cache/3.9/requests/*',
                  '.mypy_cache/3.9/requests/packages/*',
                  '.mypy_cache/3.9/requests/packages/urllib3/*',
                  '.mypy_cache/3.9/requests/packages/urllib3/packages/*',
                  '.mypy_cache/3.9/requests/packages/urllib3/packages/ssl_match_hostname/*',
                  '.mypy_cache/3.9/requests/packages/urllib3/util/*',
                  '.mypy_cache/3.9/tankobon/*',
                  '.mypy_cache/3.9/tankobon/gui/*',
                  '.mypy_cache/3.9/tankobon/iso639/*',
                  '.mypy_cache/3.9/tankobon/parsers/*',
                  '.mypy_cache/3.9/tankobon/sources/*',
                  '.mypy_cache/3.9/tankobon/tankobon/*',
                  '.mypy_cache/3.9/tankobon/tankobon/gui/*',
                  '.mypy_cache/3.9/urllib/*'],
 'tankobon.iso639': ['.mypy_cache/*',
                     '.mypy_cache/3.9/*',
                     '.mypy_cache/3.9/_typeshed/*',
                     '.mypy_cache/3.9/collections/*',
                     '.mypy_cache/3.9/concurrent/*',
                     '.mypy_cache/3.9/concurrent/futures/*',
                     '.mypy_cache/3.9/ctypes/*',
                     '.mypy_cache/3.9/email/*',
                     '.mypy_cache/3.9/http/*',
                     '.mypy_cache/3.9/importlib/*',
                     '.mypy_cache/3.9/json/*',
                     '.mypy_cache/3.9/logging/*',
                     '.mypy_cache/3.9/multiprocessing/*',
                     '.mypy_cache/3.9/os/*',
                     '.mypy_cache/3.9/requests/*',
                     '.mypy_cache/3.9/requests/packages/*',
                     '.mypy_cache/3.9/requests/packages/urllib3/*',
                     '.mypy_cache/3.9/requests/packages/urllib3/packages/*',
                     '.mypy_cache/3.9/requests/packages/urllib3/packages/ssl_match_hostname/*',
                     '.mypy_cache/3.9/requests/packages/urllib3/util/*',
                     '.mypy_cache/3.9/tankobon/*',
                     '.mypy_cache/3.9/tankobon/iso639/*',
                     '.mypy_cache/3.9/tankobon/sources/*',
                     '.mypy_cache/3.9/urllib/*'],
 'tankobon.sources': ['.mypy_cache/*',
                      '.mypy_cache/3.9/*',
                      '.mypy_cache/3.9/PySide6/*',
                      '.mypy_cache/3.9/_typeshed/*',
                      '.mypy_cache/3.9/collections/*',
                      '.mypy_cache/3.9/concurrent/*',
                      '.mypy_cache/3.9/concurrent/futures/*',
                      '.mypy_cache/3.9/ctypes/*',
                      '.mypy_cache/3.9/email/*',
                      '.mypy_cache/3.9/http/*',
                      '.mypy_cache/3.9/importlib/*',
                      '.mypy_cache/3.9/json/*',
                      '.mypy_cache/3.9/logging/*',
                      '.mypy_cache/3.9/multiprocessing/*',
                      '.mypy_cache/3.9/os/*',
                      '.mypy_cache/3.9/requests/*',
                      '.mypy_cache/3.9/requests/packages/*',
                      '.mypy_cache/3.9/requests/packages/urllib3/*',
                      '.mypy_cache/3.9/requests/packages/urllib3/packages/*',
                      '.mypy_cache/3.9/requests/packages/urllib3/packages/ssl_match_hostname/*',
                      '.mypy_cache/3.9/requests/packages/urllib3/util/*',
                      '.mypy_cache/3.9/tankobon/*',
                      '.mypy_cache/3.9/tankobon/parsers/*',
                      '.mypy_cache/3.9/tankobon/sources/*',
                      '.mypy_cache/3.9/tankobon/tankobon/*',
                      '.mypy_cache/3.9/tankobon/tankobon/sources/*',
                      '.mypy_cache/3.9/urllib/*']}

install_requires = \
['bbcode>=1.1.0',
 'beautifulsoup4>=4.9.1',
 'click>=7.1.2',
 'coloredlogs>=14.0',
 'fake-useragent>=0.1.11',
 'filetype>=1.0.7',
 'fpdf>=1.7.2',
 'html5lib>=1.1',
 'imagesize>=1.2.0',
 'MangaDex.py>=2.0.3',
 'natsort>=7.1.0',
 'requests>=2.24.0']

extras_require = \
{'dev': ['pytest', 'pytest-flake8', 'pytest-mypy', 'pydoc-markdown>=3.10.1'],
 'gui': ['PySide6>=6.0.3']}

entry_points = \
{'console_scripts': ['tankobon = tankobon.cli:main']}

setup(name='tankobon',
      version='2021.6.6',
      description='Yet another manga scraper and downloader',
      author='Ong Yong Xin',
      author_email='ongyongxin2020+github@gmail.com',
      url='https://github.com/ongyx/tankobon',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points=entry_points,
      python_requires='>=3.6',
     )
