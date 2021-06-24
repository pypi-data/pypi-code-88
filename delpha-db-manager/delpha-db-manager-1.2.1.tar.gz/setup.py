#!/usr/bin/env python
import os
from glob import glob
from setuptools import setup, find_packages


def data_files_inventory():
    data_files = []
    data_roots = ['delpha_db_manager']
    for data_root in data_roots:
        for root, subfolder, files in os.walk(data_root):
            files = [x.replace('delpha_db_manager/', '') for x in glob(root + '/*')
                     if not os.path.isdir(x)]
            data_files = data_files + files
    return data_files


PACKAGE_DATA = {'delpha_db_manager': data_files_inventory()}


if __name__ == '__main__':
    setup(
        name="delpha-db-manager",
        version='1.2.1',
        author="Hugo Paigneau",
        author_email='hugo.paigneau@delpha.io',
        description="Delpha Database Management System",
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        keywords=['database', 'salesforce api', 'cassandra api', 'aws api'],
        license='MIT',
        packages=find_packages(exclude=['docs', 'tests*']),
        package_data=PACKAGE_DATA,
        include_package_data=True,
        install_requires=[
            'requests',
            'xmltodict',
            'url-normalize',
            'cassandra-driver',
            'pandas',
            'simple-salesforce',
            'boto3'
        ],
        zip_safe=True,
        url='https://github.com/Delpha-Assistant/DelphaDBManagement',
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )
