import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="snitch_ai",
    version="1.0.0",
    description="Client library for using Snitch AI's model validation platform",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://snit.ch",
    author="Snitch AI",
    author_email="info@snit.ch",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    #package_data={'', ['cert/*.crt']},
    install_requires=["requests", "joblib", "numpy", "cryptography"],
    entry_points={},
)