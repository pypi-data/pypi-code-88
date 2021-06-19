import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BonkersDB",
    version="0.0.1",
    author="Vivaan S.",
    author_email="vivaan@blabbr.xyz",
    description="BonkersDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://replit.com/@A1PHA1/BonkersDB",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)