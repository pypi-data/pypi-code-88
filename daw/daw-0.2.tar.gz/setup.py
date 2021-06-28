import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED = [
    "requests",
    "asyncio"
]

setuptools.setup(
    name="daw",
    version="0.2",
    author="Peti",
    author_email="support@radonbot.hu",
    description="Discord API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Peti1/daw",
    project_urls={
        "Bug Tracker": "https://github.com/Peti1/daw/issues",
    },
    include_package_data=True,
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
)