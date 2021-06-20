import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="py-office-learn",
    version="0.1.151",
    description="py-office-learn is a gui for machine learning ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/YC-Lammy/py-office-learn",
    author="YC",
    author_email="yclam508@protonmail.com",
    platforms = "Linux, Mac OS X, Windows",
    license="GPL",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=["pyOfficeLearn"],
    include_package_data=True,
    install_requires=["joblib","matplotlib"],
    entry_points={
        'console_scripts': [
            'py-office-learn=pyOfficeLearn.__main__:main',],
    },
)

