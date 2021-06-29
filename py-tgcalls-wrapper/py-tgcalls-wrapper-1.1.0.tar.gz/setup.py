import setuptools

setuptools.setup(
    name="py-tgcalls-wrapper",
    version="1.1.0",
    author="Roj Serbest",
    author_email="rojserbest@icloud.com",
    description="A library to make using PyTgCalls easier.",
    url="https://github.com/callsmusic/pytgcalls-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["youtube-dl", "py-tgcalls"],
)
