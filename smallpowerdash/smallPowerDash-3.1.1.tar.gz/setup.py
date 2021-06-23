import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
name="smallPowerDash",
version="3.1.1",
author="Dorian Drevon",
author_email="drevondorian@gmail.com",
description="source codes and config Files to monitor buildings data",
long_description=long_description,
long_description_content_type="text/markdown",
# url="https://github.com/pypa/sampleproject",
# project_urls={
#     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
# },
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
# packages=setuptools.find_packages(),
packages=['smallPowerDash'],
# packages=setuptools.find_packages(exclude=["quickTest"]),
package_data={'': ['confFiles/*']},
include_package_data=True,
# install_requires=['dorianUtils==v3.1'],
python_requires=">=3.8"
)
