import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name = "upn2sepa",
    version = "1.0.1",
    description = "UPN QR to SEPA QR converter.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/janzmazek/upn2sepa",
    author="Jan Zmazek",
    author_email="jan.zmazek@gmail.com",
    license = "MIT license",
    packages = find_packages(exclude=['*test']),
    entry_points = {
        'console_scripts': [
            'upn2sepa = upn2sepa.run:run',
        ]
    },
    install_requires = ['Pillow', 'pyzbar', 'segno']
)
