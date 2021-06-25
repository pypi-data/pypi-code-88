import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Parse version number from asciiglet/__init__.py:
with open(HERE / 'asciiglet/__init__.py') as f:
    info = {}
    for line in f.readlines():
        if line.startswith('__version__'):
            exec(line, info)
            break

# This call to setup() does all the work
setup(
    name="asciiglet",
    version=info["__version__"],
    description="Asciiglet. For when you need to draw with text.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/LudwigVonChesterfield/Asciiglet",
    author="Luduk",
    author_email="ningawent@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["asciiglet"] + ['asciiglet.' + pkg for pkg in find_packages('asciiglet')],
    include_package_data=True,
    install_requires=["pyglet"],
)
