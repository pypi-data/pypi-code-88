import os

from os.path import dirname
from setuptools import Command, find_packages, setup


current_dir = dirname(__file__)

try:
    with open(os.path.join(current_dir + 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''


INSTALL_REQUIREMENTS = [
    'Flask-SQLAlchemy==2.4.1',
    'SQLAlchemy==1.3.15',
    'SQLAlchemy-JSONField==0.9.0',
    'SQLAlchemy-Utils==0.36.3',
    'coverage==5.1',
    'boto3==1.14.28',
    'celery==4.4.2',
    'pypandoc',
    'pyspark==2.3.1',
    'psycopg2',
    'flake8',
]

version = '0.0.1'


def do_setup():
    setup(
        name='learn-python',
        version=version,
        description='This is learn python module',
        long_description=long_description,
        long_description_content_type='text/markdown',
        install_requires=INSTALL_REQUIREMENTS,
        packages=find_packages(
            include=["src*"]
        ),
        package_data={
            '': ['conf/*.cfg', 'conf/*.yml', 'conf/*.yaml']
        },
        include_package_data=True,
        author='Massipssa Kerrache',
        author_email='kerrache.massipssa@gmail.com',
        url='https://github.com/Massipssa/learn-python/',
        download_url=(
                'https://pypi.org/project/learn-python/' + version),
    )


if __name__ == '__main__':
    do_setup()
