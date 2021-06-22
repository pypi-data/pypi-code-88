from setuptools import setup
import os


VERSION = "1.1.6"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


def get_data_files(rel_path):
    data_files = [
        "templates/*"
    ]
    if rel_path.endswith("/"):
        rel_path = rel_path[:-1]
    basedir = os.path.dirname(__file__)
    static_dir = os.path.join(basedir, f"{rel_path}/static/")
    for dir, subdirs, files in os.walk(static_dir):
        for file in files:
            filepath = os.path.join(dir, file).replace(
                f"{rel_path}/", ""
            )
            data_files.append(filepath)
    return data_files


setup(
    name="datasette-surveys",
    description="Datasette plugin for creating surveys and collecting responses all in one place.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Brandon Roberts",
    author_email="brandon@bxroberts.org",
    url="https://github.com/next-LI/datasette-surveys",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_surveys"],
    entry_points={"datasette": ["surveys = datasette_surveys"]},
    install_requires=[
        # "datasette>=0.56",
        "asgi-csrf>=0.7",
        "starlette",
        "aiofiles",
        "python-multipart",
        "sqlite-utils",
    ],
    extras_require={
        "test": ["pytest", "pytest-asyncio", "asgiref", "httpx", "asgi-lifespan"]
    },
    include_package_data=True,
)
