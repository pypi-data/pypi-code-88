from  setuptools import setup,find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='json-log-decorator',
    version='1.1.0',
    author="Rajesh Bathula",
    author_email="rajb2237@gmail.com",
    description="The Python LogDecorator with exception, in JSON format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajeshkbathula/json-log-decorator",
    packages=find_packages("jsonlogdecorator"),
    package_dir={'': 'jsonlogdecorator'},
    install_requires=["python-json-logger==2.0.1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)