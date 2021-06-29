from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'API client for boring stonks'

# Setting up
setup(
        name="boringstonks", 
        version=VERSION,
        author="Kevin Per",
        author_email="kevin.per@protonmail.com",
        description=DESCRIPTION,
        packages=["boringstonks"],
        install_requires=['pandas', 'requests'],
        keywords=['python'],
)
