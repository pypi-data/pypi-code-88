from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='nmea-parser',
    version='0.4.0',
    packages=['nmea'],
    url='https://gitlab.com/bek3/nmea-parser',
    license='Mozilla Public License 2.0',
    author='Brendan Kristiansen',
    author_email='b@bek.sh',
    description='Python library to parse NMEA streams',
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": 'https://www.bek.sh/nmea-parser',
        "Source Code": "https://gitlab.com/bek3/nmea_parser",
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    install_requires=['pyserial']
)
