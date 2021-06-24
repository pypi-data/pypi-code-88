
"""Setup.py for the apache-airflow-backport-providers-smtp package."""

import logging
import os

from os.path import dirname
from setuptools import find_namespace_packages, setup

logger = logging.getLogger(__name__)

version = '2021.6.24'

my_dir = dirname(__file__)

try:
    with open(os.path.join(my_dir, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''


def do_setup():
    """Perform the package apache-airflow-backport-providers-smtp setup."""
    setup(
        name='apache-airflow-backport-providers-smtp',
        description='Email provider package '
        'apache-airflow-backport-providers-smtp for Apache Airflow',
        long_description=long_description,
        long_description_content_type='text/markdown',
        license='Apache License 2.0',
        version=version,
        packages=find_namespace_packages(
            include=['airflow.providers.email', 'airflow.providers.email.*']
        ),
        zip_safe=False,
        include_package_data=True,
        install_requires=['apache-airflow~=1.10'],
        setup_requires=['setuptools', 'wheel'],
        extras_require={},
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: System :: Monitoring',
        ],
        author='Apache Software Foundation',
        author_email='dev@airflow.apache.org',
        url='https://airflow.apache.org/',
        download_url='https://archive.apache.org/dist/airflow/backport-providers',
        python_requires='~=3.6',
        project_urls={
            'Documentation': 'https://airflow.apache.org/docs/',
            'Bug Tracker': 'https://github.com/apache/airflow/issues',
            'Source Code': 'https://github.com/apache/airflow',
        }
    )


if __name__ == "__main__":
    do_setup()
