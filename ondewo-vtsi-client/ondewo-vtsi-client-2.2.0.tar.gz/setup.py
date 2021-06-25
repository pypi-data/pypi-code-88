import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requires = f.read().splitlines()

setuptools.setup(
    name="ondewo-vtsi-client",
    version="2.2.0",
    author="Ondewo GbmH",
    author_email="info@ondewo.com",
    description="sends deployment commands to the Ondewo VTSI Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ondewo/ondewo-vtsi-client-python",
    packages=[
        np
        for np in filter(
            lambda n: n.startswith('ondewo.') or n == 'ondewo',
            setuptools.find_packages()
        )
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=2.6,!=3.0.*",
    install_requires=requires,
)
