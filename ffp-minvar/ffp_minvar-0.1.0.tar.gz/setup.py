import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ffp_minvar",
    version="0.1.0",
    author="Lucius Luo",
    author_email="lucius0228@gmail.com",
    description="rewritten python package of ffp_minvar algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luciusluo/ffp_minvar",
    project_urls={
        "Bug Tracker": "https://github.com/luciusluo/ffp_minvar/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "lib"},
    packages=setuptools.find_packages(where="lib"),
    python_requires=">=3.6",
    include_package_data=True
)