from setuptools import setup

import setuptools



long_description = "This is my first test on PyPI."

setuptools.setup(

    name="botwaysPypiHelloworldHest", # Replace with your username

    version="2.0.0",

    author="<authorname>",

    author_email="<authorname@templatepackage.com>",

    description="First Test",

    long_description=long_description,

    long_description_content_type="text/markdown",

    #url="<https://github.com/authorname/templatepackage>",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "Operating System :: OS Independent",

        "Operating System :: Microsoft :: Windows",

    ],

    python_requires='>=3.6',

)