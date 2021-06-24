from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='stringfunctions',
    version='0.0.4',
    description='A all in one string function package',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/thanamesleo/stringfunctions',
    author='Leonard "thanamesleo" W.',
    author_email='jetexer1.yt@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['better', 'string', 'stringfunctions', 'function', 'setterstrings', "string function", "Better Strings"],
    packages=find_packages(),
    install_requires=["pywhatkit"]
)