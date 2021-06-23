import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Demo-example-pkg",
    version="0.0.1",
    author="Aakash Aggarwal",
    author_email="aakash10975@gmail.com",
    packages=["demo_example_pkg"],
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/example-pkg",
    license='GPT',
    python_requires='>=2.7.16',
    classifiers=[
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent"
    ],
    install_requires=[
         "pyspark>=2.0",
    ]
)