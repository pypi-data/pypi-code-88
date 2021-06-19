from setuptools import setup, find_packages

VERSION = "0.0.3"
DESCRIPTION = "A game of Tic Tac Toe, that you may RARELY WIN"

file = open("readme.md", encoding="utf-8")
LONG_DESCRIPTION = file.read()

# Setting up
setup(
    name="TicTacToe3",
    version=VERSION,
    author="Programmin-in-Python (MK)",
    author_email="<kalanithi6014@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    python_requires=">=3",
    project_urls={"HomePage":"https://github.com/Programmin-in-Python/TicTacToe-cli"},
    keywords=['python3', 'Tic Tac Toe', 'Tic-Tac-Toe', 'tic tac toe',
                'tic-tac-toe', 'tic-tac-toe-cli', 'probability'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Games/Entertainment :: Puzzle Games",
        "Topic :: Scientific/Engineering :: Mathematics"
    ]
)