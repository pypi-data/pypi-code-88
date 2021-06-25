from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='impfeature',
  version='0.0.01',
  description='Find important features',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/saikat-kolkata',  #'https://github.com/you/your_package' github link to source
  author='Saikat Mazumder, Sourav Mondal',
  author_email='saikatmaz@gmail.com', #change later
  license='MIT', 
  classifiers=classifiers,
  keywords='Feature Importance', 
  packages=find_packages(),
  install_requires=['numpy','pandas','catboost']  #libraries required
)