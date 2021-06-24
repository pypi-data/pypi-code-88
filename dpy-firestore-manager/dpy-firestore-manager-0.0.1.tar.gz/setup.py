from setuptools import setup, find_packages

with open('README.md', 'r', encoding = 'utf-8') as f:
  long_description = f.read()

setup(
  name='dpy-firestore-manager',
  version='0.0.1',
  description='Hello',
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=find_packages(),
  install_requires = [
    "discord.py>=1.0.1",
    "firebase_admin>=5.0.0"
  ]
)