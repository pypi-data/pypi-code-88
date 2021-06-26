from setuptools import setup, find_packages

setup(
    name="dfquery",
    version="0.0.2",
    install_requires=["pandas", "sqlparse"],
    author="prs-watch",
    description="Query interface for pandas.DataFrame",
    packages=find_packages(),
    classfiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
