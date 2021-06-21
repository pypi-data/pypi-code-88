from setuptools import setup

setup(name = 'cosmosis-build-standard-library',
      description       = "A simple tool to download and build CosmoSIS Standard Library.",
      long_description  = "This package mainly exists to give conda-forge "
                          "something to download. It provides a single script "
                          "which git clones the CosmoSIS standard library and then "
                          "builds it. You can do all this manually if you prefer.",
      author            = "Joe Zuntz",
      author_email      = "joezuntz@googlemail.com",
      url               = "https://bitbucket.org/joezuntz/cosmosis-csl",  
      packages = [],
      scripts = ['bin/cosmosis-build-standard-library'],
      install_requires = [],
      version="0.5",
      license_files = ('LICENSE',),
)

