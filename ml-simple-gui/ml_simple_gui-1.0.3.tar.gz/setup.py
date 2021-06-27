from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='ml_simple_gui',
    version='1.0.3',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    install_requires=[item.replace('\n', '') for item in open(join(dirname(__file__), 'requirements.txt')).readlines()],
    include_package_data=True,
)