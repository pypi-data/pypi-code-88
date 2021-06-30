from setuptools import setup, find_packages

VERSION = "0.1.dev0"

with open("README.rst", "r") as fh:
    long_description = fh.read()
    fh.close()

with open("requirements.txt", "r") as mFile:
    requirements = mFile.read().split("\n")
    mFile.close()

require = [i for i in requirements if not i == ""]

setup(name="smlearn",
      version=VERSION,
      description="Machine Learning Algorithms",
      author="Ajith",
      author_email="ajithar204@gmail.com",
      long_description=long_description,
      long_description_content_type="text/x-rst",
      license="new BSD",
      classifiers=[
          "Intended Audience :: Science/Research",
          "License :: OSI Approved",
          "Programming Language :: Python",
          "Topic :: Scientific/Engineering",
          "Development Status :: 2 - Pre-Alpha",
          "Operating System :: Microsoft :: Windows",
          "Operating System :: Unix",
          "Operating System :: MacOS",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
      ],
      packages=find_packages(),
      install_requires=require,
      python_requires=">=3.8",
      )
