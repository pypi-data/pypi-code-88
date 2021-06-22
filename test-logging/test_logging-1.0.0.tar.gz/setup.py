import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="test_logging",
    version="1.0.0",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.axiatadigitallabs.com/et/digital-telco/dte-telco/add-ons_creation/python/plugin-log",
    author="testEmailClient1996",
    author_email="testEmailClient1996@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    packages=["test_logging"],
    include_package_data=True,
    install_requires=["uuid"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)