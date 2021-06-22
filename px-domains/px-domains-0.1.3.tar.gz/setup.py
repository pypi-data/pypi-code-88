import os
import re
import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()

    return re.search('__version__ = [\'"]([^\'"]+)[\'"]', init_py).group(1)


version = get_version('px_domains')


setuptools.setup(
    name='px-domains',
    version=version,
    author='Alex Tkachenko',
    author_email='preusx.dev@gmail.com',
    license='MIT License',
    description='Simple string domains implementation.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    extras_require={
        'dev': (
            'pytest>=6.0,<7.0',
            'pytest-watch>=4.2,<5.0',
            'twine',
        ),
    },
    packages=setuptools.find_packages(exclude=('tests', 'tests.*')),
    python_requires='>=3.6',
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',

        'Programming Language :: Python :: 3',
        'Framework :: Django',

        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
