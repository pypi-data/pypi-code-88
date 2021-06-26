import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setuptools.setup(
    name="tadam", 
    version="0.0.1",
    author="kun zeng",
    author_email="zki@163.com",
    description="TAdam optimizer for Pytorch",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kunzeng/tadam",
    packages=setuptools.find_packages(),
    classifiers=[     
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'torch',
    ],
    python_requires='>=3.0',
)

