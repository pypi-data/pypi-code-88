#!/usr/bin/env python

"""The setup script."""

import io
import os
import sys

# Python supported version checks. Keep right after stdlib imports to ensure we
# get a sensible error for older Python versions
if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")


from setuptools import find_packages, setup

import versioneer


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fh:
        return fh.read()


readme = read("README.md")
changelog = read("CHANGELOG.rst")

install_requires = [
    "ruamel.yaml",
    "more_itertools",
    # eg: "numpy==1.11.1", "six>=1.7",
]

extras_require = {
    "dev": [
        "black==20.8b1",
        "isort==5.7.0",
        "flake8==3.8.4",
        "mypy==0.800",
        "pre-commit~=2.10.0",
        "pytest==6.2.2",
        "pytest-cov==2.11.1",
        "tox~=3.21.0",
        "gitchangelog==3.0.4",
        "gitlint==0.15.0",
        "invoke==1.5.0",
    ]
}


def setup_package():
    metadata = dict(
        author="qin hong wei",
        author_email="1039954093@qq.com",
        python_requires=">=3.6",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        description="An example package. Generated with cookiecutter-rrpylibrary.",
        install_requires=install_requires,
        extras_require=extras_require,
        license="MIT license",
        long_description=readme + "\n\n" + changelog,
        long_description_content_type="text/markdown",  # Optional (see note above)
        include_package_data=True,
        keywords="ymlconf",
        name="ymlconf",
        url="https://github.com/qhw0/ymlconf",
        version=versioneer.get_version(),
        package_dir={"": "src"},
        zip_safe=False,
        cmdclass=versioneer.get_cmdclass(),
        packages=find_packages("src"),
        project_urls={  # Optional
            "Bug Reports": "https://github.com/qhw0/ymlconf/issues",
            "Source": "https://github.com/qhw0/ymlconf",
        },
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
