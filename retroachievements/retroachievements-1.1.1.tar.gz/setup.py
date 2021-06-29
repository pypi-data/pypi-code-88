import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="retroachievements",
    version="1.1.1",
    author="Mattlau04",
    author_email ="Mattlau04@noemail.com",
    description="A simple API wrapper for Retroachievements.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mattlau04/retroachievements-python",
    packages=['retroachievements'],
    package_data={},
    keywords=['api', 'retroachievements'],
    classifiers=[
        "Programming Language :: Python :: 3"],
    python_requires='>=3.7',
    install_requires=[
          'requests',
      ],
)
