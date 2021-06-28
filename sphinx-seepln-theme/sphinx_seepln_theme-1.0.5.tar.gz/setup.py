# -*- coding: utf-8 -*-
"""`sphinx_seepln_theme` lives on `Github`_.

.. _github:  https://e.coding.net/ddquk/rtd/rtd_geklink_theme.git

"""
from io import open
from setuptools import setup
from sphinx_seepln_theme import __version__


setup(
    name='sphinx_seepln_theme',
    version='1.0.5',
    url='https://e.coding.net/ddquk/rtd/rtd_geklink_theme.git',
    license='MIT',
    author='LEI L',
    author_email='170517617@qq.com',
    description='Seepln Docs Theme For Sphinx',
    long_description=open('README.md', encoding='utf-8').read(),
    zip_safe=False,
    packages=['sphinx_seepln_theme'],
    package_data={'sphinx_seepln_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/assets/*.*'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_seepln_theme = sphinx_seepln_theme',
        ]
    },
    install_requires=[
       'sphinx'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
