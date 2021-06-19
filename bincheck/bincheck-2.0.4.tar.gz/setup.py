import setuptools

setuptools.setup(
    name = 'bincheck',
    version = '2.0.4',
    description = 'Brentree Bin Refrence Check',
    author = 'doesntexit',
    author_email = 'edwinhamal@gmail.com',
    py_modules = ['bincheck'],
    install_requires = [],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
