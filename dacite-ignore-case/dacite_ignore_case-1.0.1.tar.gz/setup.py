import os

import setuptools


own_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(own_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='dacite_ignore_case',
    version='1.0.1',
    description='Extends dacite.from_dict with a ignore case function',
    author='zkdev',
    author_email='dev@zeekay.dev',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    project_urls={
        'Homepage': 'https://github.com/zkdev/dacite-ignore-case',
        'Bug Tracker': 'https://github.com/zkdev/dacite-ignore-case/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
       'dacite',
    ],
    license='MIT',
    python_requires='>=3.9.*',
    packages=['dacite_ignore_case'],
)
