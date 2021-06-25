import setuptools

setuptools.setup(
    name = 'ccfind',
    version = '1.0.9',
    description = 'CC Formatter For Checker Bots',
    author = 'doesntexit',
    author_email = 'edwinhamal@gmail.com',
    py_modules = ['ccformat'],
    install_requires = [],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
