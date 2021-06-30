import setuptools

setuptools.setup(
    name="sagesaver-tools",
    version="0.0.3",
    author="Victor Lin",
    author_email="vvictor.llin@gmail.com",
    description="Utils for SageSaver server scripts",
    url="https://github.com/Cozieee/sagesaver/sagesaver-tools",
    project_urls={
        "Project Main": "https://github.com/Cozieee/sagesaver",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)