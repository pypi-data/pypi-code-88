from distutils.core import setup

VERSION = "0.2.1"

setup(
    name='mathdunders',
    version=VERSION,
    author='discretegames',
    author_email='discretizedgames@gmail.com',
    description="Decorator that adds math dunders to a class derived from a numeric type.",
    # long_description=open("README.md").read(),
    # long_description_content_type="text/markdown",
    url='https://github.com/discretegames/mathdunders',
    py_modules=['mathdunders'],
    license="MIT License",
    keywords=['python', 'math', 'mathematics', 'dunder', 'double under', 'underscore', 'magic method', 'number'],
)
