from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="GenDoc",
    version="0.0.2",
    description="Generate a Markdown Documentation file from a Python Repository with DocStrings.",
    py_modules=["gen_doc"],
    package_dir={'':'src'},
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'gendoc=src.gen_doc:main'
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