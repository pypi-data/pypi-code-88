import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("cartils/VERSION", "r") as f:
    version = f.read()

setuptools.setup(
    name="cartils",
    version=version,
    author="John Carter",
    author_email="jfcarter2358@gmail.com",
    description="A collection of useful Python utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jfcarter2358/cartils",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        'colorama==0.4.4'
    ]
)
