# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='knada-composer-wrappers',
    version='0.0.11',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    # metadata to display on PyPI
    author="NAV IKT",
    url="https://github.com/navikt/knada-composer-wrappers",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
