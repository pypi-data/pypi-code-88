import io
from setuptools import setup


setup(
    name='json-deserializer',
    version='0.0.4',
    description='Attempts to correctly deserialize objects that json decoder cannot.',
    author='Mathew Moon',
    author_email='me@mathewmoon.net',
    url='https://github.com/mathewmoon/json-deserializer',
    license='Apache 2.0',
    long_description=io.open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=['json_deserializer'],
    package_dir={'json_deserializer': 'src/json_deserializer'},
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
)
