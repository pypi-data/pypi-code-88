import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvisonic",
    version="1.0.9",
    author="DaveSmegHead",
    author_email="davesmeghead@hotmail.com",
    description="An asyncio python interface library to the visonic alarm panel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davesmeghead/pyvisonic",
    packages=setuptools.find_packages(),
    install_requires=["aconsole==0.0.8", "pyserial_asyncio==0.4"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
