import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opine-cli",
    version="0.0.1",
    author="Opine @ Cognate Systems",
    author_email="info@opine.world",
    description="A command line interface for Opine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://opine.world",
    project_urls={
        "Bug Tracker": "https://opine.world",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'opine=opinecli.cli:main',  # command=package.module:function
        ],
    },
)