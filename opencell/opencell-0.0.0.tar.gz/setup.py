from os import path
import setuptools

# Load long description
with open(
    path.join(path.abspath(path.dirname(__file__)), "README.md"), "r", encoding="utf-8"
) as fh:
    long_description = fh.read()

# with open(path.join(path.abspath(path.dirname(__file__)), "requirements.txt")) as f:
#     default_requirements = [
#         line.strip() for line in f if line and not line.startswith("#")
#     ]

setuptools.setup(
    name="opencell",
    version="0.0.0",
    author="",
    author_email="",
    description="Proteome-scale measurements of human protein localization "
                "and interactions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://opencell.czbiohub.org",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": f".{path.sep}"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)