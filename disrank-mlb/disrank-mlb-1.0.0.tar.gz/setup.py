from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='disrank-mlb',
    version='1.0.0',
    description='A modified version of disrank that has Miraculous Ladybug images.  Used for a personal bot but can '
                'be used by anyone.',
    py_modules=['generator'],
    package_dir={"": "disrank"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="minecraftpr03",
    author_email=None,
    url="https://pypi.org/project/disrank/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
