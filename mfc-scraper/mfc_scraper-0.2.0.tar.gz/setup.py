#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'pytest~=6.2.4', 'beautifulsoup4~=4.9.3', 'requests~=2.25.1', 'tqdm~=4.61.1']

test_requirements = ['pytest>=3', ]

setup(
    author="Laurent Radoux",
    author_email='radoux.laurent@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Scrapes the content of one's collection of figures listed on MyFigureCollection",
    entry_points={
        'console_scripts': [
            'mfc_scraper=mfc_scraper.__main__:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mfc_scraper',
    name='mfc_scraper',
    packages=find_packages(include=['mfc_scraper', 'mfc_scraper.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/laurent-radoux/mfc_scraper',
    version='0.2.0',
    zip_safe=False,
)
