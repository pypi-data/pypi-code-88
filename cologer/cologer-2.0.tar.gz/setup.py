import setuptools

try:
    import pypandoc

    long_description = pypandoc.convert_file('README.md', 'rst')
except Exception:
    long_description = ""

setuptools.setup(
    name="cologer",
    version="2.0",
    author="junfalin",
    author_email="ljunf817@163.com",
    description="color-loger",
    long_description=long_description,
    keywords="python package",
    url="https://github.com/junfalin/cologer",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=['colorama'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
