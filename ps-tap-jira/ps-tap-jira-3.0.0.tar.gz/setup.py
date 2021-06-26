#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="ps-tap-jira",
      version="3.0.0",
      description="Singer.io tap for extracting data from the Jira API",
      author="Stitch",
      url="http://singer.io",
      download_url = 'https://github.com/saianil58/ps_tap_jira/archive/refs/tags/3.1.tar.gz', 
      classifiers=["Programming Language :: Python :: 3 :: Only"],
      install_requires=[
          "singer-python==5.9.0",
          "requests==2.20.0",
      ],
      extras_require={
          'dev': [
              'pylint',
              'nose',
              'ipdb'
          ]
      },
      entry_points="""
          [console_scripts]
          tap-jira=tap_jira:main
      """,
      packages=["tap_jira"],
      package_data = {
          "schemas": ["tap_jira/schemas/*.json"]
      },
      include_package_data=True,
)