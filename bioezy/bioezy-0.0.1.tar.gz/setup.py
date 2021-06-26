import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bioezy",
    version="0.0.1",
    author="Surur Khan",
    author_email="surur.rkhan@gmail.com",
    description="Contains several bioinformatics scripts automating base level genomics analysis tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rukhan4/bioezpkg",
    project_urls={
        "Bug Tracker": "https://github.com/Rukhan4/bioezpkg/issues.md",
        "Documentation": "https://github.com/Rukhan4/bioezpkg/documentation.md"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
