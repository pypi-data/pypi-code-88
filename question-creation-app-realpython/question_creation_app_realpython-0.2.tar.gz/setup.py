from setuptools import setup, find_packages
import os
setup(
  name = 'question_creation_app_realpython',         # How you named your package folder (MyLib)
  packages = ['question_creation_app_realpython'], 
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Question creator',   # Give a short description about your library
  author = 'Vishnu Prasad',                   # Type in your name
  author_email = 'vishnuprasadkv55@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/vishnuprasadkv55/question-creator-distributable-pip',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/vishnuprasadkv55/question-creator-distributable-pip/archive/0.2.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  entry_points={"console_scripts": ["realpython=reader.__main__:main"]},
  include_package_data=True,
  install_requires=[            # I get to this in a second
      'altgraph',
      'boto3',
      'botocore',
      'certifi',
      'chardet',
      'click',
      'Flask',
      'Flask-Cors',
      'Flask-SQLAlchemy',
      'future',
      'idna',
      'itsdangerous',
      'Jinja2',
      'jmespath',
      'MarkupSafe',
      'numpy',
      'pandas',
      'pefile',
      'python-dateutil',
      'pytz',
      'pywin32-ctypes',
      'requests',
      's3transfer',
      'six',
      'SQLAlchemy',
      'urllib3',
      'Werkzeug'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)