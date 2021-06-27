from setuptools import setup, find_packages
import glob

VERSION = '0.0.1'
DESCRIPTION = 'Panduza Core Server'
LONG_DESCRIPTION = 'The Panduza server provide a bridge to control hardware interfaces'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="panduza_server", 
        version=VERSION,
        author="Panduza Team",
        author_email="panduza.team@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        
        install_requires=['django', 'djangorestframework', 'django-cors-headers'],

        package_data={
            'panduza_server': [
                'static/css/*.css',
                'static/img/*.png',
                'static/js/*.js',
                'templates/*.html'
            ]
        },

        entry_points = {
            'console_scripts': ['pza-run-server=panduza_server.scripts.server:run_server'],
        },
            
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)


