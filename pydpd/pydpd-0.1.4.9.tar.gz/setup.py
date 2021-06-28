from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pydpd',
    version='0.1.4.9',
    packages=['pydpd'],
    url='https://github.com/lewis-morris/pydpd',
    license='MIT',
    author='Lewis Morris',
    author_email='lewis.morris@gmail.com',
    description='DPD API Wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
