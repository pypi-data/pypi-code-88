from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="cleanify",
    version="1.0.0",
    description="CLI utility to remove remove newlines, tabs from a file and copy it to your clipboard",
    url="https://github.com/http-samc/cleanify",
    author="Samarth Chitgopekar",
    author_email="sam@chitgopekar.tech",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages = ["cleanify"],
    entry_points = {
        'console_scripts': [
            'cleanify=cleanify.main:main'
        ]
    },
    install_requires = [
        "klembord==0.2.2"
    ],
    classifiers = [
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: English"
    ]
)