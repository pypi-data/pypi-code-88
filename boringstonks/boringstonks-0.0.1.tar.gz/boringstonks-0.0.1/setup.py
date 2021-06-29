from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'API client for boring stonks'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="boringstonks", 
        version=VERSION,
        author="Kevin Per",
        author_email="kevin.per@protonmail.com",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=['pandas', 'requests'], # add any additional packages that 
        keywords=['python'],
)
