from setuptools import setup, version


def readme():
	with open('./README.md') as f:
		return f.read()

setup(
    name='envariable',
    packages=['envariable'],
    version='1.3',
    license='MIT',
    description='Change System Environment Variable permanently',
    long_description=readme(),
	long_description_content_type='text/markdown',
    author='Arshia Ihammi',
    author_email='arshiaihammi@gmail.com',
    url='https://github.com/blueboy-tm/python-envariable/',
    download_url='https://github.com/blueboy-tm/python-envariable/raw/main/dist/envariable-1.3.tar.gz',
    keywords=['env', 'variable', 'environment', 'os', 'system', 'Environment Variable', 'environ'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: System',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only'
    ],
    python_requires='~=3.3',
)
