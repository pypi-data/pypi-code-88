
from setuptools import setup
from discord_template import ( 
        __version__, __author__, __license__
    )

base_url = "https://github.com/znqi/discord_template/"


def get_long_description():

    with open("README.md", encoding="utf-8") as f:
        readme = f.read()

    return readme

setup(
    name="discordtemplate",
    description="🔹 A new and enhanced boilerplate template for discord.py",
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    author=__author__,
    url=base_url,
    license=__license__,
    include_package_data=True,
    packages=['discord_template', 'discord_template.env'],
    python_requires=">=3.5",
    version=__version__,
    entry_points = {
        "console_scripts": [
            "discord = discord_template.__main__:run"
        ]
    },
    zip_safe = False,
    install_requires=[
        "jinja2",
        "InquirerPy",
        "requests",
        "tabulate",
        "discord.py"
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
