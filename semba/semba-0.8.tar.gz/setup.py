from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(	
      install_requires=['semopy>=2.2.4', "numpyro>=0.6"],
      include_package_data=True,
      package_data={'': ['examples/*.csv', 'examples/*.npy', 'report/*.html',
                         'report/*.txt', 'examples/*.txt', 'report/css/*.css',
                         'report/js/*.js']},
      name="semba",
      version="0.8",
      author="Georgy Meshcheryakov",
      author_email="metsheryakov_ga@spbstu.ru",
      description="Bayesian  Structural Equation Modeling ",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://bayes.semopy.com",
      packages=find_packages(),
      python_requires=">=3.7",
      classifiers=[
              "Programming Language :: Python :: 3.7",
	      "Programming Language :: Python :: 3.8",
	      "Programming Language :: Python :: 3.9",
	      "Programming Language :: Python :: 3.10",
              "License :: OSI Approved :: MIT License",
	      "Development Status :: 3 - Alpha",
	      "Topic :: Scientific/Engineering",
              "Operating System :: OS Independent"])
