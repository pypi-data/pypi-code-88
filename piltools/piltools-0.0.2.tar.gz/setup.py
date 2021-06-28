import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piltools",
    version="0.0.2",
    author="Greg Krause",
    author_email="gregckrause@gmail.com",
    description="Tool suite that augments existing Python Imaging Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GregWasHere/PILTools",
    project_urls={
        "Bug Tracker": "https://github.com/GregWasHere/PILTools/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "Pillow==8.2.0"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)