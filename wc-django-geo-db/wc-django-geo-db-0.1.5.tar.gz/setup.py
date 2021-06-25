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


version = get_version('wcd_geo_db')


setuptools.setup(
    name='wc-django-geo-db',
    version=version,
    author='WebCase',
    author_email='info@webcase.studio',
    license='MIT License',
    description='Geographical database for internal projects.',
    install_requires=(
        'px-settings==0.1.2',
        'px-django-postgres==0.1.0',
        'px-django-tree==0.1.1',
        'px-django-lingua==0.1.0',
        'requests==2.25.1',
        'pandas==1.2.4',
        'openpyxl==3.0.7',
        'xlrd==2.0.1',
    ),
    extras_require={
        'dev': (
            'pytest>=6.0,<7.0',
            'pytest-watch>=4.2,<5.0',
            'pytest-django>=4.3,<5.0',
            'django-environ==0.4.5',
            'django-stubs',
            'django>=2.2,<4',
            'twine',
        ),
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(exclude=(
        'tests', 'tests.*',
        'experiments', 'pilot',
    )),
    python_requires='>=3.6',
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',

        'Programming Language :: Python :: 3',

        'Intended Audience :: Developers',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
