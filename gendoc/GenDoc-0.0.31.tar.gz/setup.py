from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="GenDoc",
    version="0.0.31",
    description="Generate a Markdown Documentation file from a Python Repository with DocStrings.",
    py_modules=["main"],
    package_dir={'':'gen_doc'},
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'gendoc=gen_doc.main:main'
        ]
    },
    url="https://github.com/http-samc/GenDoc",
    author="Samarth Chitgopekar",
    author_email="sam@chitgopekar.tech",
    long_description=long_description,
    long_description_content_type='text/markdown',
    # classifiers = [
    #     "Topic :: Utilities",
    #     "Intended Audience :: Developers",
    #     "Environment :: Console",
    #     "License :: MIT License",
    #     "Operating System :: Windows :: OSX :: Linux",
    #     "Programming Language :: Python :: >= 3.2",
    #     "Natural Language :: English :: EN"
    # ]
)