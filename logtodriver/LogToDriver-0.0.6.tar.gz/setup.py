from setuptools import setup, find_packages

setup(
    name='LogToDriver',
    version='0.0.6',
    packages=['LogToDriver'],
    keywords=['LogToDriver'],
    install_requires=[
        'elasticsearch==7.13.2',
        'robotframework==4.0.3',
        'pytz==2021.1'
    ],
)
