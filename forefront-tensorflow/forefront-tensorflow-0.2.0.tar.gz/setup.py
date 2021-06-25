from distutils.core import setup

setup(
    name='forefront-tensorflow',
    packages=['forefront_tensorflow'],
    version='0.2.0',
    license='MIT',
    description='Subpackage for forefront (tryforefront.com)',
    author='Forefront Technologies',
    author_email='pypi@tryforefront.com',
    url='https://github.com/TryForefront/forefront-tensorflow',
    download_url='https://github.com/TryForefront/forefront-tensorflow/archive/refs/tags/v0.2.0.tar.gz',
    keywords=['MACHINE LEARNING', 'DATA SCIENCE', 'ML', "TENSORFLOW"],
    install_requires=[
        'tensorflow',
        'tf2onnx'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
