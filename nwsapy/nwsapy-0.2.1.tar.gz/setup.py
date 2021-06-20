
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

version = "0.2.1"

# Steps to release a new version:
# 1. update version number above
# 2. if using a branch, push to branch, merge with master. Master is current version deployed.
# 3. Navigate to repo, create a new release. Name it the version stated above. Tag version should be the same
#       as the version name (i.e. vX.Y.Z).
# 3. In terminal: python setup.py sdist
# 4. In terminal: python twine dist/nwsapy-{version}.tar.gz
# Details: https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

setup(
  name = 'nwsapy',         # How you named your package folder (MyLib)
  packages = ['nwsapy'],   # Chose the same as "name"
  long_description=README,
  long_description_content_type="text/markdown",
  version = version,      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package to help with NWS API requests',   # Give a short description about your library
  author = 'Brandon Molyneaux',                   # Type in your name
  author_email = 'brandonmolyneaux@tornadotalk.com',      # Type in your E-Mail
  url = 'https://github.com/WxBDM/nwsapy',   # Provide either the link to your github or to your website
  download_url = f'https://github.com/WxBDM/nwsapy/archive/refs/tags/v{version}.tar.gz',    # I explain this later on
  keywords = ['national weather service', 'nws', 'nws api'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'shapely',
          'pandas',
          'numpy',
          'pint',
          'requests',
      ],
  python_requires = '>=3.8',
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      # Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
