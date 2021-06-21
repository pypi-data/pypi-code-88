from setuptools import setup, find_packages

setup(
    name = "torch_checker",
    version = "1.0.0",
    keywords = ("pytorch","function tools"),
    description = "my function tools for training neural network with pytorch.",
    long_description = "my function tools for training neural network with pytorch. long description",
    #long_description_content_type='text/markdown',
    license = "MIT Licence",
    #url = "https://github.com/xuxiaohan",
    author = "Han Xu",
    author_email = "hxu10670@gmail.com",
    maintainer = "Han Xu",
    maintainer_email = "hxu10670@gmail.com",
    packages = find_packages(),
    #include_package_data = True,
    platforms = "any",
    install_requires = [
        "numpy",
        "torch",
        ]
)

