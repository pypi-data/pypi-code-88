import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="colourpick",
    version="1.0.2",
    description="Calculation of the dominant (average) RGB value",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jay-chau/colourpick",
    author="Jay Chau",
    author_email="jay-chau@outlook.com",
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=["colourpick"],
    include_package_data=True,
    install_requires=[
        'opencv-python',
        'scikit-learn',
        'numpy',
    ]
)