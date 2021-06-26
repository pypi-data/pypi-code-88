import os
from io import open
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.en.md'), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

with open(os.path.join(here, 'requirements.txt'), "r", encoding="utf-8") as fobj:
    requires = [x.strip() for x in fobj.readlines() if x.strip()]

setup(
    name="daemon-application",
    version="0.4.3",
    description="A simple python package for creating daemon applications.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="zencore",
    author_email="dobetter@zencore.cn",
    url="https://gitee.com/rRR0VrFP/daemon-application/",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords=['daemon-application'],
    packages=find_packages("."),
    zip_safe=False,
    install_requires=requires,
)
