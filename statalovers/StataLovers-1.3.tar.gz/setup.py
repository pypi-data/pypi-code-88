from setuptools import setup

# read the contents of your README file
import os
from os import path
this_directory = os.getcwd()
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='StataLovers',
      version ='1.3',
      description = 'Stata-like functions tab and summarize',
      packages =['StataLovers'],
      author='Mila Kolpashnikova',
      author_email='kamilakolpashnikova@gmail.com',
	  long_description=long_description,
	  long_description_content_type='text/markdown',
      zip_safe=False)