from setuptools import setup,find_packages
  
# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()
  
  
# specify requirements of your package here
REQUIREMENTS = ['requests','argparse']
  
# some more details
CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: 3",
    ]
  
# calling the setup function 
setup(name='create-flask-project-cli',
      version='0.0.2',
      description='Create flask project with html and css ready using cli.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/logan0501/flaskcli.git',
      author='Loganathan',
      author_email='logan05012001@gmail.com',
      license='MIT',
      packages = find_packages(),
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='flaskapp cli html css flaskcli',
     entry_points={
        'console_scripts': ['flaskcli=flask_cli.__main__:main']
    },
    zip_safe = False
      )