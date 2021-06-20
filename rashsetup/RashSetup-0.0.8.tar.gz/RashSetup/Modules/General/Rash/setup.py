import setuptools

setuptools.setup(
    name="Rash",
    description="PySide2 Shell for my Personal Projects",
    long_description="Rash can provide GUI support for any python projects, if it finds supportive",
    author="Rahul A Ranger",
    url="https://github.com/RahulARanger/Rash/tree/master/Rash",
    python_requires=">=3.6.0",
    author_email="saihanumarahul66@gmail.com",
    install_requires=[
        "PySide2"
    ],
    license="MIT",
    include_package_data=True,
    version='0.2.0',
    packages=["Rash"],
    package_data={
        "Rash": [
            "Media/*"
        ]

    }
)
