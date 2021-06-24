from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='flaskdesign',
    version='0.0.1',
    url='https://github.com/MichaelDeMattos/flask-design',
    license='MIT License',
    author='Michael M. Ortiz',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='chelmto3000@gmail.com',
    keywords='flaskdesign',
    description=u'Design patterns for projects using flask based in blueprints',
    packages=['flaskdesign'],
    install_requires=[],)
