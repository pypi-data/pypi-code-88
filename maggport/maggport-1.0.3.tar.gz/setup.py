"""
maggport setup file
"""
from os import path
from setuptools import find_packages, setup

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Only install package dependencies in install_requires
setup(
    name='maggport',
    version='1.0.3',
    description='A mongodb aggregate export tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={'console_scripts': ['maggport = maggport.maggport:maggport']},
    url='https://github.com/ccavales3/maggport',
    author='Caesar Cavales',
    author_email='c.cavales3@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'click==8.0.1',  # https://github.com/pallets/click
        'pymongo==3.11.4',  # https://github.com/mongodb/mongo-python-driver
        'pandas==1.2.1',  # https://github.com/pandas-dev/pandas
    ],
    zip_safe=False,
)
