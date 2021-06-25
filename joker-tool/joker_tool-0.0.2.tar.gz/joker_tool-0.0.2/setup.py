import setuptools

setuptools.setup(
    name="joker_tool",
    version="0.0.2",
    author="Joker",
    author_email="joker.code@qq.com",
    description="This is a toolkit",
    long_description="Commonly used functions and encryption function collation",
    long_description_content_type="text/markdown",
    url="https://github.com/Mrzsy/Tool",
    packages=setuptools.find_packages(where='.', exclude=(), include=('*',)),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
