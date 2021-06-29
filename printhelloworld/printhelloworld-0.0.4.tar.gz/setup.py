from setuptools import setup, find_packages
VERSION = '0.0.4'
DESCRIPTION = 'Minore bug fix'
LONG_DESCRIPTION = 'A package that prints hello world.'

# Setting up
setup(
    name="printhelloworld",
    version=VERSION,
    author="Advait Shiralkar",
    author_email="advaitshiralkar2@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
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
