from setuptools import setup, find_packages

VERSION = '0.0.1.dev2'
DESCRIPTION = 'Quiffen'
LONG_DESCRIPTION = 'A Python package for parsing Quicken Interchange Format (QIF) files.'

# Setting up
setup(
    name="quiffen",
    version=VERSION,
    author="Isaac Harris-Holt",
    author_email="isaac@harris-holt.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'qif'],
    license='GNU GPLv3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3'
)