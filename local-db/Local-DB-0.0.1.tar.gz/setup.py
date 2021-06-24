from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Local-DB',
    version='0.0.1',
    description="A local PyMongo version rewritten",
    url='https://github.com/stav10/Local-DB',
    author='Stav Vanunu',
    author_email='shutzi@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='DB, PyMongo',
    packages=find_packages(),
    install_requires=[]
)