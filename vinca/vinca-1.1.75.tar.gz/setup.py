import codecs
import setuptools


setuptools.setup(
    name="vinca",
    version="1.1.75",
    author="Oscar Laird", # your name
    description="A simple spaced repetition system",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    include_package_data = True,
    packages=setuptools.find_packages(),
    install_requires=[ # dependecies package
        'readchar',
    ],
    entry_points = {
        'console_scripts': ['vinca=vinca.run:main']
    },
)
