import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="System_Information",
    version="1.0",
    description="It finds basic information about the system.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Udit Vashisht",
    author_email="admin@saralgyaan.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["System_Information"],
    include_package_data=True,
    install_requires=['wmi','platform'],
    entry_points={
        "console_scripts": [
            "System_Information=System_Information.__main__:main",
        ]
    },
)