from os.path import join, isfile
from os import walk
import io
import os
from setuptools import find_packages, setup


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

NAME = 'giting'
FOLDER = 'giting'
DESCRIPTION = 'An awesome easy to use git tool written in python, enjoy ~'
URL = 'https://github.com/szj2ys/giting'
EMAIL = 'szj2ys@qq.com'
AUTHOR = 'szj'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

REQUIRED = read_requirements('requirements.txt')

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    with open(os.path.join(here, FOLDER, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


def package_files(directories):
    paths = []
    for item in directories:
        if isfile(item):
            paths.append(join('..', item))
            continue
        for (path, directories, filenames) in walk(item):
            for filename in filenames:
                paths.append(join('..', path, filename))
    return paths

setup(
    name=NAME,
    version=about['__version__'],
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=['examples','datasets']),
    install_requires=REQUIRED,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pygit=giting.cli:run'
        ],
    },
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    zip_safe=False,
)
