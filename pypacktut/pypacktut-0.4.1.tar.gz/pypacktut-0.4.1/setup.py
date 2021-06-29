from setuptools import setup, find_packages

VERSION = '0.4.1'
DESCRIPTION = 'Python package tutorial'
LONG_DESCRIPTION = 'Package package tutorial with a slightly longer description'
find_packages_in = ['pypacktut/*', ]
other_reqs = ['numpy>=1.14.5']

setup(
    name='pypacktut',
    version=VERSION,
    author="Nitin Singh",
    author_email="singh.nitin512@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(include=find_packages_in),
    install_requires=other_reqs,
    keywords=['python', 'package tutorial'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)