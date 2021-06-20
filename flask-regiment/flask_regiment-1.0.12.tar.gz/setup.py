from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'flask extension for regiment.tech\'s instalog'
LONG_DESCRIPTION = 'flask extension for regiment.tech\'s instalog'

setup(
    name="flask_regiment", 
    version=VERSION,
    author="RamHarsha, Adithya",
    author_email="kunchamharsha@gmail.com, samavenkatadithya@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="https://bitbucket.org/adithya_sama/tattler_client/src/master/flask_tattler/",
    license="MIT",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "flask",
        "requests",
        "blinker"
    ],
    classifiers= [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ]
)
