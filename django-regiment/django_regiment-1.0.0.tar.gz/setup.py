from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'django middleware for regiment.tech\'s bulletlog'
LONG_DESCRIPTION = 'django middleware for regiment.tech\'s bulletlog'

setup(
    name="django_regiment", 
    version=VERSION,
    author="regiment.tech",
    author_email="support@regiment.tech",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="https://bitbucket.org/adithya_sama/tattler_client/src/master/flask_tattler/",
    license="MIT",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "django"
        "requests",
    ],
    classifiers= [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ]
)
