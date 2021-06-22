import re
from pathlib import Path

from setuptools import find_packages, setup


def read(fname):
    p = Path(__file__).parent / fname
    with p.open(encoding="utf-8") as f:
        return f.read()


def get_version(prop, project):
    project = Path(__file__).parent / project / "__init__.py"
    result = re.search(
        r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), project.read_text()
    )
    return result.group(1)


setup(
    name="bospell",
    version=get_version("__version__", "bospell"),
    author="Esukhia developers",
    author_email="10zin@esukhia.org",
    description="Spell checking toolkit for Tibetan (boyig)",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Esukhia/bospell",
    packages=find_packages(),
    package_data={
        "bospell": [
            "resources/dictionaries/*",
        ]
    },
    package_dir={"bospell": "bospell"},
    include_package_data=True,
    install_requires=["botok>=0.8.6, <1.0", "symspellpy>=6.7.0, <7.0"],
    python_requires=">=3.8",
    tests_require=["pytest"],
)
