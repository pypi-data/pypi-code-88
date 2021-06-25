from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='coep_package',
  version='0.0.9',
  description='to create csv file and create latex code',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Rohan Pol',
  author_email='rohanpol36@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='coep', 
  package_data={'coep_package': ['credentials.json']},
  packages=find_packages(),
  install_requires=[
    "google-api-python-client>=2.10.0",
    "google-auth-httplib2>=0.1.0",
    "google-auth-oauthlib>=0.4.4"
  ] 
)