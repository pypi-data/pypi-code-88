import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pym-pkg-Fry",
    version="0.0.1",
    author="Fry",
    author_email="",
    description="A pip package that add's new If , Else , Elif , While , For statements.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fryghtened/pym",
    project_urls={
        "Bug Tracker": "https://github.com/Fryghtened/pym/issues",
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

