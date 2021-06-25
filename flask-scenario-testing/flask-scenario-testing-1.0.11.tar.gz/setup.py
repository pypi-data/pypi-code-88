import setuptools
import os


loc = os.path.dirname(os.path.abspath(__file__))

with open(loc + '/requirements.txt') as f:
    required = f.read().splitlines()


setuptools.setup(
    name="flask-scenario-testing",
    scripts=['bin/run-simulation'],
    version='1.0.11',
    setup_requires=['setuptools_scm'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    platforms='Any',
    zip_safe=False,
    test_suite='tests.get_test_suite',
    url='https://github.com/thejager/flask-scenario-testing',
    author="Johan de Jager, Mircea Lungu",
    author_email="johanthejager@gmail.com",
    description="Automatically monitor the evolving performance of Flask/Python web services.",
    install_requires=required,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Flask',
    ],
    project_urls={
    },
)
