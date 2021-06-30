import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flcrypt",
    version="0.0.0",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
            },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)