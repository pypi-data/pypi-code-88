import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='changeplan',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    author='Julio Miranda',
    author_email='dorlin_123@hotmail.com',
)