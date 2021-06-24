import pathlib
from setuptools import setup


__version__ = '0.2'
__author__ = 'Jeff Barfield'
__author_email__ = 'jeffreybarfield@protonmail.com'


HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()


setup(
    name='pwea',
    version=__version__,
    description='A simple weather tool.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/jeffreybarfield/myweather',
    author=__author__,
    author_email=__author_email__,
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['pwea'],
    include_package_data=True,
    install_requires=['requests', 'rich'],
    entry_points={'console_scripts': ['pwea=pwea.__main__:main']},
    python_requires=">=3.6"
)
