from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(name='youtea',
      version='0.1.8',
      include_package_data = True,
      description='Display statistics from youtube video',
      packages=['youtea'],
      author_email='leykoderto@gmail.com',
      long_description=readme,
      zip_safe=False)
