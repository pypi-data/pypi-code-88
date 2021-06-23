import setuptools

setuptools.setup(
    name = 'ArithmaticPackage',
    version = "0.0.2",
    author = "Pooja Solaikannu",
    author_email = "poojasolai97@gmail.com",
    description = "Simple arithmatic problem",
    long_description = "Just a simple function which does addition of two numbers given inputs of two numbers(a, b)",
    long_description_content_type = "text/plain",
    url="https://github.com/pooja-solaikannu/jubilant-garbanzo",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)