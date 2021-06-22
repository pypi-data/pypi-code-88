import setuptools

with open("README.md", "r") as fh:
    long_description_md = fh.read()

setuptools.setup(
    name="snakewhisper",
    version="1.1.1",
    author="Anthony Chen",
    description="Proof of concept of an end-to-end encrypted peer-to-peer chat program written in Python.",
    long_description=long_description_md,
    long_description_content_type="text/markdown",
    url="https://github.com/slightlyskepticalpotat/snakewhisper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "cryptography>=3.4.7"
    ],
    python_requires='>=3.6',
)

