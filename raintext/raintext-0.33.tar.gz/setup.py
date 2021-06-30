from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
long_description = """
Raintext is a python package used for rainbow text!
Look at https://github.com/coolkidmacho/raintext for instructions!
This project will be updated frequently and all updates will be uploaded here but shown there.
"""
setup(
  name = 'raintext',         # How you named your package folder (MyLib)
  packages = ['raintext'],   # Chose the same as "name"
  version = '0.33',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package for rainbow text',   # Give a short description about your library
  author = 'Coolkidmacho',                   # Type in your name
  url = 'https://github.com/coolkidmacho/raintext',   # Provide either the link to your github or to your website
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'colorama',
          'itertools',
      ],
  long_description=long_description,
    long_description_content_type='text/markdown',
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