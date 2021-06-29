# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages

setup(
    name='ds_plugin',
    packages=find_packages(where='.', exclude=(), include=('*',)),
    # py_modules=[     # 在 package 之外添加两个独立的 module
    #     'isolated_greeting_module_1',
    #     'isolated_greeting_module_2'
    # ],
    version='0.1.0',
    install_requires=[         
        'lxml',
        'requests',
        'numpy',
        'click==7.0',
        'protobuf>=3.12,<4',
        'pyyaml>=5.1',
        'six>=1.10,<2',
        'docker>=4,<5',
        'versioneer==0.18',
        'kubernetes==11.0.0',
        'urllib3<1.25,>=1.15',
        'bs4>=0.0.1',
        'tabulate==0.8.3',
        'pip-api==0.0.14',
        'pre-commit==2.4.0',
        'psutil==5.7.2',
        'boto3==1.14.52',
        'pytz==2020.1',
        'kazoo==2.7.0',
        'kafka-python==2.0.1',
        'lz4==3.1.0',
        'pykafka==2.7.0',
        'pyarrow==3.0.0',
    ],
    # extras_require={
    #     'interactive': ['matplotlib>=2.2.0,<3.0.0', 'jupyter']
    # },
    # entry_points={       
    #     'console_scripts': [
    #         'greeting=greeting_pkg.greeting_module:main'
    #     ]
    # }
)
