import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="probat",
    version="1.1.0",
    description="Battery life saver and reminder",
    url="https://github.com/codeswhite/probat",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.8',
    install_requires=[
        'termcolor',
    ],
    entry_points={
        'console_scripts': [
            'probat = probat:main',
        ],
    },
    author="Max G",
    author_email="max3227@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages()
)
