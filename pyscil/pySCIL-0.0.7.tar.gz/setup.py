import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pySCIL",
    version="0.0.7",
    author="Max Schwartz, Esteban Castillo Juarez, Ivan Leon",
    author_email="schwam4@rpi.edu, castie2@rpi.edu, leoni@rpi.edu",
    description="A sociolinguistics package for NLP research.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.rpi.edu/LACAI/pySCIL",
    project_urls={
        "Documentation": "https://github.rpi.edu/LACAI/pySCIL",
        "Source Code": "https://github.rpi.edu/LACAI/pySCIL",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
)
