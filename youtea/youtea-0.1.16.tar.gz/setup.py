import io
import os
from setuptools import setup

# with open('README.md', 'r') as f:
#     readme = f.read()
DESCRIPTION = "Display statistics from youtube video"
here = os.path.abspath(os.path.dirname(__file__))

def get_long_description():
    """
    Return the README.
    """
    try:
        with io.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
            long_description = "\n" + f.read()
    except FileNotFoundError:
        long_description = DESCRIPTION
    return long_description

setup(name='youtea',
      version='0.1.16',
      license=open('LICENSE.txt').read(),
      include_package_data = True,
      description='Display statistics from youtube video',
      packages=['youtea'],
      author_email='leykoderto@gmail.com',
      long_description=get_long_description(),
      zip_safe=False)
