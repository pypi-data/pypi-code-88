import setuptools

with open('README.MD', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='pytoDus',
    version='0.0.1',
    author='Jose Angel Sanchez Velazquez',
    author_email='sanchezvelazquezjoseangel@gmail.com',
    description='toDus python API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/RathHunt/pytoDus',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
