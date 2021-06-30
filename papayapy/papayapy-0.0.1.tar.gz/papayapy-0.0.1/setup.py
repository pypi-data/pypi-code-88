import setuptools

setuptools.setup(
    name="papayapy",
    version="0.0.1",
    author="Example Author",
    author_email="hi@papayapy.com",
    description="Automate iOS Using Python",
    url="https://papayapy.com",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)