import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastnet",
    version="1.0.0",
    author="Rodrigo Coura Torres",
    author_email="torres.rc@gmail.com",
    description="A wrapper around PyTorch for Neural Network-related projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rctorres/fastnet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
