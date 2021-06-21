from setuptools import find_packages, setup

setup(
    name='skerrorlearner',
    packages=find_packages(include=['skerrorlearner']),
    version='0.1.4',
    description='Skerrorlearner is an Error Learning Package for Machine Learning',
    author='Indrashis Das',
    author_email='indrashisdas98@gmail.com',
    license='Apache License 2.0',
    long_description=open("README.rst").read(),
    zip_safe=True,
    url='https://github.com/IndrashisDas/skerrorlearner',
    keywords=['skerrorlearner','machine learning','artificial intelligence','scikit learn','sklearn','numpy','pandas','scipy','xgboost','lightgbm','catboost'],
    install_requires=['numpy','pandas','scikit-learn','xgboost','lightgbm','catboost'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)