import setuptools

with open ( "README.md" ) as file:
    README_description = file.read (  )

setuptools.setup (
    name = "MyDecorators",
    version = "0.1",
    author = "Danila Baranov",
    author_email = "danilabaranov@gmail.ru",
    description = "This library includes some useful decorators.",
    long_description = README_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/DanilaBaranov/MyDecorators.git",
    packages = [ 'MyDecorators' ],
    classifilers = [
        "Programming language :: Python :: 3",
        "License :: MIT Liesense",
        "Operating System :: Windows"
    ],
    python_requires = '>=3.9'
)