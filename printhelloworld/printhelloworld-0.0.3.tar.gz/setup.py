from setuptools import setup, find_packages
VERSION = '0.0.3'
DESCRIPTION = 'Bug fix'
LONG_DESCRIPTION = 'See README.md'
setup(
    name="printhelloworld",
    version=VERSION,
    author="Advait Shiralkar",
    author_email="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[''],
    keywords=[''],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
