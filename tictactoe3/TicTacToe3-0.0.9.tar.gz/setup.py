# Don't forget to update the Release Notes

from setuptools import setup, find_packages

VERSION = "0.0.9" # It is already the New
DESCRIPTION = "A game of Tic Tac Toe, that you may RARELY WIN"

file = open("readme.md", encoding="utf-8")
LONG_DESCRIPTION = file.read()

# Setting up
setup(
    author="Programmin-in-Python (MK)",
    author_email="<kalanithi6014@gmail.com>",
    description=DESCRIPTION,
    install_requires=["PyGithub"],
    keywords=['python3', 'Tic Tac Toe', 'Tic-Tac-Toe', 'tic tac toe',
                'tic-tac-toe', 'tic-tac-toe-cli', 'probability'],
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    name="TicTacToe3",
    packages=find_packages(),
    project_urls={  "GitHub":"https://github.com/Programmin-in-Python/TicTacToe-cli",
                    "Release Notes":"https://github.com/Programmin-in-Python/TicTacToe-cli/releases/tag/v0.0.9",
                    "Home Page":"https://github.com/Programmin-in-Python/TicTacToe-cli"},
    python_requires=">=3",
    version=VERSION,
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