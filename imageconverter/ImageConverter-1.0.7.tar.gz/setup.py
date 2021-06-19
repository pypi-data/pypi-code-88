from setuptools import setup

# version of the software from ImageConverter/converter.py
exec(compile(open('ImageConverter/version.py').read(), 'ImageConverter/version.py', 'exec'))

def readme():
    with open('README.md', encoding="utf8") as f:
        README = f.read()
    return README


keywords = ['image', 'converter', 'jpg', 'png' ,'jpeg' ,'jpeg to png', 'jpg to png']

setup(
    name="ImageConverter",
    version= "1.0.7",
    description="A python package for converting .jpg and .jpeg file formats to .png",
    long_description=readme(),
    # long_description_content_type="text/markdown",
    contact_email = 'dailycodingpro@gmail.com',
    url="https://github.com/xXSD11Xx/imageconversion",
    author="xXSDXx",
    author_email="dailycodingpro@gmail.com",
    # install_requires=['PIL'],
    keywords = ['image', 'converter', 'jpg', 'png' ,'jpeg' ,'jpeg to png', 'jpg to png'],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    packages=["ImageConverter"], #modules 
    include_package_data=False,
    install_requires=["Pillow"], #3rd party install requirements
    entry_points={
        "console_scripts": [
            "ImageConversion=ImageConverter.cli:main",
        ]
    },
)