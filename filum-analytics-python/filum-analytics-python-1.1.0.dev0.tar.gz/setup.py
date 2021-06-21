
import os
import sys
from pathlib import Path

try:
    with open(Path(__file__).parent / 'filum_analytics' / 'version.py') as version_file:
        version = version_file.read().strip().split("=")[1].replace("'", '').strip()
except Exception as e:
    version = "1.0.0"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Don't import analytics-python module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'filum_analytics'))

long_description = '''
Filum aims to be the first and the BEST Business Data Platform in South East Asia.
Filum Python SDK help you to transform data into Filum events with ease
This is the official Python package that realizes the Filum Standard Event Schema.
'''

install_requires = [
    "requests>=2.7,<3.0",
    "six>=1.5",
    "monotonic>=1.5",
    "backoff==1.6.0",
    "python-dateutil>2.1"
]

tests_require = [
    "mock>=2.0.0"
]

setup(
    name='filum-analytics-python',
    version=version,
    url='https://github.com/Filum-AI/filum-python-sdk',
    author='Filum AI',
    author_email='hiep@filum.ai',
    maintainer='Filum AI',
    maintainer_email='hiep@filum.ai',
    packages=['filum_analytics'],
    license='MIT License',
    install_requires=install_requires,
    tests_require=tests_require,
    description='The official Python SDK for Filum BDP',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
